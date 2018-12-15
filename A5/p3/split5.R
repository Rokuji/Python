library("igraph")
library(igraphdata)
data(karate)
Karate_eb <- edge.betweenness.community(karate)
groups <- cutat(Karate_eb, 5)
colors <- terrain.colors(5, 1)
plot(karate, 
     vertex.color=colors[groups],
     vertex.size = 10,
     main="Predicted Karate Club Social Interaction Graph when the Club splits into 5 groups"
)