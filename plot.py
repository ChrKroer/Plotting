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

matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True

if len(sys.argv) < 6:
    print "\n\nHow to use:"
    print "Sys.argv[1]: Path to input file"
    print "Sys.argv[2]: Title of plot"
    print "Sys.argv[3]: x-axis name"
    print "Sys.argv[4]: y-axis name"
    print "Sys.argv[5]: Filename to save to \n"
    quit()



colors = ['y', 'g', 'r', 'c', 'm', 'b', 'k', 'w']
linestyles = ['-', '--', '-.', ':', '-', '--', 'k', 'w']
markers = ['o', '+', '*', 'h', 's', 'D', 'p', 'w']
width = 0.15       # the width of the bars


data = open(sys.argv[1])
names = data.readline().split('\t')
bars = [[] for i in  range((len(names))) if names[i].lstrip()]

# epsilon is added to each bar to force visibility, otherwise matplotlib squeezes it
epsilon = 1e-7

for line in data:
    for idx, entry in enumerate(line.split('\t')):
        if entry.lstrip():
            bars[idx].append(int(entry))



index = np.arange(len(bars[0]))  # the x locations for the groups
#print index
fig, ax = plt.subplots()
rects = []

# x_offset for arrows when a plot is immediately zero
x_offset = 40
y_offset = 20

for idx, bar in enumerate(bars[1:]):
    rects.append(ax.plot(index, bar, marker=markers[idx], color=colors[idx], ls=linestyles[idx]))
    if bar[0] is 0:
        label = names[idx+1]
        x = 0
        y = 0
        plt.annotate(
            "{0}".format(label),
            xy = (x, y), xytext = (x_offset, y_offset),
            textcoords = 'offset points', ha = 'right', va = 'bottom',
            #bbox = dict(boxstyle = 'round,pad=0.1', fc = 'white', alpha = 0.5),
            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
        x_offset += 20
        y_offset -= 10


plt.rcParams.update({'font.size': 22})
#ax.set_ylim(-0.5)
ax.set_xlim([0,len(bars[1])])
ax.set_ylabel(sys.argv[4])
ax.set_xlabel(sys.argv[3])
ax.set_title(sys.argv[2])
ax.set_xticks(index)
ax.set_xticklabels(bars[0])

ax.legend( [x[0] for x in rects], names[1:] , prop={'size' :18})


fname = sys.argv[5]
plt.tight_layout()
plt.savefig(fname, dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        frameon=None)


