#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:27:44 2019

@author: rey10
"""

#Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#Importing the dataset
dataset = pd.read_csv('mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values

#Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i,init ="k-means++", n_init = 10,max_iter = 300, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title("The Elbow Method")
plt.xlabel("Number of clusters")
plt.ylabel('WCSS')
plt.show()

#Applying k-means to mall dataset
kmeans = KMeans(n_clusters = 5,init ="k-means++", n_init = 10,max_iter = 300, random_state = 0)
y_kmeans = kmeans.fit_predict(X)

#Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0,1], s = 100, c = "red", label = "Careful")
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1,1], s = 100, c = "green", label = "Standard")
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2,1], s = 100, c = "blue", label = "Target")
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3,1], s = 100, c = "cyan", label = "Careless")
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4,1], s = 100, c = "violet", label = "Sensible")
plt.scatter(kmeans.cluster_centers_[:, 0],kmeans.cluster_centers_[:, 1],s = 300,c ="yellow",label = "Centroids")
plt.title("Clusters of clients")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()