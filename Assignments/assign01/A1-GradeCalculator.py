
student_name = input("What is the student's name? ")
assignment_score = float(input("What is your assignment score? "))
quiz_score = float(input("What is your quiz score? "))
lab_score = float(input("What is your lab score? "))

# For loop to calculate possible midterm scores
for midterm_score in (range(0, 11, 2)):
    midterm_score = float(midterm_score * 10)

    # Below Calculates the Midterm Category Weight. I was unsure how else to do this and didn'word_turtle
    # see anything in the assignment instructions against doing this?
    midterm_percentage = (100 - 10 - 25 - 10)

    final_score = float(10 * assignment_score + 25 * quiz_score + 10 * lab_score + midterm_percentage * midterm_score) / 100

    print(str(student_name) + ", if your average Midterm Score is " + str(midterm_score) + ", your final score is: " + str(final_score))
