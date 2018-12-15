library(igraph)
library(igraphdata)
data(karate)
plot.igraph(karate,
            vertex.color="white",
            vertex.size = 10,
            main="Karate Club Social Interaction Graph Before Club Fission"
)
