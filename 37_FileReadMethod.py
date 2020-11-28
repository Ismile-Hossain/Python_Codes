with open("D:\Study\Python\Codes\with.txt","r") as _read:
   print( _read.read())

#read a file and save it in a list
_list=list()
with open("D:\Study\Python\Codes\with.txt","r") as __read:
    _list.append(__read.read())

print( _list)