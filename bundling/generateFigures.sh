#!/bin/bash


# make bar graph version

python ~/github/Plotting/bargraph.py ~/Documents/research/channel_abstraction/data-2014/num_solved_arbitrary.txt 'Arbitrary distribution' '#items' '#solved' ~/Dropbox/christian-tuomas-shared/bundling/figures/arbitrary_items_bar.pdf

python ~/github/Plotting/bargraph.py ~/Documents/research/channel_abstraction/data-2014/num_solved_regions.txt 'Regions distribution' '#items' '#solved' ~/Dropbox/christian-tuomas-shared/bundling/figures/regions_items_bar.pdf

python ~/github/Plotting/bargraph.py ~/Documents/research/channel_abstraction/data-2014/num_solved_matching.txt 'Matching distribution' '#items' '#solved' ~/Dropbox/christian-tuomas-shared/bundling/figures/matching_items_bar.pdf

python ~/github/Plotting/bargraph.py ~/Documents/research/channel_abstraction/data-2014/num_solved_scheduling.txt 'Scheduling distribution' '#items' '#solved' ~/Dropbox/christian-tuomas-shared/bundling/figures/scheduling_items_bar.pdf

python ~/github/Plotting/bargraph.py ~/Documents/research/channel_abstraction/data-2014/num_solved_paths.txt 'Paths distribution' '#items' '#solved' ~/Dropbox/christian-tuomas-shared/bundling/figures/paths_items_bar.pdf

# make plot version

python ~/github/Plotting/plot.py ~/Documents/research/channel_abstraction/data-2014/num_solved_arbitrary.txt 'Arbitrary distribution' '#items' '#solved' ~/Dropbox/christian-tuomas-shared/bundling/figures/arbitrary_items_plot.pdf

python ~/github/Plotting/plot.py ~/Documents/research/channel_abstraction/data-2014/num_solved_regions.txt 'Regions distribution' '#items' '#solved' ~/Dropbox/christian-tuomas-shared/bundling/figures/regions_items_plot.pdf

python ~/github/Plotting/plot.py ~/Documents/research/channel_abstraction/data-2014/num_solved_matching.txt 'Matching distribution' '#items' '#solved' ~/Dropbox/christian-tuomas-shared/bundling/figures/matching_items_plot.pdf

python ~/github/Plotting/plot.py ~/Documents/research/channel_abstraction/data-2014/num_solved_scheduling.txt 'Scheduling distribution' '#items' '#solved' ~/Dropbox/christian-tuomas-shared/bundling/figures/scheduling_items_plot.pdf

python ~/github/Plotting/plot.py ~/Documents/research/channel_abstraction/data-2014/num_solved_paths.txt 'Paths distribution' '#items' '#solved' ~/Dropbox/christian-tuomas-shared/bundling/figures/paths_items_plot.pdf
