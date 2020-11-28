_list1=["one","two","three"]
_list2=["four","five","six"]
_list=[]
for show in _list1:
    show= show.upper()
    _list.append(show)

for show in _list2:
    show=show.upper()
    _list.append(show)
print(_list)