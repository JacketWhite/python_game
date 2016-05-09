def Listing():
    listing = open('TaskList.md', 'r')
    text_in_file = listing.readlines()
    listing.close()
    lines = 1
    for i in text_in_file:
        print(str(lines) + '. [ ] ' + i, end = "")
        lines += 1
Listing()
