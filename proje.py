#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Student Management System"""

def calculateFinalGrade(grades):#takes a dictionary including midterm, final and project grades then returns the final grade after some calculations.
    midterm = int(grades.get('midterm'))
    final = int(grades.get('final'))
    project = int(grades.get('project'))
    
    final_grade = (midterm * 30 / 100)  + (final * 50 / 100) + (project * 20 / 100)
    return final_grade

def determinePassingGrade(grade):
    pass_grade = ""
    
    if grade >= 90:
        pass_grade = "AA"
    elif grade <90 and grade >=70:
        pass_grade = "BB"
    elif grade < 70 and grade >= 50:
        pass_grade = "CC"
    elif grade <50 and grade >= 30:
        pass_grade = "DD"
    else:
        pass_grade = "FF"

    return pass_grade

def studentManagementSystem():
    from random import randrange
    
    attempts = 3
    while attempts > 0:
        name = input("Please enter your name..")
        surname = input("Please enter your surname..")
        if name == "" or surname == "":
            print("Incorrect name or surname. Please enter both your name and surname correctly.")
            attempts = attempts - 1
        else:
            break
        if attempts == 0:
            print("Please try again later.")
            return

    lessons = []
    for i in range(1,6):
        lesson = input("Please write the name of the course you want to take or write q to continiue.")
        if lesson == 'q':
            if len(lessons) < 3:
                return('You failed in class')
            else:
                break
        else:
            lessons.append(lesson)
    
    i = 1
    print()
    print("----- Lessons You Took -----")
    for lesson in lessons:
        print(f"Lesson {i} - {lesson}")
        i = i + 1
        
    while True:
        try:
            chosen_lesson = int(input(f"Please choose a lesson number to take exams.(1 - {len(lessons)})"))
            if chosen_lesson < 1 or chosen_lesson > len(lessons):
                print("Please choose a correct lesson number.")
            else:
                break
        except:
            print("Please choose a correct lesson number.")
    lesson = lessons[chosen_lesson - 1]
    #print(lesson)
    
    midterm = randrange(101)
    final = randrange(101)
    project = randrange(101)
    grades = {"midterm": midterm, 'final':final, 'project':project}
       
    final_grade = calculateFinalGrade(grades)
    note = determinePassingGrade(final_grade)
    
    if note == "FF":
        pass
    else:
        print(f"NOTE: {note}")
    
studentManagementSystem()


# In[ ]:




