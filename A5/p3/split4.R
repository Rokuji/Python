library("igraph")
library(igraphdata)
data(karate)
Karate_eb <- edge.betweenness.community(karate)
groups <- cutat(Karate_eb, 4)
colors <- terrain.colors(4, 1)
plot(karate, 
     vertex.color=colors[groups],
     vertex.size = 10,
     main="Predicted Karate Club Social Interaction Graph when the Club splits into 4 groups"
)
