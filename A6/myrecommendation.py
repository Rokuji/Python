import recommendations as rec

pref= rec.loadMovieLens()

top = 'Toy Story (1995)'
bot = 'Braveheart (1995)'

topmov = rec.calculateSimilarItems(1, pref, 5)
botmov = rec.calculateSimilarItems(0, pref, 5)

print 'Best Recommended movies for ' + top + ':'
print '---------------------------------------------------------------'
for movie in topmov[top]:
    print movie[1]
print "--------------------------------------------------------"
print 'Least Recommended movies for ' + top + ':'
print '---------------------------------------------------------------'
for movie in botmov[top]:
    print movie[1]
print "--------------------------------------------------------"
print 'Best Recommended movies for ' + bot + ':'
print '---------------------------------------------------------------'
for movie in topmov[bot]:
    print movie[1]
print "--------------------------------------------------------"
print 'Least Recommended movies for' + bot + ':'
print '---------------------------------------------------------------'
for movie in botmov[bot]:
    print movie[1]
print "--------------------------------------------------------"
