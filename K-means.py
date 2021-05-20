# Algorithm
# randomly choose k examples as initial centroids
# while true:
#   create k clusters by assigning each example to closest centroid
#   compute k new centroids by averaging examples in each cluster
#   if centroids don't change:
#           break

import math
from random import randint


# Assign all the points to the closest cluster a centroid Find the distance first from current point in data
# list to the 3 centroids compare the 3 distances then store the points with the shortest distance to any of the
# the 3 centroids to the appropriate cluster list
def assignment(Centoroids_list1,Centoroids_list3,Centoroids_list2,Data_list,Clustures_list1,Clustures_list3,Clustures_list2):
    #loop through columns of size 8
    for x in range(len(Data_list[0])) :
        #Centroid 1
        distance_x =(Data_list[0][x]-Centoroids_list1[0])*(Data_list[0][x]-Centoroids_list1[0])
        distance_y=(Data_list[1][x]-Centoroids_list1[1])*(Data_list[1][x]-Centoroids_list1[1])
        distance1=math.sqrt(distance_y+distance_x)  # type: float

        #Centroid 2
        distance_x =(Data_list[0][x]-Centoroids_list2[0])*(Data_list[0][x]-Centoroids_list2[0])
        distance_y=(Data_list[1][x]-Centoroids_list2[1])*(Data_list[1][x]-Centoroids_list2[1])
        distance2=math.sqrt(distance_y+distance_x)  # type: float

        #Centroid 3
        distance_x =(Data_list[0][x]-Centoroids_list3[0])*(Data_list[0][x]-Centoroids_list3[0])
        distance_y=(Data_list[1][x]-Centoroids_list3[1])*(Data_list[1][x]-Centoroids_list3[1])
        distance3=math.sqrt(distance_y+distance_x)  # type: float

        # find the cluster each point belongs to
        if(distance1<distance2) & (distance1<distance3):
            Clustures_list1.append(x)
        elif (distance2<distance1) & (distance2<distance3):
            Clustures_list2.append(x)
        else:
            Clustures_list3.append(x)

#  Recompute the centroids of the newly formed clusters
def recompute(Data_list,Cluster_list):
   #compute the means of all points in the assigned to the cluster
   Centroid=[]
   sum_x=0
   sum_y=0
   for i in range(len(Cluster_list)):
       pos=Cluster_list[i]
       x=Data_list[0][pos]
       y=Data_list[1][pos]
       sum_x=sum_x+x
       sum_y=sum_y+y

   position_x=sum_x/len(Cluster_list) # type: float
   position_y=sum_y/len(Cluster_list)  # type: float
   Centroid.insert(0,position_x)
   Centroid.insert(1,position_y)
   return Centroid

# compare distances between old centroids list and new centroids list to see if they do not converge
def compare(List2, List1):
    sum=0
    dist_x=(List2[0]-List1[0])*(List2[0]-List1[0])
    dist_y=(List2[1]-List1[1])*(List2[1]-List1[1])
    dist=math.sqrt(dist_x+dist_y)
    sum=sum+dist
    if(sum==0):
        return True
    else:
        False

Clustures_list1=[]
Clustures_list2=[]
Clustures_list3=[]
Data_list=[[2, 2, 8, 5, 7, 6, 1, 4],[10, 5, 4, 8, 5, 4,2,9 ]]
# Step 1 initialize number of clusters =3
k=3

# Step 2 initialize select random points from data as centroids
Centoroids_list1=[2.0,10.0]  # type: float
Centoroids_list2=[5.0,8.0]  # type: float
Centoroids_list3=[1.0,2]  # type: float

Iteration_num=1
for i in range(100000000):

    #Step 3  Assign all the points to the closest cluster a centroid Find the distance first from current point in data
    if (len(Clustures_list1)!=0):
        del Clustures_list1[:]
    if (len(Clustures_list2)!=0):
        del Clustures_list2[:]
    if (len(Clustures_list3)!=0):
        del Clustures_list3[:]
    assignment(Centoroids_list1,Centoroids_list2,Centoroids_list3,Data_list,Clustures_list1,Clustures_list2,Clustures_list3)

    Prev_Centroid1=Centoroids_list1
    Prev_Centroid2=Centoroids_list2
    Prev_Centroid3=Centoroids_list3

    # Step 4 Recompute the centroids of the newly formed clusters
    #recompute(Data_list,Clustures_list1,Clustures_list2,Clustures_list3,Centoroids_list1,Centoroids_list3,Centoroids_list2)
    Centoroids_list1=recompute(Data_list,Clustures_list1)
    Centoroids_list2=recompute(Data_list,Clustures_list2)
    Centoroids_list3=recompute(Data_list,Clustures_list3)
    flag0=compare(Centoroids_list1,Prev_Centroid1)
    flag1=compare(Centoroids_list2,Prev_Centroid2)
    flag2=compare(Centoroids_list3,Prev_Centroid3)

    # Step5 repeat 3 & 4
    # Condition to stop
    # Centroids of newly formed clusters do not change i.e.(Prev Centroids_list== Current Centroids_list)
    # Points remain in the same cluster i.e.(Prev Cluster1_list==Current Cluster1_list or Cluster2_list==Cluster2_list)

    if(flag0==True) & (flag2==True) &(flag1==True):
        break
    else:
        print('Iteration ',Iteration_num)

        print("Cluster1: ")
        for i in range (len(Clustures_list1)):
            print(Clustures_list1[i])
        print("Centroid1: ")
        for i in range (len(Centoroids_list1)):
            print(Centoroids_list1[i])

        print("Cluster2: ")
        for i in range (len(Clustures_list2)):
            print(Clustures_list2[i])
        print("Centroid2: ")
        for i in range (len(Centoroids_list2)):
            print(Centoroids_list2[i])

        print("Cluster3: ")
        for i in range (len(Clustures_list3)):
            print(Clustures_list3[i])
        print("Centroid3: ")
        for i in range (len(Centoroids_list3)):
            print(Centoroids_list3[i])

    Iteration_num=Iteration_num+1


















