# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:19:49 2016

@author: Gaurav
"""


# this is the main file
# just run it and file the parameters

import numpy as np
import random
import math
import WOA
import matplotlib.pyplot as plt
import time
# to get the convex hull from given set of points
from scipy.spatial import ConvexHull
# to check whether point lie inside a convex hull or not
from matplotlib.path import Path


start = time.time()
def Euclid_distance(q, w):
    """
    :param q: seg [i][x] value
    :param w: seg [i][y] value
    :param e: seg [j][x] value
    :param r: seg [j][y] value
    :return: Euclidain distance of 2 segments
    """
    vector1 = q
    vector2 = w
    dist = [(a - b) ** 2 for a, b in zip(vector1, vector2)]
    dist = math.sqrt(sum(dist))
    return dist
count_relay_list = []

loop =  1
for _ in range(loop):
    Lower = 0  # lower values of x and y cordinates
      # upper values of x and y cordinates
    
    #   area is a square value
    area = 1000 #int(input("Ënter the size of area: "))
    
    range_RN = 150  #float(input("Enter the communication range of Relay Node: "))

    Upper = area
    
    num_of_seg = 7 #int(input("Enter the Number of disconnecte Segments: "))
    
    
    count_Relay = num_of_seg  # Initial count of relay nodes
    
    # Seg_positions is a numpy 2D array contaianing the positions of
    # segments in terms of x and y cordinates
    seg_positions = np.zeros((num_of_seg, 2), dtype=np.int)
    
    # it's a 2d list used to keep track of relay nodes in same segments.
    seg_obj_list = []
    
    #check_node_list is a list to cancel a node which is already present in list this wil decrease node count and give actual answer
    check_node_list = []
    ###############################
    # as vector al
    
    """
    # to place random values    
    for i in range(num_of_seg):
        #x_seg, y_seg = input("Enter the cordinate of segment " + str(i + 1) + " : ").strip().split()
        x_seg, y_seg = random.randint(0,area), random.randint(0,area)
        seg_positions[i] = [x_seg, y_seg]
        #########################################
        # Add all relay nodes as seperate segments as a 2d list
    
        seg_obj_list.append([x_seg, y_seg])
        check_node_list.append([x_seg, y_seg])
            
