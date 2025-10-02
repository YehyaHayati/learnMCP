---
tags:
  - AI-900
  - Azure
  - MLConcepts
  - Clustering
  - UnsupervisedLearning
---
_Clustering_ is a form of unsupervised machine learning in which ==observations are grouped into clusters based on similarities in their data values, or features==. This kind of machine learning is considered unsupervised because it ==doesn't make use of previously known label values to train a model.== In a clustering model, the label is the cluster to which the observation is assigned, based only on its features.
### Evaluating a clustering model
Since there's no known label with which to compare the predicted cluster assignments, ==evaluation of a clustering model is based on how well the resulting clusters are separated from one another.==
There are multiple metrics that you can use to evaluate cluster separation, including:
- **==Average distance to cluster center==**: How close, on average, each point in the cluster is to the centroid of the cluster.
- **==Average distance to other center==**: How close, on average, each point in the cluster is to the centroid of all other clusters.
- **==Maximum distance to cluster center==**: The furthest distance between a point in the cluster and its centroid.
- **==Silhouette==**: A value between -1 and 1 that summarizes the ratio of distance between points in the same cluster and points in different clusters (The closer to 1, the better the cluster separation).