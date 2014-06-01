'''
Created on 31-May-2014

@author: akhilkarra
'''
if __name__ == '__main__':
    class CricketPlayer:
        'Class to represent Cricket player in cricket attax game'
        name = ""
        team = ""
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
        
    def display():
        print "name %s, team %s, bowling %s, batting %s, stars %s, runs %s, point %s" % (name, team, bowling, batting, stars, runs, points)
            
            


    
    