welcome <3
# tasktrackerroadmap
task tracker project on roadmap 
link to project page: https://roadmap.sh/projects/task-tracker


# KIWI'S TASK TRACKER PROGRAM

this is my to do list / task tracker program! big ups roadmap.sh 

## usage

there are 2 (two) ways to use this application! <br />
first of all, running the project without any other command line arguments or using "start" <br />
this will create a input feedback loop where you can run commands that output to terminal<br />
to close this feedback loop, pass "exit" <br />
second of all, running the project with arguments<br />
this is intended for single use cases, where you don't need to open the program then close it after you are done

## task attributes:
every task has 5 attributes:

ID: automatically assigned at task creation, used to run commands on specific tasks such as "update" and "delete"<br />
description: description of task from "add" command, and updated with "update"<br />
status: set to "todo" on creation, can be changed to "in-progress" or "done" through commands<br />
createdAt: date and time task was created<br />
updatedAt: date and time task was last updated

## list of arguments:

### "start" 
starts the program! input feedback loop in terminal, where you can pass other commands into the program

### "exit"
exits the program

### "add" 
creates a task, with a description that you pass after the argument<br />
example use:<br />
add "Buy groceries"

### "update"
updates the task at a given ID with a new description<br />
example use:<br />
update 1 "Return groceries"<br />

note: for "add" and "update" you don't need to put quotation marks around your description! just a sentence or two is enough

### "delete"
deletes task at a given ID<br />
example use:<br />
delete 1

### "markinprogress"
gives task at given ID status "in-progress"<br />
example use:<br />
markinprogress 1

### "markdone"
gives task at given ID status "done"<br />
example use:<br />
markdone 1

### "list"
lists tasks based on signifier:<br />
all - lists all tasks<br />
todo - lists all tasks with "todo" status<br />
in-progress - lists all tasks with "in-progress" status<br />
done - lists all tasks with "done" status<br />
example uses:<br />
list all<br />
list in-progress


## ramble

this is my first ever project like this, so if you're reading this right now then thank you for checking me out (pause)<br />
onto the next one
