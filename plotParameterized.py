"""
Makes histogram from tab-separated file.

Assumes the following raw data format:

x-axis name \t legend 1 \t legend 2 ...
x-axis value \t y-value \t y-value ...

"""

import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn

matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True


if len(sys.argv) < 8:
    print "\n\nHow to use:"
    print "Sys.argv[1]: Path to input file"
    print "Sys.argv[2]: Title of plot"
    print "Sys.argv[3]: x-axis name"
    print "Sys.argv[4]: y-axis name"
    print "Sys.argv[5]: filename to save to \n"
    print "Sys.argv[6]: index of x-axis"
    print "Sys.argv[7]: index of first y-axis"
    print "Sys.argv[8+3i]: (file, index of i+1'th y-axis, name) (we can only reasonably handle ~4 plots)"
    quit()


inputFilePath = sys.argv[1]
plotTitle = sys.argv[2]
xAxisName = sys.argv[3]
yAxisName = sys.argv[4]
outputFileName = sys.argv[5]
indexOfXAxis = int(sys.argv[6])
filesOfYValues = [y for y in sys.argv[7::3]]
indicesOfYValues = [int(y) for y in sys.argv[8::3]]
namesOfYValues = [y for y in sys.argv[9::3]]

assert(len(indicesOfYValues) > 0)
assert(len(indicesOfYValues) == len(namesOfYValues) == len(filesOfYValues))

colors = ['y', 'g', 'r', 'c', 'm', 'b', 'k', 'w']
linestyles = ['-', '--', '-.', ':', '-', '--', 'k', 'w']
markers = ['o', '+', '*', 'h', 's', 'D', 'p', 'w']
width = 0.15       # the width of the bars


xdata = open(sys.argv[1])
#names = data.readline().split('\t')
bars = [[] for i in range(len(namesOfYValues)+1)]

# epsilon is added to each bar to force visibility, otherwise matplotlib squeezes it
epsilon = 1e-7

for line in xdata:
    splitLine = line.split('\t')
    bars[0].append(float(splitLine[indexOfXAxis]))
    # for idx, val in enumerate(indicesOfYValues):
    #     bars[idx+1].append(float(splitLine[val]))

# this way of handling multiple files may cause the same file to be read 1+len(filesOfYValues) times, if all data is in the same file    
for idx, filename in enumerate(filesOfYValues):
    ydata = open(filename)
    for line in ydata:
        splitLine = line.split('\t')
        bars[idx+1].append(float(splitLine[indicesOfYValues[idx]]))

#print bars[0]
index = np.arange(len(bars[0]))  # the x locations for the groups
#print index            
fig, ax = plt.subplots()
rects = []

# x_offset for arrows when a plot is immediately zero
x_offset = 40
y_offset = 20

for idx, bar in enumerate(bars[1:]):
    rects.append(ax.plot(bars[0], bar, marker=markers[idx], color=colors[idx], ls=linestyles[idx]))
    # if bar[0] is 0:
    #     label = names[idx+1]
    #     x = 0
    #     y = 0
    #     plt.annotate(
    #         "{0}".format(label), 
    #         xy = (x, y), xytext = (x_offset, y_offset),
    #         textcoords = 'offset points', ha = 'right', va = 'bottom',
    #         #bbox = dict(boxstyle = 'round,pad=0.1', fc = 'white', alpha = 0.5),
    #         arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    #     x_offset += 20
    #     y_offset -= 10


plt.rcParams.update({'font.size': 22})    
#ax.set_ylim(-0.5)
#ax.set_xlim([0,len(bars[1])])



ax.set_ylabel(yAxisName)
ax.set_xlabel(xAxisName)
ax.set_title(plotTitle)
#ax.set_xticks(index)
#ax.set_xticklabels(bars[0])

#ax.legend( [x[0] for x in rects], names[1:] , prop={'size' :18})
ax.legend( [x[0] for x in rects], namesOfYValues , prop={'size' :18}, loc='lower left')




def setAxLinesBW(ax):
    """
    Take each Line2D in the axes, ax, and convert the line style to be
    suitable for black and white viewing.
    """
    MARKERSIZE = 5

    COLORMAP = {
        'b': {'marker': 'o', 'dash': (None,None)},
        'g': {'marker': 's', 'dash': [5,5]},
        'r': {'marker': '*', 'dash': [5,3,1,3]},
        'c': {'marker': 'h', 'dash': [1,3]},
        'm': {'marker': '+', 'dash': [5,2,5,2,5,10]},
        'y': {'marker': 'D', 'dash': [5,3,1,2,1,10]},
        'k': {'marker': 'o', 'dash': (None,None)} #[1,2,1,10]}
        }

    for line in ax.get_lines() + ax.get_legend().get_lines():
        origColor = line.get_color()
        line.set_color('black')
        line.set_dashes(COLORMAP[origColor]['dash'])
        line.set_marker(COLORMAP[origColor]['marker'])
        line.set_markersize(MARKERSIZE)

def setFigLinesBW(fig):
    """
    Take each axes in the figure, and for each line in the axes, make the
    line viewable in black and white.
    """
    for ax in fig.get_axes():
        setAxLinesBW(ax)


# methods below here are hacks for specific papers
# horrible hack to add constant lines for imperfect-recall paper
def addConstantLines():
    constants = {'0' :  0.000, '0.01' :  0.275, '0.02' :  0.539, '0.03' :  0.804, '0.04' :  1.078, '0.05' :  1.338, '0.06' :  1.636, '0.07' :  2.037}
    for idx, name in enumerate(namesOfYValues):
        ax.axhline(y=constants[name], marker=markers[idx], color=colors[idx], ls=linestyles[idx])


def setImperfectRecallEC15Mode():
    addConstantLines()
    ax.set_yscale('log')
    ax.set_xscale('log')
setImperfectRecallEC15Mode()

fname = sys.argv[5]
plt.tight_layout()
plt.savefig(fname.split('.')[0]+"_color."+fname.split('.')[1], dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        frameon=None)


setFigLinesBW(fig)
plt.savefig(fname.split('.')[0]+"_bw."+fname.split('.')[1], dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        frameon=None)


