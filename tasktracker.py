#i have no idea how to do any of this but let's go i guess
import json
import sys
import datetime

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

# FUNCTIONS HERE

def add_task(new_task, filename="to_do_list.json"):
    with open(filename, "r+") as file:
        file_data = json.load(file)
        file_data["tasks"].append(new_task)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def id_assigner():
    f = open("to_do_list.json",)
    json_file_dict = json.load(f)
    id_numbers = [d["id"] for d in json_file_dict["tasks"]]
    f.close
    if 1 not in id_numbers:
        return 1
    for i in id_numbers:
        if i + 1 not in id_numbers:
            return i + 1
        
def task_creator(task_description):
    task_description = task_description
    #lol
    task_description = task_description.rstrip().strip("\"")
    return {
        "id" : id_assigner(),
        "description" : "%s" % task_description,
        "status" : "todo",
        "createdAt" : str(datetime.datetime.now()).split(".")[0],
        "updatedAt" : str(datetime.datetime.now()).split(".")[0]
    } 

def delete_task(id_of_task):
    found_task = False
    f = open("to_do_list.json",)
    json_file_dict = json.load(f)
    #id_numbers = [d["id"] for d in json_file_dict["tasks"]]
    #print(range(len(json_file_dict["tasks"])))
    # idx stands for index, this code finds the index of selected task in list
    for idx, object in enumerate(json_file_dict["tasks"]):
        if object["id"] == int(id_of_task):
            found_task = True
            print("deleting task at id " + str(id_of_task))
            json_file_dict["tasks"].pop(idx)
            with open("to_do_list.json", "w") as f:
                json.dump(json_file_dict, f, indent=2)
            break
    if found_task == False:
        print("task id not found")

def update_task(id_of_task, new_description):
    found_task = False
    f = open("to_do_list.json",)
    json_file_dict = json.load(f)
    #id_numbers = [d["id"] for d in json_file_dict["tasks"]]
    #print(range(len(json_file_dict["tasks"])))
    for idx, object in enumerate(json_file_dict["tasks"]):
        if object["id"] == int(id_of_task):
            found_task = True
            print("updating task at id " + str(id_of_task) + " with description: " + str(new_description))
            object.update({"updatedAt" : str(datetime.datetime.now()).split(".")[0]})
            object.update({"description": new_description})
            with open("to_do_list.json", "w") as f:
                json.dump(json_file_dict, f, indent=2)
            break
    if found_task == False:
        print("task id not found")

def mark_in_progress(id_of_task):
    found_task = False
    f = open("to_do_list.json",)
    json_file_dict = json.load(f)
    #id_numbers = [d["id"] for d in json_file_dict["tasks"]]
    #print(range(len(json_file_dict["tasks"])))
    for idx, object in enumerate(json_file_dict["tasks"]):
        if object["id"] == int(id_of_task):
            found_task = True
            print("changing task status to 'in progress' at id " + str(id_of_task))
            object.update({"updatedAt" : str(datetime.datetime.now()).split(".")[0]})
            object.update({"status": "in-progress"})
            with open("to_do_list.json", "w") as f:
                json.dump(json_file_dict, f, indent=2)
            break
    if found_task == False:
        print("task id not found")

def mark_done(id_of_task):
    found_task = False
    f = open("to_do_list.json",)
    json_file_dict = json.load(f)
    #id_numbers = [d["id"] for d in json_file_dict["tasks"]]
    #print(range(len(json_file_dict["tasks"])))
    for idx, object in enumerate(json_file_dict["tasks"]):
        if object["id"] == int(id_of_task):
            found_task = True
            print("changing task status to 'done' at id " + str(id_of_task))
            object.update({"updatedAt" : str(datetime.datetime.now()).split(".")[0]})
            object.update({"status": "done"})
            with open("to_do_list.json", "w") as f:
                json.dump(json_file_dict, f, indent=2)
            break
    if found_task == False:
        print("task id not found")

def list_tasks(status):
    f = open("to_do_list.json",)
    json_file_dict = json.load(f)
    #code to filter out tasks by status
    output_list = []
    status = status.rstrip()
    if status == "all":
        print("listing tasks...")
        if not json_file_dict["tasks"]:
            print("no tasks yet!")
        else:
            for task in json_file_dict["tasks"]:
                print("task number", task["id"])
                for key, value in task.items():
                    print(f"{key}: {value}")
                print("\n")
    elif status == "done" or status == "todo" or status == "in-progress":
        #code to filter out tasks by status
        for idx, object in enumerate(json_file_dict["tasks"]):
            if object["status"] == str(status):
                output_list.append(json_file_dict["tasks"][idx])
        #python dictionary now
        print("listing tasks...")
        #print(pretty_json_output)
        if not output_list:
            print("no tasks yet!")
        else:
            for task in output_list:
                print("task number", task["id"])
                for key, value in task.items():
                    print(f"{key}: {value}")
                print("\n")
    else:
        print("specify status or pass 'all' as second argument to see every task on the list")
    #dump unchanged file
    with open("to_do_list.json", "w") as f:
        json.dump(json_file_dict, f, indent=2)



