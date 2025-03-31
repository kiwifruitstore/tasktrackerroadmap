#i have no idea how to do any of this but let's go i guess
import json
import sys

print("hey hi welcome")

# okay so first off json files, how do they work
# worked with like coded in databases before so writing functions and stuff should be okay
# never used a json file or separate database thing before tho so we're gonna firstly try to set this up

# okay after reading i think i get it now
# when first starting the program we want to prompt user if they have an external json file that they want to load in, otherwise create a new one
# cli time

#print("first off, do you have an external json file you would like to load? use [some command - load (file)], otherwise create a new one with [some command - start]")

start_file = {

}

# if something something
#with open("to_do_list.json", mode="w", encoding="utf-8") as write_file:
 #   json.dump(start_file, write_file)
#creates a new task tracker json file (hopefully!)


#with open("task_tracker.json", mode="r", encoding="utf-8") as read_file:
#       task_tracker_data = json.load(read_file)
# loads task tracker json file (if there already is one) and creates a variable "task_tracker_data" for it
# not sure how to handle the name of the file if it isn't already "task_tracker.json"...

# break time

# coming back to this now and we don't need to create shit
# just have the file there
# lol

# also using sys for command line argument


"""
all interactive code goes in the loop
this will read user input
typing "exit" will exit the program 
"""
for line in sys.stdin:
    if "exit" == line.rstrip():
        break
    if "add" == line.split(" ")[0]:
        print(f"adding: {line.split(" ")[1]}")
    #print(f"Input : {line}")
    #print(line.split(" "))
print("see you!")

# works