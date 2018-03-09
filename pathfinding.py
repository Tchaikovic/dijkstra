from ast import literal_eval
import ast
import numpy as np

def check_not_already_added(list1,list2):
    k=0
    if list2!=[]:
        for i in range(len(list2)/3):
            if list1[0:2]==list2[3*i:3*i+2]:
                k=1
    if k==0:
        return True
    if k==1:
        return False

def plot_shortest_path(path):
    start=path[len(path)-3:]
    distance=start[2]
    shortest=start[:2]
    point=start[:]
    while distance!=0:
        for i in range(len(path)/3):
            if bool(abs(sum(point[0:2])-sum(path[3 * i:3 * i + 2]))==1) & bool(path[3*i+2]==distance-1):
                point=path[3 * i:3 * i + 2]
                distance=distance-1
                shortest=shortest+point
    return shortest


def path_between_points(start_x, start_y, end_x, end_y, map_file_location):
    text_file = open(map_file_location+"/map.txt", "r")
    lines = text_file.readlines()
    aus=[end_x, end_y, 0]
    k=1
    path=[]
    path=path+aus

    count=1
    new_nodes_list=[end_x, end_y, 0]
    while k!=0:
        list = []
        for i in range(len(new_nodes_list)/3):
            print i
            print 'working on point',new_nodes_list[3*i],new_nodes_list[3*i+1]
            if bool(lines[new_nodes_list[3*i]+1][2+5*new_nodes_list[3*i+1]]!='x') & check_not_already_added([new_nodes_list[3 * i] + 1, new_nodes_list[3 * i + 1]], path):
                list = list + [new_nodes_list[3 * i] + 1, new_nodes_list[3 * i + 1], count]
                path = path + [new_nodes_list[3 * i] + 1, new_nodes_list[3 * i + 1], count]
                if [new_nodes_list[3*i]+1,new_nodes_list[3*i+1]]==[start_x,start_y]:
                    k=0
            if bool(lines[new_nodes_list[3*i]-1][2+5*new_nodes_list[3*i+1]] != 'x') & check_not_already_added([new_nodes_list[3 * i] - 1, new_nodes_list[3 * i + 1]], path):
                list = list + [new_nodes_list[3 * i] - 1, new_nodes_list[3 * i + 1], count]
                path = path + [new_nodes_list[3 * i] - 1, new_nodes_list[3 * i + 1], count]
                if [new_nodes_list[3*i]-1, new_nodes_list[3*i+1]]==[start_x,start_y]:
                    k=0
            if bool(lines[new_nodes_list[3*i]][2+5*(new_nodes_list[3*i+1]+1)] != 'x') & check_not_already_added([new_nodes_list[3 * i], new_nodes_list[3 * i + 1] +1], path):
                list = list + [new_nodes_list[3 * i], new_nodes_list[3 * i + 1] + 1, count]
                path = path + [new_nodes_list[3 * i], new_nodes_list[3 * i + 1] + 1, count]
                if [new_nodes_list[3*i], new_nodes_list[3*i+1]+1] == [start_x,start_y]:
                    k=0
            if bool(lines[new_nodes_list[3*i]][2+5*(new_nodes_list[3*i+1]-1)] != 'x') & check_not_already_added([new_nodes_list[3 * i], new_nodes_list[3 * i + 1]-1], path):
                list = list + [new_nodes_list[3 * i], new_nodes_list[3 * i + 1] - 1, count]
                path = path + [new_nodes_list[3 * i], new_nodes_list[3 * i + 1] - 1, count]
                #print list
                if [new_nodes_list[3*i], new_nodes_list[3*i+1]-1]==[start_x, start_y]:
                    k=0

        count=count+1
        new_nodes_list = list[:]



    shortest=plot_shortest_path(path)
    #a="S"
    #a=np.zeros()
    #lines[shortest[0]][2+5*shortest[1]]='S'
    a=lines[shortest[0]]
    b=a[0:2+5*shortest[1]]+'S'+a[2+5*shortest[1]+1:]
    lines[shortest[0]]=b
    #print b
    #print a
    #lines[shortest[len(shortest)-1]][2+5*shortest[len(shortest)]]='E'
    #print shortest[len(shortest)-2]

    a = lines[shortest[len(shortest)-2]]
    #print shortest[len(shortest)-1]
    b = a[0:2+5*shortest[len(shortest)-1]] + 'E' + a[2+5*shortest[len(shortest)-1]+1:]
    lines[shortest[len(shortest)-2]] = b

    for i in range(len(shortest)/2-2):
        a = lines[shortest[2+2*i]]
        b = a[0:2 + 5 * shortest[2+2*i+1]] + 'O' + a[2 + 5 * shortest[2+2*i+1]+1:]
        lines[shortest[2+2*i]]=b
        #lines[shortest[2+2*i]][2 + 5 * shortest[2+2*i+1]] = 'O'


    thefile = open('shortest_path.txt', 'w')
    for item in lines:
        thefile.write("%s\n" % item)
    map_output = lines

    return map_output


path_between_points(1,1,5,4,"map")