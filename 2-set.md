# Set

In some mathematics courses you might have learned something about sets, maybe you remember the Venn diagram and some operations related with sets, if not that’s okay. In Computer Science we have this type of data structure, we will learn some about this using Python as our tool. 

As mentioned about Python, this programming language has it's own build-in function to create Sets and to make operations with it. This is how you create a set in Python:

``` python
# When creating an empty set you need to explicitly write 'set' followed by a parenthesis.
mySet = set()

# You can also create a set with values already in it, for this you need to use the curly braces.
anotherSet = {1,2,3}
```


## Characteristics

The set data structure has characteristics that make a high contrast with other types of collections of elements. Elements in Sets have the following characteristics:

* Don't follow any particular order
* Are unique
* Are hashable 

Some clarifications on this, disregarding how you add or create a Set, the order in which the elements are placed will not matter. They are unique in the sense that even if you try to add an element in the set that already is in there it will ignore it and keep the one that’s already there. Objects in Sets have to be hashable, the Python documentattion explains this:

> _"An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method), and can be compared to other objects (it needs an __eq__() method). Hashable objects which compare equal must have the same hash value." <br/> _"Most of Python’s immutable built-in objects are hashable; mutable containers (such as lists or dictionaries) are not; immutable containers (such as tuples and frozensets) are only hashable if their elements are hashable."_ [Python Documentation](https://docs.python.org/3/glossary.html#term-hashable)



``` python
# Sets can be made of integers
intSet = {1,2,3}

# They can also be made of strings
strSet = {'Hi', 'I', 'am', 'a', 'set'}

# Remeber, sets can be made of any hashable objects
coolSet = {1, 'cool', 3.5, False, (1,2,3)}

```
## Operations

Sets contain many interesting operations, some of the most relevant are the following:

* Union
* Intersection
* Difference
* Symmetric Difference

![set-operations](images/set-operations.png)

Python include both operators and methods for this operations in sets. We will review both. Even thou they both accomplish the same task there is a difference between them. We will use the union operations to explain their differences.

``` python
# Union Example

set1 = {1,2,3}
set2 = {3,4,5}

# Union operation using operator, this will work
set1 | set2

# This won't work
set1 | (4,5,6)

# Union operation usign method, this will work
set1.union((4,5,6))

# Result: {1,2,3,4,5}

```
The **union operation** will return a set containing all values found in both sets, with no duplicates. 

Methods will take any iterable as an argument and will convert it into a set, allowing different opeartions to work. Operators in the other hand require for both arguments to be sets, otherwise won't work.

``` python
# Intersection Example

set1 = {1,2,3}
set2 = {3,4,5}

# Intersection Operator
set1 & set2

#Intersection Method
set1.intersection(set2)

# Result: {3}

```
The **intersection operation** will return values only found in both sets.

``` python
# Difference Example

set1 = {1,2,3}
set2 = {3,4,5}

# Difference Operator
set1 - set2

# Difference Method
set1.difference(set2)

# Result: {1,2}
```
The **difference operation** will return the values in set1 excluding those that are also in set2.

```python
# Symmetric Difference

set1 = {1,2,3}
set2 = {3,4,5}

# Symmetric Difference Operator
set1 ^ set2

#Symmetric Difference Method
set1.symmetric_difference(set2)

# Result: {1,2,4,5}
```
The **symmetric difference operation** will return the values on both sets excluding those that are found in both.

### Modifying Operations

We also have some other operations to help us add, remove or delete the whole set. 

``` python
set1 = {1,2,3}
# Add a value
set1.add(4)

# Result: {1,2,3,4}


set2 = {4,5,6}
# Remove a value
set1.remove(5)

# Result: {4,6}


set3 = {'cat', 'dog', 'bird'}
# Clear all values
set3.clear()

# Result: set(), which is an empty set


# Check if we have a value
if value in coolSet:
    # code...
# If the value exist in the set it will return True.


set4 = {1,2,3,4}
# Get the size
length = len(set4)

# length has a size of 4

```
| Operation | Performance |
|-------|--------|
|   Union   |   O(n)   |
|   Intersection   |  O(n)  | 
|   Difference   |  O(n)  |
|   Symmetric Difference   |  O(n)  | 
|   Add   |  O(1)  | 
|   Remove   |  O(1) |
|   Clear   |  O(1)  | 
|   If in   |  O(1) |
|   Size   |  O(1)  |

## Example : Fruits in the Market

Imagine you're in charge of the marketing team of a big super market. Your team and you decided it would be a great idea to make a campaign showing all the fruits the super market offers. But there is a problem, the market doesn't have a list of all fruits you sell, or at least not in one list. They have several deparment selling different fruits, because remember is a very market.

You remembered the data structures course you took on college and though, "Hey! I can solve this"

You start by solving that you will want to get a set, because it doesn't really matter the quantity of fruits or if there is one type of fruit in more than one deparment.

```python
# First we gather the lists containing the fruits
dep1 = ['berry', 'avocado', 'pinapple']
dep2 = ['apple', 'banana', 'tomatoes']
dep3 = ['tomatoes', 'chilies', 'berry']

# Because we will want to end up with a set let's convert it now.
dep1 = set(dep1)

# We could have directly converted all departments into sets and used the union operator, but you remembered the union method will do that for you so you saved some coding lines.

# Let's save our set of fruits (and some other stuff...)
fruits = dep1.union(dep2, dep3)

# Here we go, now we have our set of fruits ready for our marketing campaign!
print(fruits)
```
Sets have many applications in the real world, for example they are widely use in databases where you opperate with many joins.

## Problem to Solve : What are the kids watching these days?

Imagine you are a teacher at an elementary school and you want to figure out what are the cartoons kids are watching these days.

To solve this you decided to make a survey, you want to create a program that will ask how many people is going to answer the survey and get the cartoons seen by the kids. Finally you want to display the set containing all cartoons.

To solve this there are a few requierements must be followed:

* There should not be any repeated elements
* Must return a set
* Efficiency must be at least O(n)
* Assume kids will write the cartoon's names the same way with no errors (they are very smart kids!)

You can check your code with the solution here: [Solution](solution-set.py)

[Back to Welcome Page](README.md)