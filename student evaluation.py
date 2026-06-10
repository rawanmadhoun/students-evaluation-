
#Quiz score out of 100:
#Participation score out of 100:

def final_grade (Attend, Homework, Quiz,Part): 
    final  = (Attend * .20)+ (Homework *.35)
    + (Quiz * .35)+ ( Part*.10)    
    return final  

def get_valid_students_number():
    while True:
            number = int(input("How many students do you want to evaluate? "))
            if number > 0:
                return number
            else:
                print("Number of students must be greater than 0.")
        
def get_valid_score(message):
    while True:
        score = float(input(message))
        if 0 <= score <= 100:
         return score
        else:
        print("Invalid score. Please enter a number between 0 and 100.")

    for i in range (student_number ) : 
        student_name = input ("please enter the student name")
        Attendance_score = float(input("please add the attendance scoe out of 100" ))
        Home_work_score = float(input("please add the home work scoe out of 100" ))
        Quiz_score = float(input("please add the quiz scoe out of 100" ))
        participlation_score=  float(input("please add the participation  scoe out of 100" ))
        grade = final_grade(Attendance_score,Home_work_score,Quiz_score,participlation_score)
        print(f"Student Name: {student_name}, Final Grade:{grade}")

    
    def get_student_status(final_grade, attendance):
        if grade >= 85 :
            print ("status is Excellent")
        elif 70 <= grade < 84:
            print ("status is Good ")
        elif 50 <= grade < 69:
            print ("status is need improvment ")
        elif  grade < 50:
            print ("status is Failed ")

    def get_student_status (final_grade, attendance): 
        if grade >= 50 and Attendance_score >= 50 : 
         print ("student is Passed ")
        elif  grade >= 50 and Attendance_score < 50:
         print ("student is fail because of low attendance")

