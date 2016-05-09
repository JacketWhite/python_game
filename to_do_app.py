def Listing():
    print ("You saved the following to-do items:")
    listing = open('TaskList.md', 'r')
    text_in_file = listing.readlines()
    listing.close()
    lines = 1
    for i in text_in_file:
        print(str(lines) + i, end = "")
        lines += 1

def Archive():
    print("All completed tasks got deleted")
    with open("TaskList.md", "r+") as f:
        text_in_file = f.readlines()
        f.seek(0)
        for line in text_in_file:
            if "[x]" not in line:
                f.write(line)
        f.truncate()

def AddingTask():
    task = input("Add an item: ")
    with open("TaskList.md", "a+") as f:
        f.write(". [ ] " + task + "\n")
    print("Item added!")



def MarkingTask():
    complete = input("Which one you want to mark as completed: ")
    with open("TaskList.md", "r+") as f:
        LinesInFile = f.readlines()
        f.seek(0)
        lines = 1
        for line in LinesInFile:
            if lines == int(complete):
                line_array = list(line)
                line_array[3] = "x"
                f.write("".join(line_array))
                print("".join(line_array[6:len(line_array)-2]) + " is completed!")
            else:
                f.write(line)
            lines += 1
