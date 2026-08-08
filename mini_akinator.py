import json
import os

class AkinatorGame:
    def __init__(self):
        self.questions_file = "questions.json"
        self.characters_file = "characters.json"
        self.questions = self.load_data(self.questions_file)
        self.characters = self.load_data(self.characters_file)
        self.current_node = 0  # Start with the first question
    
    def load_data(self, filename):
        """Load questions or characters from JSON file"""
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
        else:
            # Initialize with default data if files don't exist
            if filename == self.questions_file:
                return [
                    {"id": 0, "question": "Is your character male?", "yes": 1, "no": 2},
                    {"id": 1, "question": "Is your character a real person?", "yes": 3, "no": 4},
                    {"id": 2, "question": "Is your character from a movie?", "yes": 5, "no": 6},
                    {"id": 3, "question": "Is your character alive?", "yes": None, "no": None},
                    {"id": 4, "question": "Is your character a superhero?", "yes": None, "no": None},
                    {"id": 5, "question": "Is your character an animal?", "yes": None, "no": None},
                    {"id": 6, "question": "Is your character from a book?", "yes": None, "no": None}
                ]
            else:
                return {}
    
    def save_data(self):
        """Save questions and characters to JSON files"""
        with open(self.questions_file, 'w') as f:
            json.dump(self.questions, f, indent=2)
        with open(self.characters_file, 'w') as f:
            json.dump(self.characters, f, indent=2)
    
    def get_question(self, question_id):
        """Get question by ID"""
        for q in self.questions:
            if q["id"] == question_id:
                return q
        return None
    
    def get_yes_no_input(self, prompt):
        """Get yes/no input from user"""
        while True:
            answer = input(prompt).strip().lower()
            if answer in ['y', 'yes']:
                return True
            elif answer in ['n', 'no']:
                return False
            else:
                print("Please answer with 'yes' or 'no' (y/n).")
    
    def ask_question(self, question_id):
        """Ask a question and return the next question ID based on answer"""
        question = self.get_question(question_id)
        if question is None:
            return None
        
        answer = self.get_yes_no_input(f"{question['question']} (y/n): ")
        
        if answer:
            return question.get("yes")
        else:
            return question.get("no")
    
    def add_new_character(self, current_question_id, answer):
        """Add a new character to the database"""
        print("\nI give up! Who were you thinking of?")
        new_character = input("Enter the character's name: ").strip()
        
        print(f"What question would distinguish {new_character} from my guess?")
        new_question = input("Enter a yes/no question: ").strip()
        
        # Add new question
        new_question_id = max([q["id"] for q in self.questions]) + 1
        self.questions.append({
            "id": new_question_id,
            "question": new_question,
            "yes": None,
            "no": None
        })
        
        # Update the current question to point to the new question
        current_question = self.get_question(current_question_id)
        if answer:
            current_question["yes"] = new_question_id
        else:
            current_question["no"] = new_question_id
        
        # Add the new character
        self.characters[new_question_id] = new_character
        
        print(f"Thanks! I'll remember {new_character} for next time.")
        self.save_data()
    
    def play_round(self):
        """Play one round of the game"""
        print("\nThink of a character (real or fictional), and I'll try to guess it!")
        print("Answer with 'yes' or 'no' (y/n).\n")
        
        current_node = 0
        
        while True:
            next_node = self.ask_question(current_node)
            
            # If we've reached a leaf node (character guess)
            if next_node is None:
                # Check if we have a character at this node
                if current_node in self.characters:
                    guess = self.characters[current_node]
                    if self.get_yes_no_input(f"Is your character {guess}? (y/n): "):
                        print("Yay! I guessed it!")
                    else:
                        self.add_new_character(current_node, True)
                else:
                    self.add_new_character(current_node, False)
                break
            
            current_node = next_node
    
    def play_game(self):
        """Main game loop"""
        print("Welcome to the Akinator-style Game!")
        
        while True:
            self.play_round()
            
            if not self.get_yes_no_input("\nDo you want to play again? (y/n): "):
                print("Thanks for playing!")
                break

# Run the game
if __name__ == "__main__":
    game = AkinatorGame()
    game.play_game()