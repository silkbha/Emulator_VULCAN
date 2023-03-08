
''' This script scrapes raw_runs_list.txt and returns a version with all
    numerical values rounded to a user-defined decimal place.
    Makes checking for duplicate runs easier.
    Also appends metallicity value of 1.0 to each string.
'''

# round to x decimals
x = 3

with open('raw_runs_list.txt') as file:
    with open('runs_index.txt',"w") as fileR:
        for line in file:
            line = line.removeprefix("vulcan_cfg_")
            line = line.removesuffix(".py\n")
            contents = line.split("_")
            new = []
            for element in contents:
                new.append(str(round(float(element),x)))
            new.append("1.0") # add metallicity
            string = "_".join(new)
            fileR.write(string+"\n")

# with open('raw_runs_list.txt') as file:
#     with open('runs_index_exact.txt',"w") as fileR:
#         for line in file:
#             line = line.removeprefix("vulcan_cfg_")
#             line = line.removesuffix(".py\n")
#             fileR.write(line+"\n")