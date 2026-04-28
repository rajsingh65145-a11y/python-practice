questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": 2
    },
    {
        "question": "Which language is used for web development?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": 2
    },
    {
        "question": "Who developed Python?",
        "options": ["Dennis Ritchie", "James Gosling", "Guido van Rossum", "Bjarne Stroustrup"],
        "answer": 3
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "<!-- -->"],
        "answer": 2
    }
]

score = 0

print("---- Welcome to Quiz Application ----\n")

for i, q in enumerate(questions, 1):
    print(f"Q{i}. {q['question']}")
    
    for idx, option in enumerate(q["options"], 1):
        print(f"{idx}. {option}")
    
    user_ans = int(input("Enter your answer (1-4): "))
    
    if user_ans == q["answer"]:
        print("Correct \n")
        score += 1
    else:
        print("Wrong \n")

print("Quiz Completed ")
print("Your Score:", score, "/", len(questions))