#tuples in a list
location=[]  #It is a list
#tuples--la,chicago
la=(12.12321,4.23423)
chicago=(3234.2332,21,32213)
#tuples are stored in a list
location.append(la)
location.append(chicago)
print(location)


#list in a tuple
#two list
one=["hbankb","aadh"]
two=["ahiua",'Njkab']
number=(one,two) #tuple
print(number)
print(number[0])#accessing each list
print(number[0][1])#accessing each items in a list

#tuple and list in dictionaries
my={"loction":(2132,23423),                #tuple
    "celebs":["jhabdjh","asghdiw","djkh"], #list
    "facts":{"state":"bjh","counry":"Bangladesh"} #dictionaries
    }