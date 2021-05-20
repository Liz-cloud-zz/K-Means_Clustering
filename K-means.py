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
    for x in range(8) :
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
def recompute(Data_list,Clustures_list1,Clustures_list2,Clustures_list3,Centoroids_list1,Centoroids_list3,Centoroids_list2):
    #compute the means of all points in the assigned to the cluster
    sum=0
    for i in range(len(Clustures_list1)):
        sum=sum+Clustures_list1[i];
    position=sum/len(Clustures_list1)
    Centoroids_list1.insert(0,Data_list[0][position])
    Centoroids_list1.insert(1,Data_list[1][position])

    for i in range(len(Clustures_list2)):
        sum=sum+Clustures_list2[i]
    position=sum/len(Clustures_list2)
    Centoroids_list2.insert(0,Data_list[0][position])
    Centoroids_list2.insert(1,Data_list[1][position])

    for i in range(len(Clustures_list3)):
        sum=sum+Clustures_list3[i]
    position=sum/len(Clustures_list3)
    Centoroids_list3.insert(0,Data_list[0][position])
    Centoroids_list3.insert(1,Data_list[1][position])

# compare 2 lists
def compare(List1, List2):
    a=set(List1)
    b=set(List2)
    if a==b:
        return True
    else:
        return False

Clustures_list1=[]
Clustures_list2=[]
Clustures_list3=[]
Data_list=[[2, 2, 8, 5, 7, 6, 1, 4],[10, 5, 4, 8, 5, 4,2,9 ]]
# Step 1 initialize number of clusters =3
k=3

# Step 2 initialize select random points from data as centroids
Centoroids_list1=[2,10]
Centoroids_list2=[5,8]
Centoroids_list3=[1,2]

for i in range(100000):
    Iteration_num=1
    Prev_Centroid1=Centoroids_list1
    Prev_Centroid2=Centoroids_list2
    Prev_Centroid3=Centoroids_list3

    #Step 3  Assign all the points to the closest cluster a centroid Find the distance first from current point in data
    assignment(Centoroids_list1,Centoroids_list2,Centoroids_list3,Data_list,Clustures_list1,Clustures_list2,Clustures_list3)
    flag0=compare(Centoroids_list1,Prev_Centroid1)
    flag1=compare(Centoroids_list2,Prev_Centroid2)
    flag2=compare(Centoroids_list3,Prev_Centroid3)

    Prev_Cluster1=Clustures_list1
    Prev_Cluster2=Clustures_list2
    Prev_Cluster3=Clustures_list3

    # Step 4 Recompute the centroids of the newly formed clusters
    recompute(Data_list,Clustures_list1,Clustures_list2,Clustures_list3,Centoroids_list1,Centoroids_list3,Centoroids_list2)
    flag3=compare(Clustures_list1,Prev_Cluster1)
    flag4=compare(Clustures_list2,Prev_Cluster2)
    flag5=compare(Clustures_list3,Prev_Cluster3)

    # Step5 repeat 3 & 4
    # Condition to stop
    # Centroids of newly formed clusters do not change i.e.(Prev Centroids_list== Current Centroids_list)
    # Points remain in the same cluster i.e.(Prev Cluster1_list==Current Cluster1_list or Cluster2_list==Cluster2_list)

    if(flag0==flag1) & (flag0==flag2):
        if(flag3==flag4) & (flag3==flag5):
            break
        else:
            print("Iteration ",Iteration_num)

            print("Cluster1: ")
            for i in range (len(Clustures_list1)):
                print(Clustures_list1[i])
            print('\n')
            print("Centroid1: (")
            for i in range (len(Centoroids_list1)):
                print(Centoroids_list1[i])

            print("Cluster2: ")
            for i in range (len(Clustures_list2)):
                print(Clustures_list2[i])
            print('\n')
            print("Centroid2: (")
            for i in range (len(Centoroids_list2)):
                print(Centoroids_list2[i])

            print("Cluster3: ")
            for i in range (len(Clustures_list3)):
                print(Clustures_list3[i])
            print('\n')
            print("Centroid3: (")
            for i in range (len(Centoroids_list3)):
                print(Centoroids_list3[i])

            # print("Iteration",end='')
            # print (Iteration_num, end='\n')
            # print("Cluster 1:", end=' ')
            # print (*Clustures_list1, sep=',')
            # print ("Centroid: (",end='')
            # print (*Centoroids_list, sep=',')
            # print (")", end='\n')
            #
            # print("Cluster 2: ")
            # print (*Clustures_list2, sep=',')
            # print ("Centroid: (",end="")
            # print (*Centoroids_list, sep=',')
            # print (")", end='\n')
            #
            # print("Cluster 3: ")
            # print (*Clustures_list3, sep=',')
            # print ("Centroid: (",end='')
            # print (*Centoroids_list, sep=',')
            # print (")", end='\n')

            # increment iteration
            Iteration_num=Iteration_num+1

















