# Run this cell first!

from helpers import Map, load_map, show_map
from student_code import shortest_path

%load_ext autoreload
%autoreload 2

# Map basics
map_10 = load_map('map-10.pickle')
show_map(map_10)


map_10.intersections


# this shows that intersection 0 connects to intersections 7, 6, and 5
map_10.roads[0] 


# This shows the full connectivity of the map
map_10.roads


# map_40 is a bigger map than map_10
map_40 = load_map('map-40.pickle')
show_map(map_40)


# run this code, note the effect of including the optional
# parameters in the function call.
show_map(map_40, start=5, goal=34, path=[5,16,37,12,34])