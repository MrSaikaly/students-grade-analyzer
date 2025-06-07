#python program to enter students' names and grades 
#1- Prints students names and grades
#2- Prints the average grade of the class
#3- Prints the highest grade earned (Student name and grade)
#4- Prints the count of students who passed (grade >= 60)



#fucntions to be used in the software
def display_student_summary(student_list):# display student summary fucntion 
    print("we will work on following Students:_ ")
    for index,student in enumerate(student_list):
        print(  index+1 , "Student:_"+ student[0]+ " with grade :_", student[1] )

def get_avg_grade(student_list):# Calculate student average fucntion 
        sum=0
        for index,student in enumerate(student_list):
            sum= sum + student[1]
        return sum / len(student_list)
         






#  

#Informing the user about the Software 
print("This Software will read Students Names and Grades and helps you calculating the following:\n1-Class Average \n2-Highest Grade\n3-Count of students who passed")

#Taking user Input
#I know we have not taken it in class, I work on other languages (vb.net / C# / C++)
#it is a fast way to test user input... 
#sorry for using advanced code
while True:
    try: 
        student_count=-1
        while student_count <=0: #checking that number of students greater than zero
            student_count=int(input("Please Enter positive number of students:_ "))
        break
#throwing an error excption if value of input not integer
    except ValueError:
        print('You entered a non integer value, try again.')
        continue
print("we will now work on - " + str(student_count)  + " - Student grades") # informing the user of number of students that he will work on

# now taking Student name and grades from user
students_list=[]
for i in range(student_count): # looping on number of students
    #student name
    print("you are now working on student " +str(i+1) + " of total " + str(student_count))
    student_name= input("Please enter Student Name:")

    #student grade must be float - making
    while True:
        try: #checking student grade to be float and between 0 and 100
            student_grade=-1
            while student_grade <=0 or student_grade>100 :
                student_grade=float(input("Please Enter student grade between 0 and 100:_ "))              
            break
#throwing excption if non numeric value entered
        except ValueError:
            print('You entered a non numeric value, try again.')
            continue
        
#appending student to student list
    student=[student_name, student_grade] #making name and grade to student
    students_list.append(student)#adding student data to collection

#now printing student name and its grade
display_student_summary(students_list)
print("your class Average grade is:_ ",get_avg_grade(students_list))
