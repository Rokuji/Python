import recommendations as rec

pref= rec.loadMovieLens()
correlated = rec.topMatches(1, pref, '73')
noncorrelated =  rec.topMatches(0, pref, '73')
print "Five Most Correlated Users: " + '73'
print "--------------------------------------------------------"
for user in correlated:
	print user[1]

print "--------------------------------------------------------"

print "Five Least Correlated Users: " + '73'
print "--------------------------------------------------------"
for user in noncorrelated:
	print user[1]