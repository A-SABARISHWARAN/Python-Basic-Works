#Python Quiz Game

print("Last Day of Coding Challenge, So Let's Us REVISE!")

questions = ("1. Who developed Python Programming Language?: ",
             "2. Which of the following is the correct extension of the Python file?: ",
             "3. All keywords in Python are in _________?: ",
             "4. Which keyword is used for function in Python language?: ",
             "5. Which of the following character is used to give single-line comments in Python?: ")

options = (("A.Wick van Rossum","B.Rasmus Lerdorf","C.Guido van Rossum","D. Niene Stom"),
           ("A..python","B. .pl","C. .py","D. .ph"),
           ("A. Capitalized","B.lower case","C. UPPER CASE","D. None of these"),
           ("A.Function","B. def","C. Fun","D. Define"),
           ("A. //","B. #","C. /","D. !"))


answers = ("C","C","D","B","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("**************")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your Guess (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------")
print("    RESULT      ")
print("----------------")

print("Answers : ", end="")
for answer in answers:
    print(answer, end=' ')
print()

print("Guesses : ", end="")
for guess in guesses:
    print(guess, end=' ')
print()

score = int(score / len(questions) * 100)
print(f"Your Score is : {score}%")
