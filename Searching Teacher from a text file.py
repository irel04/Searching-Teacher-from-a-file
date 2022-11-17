# CMPE3032 - Onbjected Oriented Programming

print(f"\n{'=' * 75}")
print(f"{'|'}{' ': >11}{'Lab Exercise 7 | Programmed by Irel Kian C. Bacolod'}{' ': >11}{'|'}")
print(f"{'=' * 75}")

# record = open("tchr_files.txt", "a")
# record.writelines("Roy Dimaculangan | Reserved Officers' Training Corps\n"
#                   "Myrna Aparente | Purposive Communication\n"
#                   "Josh Nasugbu | Computer Technology 2\n"
#                   "Lance Gampanin | Computer Technology 2\n"
#                   "Julius Novachrono | Physics\n"
#                   "Jerome Malabanan | Engineering Data Analysis\n"
#                   "Myrna Gairanod | Engineering Data Analysis\n"
#                   "Alyanna Garcia | Purposive Communication\n"
#                   "Cardo Ramirez | Object Oriented Programming\n"
#                   "Julius Morante | Object Oriented Programming\n"
#                   "Raymart Bukal | Discrete Mathematics\n"
#                   "Albert Hernandez | Calculus 2\n"
#                   "Marcus Dimaculangan | Calculus 2\n"
#                   "Nayeon Im | Rhythmic Activities\n"
#                   "Santita Morante | Purposive Communication\n"
#                   "Christian Gampanin | Civic Welfare Training Service\n"
#                   "Lolit Dela Cruz | Discrete Mathematics\n"
#                   "Chaeyoung Park | Rhythmic Activities\n"
#                   "Cardo Verde | Physics\n"
#                   "Tristan Montefalco | Reserved Officers' Training Corps\n")
#
# record.close()

# Reading Text File
record = open("tchr_files.txt", "r")

record_read = record.readlines()

# List for sorting all lines in the text
list_1 = []
run = "y"

# Splitting Elements that are unnecessary in the list
for i in record_read:
    split = i.replace("\n", "").split(" | ")
    list_1.append(split)

# Prompting to start the search function
while run.lower() == "y":
    prompt1 = input("\nChoose want to search (subject/teacher): ")
    # Searching teacher's name if-elif
    if prompt1.lower() == "teacher":
        tchr_name = input("Enter name: ")
        count = 0
        print("\nSearch Results for name {}:\n".format(tchr_name.title()))
        # Calling elements in the list
        for j in list_1:
            if tchr_name.title() in j[0]:
                result = j[0] + (" " * (30 - len(j[0])) + "Subject: " + j[1])
                count = 1
                print(result)
            elif tchr_name.title() not in j[0]:
                if count == 0:
                    if j == list_1[19]:
                        print("Record not found!!!")
                    else:
                        continue
                elif count > 0:
                    continue
    # Searching teachers in following subjects if-elif
    elif prompt1.lower() == "subject":
        subj = input("Enter complete name of the subject: ")
        count = 0
        print("\nHere are the lists of teachers in {}:\n".format(subj.title()))
        # Calling elements in the list
        for j in list_1:
            if subj.title() == j[1]:
                result = j[0]
                count = 1
                print(result)
            elif subj.title() not in j[1]:
                if count == 0:
                    if j == list_1[19]:
                        print("Subject not found. Please check if there are wrong input on the name of the subject.")
                    else:
                        continue
                elif count > 0:
                    continue
    else:
        print("\nInvalid. Please choose between teacher and subject!!!")
        continue
    # Prompting if the user want to try again
    run = input("\nDo you want to try again (y/n)? ")

# Closing Text file
record.close()

print(f"\n{'<' * 25}{' End of the Program '}{'>' * 30}")
