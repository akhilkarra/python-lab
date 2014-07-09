print "Welcome to our restaurant!"

starter = raw_input("What would you like for the starters?")

if starter == "Nothing":
   print "Ok"
else:
   print "Ok, so you would like %s for your starters." % (starters)

main = raw_input("What would you like for the main course?")
print "So you would like %s for the main course" % (main)

dessert = raw_input("What would you like for the dessert?")
if dessert == "Nothing":
   print "Ok"
else:
   print "Ok, so you would like %s for your dessert." % (dessert)

if starter == "Nothing" and dessert != "Nothing":
   print "Price:"
   print 4000  + 100 
   print "Rs/-"
elif starter and dessert != "Nothing":
   print "Price:"
   print 4000 + 100  + 240 
   print "Rs/-"
elif starter and dessert == "Nothing":
   print "Price:"
   print 4000 
   print "Rs/-"  
else:
   print "Price:"
   print 240 + 4000
   print "Rs/-"  

print "Thank you for visiting our restaurant. Hope you come again!"ss