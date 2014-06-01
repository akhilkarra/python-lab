'''
Created on 31-May-2014

@author: akhilkarra
'''

class CricketPlayer:
    'Class to represent Cricket player in cricket attax game'
    name = " "
    team = " "
    bowling = 0
    batting = 0
    stars = 0
    runs = 0
    points = 0

    def __init__(self, name, team, bowling, batting, stars, runs, points):
        self.name = name
        self.team = team
        self.bowling = bowling
        self.batting = batting
        self.stars = stars
        self.runs = runs
        self.points = points
   
    def print_stars(self):
        i = 0
        while(i < self.stars):
            print("*"),
            i = i + 1 
                  
    def display(self):
        print "________________________"
        print "  " , self.team, " ", self.name
        print
        print
        print
        print
        print
        print "         " , self.runs
        print "        " , "runs"
        print "  " , self.bowling, "          " , self.batting
        print "bowling" "       batting" 
        print "     " ,
        self.print_stars()
        print
        print "         ", self.points
        print "________________________"
        
    
        
            
viratKolhi = CricketPlayer("Virat Kohli", "RCB", 27, 87, 5, 32, 114)
viratKolhi.display()
    
dinesh = CricketPlayer("Dinesh Karthik", "DD", 10, 92, 5, 30, 166)
dinesh.display()

kaul = CricketPlayer("Siddarth Kaul", "DD", 57, 29, 2, 7, 36)
kaul.display()