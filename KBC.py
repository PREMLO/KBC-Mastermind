import tkinter as tk
from tkinter import messagebox
import random

# All 60 questions (50 original + 10 additional)
all_questions = [
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Mumbai", "Chennai", "Kolkata"],
        "answer": "New Delhi"
    },
    {
        "question": "Who is the Prime Minister of India?",
        "options": ["Narendra Modi", "Manmohan Singh", "Rahul Gandhi", "Amit Shah"],
        "answer": "Narendra Modi"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Mars", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "Which language is used to create web pages?",
        "options": ["Python", "Java", "HTML", "C++"],
        "answer": "HTML"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Lyon", "Marseille", "Nice"],
        "answer": "Paris"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Japan", "South Korea", "Vietnam"],
        "answer": "Japan"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "George Orwell", "Jane Austen"],
        "answer": "William Shakespeare"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Gold", "Oxygen", "Osmium", "Oganesson"],
        "answer": "Oxygen"
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["1905", "1912", "1920", "1930"],
        "answer": "1912"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Who discovered penicillin?",
        "options": ["Marie Curie", "Alexander Fleming", "Isaac Newton", "Albert Einstein"],
        "answer": "Alexander Fleming"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mercury", "Venus", "Earth", "Mars"],
        "answer": "Mars"
    },
    {
        "question": "Which country hosted the 2016 Summer Olympics?",
        "options": ["China", "Brazil", "UK", "Russia"],
        "answer": "Brazil"
    },
    {
        "question": "What is the square root of 144?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "Which gas is most abundant in the Earth's atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Nitrogen"
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "options": ["Tomato", "Cucumber", "Avocado", "Lettuce"],
        "answer": "Avocado"
    },
    {
        "question": "Who is the author of 'Harry Potter' series?",
        "options": ["J.R.R. Tolkien", "J.K. Rowling", "Stephen King", "George R.R. Martin"],
        "answer": "J.K. Rowling"
    },
    {
        "question": "Which planet has the most moons?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "Which country is known as the Land of the Pharaohs?",
        "options": ["Greece", "Rome", "Egypt", "Persia"],
        "answer": "Egypt"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
        "answer": "Canberra"
    },
    {
        "question": "What is the smallest continent?",
        "options": ["Africa", "Australia", "Europe", "Antarctica"],
        "answer": "Australia"
    },
    {
        "question": "Who wrote 'Pride and Prejudice'?",
        "options": ["Jane Austen", "Emily Bronte", "Charles Dickens", "George Eliot"],
        "answer": "Jane Austen"
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "answer": "Nile"
    },
    # Add your original 47 questions here...

    {
        "question": "Which country experienced significant protests in 2023 against judicial reforms proposed by its government?",
        "options": ["Israel", "Poland", "Turkey", "Hungary"],
        "answer": "Israel"
    },
    {
        "question": "Who is the current President of Nigeria following the 2023 elections?",
        "options": ["Muhammadu Buhari", "Atiku Abubakar", "Bola Tinubu", "Goodluck Jonathan"],
        "answer": "Bola Tinubu"
    },
    {
        "question": "Which country enacted a strict immigration policy called 'Operation Sovereign Borders'?",
        "options": ["United States", "Australia", "United Kingdom", "Canada"],
        "answer": "Australia"
    },
    {
        "question": "Who is the current President of South Korea, elected in 2022?",
        "options": ["Moon Jae-in", "Park Geun-hye", "Yoon Suk-yeol", "Lee Jae-myung"],
        "answer": "Yoon Suk-yeol"
    },
    {
        "question": "Which African country had a major political scandal involving corruption in its state oil company, Petrobras, in recent years?",
        "options": ["Nigeria", "Angola", "South Africa", "Kenya"],
        "answer": "Nigeria"
    },
    {
        "question": "Who is the Prime Minister of Italy as of 2023?",
        "options": ["Mario Draghi", "Matteo Renzi", "Giuseppe Conte", "Giorgia Meloni"],
        "answer": "Giorgia Meloni"
    },
    {
        "question": "Which country’s president announced in 2023 that he would not seek re-election after massive protests over a pension reform plan?",
        "options": ["France", "Colombia", "Peru", "Chile"],
        "answer": "Colombia"
    },
    {
        "question": "Which Southeast Asian country has seen significant political unrest and protests demanding monarchy reform since 2020?",
        "options": ["Thailand", "Malaysia", "Indonesia", "Philippines"],
        "answer": "Thailand"
    },
    {
        "question": "Who is the Prime Minister of Japan, having taken office in 2021?",
        "options": ["Shinzo Abe", "Yoshihide Suga", "Fumio Kishida", "Taro Kono"],
        "answer": "Fumio Kishida"
    },
    {
        "question": "Which country experienced a major cyberattack in 2023 targeting its healthcare system, leading to significant data breaches?",
        "options": ["Canada", "Ireland", "New Zealand", "Finland"],
        "answer": "Ireland"
    }
    # Add your additional 7 questions here...
]

