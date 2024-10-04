numbers = ['six','seven','eight','nine','ten','eleven','twelve']
fruits=['apple','grapes','watermelon','lemon','lime','pineapple','guaba']
vegetables=['cucumber','tomato','potato','carrot','pumpkin']
#You can also use for/in to work on a string. The string acts like a list of its chars
box="una mañana linda"
for character in box:
    print(character)

#The "in" keyword: on its own is an easy way to test if an element appears in a list (or other collection) returning True/False. The in keyword has two purposes, 1-to check if a value is present in a sequence (list, range, string etc.) 2-to iterate through a sequence in a for loop

if "six" in numbers:
    print("hello")
else:
    print("goodbye")

while "eight" in numbers:
    print(numbers)
    numbers.pop(0)

text = "i miss jack sparrow"
print("orlando" in text)
print("sparrow" in text)
#join() function is the opposite of split() function as it joins all items in an iterable (tuple, dictionay, list, etc) and joins them into one string separated by a chosen character
print("".join(["one","two","three","four","five"]))
print("look at this","potato".join(numbers))
print("\n".join(numbers))
#when used in an f-string we have to be cautious with the use of 'single' and "double" quotes in the same f-string
print(f"{'ice'.join(numbers)}")
print(f"here is an example of join function {' '.join(numbers)}")

print(numbers)
#append() adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
numbers.append(13)
print(numbers)
#insert() inserts the element at the given index, shifting elements to the right.
numbers.insert(2,'coconut')
numbers.insert(5,'coconut')
print(numbers)
#extend() adds the elements of one list to the end of another list. Using + or += on a list is similar to using extend() it only works with iterables like strings and lists
example_list=[]
example_list.extend("sol")
example_list+="luna"
example_list.extend([8])
example_list+=[4]
example_list.extend(["purple","brown"])
example_list+=[3,1,5,9,"play"]
print(example_list)

numbers.extend('fourteen')
print(numbers)

print(fruits)
fruits.extend(vegetables)
print(fruits)

concatenated_list=fruits+numbers
print(concatenated_list)

nested_list=[fruits,numbers]
print(nested_list)
#index() searches for the given element from the start of the list and returns its index,only returns the index of the first match to its argument Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
print(vegetables.index('tomato'))
print(vegetables.index('pumpkin'))
print(numbers.index(13))
charmander = range(5, 15)
print(charmander.index(9))
#The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument
print(concatenated_list.index('potato',6,12))
print(concatenated_list.index('coconut',15))
#count() Return the number of times an item appears in the list
print(concatenated_list.count('coconut'))
print(concatenated_list.count('e'))
print(concatenated_list.count('o'))

#remove() searches for the first instance of the given element and removes it (throws ValueError if not present)
numbers.remove('e')
numbers.remove('u')
print(numbers)
#sort() sorts the list in place (does not return it). (The sorted() function is preferred.)
print(vegetables)
vegetables.sort()
print(vegetables)

woo=[9,4,7,3,6,1,0]
woo.sort()
print(woo)

print(concatenated_list)
print(nested_list)

squirtle = sorted((1, 3, 5, 7, 9, 2, 4, 6, 8))
print(squirtle)

chameleon = sorted(range(10), reverse=True)
print(chameleon)

#reverse() reverses the list in place (does not return it)
numbers.reverse()
print(numbers)
numbers.reverse()
print(numbers)

#pop() removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
print(numbers.pop(2))
numbers.pop(4)
print(numbers.pop())
print(numbers)
#clear() Remove all items from the list
print(vegetables)
vegetables.clear()
print(vegetables)
#copy() You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2. So instead we use the copy() function that returns a shallow copy of the list, a shallow copy means any modification in the new list won’t be reflected in the original list. 
long_list=concatenated_list.copy()
print(long_list)
#for more methods search for list() function and deepcopy() function

#slices: are specific parts of strings, lists or tuples
print("guadalajara"[:])
print("guadalajara"[:1])
print("guadalajara"[1:])
print("guadalajara"[1:5])
print("guadalajara"[1:-1])
print(numbers[1:4])
#and can also be used to change sub-parts of the list
numbers[1:4]=10,11,12
print(numbers)

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
piano_keys = ("a", "b", "c", "d", "e", "f", "g")
print(piano_keys)
print(piano_keys[2:5])
print(piano_keys[2:])
print(piano_keys[:5])

print(piano_tuple[:])
print(piano_tuple[3:])
print(piano_tuple[:3])

print(piano_tuple[2:-2])
print(piano_tuple[3:6])
print(piano_tuple[-6:-1])
# we can also add a "step" parameter
print(piano_keys[2:6:2])
print(piano_keys[::2])
print(piano_tuple[2:7:2])
# the "step" can also be negative to go backwards
print(piano_keys[::-1])
print(piano_tuple[-1:-8:-1])

#https://developers.google.com/edu/python/lists#for-and-in
#https://www.askpython.com/python/python-import-statement
#https://developers.google.com/edu/python/lists#list-methods

# https://docs.python.org/3/howto/sorting.html

# https://www.w3schools.com/python/ref_keyword_in.asp

# https://www.w3schools.com/python/ref_string_join.asp
