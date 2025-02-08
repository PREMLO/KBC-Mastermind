import tkinter as tk
from tkinter import messagebox
import random

# All categorized questions
easy_questions = [
    {"question": "What is the smallest planet in our solar system?", "options": ["Earth", "Venus", "Mercury", "Mars"], "answer": "Mercury"},
    {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "South Korea", "Vietnam"], "answer": "Japan"},
    {"question": "What is the capital city of Tamil Nadu?", "options": ["Mumbai", "Bangalore", "Chennai", "Kolkata"], "answer": "Chennai"},
    {"question": "Which bird is India's national bird?", "options": ["Peacock", "Parrot", "Sparrow", "Eagle"], "answer": "Peacock"},
    {"question": "What is the boiling point of water in degrees Celsius?", "options": ["90", "100", "110", "120"], "answer": "100"},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "options": ["Shakespeare", "Charles Dickens", "George Orwell", "Jane Austen"], "answer": "Shakespeare"},
    {"question": "Which animal is known as the king of the jungle?", "options": ["Tiger", "Lion", "Elephant", "Wolf"], "answer": "Lion"},
    {"question": "How many days are there in a leap year?", "options": ["365", "366", "364", "360"], "answer": "366"},
    {"question": "Which is the largest mammal in the world?", "options": ["Elephant", "Blue whale", "Giraffe", "Shark"], "answer": "Blue whale"},
    {"question": "What is the currency of the United States?", "options": ["Pound", "Dollar", "Euro", "Yen"], "answer": "Dollar"},
]

medium_questions = [
    {"question": "Who invented the telephone?", "options": ["Edison", "Alexander Graham Bell", "Tesla", "Newton"], "answer": "Alexander Graham Bell"},
    {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Diamond", "Iron", "Platinum"], "answer": "Diamond"},
    {"question": "Which planet is known for its rings?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Saturn"},
    {"question": "What is the capital city of Canada?", "options": ["Toronto", "Ottawa", "Montreal", "Vancouver"], "answer": "Ottawa"},
    {"question": "Who is known as the 'Father of the Indian Constitution'?", "options": ["Nehru", "Gandhi", "B.R. Ambedkar", "Sardar Patel"], "answer": "B.R. Ambedkar"},
    {"question": "What is the chemical formula for table salt?", "options": ["NaCl", "H2O", "CO2", "O2"], "answer": "NaCl"},
    {"question": "In which year did India gain independence?", "options": ["1947", "1950", "1935", "1962"], "answer": "1947"},
    {"question": "Who is the author of 'Harry Potter' series?", "options": ["J.K. Rowling", "J.R.R. Tolkien", "George Orwell", "Dan Brown"], "answer": "J.K. Rowling"},
    {"question": "Which gas is most abundant in the Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "answer": "Nitrogen"},
    {"question": "What is the square root of 144?", "options": ["10", "12", "14", "16"], "answer": "12"},
]

hard_questions = [
    {"question": "Who was the king of the gods in Greek mythology?", "options": ["Hades", "Zeus", "Apollo", "Hermes"], "answer": "Zeus"},
    {"question": "Who painted 'The Last Supper'?", "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "answer": "Leonardo da Vinci"},
    {"question": "Which physicist developed the theory of relativity?", "options": ["Newton", "Tesla", "Einstein", "Bohr"], "answer": "Einstein"},
    {"question": "What is the capital city of Mongolia?", "options": ["Astana", "Beijing", "Ulaanbaatar", "Bishkek"], "answer": "Ulaanbaatar"},
    {"question": "Who wrote 'The Republic'?", "options": ["Aristotle", "Plato", "Socrates", "Descartes"], "answer": "Plato"},
    {"question": "Which battle in 1314 saw Robert the Bruce defeat the English?", "options": ["Battle of Hastings", "Battle of Agincourt", "Battle of Bannockburn", "Battle of Waterloo"], "answer": "Battle of Bannockburn"},
    {"question": "What is the scientific name for the knee cap?", "options": ["Femur", "Patella", "Tibia", "Fibula"], "answer": "Patella"},
    {"question": "Which planet has the shortest year in the solar system?", "options": ["Mercury", "Venus", "Mars", "Neptune"], "answer": "Mercury"},
    {"question": "Which Mughal emperor built the Taj Mahal?", "options": ["Akbar", "Aurangzeb", "Shah Jahan", "Babur"], "answer": "Shah Jahan"},
    {"question": "What was the name of the ship on which the Pilgrims traveled to America in 1620?", "options": ["Santa Maria", "Titanic", "Mayflower", "Endeavour"], "answer": "Mayflower"},
]

# Selecting 5 random questions from each difficulty level
selected_questions = random.sample(easy_questions, 5) + random.sample(medium_questions, 5) + random.sample(hard_questions, 5)

# Prize money for each question
amounts = ["₹1,000", "₹2,000", "₹5,000", "₹10,000", "₹20,000", "₹40,000", "₹80,000", "₹1,60,000", "₹3,20,000", "₹6,40,000",
           "₹12,50,000", "₹25,00,000", "₹50,00,000", "₹1 Crore", "₹7 Crore"]

class KBCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaun Banega Crorepati")
        self.root.config(bg="#003366")
        self.question_index = 0
        self.correct_answers = 0
        self.create_widgets()
        self.show_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=400, font=("Arial", 16), bg="#003366", fg="white")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", wraplength=400, font=("Arial", 14), bg="white", fg="#003366", command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

    def show_question(self):
        question_data = selected_questions[self.question_index]
        self.question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option, state="normal")

    def check_answer(self, selected_index):
        question_data = selected_questions[self.question_index]
        if question_data["options"][selected_index] == question_data["answer"]:
            self.correct_answers += 1
        self.question_index += 1
        self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = KBCApp(root)
    root.mainloop()
