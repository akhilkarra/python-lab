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


starter_price = "90 Rs/-"
main_price = "4,000 Rs/-"
dessert_price = "100 Rs/-"

if starter == "Nothing" and dessert != "Nothing":
   print ("main_price  +  dessert_price")
elif starter and dessert != "Nothing":
   print ("starter_price  +  main_price  +  dessert_price")
elif starter and dessert == "Nothing":
   print main_price  
else:
   print ("starter_price"  +  "main_price")

print "Thank you for visiting our restaurant. Hope you come again!"