# Shuffle questions at the start of the game
random.shuffle(all_questions)

# Limit to 20 questions
all_questions = all_questions[:20]

# Prize amounts for each question
amounts = [
    "₹1,000", "₹2,000", "₹3,000", "₹5,000", "₹10,000", 
    "₹20,000", "₹40,000", "₹80,000", "₹1,60,000", "₹3,20,000", 
    "₹6,40,000", "₹12,50,000", "₹25,00,000", "₹50,00,000", "₹1 Crore",
    "₹3 Crore", "₹5 Crore", "₹7 Crore", "₹10 Crore", "₹15 Crore"
]

class KBCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaun Banega Crorepati")
        self.root.config(bg="#003366")  # Dark Blue Background
        self.question_index = 0
        self.correct_answers = 0
        self.lifelines_used = {
            "50-50": False,
            "Phone a Friend": False,
            "Ask the Audience": False,
            "Flip the Question": False
        }
        self.create_widgets()
        self.show_welcome_message()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=400, font=("Arial", 16), bg="#003366", fg="white")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", wraplength=400, font=("Arial", 14), bg="white", fg="#003366", command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.lifeline_frame = tk.Frame(self.root, bg="#003366")
        self.lifeline_frame.pack(pady=20)

        self.lifeline_buttons = {}
        for lifeline in self.lifelines_used.keys():
            button = tk.Button(self.lifeline_frame, text=lifeline, font=("Arial", 12), bg="#ffffff", fg="#003366", command=lambda l=lifeline: self.use_lifeline(l))
            button.pack(side="left", padx=10)
            self.lifeline_buttons[lifeline] = button

    def show_welcome_message(self):
        messagebox.showinfo("Welcome", "Welcome to Kaun Banega Crorepati! Get ready to play and win!")
        self.show_question()

    def show_question(self):
        if self.question_index < len(all_questions):
            question_data = all_questions[self.question_index]
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option, state="normal")
        else:
            self.show_final_amount()

    def check_answer(self, selected_index):
        question_data = all_questions[self.question_index]
        selected_option = question_data["options"][selected_index]
        if selected_option == question_data["answer"]:
            self.correct_answers += 1
            self.show_won_amount()
            self.question_index += 1
            self.show_question()
        else:
            self.end_game()

    def show_won_amount(self):
        if self.correct_answers > 0:
            won_amount = amounts[self.correct_answers - 1]
            messagebox.showinfo("Congratulations!", f"You have won {won_amount} so far!")
        else:
            messagebox.showinfo("Congratulations!", "You have won ₹0 so far!")

    def show_final_amount(self):
        if self.correct_answers > 0:
            final_amount = amounts[self.correct_answers - 1]
        else:
            final_amount = "₹0"
        messagebox.showinfo("Game Over", f"Congratulations! You have won {final_amount}.")
        self.root.quit()

    def end_game(self):
        if self.correct_answers > 0:
            won_amount = amounts[self.correct_answers - 1]
        else:
            won_amount = "₹0"
        messagebox.showinfo("Game Over", f"Wrong answer! You have won {won_amount}.")
        self.root.quit()

    def use_lifeline(self, lifeline):
        if not self.lifelines_used[lifeline]:
            if lifeline == "50-50":
                self.use_50_50()
            elif lifeline == "Phone a Friend":
                self.use_phone_a_friend()
            elif lifeline == "Ask the Audience":
                self.use_ask_the_audience()
            elif lifeline == "Flip the Question":
                self.use_flip_the_question()
            self.lifelines_used[lifeline] = True
            self.lifeline_buttons[lifeline].config(state="disabled")
        else:
            messagebox.showinfo("Lifeline", f"You have already used the {lifeline} lifeline.")

    def use_50_50(self):
        question_data = all_questions[self.question_index]
        correct_option = question_data["answer"]
        options = question_data["options"]
        options_to_remove = random.sample([opt for opt in options if opt != correct_option], 2)
        for i, option in enumerate(options):
            if option in options_to_remove:
                self.option_buttons[i].config(text="", state="disabled")

    def use_phone_a_friend(self):
        question_data = all_questions[self.question_index]
        correct_option = question_data["answer"]
        messagebox.showinfo("Phone a Friend", f"Your friend suggests the answer might be: {correct_option}")

    def use_ask_the_audience(self):
        question_data = all_questions[self.question_index]
        correct_option = question_data["answer"]
        messagebox.showinfo("Ask the Audience", f"The audience suggests the answer might be: {correct_option}")

    def use_flip_the_question(self):
        self.question_index += 1
        self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = KBCApp(root)
    root.mainloop()
