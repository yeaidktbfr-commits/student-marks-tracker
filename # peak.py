# peak

while True:
    print("1.Enter new marks")
    print("2.View saved marks")
    print("3.Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        marks = {}
        while True:
            subject = input("Enter subject name (or 'done' to finish): ")
            if subject.lower() == "done":
                break
            mark = input("Enter mark for {}: ".format(subject))
            try:
                marks[subject] = float(mark)
            except ValueError:
                print("Please enter a valid number for the mark.")
                continue

        if not marks:
            print("No marks entered.")
            continue

        average = sum(marks.values()) / len(marks)

        for subject, mark in marks.items():
            if mark < 70:
                print(subject, ":", mark, "Fail")
            else:
                print(subject, ":", mark, "Pass")

        print("Average marks:", average, "%")

        with open("marks.txt", "w") as file:
            file.write(f"Average: {average:.1f}%\n")
            for subject, mark in marks.items():
                file.write(f"{subject}: {mark}\n")

        print("Marks saved!")
    elif choice == "2":
        try:
            with open("marks.txt", "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("No marks found. Please enter marks first.")
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
   















