Boolean Operators
=================

 And                       | Or                         |  Not
-------------------------- | -------------------------- |  --------------------                     
* True and True is True    | * True or True is True     | * Not True is False
* True and False is False  | * True or False is True    | * Not False is True
* False and True is False  | * False or True is True    | 
* False and False is False | * False or False is False  |



This and That (or This, But Not That!)
Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, there's an order of operations for boolean operators:

not is evaluated first;
and is evaluated next;
or is evaluated last.
For example, True or not False and False returns True. If this isn't clear, look at the Hint.

Parentheses () ensure your expressions are evaluated in the order you want. Anything in parentheses is evaluated as its own unit.
