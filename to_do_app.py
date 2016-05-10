import os

def Listing():
    if os.stat("TaskList.md").st_size != 0:
        print ("\n>>You saved the following to-do items:")
        listing = open('TaskList.md', 'r')
        text_in_file = listing.readlines()
        listing.close()
        lines = 1
        for i in text_in_file:
            if "[x]" not in i:
                print("\t" + str(lines) + i, end = "")
            else:
                print('\033[92m' + "\t" + str(lines) + i + '\033[0m', end = "")
            lines += 1
        print("")
        Stats()
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
            else:
                with open("Archive.md", "a") as a:
                    a.write(line)
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
                print('\033[92m' + ">>" + "".join(line_array[6:len(line_array)-1])
                        + " is completed!\n" + '\033[0m')
            else:
                f.write(line)
        lines += 1

def AListing():
    if os.stat("Archive.md").st_size != 0:
        print ("\n>>You did the following items:")
        listing = open('Archive.md', 'r')
        text_in_file = listing.readlines()
        listing.close()
        lines = 1
        for i in text_in_file:
            print('\033[94m' + "\t" + str(lines) + i, end = "" + '\033[0m')
            lines += 1
        print("\n")
    else:
        print("\n>>Nothing was archived!")
        main()

def Stats():
    x_lines = 0
    empty_lines = 0
    with open("TaskList.md", "r") as f:
        text_in_file = f.readlines()
        for i in text_in_file:
            if "[x]" not in i:
                x_lines += 1
            else:
                empty_lines += 1
    print(">>Unfinished tasks:", str(empty_lines), "\n>>Finished tasks:", str(x_lines))


def main():
    commands = {"list" : Listing, "archive" : Archive,
                "add" : AddingTask, "mark" : MarkingTask,
                "alist" : AListing, "quit" : exit}
    while True:
        try:
            cmd = input("\n>>>>Please specify a command [list, add, mark, archive, alist, quit]: ")
            commands["".join(cmd.split())]()
        except FileNotFoundError:
            print("\n>>File not yet created!")
        except KeyError:
            print("\n>>No such command!")

main()
