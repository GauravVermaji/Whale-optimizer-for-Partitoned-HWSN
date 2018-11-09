# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:19:49 2016

@author: Gaurav
"""
import random
import numpy as np
import math
import matplotlib.pyplot as plt
#import time


def whale_optimizer(lb, ub, max_iter, SearchAgents_no, positions, range_RN):
    """
    :param lb: lower bound of map or area 
    :param ub: upper bound of map or area
    :param max_iter: number of times while loop executes
    :param SearchAgents_no: number of segments
    :param seg_position: given positions segments
    
    """
    print("WOA started")
    dim = 2 # 2d plain is used
    lower_value = np.amin(positions)
    upper_value = np.amax(positions)
    

    # initialize position vector and score for the leader
    leader_pos = np.zeros(dim)
    
    rand_leader_index1 = random.randint(1, SearchAgents_no)-1
    leader_pos = positions[rand_leader_index1]
    
    iteration = 0
    
    # While loop for program 
    while(iteration< max_iter):
       # print("inisde while " + str(iteration) )
        
        
        a = 2 + iteration * ((-2) / max_iter); # a decreases linearly fron 2 to 0 in Eq. (2.3)
        
        # a2 linearly dicreases from -1 to -2 to calculate t in Eq. (3.12)
        a2 = 1 + iteration * ((1) / max_iter);
        
        # Update the position of search agents
        for i in range(0, SearchAgents_no):
            r1= random.random() # r1 is a random number in [0,1]
            r2= random.random() # r2 is a random number in [0,1]
            
            A= 2*a*r1-a  # Eq. (2.3) in the paper
            C= 2*r2      # Eq. (2.4) in the paper
            
            
            b= 1;               #  parameters in Eq. (2.5)
            l= (a2-1)*random.random()+1   #  parameters in Eq. (2.5)
            
            p = random.random()        # p in Eq. (2.6)
            
            for j in range(0,dim):
                
                if p<0.5:
                    if abs(A) >= 1:
                        # Because arrays take index position from 0 to 1 while randint gerate number between 0<= i <= size(seg_position)
                        rand_leader_index = random.randint(1, SearchAgents_no)-1
                        x_rand = positions[rand_leader_index, :]
                        d_x_rand=abs( C * x_rand[j] - positions[i,j]) 
                        positions[i,j]=abs(x_rand[j] - A * d_x_rand)
                       # print("A>1")
                       # print(positions[i,:])
                        
                    elif abs(A)<1:
                       D_Leader=abs(C*leader_pos[j] - positions[i,j]) 
                       positions[i,j]=abs(leader_pos[j] - A*D_Leader)      
                     #  print("A<1")
                     #  print(positions[i,:])
                    
                elif p>=0.5:
                  
                    distance2Leader=abs(leader_pos[j] - positions[i,j])
                    # Eq. (2.5)
                    positions[i,j] = abs(distance2Leader * math.exp(b*l) * math.cos(l * 2 * math.pi) + leader_pos[j])
                   # print("P>0.5")
                   # print(positions[i,:])
                
                
        # Check if any search agent goes beyond the search space and amend it
        for i in range(0, SearchAgents_no):
            positions[i,:]=np.clip(positions[i,:],lower_value , upper_value)
            
        #print(positions)   
      #  plt.plot(positions[:,0], positions[:,1], 'r^')
      #  plt.show()
        rand_leader_index = random.randint(1, SearchAgents_no)-1
        leader_pos = positions[rand_leader_index]

        iteration += 1
    
    
    ans=[]
    ans.append(leader_pos[0])
    ans.append(leader_pos[1])
    return ans
        

				
		
		
		
