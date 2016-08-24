from linecache import getline
with open("output.txt") as f:
    for ind, line in enumerate(f,1):
        if line.rstrip() == "Reference":
            print(getline(f.name, ind+1))