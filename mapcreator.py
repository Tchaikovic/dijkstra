import os
import csv
import numpy as np

def parse_and_create_map(coordinates_directory):

    points=[]
    for filename in os.listdir(coordinates_directory):
        f = open(coordinates_directory+'/'+filename, 'r')
        reader = csv.reader(f, delimiter=',')
        app=[]
        for line in reader:
            line = [x.strip(' ') for x in line]
            app=app+line
            points=points+app
        filtered=filter(lambda a: a != '', points)

    points_matrix=[[0 for x in range(len(filtered))] for y in range(2)]

    for i in range(len(filtered)):
        points_matrix[0][i]= int(filtered[i][1:].split("y")[0])
        points_matrix[1][i] = int(filtered[i][1:].split("y")[1])

    map=[["." for x in range(max(points_matrix[0])+1)] for y in range(max(points_matrix[1])+1)]

    for i in range(len(points_matrix[0])):
        map[points_matrix[1][i]][points_matrix[0][i]]="x"

    print map
    thefile = open('map.txt', 'w')
    for item in map:
        thefile.write("%s\n" % item)

    map_output = map
    return map_output

#parse_and_create_map("test_files/mapcreator_test_files")
parse_and_create_map("CoordinateSystem")