400	300
600	300
78	56
251	500
500	800

    """
    seg_obj_list = [[800,900],[900,950],[250,200],[200,600],[500,700],[700,200],[400,50]]
    seg_positions = np.array([[800,900],[900,950],[250,200],[200,600],[500,700],[700,200],[400,50]])
    check_node_list = [[800,900],[900,950],[100,200],[200,600],[500,700],[700,200],[400,108]]
    
    """#############################################################
    print("beta 1")
    print(seg_positions)
    print(seg_obj_list)
    #########"""
    
    # To print segments
    for i in range(len(seg_obj_list)):
        print("Segment " + str(i + 1) + " : x = " + str(seg_obj_list[i][0]) + ", y = " + str(seg_obj_list[i][1]))
    
    #################################################
    # Decreasing no. of segments by using euclidian distance
    i, j = 0, 1
    flag1 = False
    while(i< len(seg_obj_list) and len(seg_obj_list) != 1):
        
        
        while(j< len(seg_obj_list)):
            flag1 = False
            print(str(i) + ", " + str(j))
            if (Euclid_distance(seg_obj_list[i], seg_obj_list[j]) < range_RN * 2):
                print("Segment " + str(j + 1) + ": x = " + str(seg_obj_list[j][0]) + ",y = " + str(
                    seg_obj_list[j][1]) + " is in range of segment " + str(i + 1) + ": x = " + str(
                    seg_obj_list[i][0]) + ",y = " + str(seg_obj_list[i][1]))
                # add segment j in segment i and remove segment j from seg_obj_list and numpy array segment_position
                seg_obj_list[i] = seg_obj_list[i] + seg_obj_list[j]
                # deleting j segment from seg_obj_list
                del seg_obj_list[j]
                # delete x and y values of j segment from seg_postion
                seg_positions = np.delete(seg_positions, j, 0)
    
                # restart the indexs i and j
                i, j = 0, i + 1
                print("i = " + str(i) + ", j = " + str(j))
                print(seg_obj_list)
                flag1 = True
            
            if flag1 == False:
                j +=1
        if(flag1 == False):
            i += 1
            """#########################################################
        print("beta 2")
        print(seg_positions)
        print(seg_obj_list)
    ##############################################################"""
    
    print ("BEfore whhile loop")
    while_count = 1
    ################################################
    # while loop
    while (np.size(seg_positions) > 4):
        print("inside While count = " + str(while_count))
        while_count +=1
        print(seg_positions)
    
        for i in range(len(seg_obj_list)):
            print("Segment " + str(i + 1) + " : x = " + str(seg_obj_list[i][0]) + ", y = " + str(seg_obj_list[i][1]))
    
        ############################################
        # XX is a copy of seg_positions numpy array
        XX = seg_positions.copy()
    
        ##############################
        # calling Whale optimization algo function
        # it will return a point as a list
        ans = WOA.whale_optimizer(Lower, Upper, 5, np.size(seg_positions, axis=0), XX, range_RN)
    
        # create a concex hull from given segments
        seg_polygen = ConvexHull(seg_positions)
    
        # To Check whether a point lie inside polygen or not
        seg_polygen_path = Path(seg_positions[seg_polygen.vertices])
    
        # contain_point takes a point ans check whether it lies inside polygen
        # or not. the popnt is ans list return by whale optimization algo
        if (seg_polygen_path.contains_point(ans) and (ans not in check_node_list)):
            count_Relay += 1
            check_node_list.append(ans)
    
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("\n")
            print("relay node added count increased to " + str(count_Relay))
            print("Cordinates are x = " + str(ans[0]) + ", y = " + str(ans[1]))
    
            # a list which store position of segment in range
            seg_in_range = []
    
            for i in range(len(seg_obj_list)):
    
                flag = True
    
                # if seg_obj_list is not empty then checking segments in range
                if (len(seg_obj_list[i]) > 0):
                    for j in range(0, len(seg_obj_list[i]), 2):
                        if (Euclid_distance(ans, seg_obj_list[i][j : j+2]) < range_RN * 2 and flag):
                            print("Node x = " + str(seg_obj_list[i][j]) + " y = " + str(
                                seg_obj_list[i][j + 1]) + " of segment " + str(
                                i + 1) + " with in range of current relay node")
                            seg_in_range.append(i)
                            flag = False
    
            if (len(seg_in_range) == 0):
                seg_obj_list.append(ans)
    
                seg_positions = np.append(seg_positions, [ans], axis=0)
                
                
                """#######################################33
                print("beta 3")
                print(seg_positions)
                print(seg_obj_list)
    ############################################################"""
    
            elif (len(seg_in_range) == 1):
                seg_obj_list[seg_in_range[0]].append(ans[0])
                seg_obj_list[seg_in_range[0]].append(ans[1])
                
                """##############################################33
                print("beta 4")
                print(seg_positions)
                print(seg_obj_list)
    ###########################################################"""
    
            else:
                temp1 = 0
                temp2 = 0
                for i in range(1, len(seg_in_range)):
                    # to add all the nodes of neigbor segment in segment[seg_in_range[0]]
                    seg_obj_list[seg_in_range[0]] = seg_obj_list[seg_in_range[0]] + seg_obj_list[seg_in_range[i] - temp2]
    
                    # delete the segment which is added from seg_obj_list
                    del seg_obj_list[seg_in_range[i] - temp2]
    
                    # also delete them from seg_position numpy array
                    seg_positions = np.delete(seg_positions, (seg_in_range[i] - temp1), axis=0)
                    
                    temp2 +=1
                    temp1 +=1
                # finally add current relay node in first segment
    
                seg_obj_list[seg_in_range[0]].append(ans[0])
                seg_obj_list[seg_in_range[0]].append(ans[1])
                
                """###########################################################
                print("beta 6")
                print(seg_positions)
                print(seg_obj_list)
    #######################################################3"""
                
            plt.plot(seg_positions[:,0], seg_positions[:,1], 'g^')
            plt.show()
    
    
        else:
            print("Discarded Relay Node  x = " + str(ans[0]) + ", y = " + str(ans[1]))
    
    print("Last segments are")
    for i in range(np.size(seg_positions, axis=0)):
        print(seg_positions[i])
    
    if (np.size(seg_positions, axis= 0) > 1):
        count_Relay += int(((Euclid_distance(seg_positions[0], seg_positions[1]) - 2 * range_RN) / (2 * range_RN)) + 1)
    
    print("Total relay node count = " + str(count_Relay))
    
    """
    np_node_list = np.array(check_node_list)
    plt.plot(np_node_list[:,0], np_node_list[:,1], 'bo')
    plt.show()
    """
    
    count_relay_list.append(count_Relay)

average = sum(count_relay_list)/loop
print(average)
end = time.time()
print("average execution time")
total_time = (end-start)/loop

print ("max = " + str(max(count_relay_list )))
print("min = " + str(min(count_relay_list)))
print(total_time)
