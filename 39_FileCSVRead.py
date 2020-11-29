import csv
with open("D:\Study\Python\Codes\csvv.csv","r") as _r:
    r=csv.reader(_r,delimiter=",")
    for row in r:
        print(",".join(row))