def Listing():
    print ("You saved the following to-do items:")
    listing = open('TaskList.md', 'r')
    text_in_file = listing.readlines()
    listing.close()
    lines = 1
    for i in text_in_file:
        print(str(lines) + i, end = "")
        lines += 1

Listing()

def Archive():
    print("All completed tasks got deleted")
    with open("TaskList.md", "r+") as f:
        text_in_file = f.readlines()
        f.seek(0)
        for line in text_in_file:
            if "[x]" not in line:
                f.write(line)
        f.truncate()
