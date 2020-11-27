my_name="Ismile"
print(my_name[0])
print(my_name[-1])
_string="I can not change the string means immutable"
print(_string)


my_name="ismile"*2
print(my_name)
print(my_name.upper())
print(my_name.lower())
print(my_name.capitalize())

#formate method for concatanation
name=input("Enter word name ")
mine=input("Enter the name ")
line="""My {} is {}""".format(name,mine)
print(line)

#split method
str=[]
str="My name is Ismile.I am 25 years old".split(".")
print(str[0])
print(str[1])

#join method
name="MynameisIsmile"
result=" ".join(name)
print(result)
name=["My","name","is","Ismile"]
_name=" ".join(name)
print(_name)

#strip method remove the white space
s=" Ismile "
remove_space_s=s.strip()
print(remove_space_s)
