#!/usr/bin/env python3



import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

example1 = "Example1.txt"


with open(example1,"r") as File1:
    i = 0;
    for line in File1:
        print("Iteration", i+1, ": ", line)
        i=i+1
    
