#python program to enter students' names and grades 
#1- Prints students names and grades
#2- Prints the average grade of the class
#3- Prints the highest grade earned (Student name and grade)
#4- Prints the count of students who passed (grade >= 60)

#Informing the user about the Software 
print("This Software will read Students Names and Grades and helps you calculating the following:\n1-Class Average \n2-Highest Grade\n3-Count of students who passed")

#Taking user Input
#I know we have not taken it in class, I work on other languages (vb.net / C# / C++)
#it is a fast way to test user input... 
#sorry for using advanced code
while True:
    try: 
        student_count=int(input("Please Enter the number of students:_ "))
        break
    except ValueError:
        print('You entered a non integer value, try again.')
        continue
print("we will now work on - " + str(student_count)  + " - Student grades")