# arguments so far: "start", "add", "update", "delete", "markinprogress", "markdone", "list"
# COMMAND LINE ARGUMENTS FOR SINGLE USES
#print("Arguments passed:", str(sys.argv))
program_start = True
try:
    if sys.argv[1] != "start":
        program_start = False

    try:
        #print(sys.argv[1])
        if sys.argv[1] == "add":
            list_of_commands = list(sys.argv)
            description_output_from_cli = list_of_commands[2:]
            string_description_output_from_cli = " ".join(description_output_from_cli)
            print(f"adding: {task_creator(string_description_output_from_cli)} (at id {id_assigner()})")
            add_task(task_creator(string_description_output_from_cli))
    except IndexError:
        print("index error! pass your description in after the [add] command")
    
    try:
        #print(sys.argv[1])
        if sys.argv[1] == "delete":
            delete_task(sys.argv[2])
    except IndexError:
        print("index error! please set input in the following form: delete (id number of task you wish to delete)")

    try:
        #print(sys.argv[1])
        if sys.argv[1] == "update":
            list_of_commands = list(sys.argv)
            update_description_output_from_cli = list_of_commands[3:]
            update_string_description_output_from_cli = " ".join(update_description_output_from_cli).rstrip()
            update_task(sys.argv[2], update_string_description_output_from_cli)
    except IndexError:
        print("index error! please set input in the following form: update (id number of task you wish to delete) (new description)")

    try:
        #print(sys.argv[1])
        if sys.argv[1] == "markinprogress":
            mark_in_progress(sys.argv[2])
    except IndexError:
        print("index error! please set input in the following form: markinprogress (id number of task you wish to delete)")
    
    try:
        #print(sys.argv[1])
        if sys.argv[1] == "markdone":
            mark_done(sys.argv[2])
    except IndexError:
        print("index error! please set input in the following form: markdone (id number of task you wish to delete)")
    
    try:
        #print(sys.argv[1])
        if sys.argv[1] == "list":
            list_tasks(sys.argv[2])
    except IndexError:
        print("index error! please set input in the following form: list (status of tasks you'd like to see, or 'all' if you'd like to see every task on the list)")

except IndexError:
    program_start = True
#print(program_start)

# block for adding commands (command block haha get it it's like minecraft the command block from minecraft)
# also avoid setting variables to generalize cli commands (index errors are fucked and cba with flowcharts atm)
"""
try:
    if sys.argv[1] == "[COMMAND NAME]":
        do thing!
except IndexError:
    print("index error!")
"""


# if you run the program with the start command or no commands at all, it starts the program
# otherwise program start is false and does not run iterative loop
# this is for single use cases of the program, if you just wanna change one thing then get back to work (and not have to write "exit" all the time)
# now we add functions for all of our commands, and just run them once for single uses and again in the loop
# one test case function "add" right now
# at this rate i'll have to make a try except package for every single command :sob:


# LOOP FOR STARTING AND STOPPING
"""
all interactive code goes in the loop
this will read user input
typing "exit" will exit the program 
"""
if program_start == True:
    for line in sys.stdin:
        if "exit" == line.rstrip():
            break
        if "add" == line.split(" ")[0]:
            description_output = " ".join(line.split(" ")[1:])
            print(f"adding: {description_output} (at id {id_assigner()})")
            add_task(task_creator(description_output))
        if "delete" == line.split(" ")[0]:
            delete_task(line.split(" ")[1])
        if "update" == line.split(" ")[0]:
            update_description_input = " ".join(line.split(" ")[2:]).rstrip()
            update_task(line.split(" ")[1], update_description_input)
        if "markinprogress" == line.split(" ")[0]:
            mark_in_progress(line.split(" ")[1])
        if "markdone" == line.split(" ")[0]:
            mark_done(line.split(" ")[1])
        if "list" == line.split(" ")[0]:
            list_tasks(line.split(" ")[1])
        print(f"Input : {line}")
    #print(line.split(" "))

print("see you!")
# works


# now to fuck w json
# first rung: add, edit, delete tasks
# add command: input like [tasktracker.py add "task"]
# task properties: id (assigned automatically), description (string passed when adding), status, createdAt, updatedAt


# a task should look like this ideally:
"""
{
    "id": "[NUMBER]",
    "description": "[DESCRIPTION]",
    "status": ["todo", "in-progress", or "done"],
    "createdAt": "[date and time task was created]",
    "updatedAt": "[last updated date and time]",
}
"""
# at a point where i have to do the automatic id assigning thing
# thought about this for a couple of days and i've decided i don't need to make the id numbers changeable because completed tasks will still stay in the database
# so ! just gonna write a function that reads the ids given out so far and spits out the next one
# hopefully it should output 3 after reading 1 2 4 5
# because deleting tasks will be a feature too!

# thank fuck it works

# add and delete commands added and working, feel fucking good man

# update command added and working, feels good to derust :)

# status commands added! forgot to update lol

# i've a couple hours before a party so i'll add this list function rq

# how do i want all the tasks to look...

"""
task ID: X
description: [description]
status: ["todo", "in-progress", or "done"]
created at: [date and time task was created]
updated at: [last updated date and time]



"""

# DONE WITH EVERY COMMAND LET'S FUCKING GO
# now to add createdAt and updatedAt attributes
# and then i'm doneeeee
