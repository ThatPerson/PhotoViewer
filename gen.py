import json
import sys
import os

## Give Directory containign images, name, date ,location. Outputs to pics.json.
# Directory must have images in /final/ and /original/
# as given by shrink.sh


filename = "pics.json"
directory = input("Directory: ")
title = input("Name: ")
date = input("Date: ")
location = input("Location: ")

thisentry = {
    "name": title,
    "date": date,
    "location": location,
    "directory": directory,
    "pics":[]
}

print(thisentry)
y = input("Is this correct? [y/n]: ")
if (y != "y"):
    print("Failing..")
    exit(0)

thisentry['pics'] = os.listdir(directory+"/final/")
print(thisentry)



with open(filename, "r") as f:
    data = json.load(f)
    data['p'].append(thisentry)

os.remove(filename)
with open(filename, "w") as f:
    json.dump(data, f, indent=4)


