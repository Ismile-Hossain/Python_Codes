s="cat in the hat"
print("cat" in s)
print("bat" in s)
print("pot" not in s)

#Escaping
print("My name is \"Ismile\"")

#Slicing iterable[start_index:end_index]
_list=["My","name","is","Ismile"]
print(_list[0:3])
print(_list[0:4])

_string="My name is Ismile"
print(_string[:10])
print(_string[:])

#Replace method
_String="My name is Ismile"
print(_String.replace('is','@'))

#first appears method
print("animals".index('m'))

#Iterate character by character
name="Ismile"
for character in name:
    print(character)

#Iterate word by word in a list
_list=["My","name","is","Ismile"]
for show in _list:
    print(show)

#Iterate word by word in a tuple
_list=("My","name","is","Ismile")
for show in _list:
    print(show)