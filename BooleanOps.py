'''
Created on 26-May-2014

@author: akhilkarra
'''

"""
     Boolean Operators
---------------------------
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""

"""
This and That (or This, But Not That!)
Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, there's an order of operations for boolean operators:

not is evaluated first;
and is evaluated next;
or is evaluated last.
For example, True or not False and False returns True. If this isn't clear, look at the Hint.

Parentheses () ensure your expressions are evaluated in the order you want. Anything in parentheses is evaluated as its own unit.

"""

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
