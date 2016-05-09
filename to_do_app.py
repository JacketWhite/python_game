import os

def Listing():
    if os.stat("TaskList.md").st_size != 0:
        print ("\n>>You saved the following to-do items:")
        listing = open('TaskList.md', 'r')
        text_in_file = listing.readlines()
        listing.close()
        lines = 1
        for i in text_in_file:
            print("\t" + str(lines) + i, end = "")
            lines += 1
        print("\n")
    else:
        print("\n>>There's no more tasks to do!")
        main()

def Archive():
    with open("TaskList.md", "r+") as f:
        text_in_file = f.readlines()
        f.seek(0)
        for line in text_in_file:
            if "[x]" not in line:
                f.write(line)
        f.truncate()
    print("\n>>All completed tasks got deleted\n")

def AddingTask():
    task = input("\n>>>>Add an item: ")
    with open("TaskList.md", "a+") as f:
        f.write(". [ ] " + task + "\n")
    print(">>Item added!\n")

def MarkingTask():
    Listing()
    complete = input("\n>>>>Which one you want to mark as completed: ")
    with open("TaskList.md", "r+") as f:
        LinesInFile = f.readlines()
        f.seek(0)
        lines = 1
        for line in LinesInFile:
            if lines == int(complete):
                line_array = list(line)
                line_array[3] = "x"
                f.write("".join(line_array))
                print(">>" + "".join(line_array[6:len(line_array)-1])
                        + " is completed!\n")
            else:
                f.write(line)
            lines += 1


def main():
    commands = {"list" : Listing, "archive" : Archive,
                "add" : AddingTask, "mark" : MarkingTask}

    cmd = input("\n>>>>Please specify a command [list, add, mark, archive]: ")
    commands[cmd]()


main()
