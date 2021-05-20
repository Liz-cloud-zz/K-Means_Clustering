# Step 1 initialize number of clusters =3
# Step 2 initialize select random points from data as centroids with number 1,4,7 coordinate points
# Step 3  Assign all the points to the closest cluster a centroid Find the distance first from current point in data
# Step 4 Recompute the centroids of the newly formed clusters
# Step5 repeat 3 & 4
# Condition to stop
# Centroids of newly formed clusters do not change i.e.(Prev Centroids_list== Current Centroids_list)
# Points remain in the same cluster i.e.(Prev Cluster_list==Current Cluster_list)

#assignment method:
# Assign all the points to the closest cluster a centroid Find the distance first from current point in data
# list to the 3 centroids compare the 3 distances then store the points with the shortest distance to any of the
# the 3 centroids to the appropriate cluster list

#recompute method:
#  Recompute the centroids of the newly formed clusters

# compare:
# compare distances between old centroids list and new centroids list to see if they do not converge

