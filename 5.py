
#1.	Create a dictionary with Fname, Lname and DOB as Keys ( dictionary should look like {Fname: ‘Tux’, Lname: ‘Python’, DOB: ‘1989’}) and do the following:
#.	Iterate through the dictionary and print key, value on to stdout
#.#	Add {Place: ‘Netherlands’} to the dictionary
#	Remove value Python from dictionary
thisdist = {
    "fname" : "tux",
    "lname": "python",
    "DOB" : 1980
}
x= thisdist.items()
print(x)
thisdist["place"] = "netherlands"
print(thisdist)
del thisdist["python"]
print(thisdist)