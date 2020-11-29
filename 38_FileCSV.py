#two store row by row value and separation of column in xl file
import csv
with open("D:\Study\Python\Codes\csvv.csv","w",newline='') as _csv:
    write=csv.writer(_csv,delimiter=",")
    write.writerow(["one","two","three"])
    write.writerow(["four","five","six"])