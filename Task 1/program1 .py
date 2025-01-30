import logging

# Setup logging for better tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def display_question(question):
    """Display the question and options."""
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)

def get_valid_answer():
    """Ensure the user inputs a valid answer (1-4)."""
    while True:
        try:
            answer = int(input("Choose the correct option (1-4): "))
            if 1 <= answer <= 4:
                return answer
            else:
                print("Please choose a valid option between 1 and 4.")
        except ValueError:
            print("Invalid input! Please choose a number between 1 and 4.")

def check_answer(user_answer, correct_answer):
    """Check if the user's answer is correct and return feedback."""
    if user_answer == correct_answer:
        return True
    else:
        return False

def ask_questions(questions):
    """Loop through each question and collect answers."""
    score = 0
    for question in questions:
        display_question(question)
        answer = get_valid_answer()
        
        if check_answer(answer, question["correct_answer"]):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    
    return score

def play_game():
    """Main function to run the quiz game."""
    logging.info("Starting the quiz game")

    # List of questions, options, and the correct answer
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["1. Paris", "2. London", "3. Berlin", "4. Madrid"],
            "correct_answer": 1
        },
        {
            "question": "Who developed the theory of relativity?",
            "options": ["1. Isaac Newton", "2. Albert Einstein", "3. Galileo Galilei", "4. Nikola Tesla"],
            "correct_answer": 2
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["1. Atlantic Ocean", "2. Indian Ocean", "3. Pacific Ocean", "4. Arctic Ocean"],
            "correct_answer": 3
        }
    ]

    # Ask the questions and get the score
    score = ask_questions(questions)
    
    # Display final score
    print(f"\nYour final score is: {score}/{len(questions)}")
    
    # Replay option
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        
        if play_again == "yes":
            play_game()  # Restart the quiz
            break
        elif play_again == "no":
            print("Thanks for playing!")
            logging.info("Game ended by user.")
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

# Start the game
if __name__ == "__main__":
    play_game()
