"""
Take the items in this list of lists:
[["Top Gun", "Risky Business", "Minority Report"],
["Titanic", "The Revenant", "Inception"],
["Training Day", "Man on Fire", "Flight"]]
and write them to a CSV file.
The data from each list should be a row in the file,
with each item in the list separated by a
"""
import csv

_list=[["Top Gun", "Risky Business", "Minority Report"],
["Titanic", "The Revenant", "Inception"],
["Training Day", "Man on Fire", "Flight"]]

with open("D:\\Study\\Python\\Codes\\New folder\\new.csv","w",newline='') as new:
    _write=csv.writer(new,delimiter=",")
    _write.writerow(_list[0])
    _write.writerow(_list[1])
    _write.writerow(_list[2])
