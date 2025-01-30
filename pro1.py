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

    # List of 20 questions, options, and the correct answer
    questions = [
        {"question": "What is the capital of France?", "options": ["1. Paris", "2. London", "3. Berlin", "4. Madrid"], "correct_answer": 1},
        {"question": "Who developed the theory of relativity?", "options": ["1. Isaac Newton", "2. Albert Einstein", "3. Galileo Galilei", "4. Nikola Tesla"], "correct_answer": 2},
        {"question": "What is the largest ocean on Earth?", "options": ["1. Atlantic Ocean", "2. Indian Ocean", "3. Pacific Ocean", "4. Arctic Ocean"], "correct_answer": 3},
        {"question": "Which planet is known as the Red Planet?", "options": ["1. Venus", "2. Mars", "3. Jupiter", "4. Saturn"], "correct_answer": 2},
        {"question": "Who was the first president of the United States?", "options": ["1. Abraham Lincoln", "2. George Washington", "3. John Adams", "4. Thomas Jefferson"], "correct_answer": 2},
        {"question": "What is the hardest natural substance on Earth?", "options": ["1. Gold", "2. Diamond", "3. Iron", "4. Lead"], "correct_answer": 2},
        {"question": "What is the chemical symbol for water?", "options": ["1. H2O", "2. O2", "3. CO2", "4. H2"], "correct_answer": 1},
        {"question": "In which continent is the Amazon Rainforest located?", "options": ["1. Africa", "2. Asia", "3. South America", "4. North America"], "correct_answer": 3},
        {"question": "What is the smallest planet in our solar system?", "options": ["1. Mercury", "2. Venus", "3. Mars", "4. Pluto"], "correct_answer": 1},
        {"question": "What is the tallest mountain in the world?", "options": ["1. Mount Kilimanjaro", "2. Mount Everest", "3. Mount Fuji", "4. K2"], "correct_answer": 2},
        {"question": "Who painted the Mona Lisa?", "options": ["1. Vincent van Gogh", "2. Pablo Picasso", "3. Leonardo da Vinci", "4. Claude Monet"], "correct_answer": 3},
        {"question": "Which country is known as the Land of the Rising Sun?", "options": ["1. China", "2. Japan", "3. Korea", "4. Thailand"], "correct_answer": 2},
        {"question": "What is the largest desert in the world?", "options": ["1. Sahara", "2. Arabian", "3. Gobi", "4. Antarctica"], "correct_answer": 4},
        {"question": "Which element has the chemical symbol 'O'?", "options": ["1. Oxygen", "2. Osmium", "3. Ozone", "4. Opium"], "correct_answer": 1},
        {"question": "Who wrote the play 'Romeo and Juliet'?", "options": ["1. William Shakespeare", "2. Charles Dickens", "3. Mark Twain", "4. Jane Austen"], "correct_answer": 1},
        {"question": "Which gas do plants absorb from the atmosphere?", "options": ["1. Oxygen", "2. Carbon Dioxide", "3. Nitrogen", "4. Methane"], "correct_answer": 2},
        {"question": "What is the capital of Japan?", "options": ["1. Seoul", "2. Beijing", "3. Tokyo", "4. Bangkok"], "correct_answer": 3},
        {"question": "What is the national flower of the United States?", "options": ["1. Rose", "2. Lily", "3. Tulip", "4. Orchid"], "correct_answer": 1},
        {"question": "Who invented the telephone?", "options": ["1. Nikola Tesla", "2. Alexander Graham Bell", "3. Thomas Edison", "4. Michael Faraday"], "correct_answer": 2},
        {"question": "Which ocean lies between Africa and Australia?", "options": ["1. Atlantic Ocean", "2. Indian Ocean", "3. Pacific Ocean", "4. Southern Ocean"], "correct_answer": 2}
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
