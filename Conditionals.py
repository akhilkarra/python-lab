'''
Created on 26-May-2014

@author: akhilkarra
'''

if __name__ == '__main__':
    def the_flying_circus():
        x = raw_input("What number do you choose?")
        
        if (x % 3 == 0 and x % 5 == 0):
            print "Divisible by three and five"
        elif ( x % 4 == 0):
            print "Divisible by four"
        else:
            print "Not divisible by (three and five) or four"
        return True