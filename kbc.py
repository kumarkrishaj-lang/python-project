# KBC Game in Python

# Questions, Options and Answers
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "answer": "C"
    },
    {
        "question": "Who is known as the Father of the Nation (India)?",
        "options": ["A. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. B. R. Ambedkar", "D. Sardar Patel"],
        "answer": "B"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "answer": "C"
    }
]

# Prize money for each question
prizes = [1000, 2000, 5000, 10000]

print("🙏 Welcome to Kaun Banega Crorepati (KBC) 🙏\n")

total_winnings = 0

for i in range(len(questions)):
    q = questions[i]
    print(f"Question {i+1} for ₹{prizes[i]}:")
    print(q["question"])
    for option in q["options"]:
        print(option)

    # User input
    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == q["answer"]:
        print("✅ Correct Answer!")
        total_winnings = prizes[i]
    else:
        print("❌ Wrong Answer!")
        print(f"Correct Answer was: {q['answer']}")
        break

    print(f"Your total winnings: ₹{total_winnings}\n")
    print("-" * 40)

print(f"\n🎉 You won a total of ₹{total_winnings}. Thanks for playing KBC! 🎉")
