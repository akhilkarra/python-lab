'''
Created on 26-May-2014

@author: akhilkarra
'''

if __name__ == '__main__':
    # Use boolean expressions as appropriate on the lines below!

    # Make me false!
    bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!
    assert not bool_one

    # Make me true!
    bool_two = (2 == 2) or "Cat" == "Meow"
    assert bool_two

    # Make me false!
    bool_three = (3 == 2) and not "Dog" == "Meow"
    assert not bool_three

    # Make me true!
    bool_four = (8 == 4 + 4) and "Dog" != "Cat"
    assert bool_four

    # Make me true!
    bool_five = (4 == 4) and "Car" != "Bus"
    assert bool_five
