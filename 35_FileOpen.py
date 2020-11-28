"""
'r'--open a file for reading only
'w'--open a file for writing only
'w+'--open a file for reading and writing

open([file_path],[mode])
"""
_open=open("file.txt","w")
_open.write("I make this file!!!")
_open.close()