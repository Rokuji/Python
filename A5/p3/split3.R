library("igraph")
library(igraphdata)
data(karate)
Karate_eb <- edge.betweenness.community(karate)
groups <- cutat(Karate_eb, 3)
colors <- terrain.colors(3, 1)
plot(karate, 
     vertex.color=colors[groups],
     vertex.size = 10,
     main="Predicted Karate Club Social Interaction Graph when the Club splits into 3 groups"
)
