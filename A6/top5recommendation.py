import recommendations as rec

pref= rec.loadMovieLens()
recom = rec.getRecommendations(pref, '73')

print "Five Most recommended Movies for My Substitute: " + '73'
print "--------------------------------------------------------"
for movie in recom[:5]:
        print movie[1]

print "--------------------------------------------------------"

print "Five Least Recommended Movies for My Substitute: " + '73'
print "--------------------------------------------------------"
for movie in recom[-5:]:
        print movie[1]

print "--------------------------------------------------------"
