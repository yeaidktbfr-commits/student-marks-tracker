#testing

marks = {}
while True:
    subject= input("Enter subject name (or 'done' to finish): ")
    if subject.lower() == "done":
        break
    mark = input("Enter mark for {}: ".format(subject))
    marks[subject] = mark