quiz = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "2. Who is known as the Father of the Nation?",
        "options": ["A. Jawaharlal Nehru", "B. Subhas Chandra Bose", "C. Mahatma Gandhi", "D. Bhagat Singh"],
        "answer": "C"
    },
    {
        "question": "3. Which planet is called the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "4. Who wrote the Indian National Anthem?",
        "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Mahatma Gandhi", "D. Subhas Chandra Bose"],
        "answer": "A"
    },
    {
        "question": "5. What is the national animal of India?",
        "options": ["A. Elephant", "B. Tiger", "C. Lion", "D. Peacock"],
        "answer": "B"
    },
    {
        "question": "6. Which is the largest ocean in the world?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
        "answer": "C"
    },
    {
        "question": "7. Who was the first Prime Minister of India?",
        "options": ["A. Mahatma Gandhi", "B. Sardar Vallabhbhai Patel", "C. Jawaharlal Nehru", "D. Rajendra Prasad"],
        "answer": "C"
    },
    {
        "question": "8. Which gas do plants release during photosynthesis?",
        "options": ["A. Carbon Dioxide", "B. Oxygen", "C. Nitrogen", "D. Hydrogen"],
        "answer": "B"
    },
    {
        "question": "9. In which year did India gain independence?",
        "options": ["A. 1942", "B. 1945", "C. 1947", "D. 1950"],
        "answer": "C"
    },
    {
        "question": "10. Who is known as the Missile Man of India?",
        "options": ["A. Dr. APJ Abdul Kalam", "B. Homi Bhabha", "C. Vikram Sarabhai", "D. Satish Dhawan"],
        "answer": "A"
    }
]
win_amt=100000
total_won=0
for q in quiz:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    
    ans=input("Enter you answer (A/B/C/D): ")

    if ans.upper()== q["answer"]:
        total_won+=10000
        print("Congrats you made into the next question and won amt Rs.",total_won,"\n")
        if total_won==win_amt:
            print("")
    else:
        print("Sorry!, Better luck next time")
        break
if total_won==win_amt:
    print("Congratulations you have won 1 lakh and won KBC")
else:
    print("Sorry for not winning kbc, Better luck next time! You Won = Rs.",total_won)
