import tkinter as tk
from tkinter import messagebox, ttk
import random
import math

class TreasureHuntGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mathematical Treasure Hunt")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        # Game state variables
        self.current_puzzle = 0
        self.puzzle_answers = []
        self.solved_puzzles = []
        self.game_phase = "welcome"  # welcome, puzzles, treasure, results
        
        # Define interconnected mathematical puzzles
        self.puzzles = [
            {
                "question": "What is the sum of the first 5 prime numbers?",
                "answer": 28,  # 2+3+5+7+11
                "hint": "Prime numbers are: 2, 3, 5, 7, 11..."
            },
            {
                "question": "If the previous answer is X, what is X² - 100?",
                "answer": 684,  # 28² - 100 = 784 - 100
                "hint": "Square the previous answer and subtract 100"
            },
            {
                "question": "Find the square root of the previous answer.",
                "answer": 26,  # √684 ≈ 26.15, but we'll accept 26
                "hint": "What number when multiplied by itself gives approximately the previous answer?"
            },
            {
                "question": "If Y is the previous answer, what is the value of 3Y + 22?",
                "answer": 100,  # 3×26 + 22 = 78 + 22
                "hint": "Multiply the previous answer by 3 and add 22"
            },
            {
                "question": "What is the factorial of 5 minus the previous answer?",
                "answer": 20,  # 5! - 100 = 120 - 100
                "hint": "5! = 5×4×3×2×1, then subtract the previous answer"
            }
        ]
        
        # Treasure box contents
        self.treasure_boxes = [
            {"type": "reward", "content": "🏆 CONGRATULATIONS! You found the legendary Golden Treasure! 💰"},
            {"type": "insult", "content": "💩 Empty box! Better luck next time, treasure hunter!"},
            {"type": "clue", "content": "🗝️ Clue: The real treasure was the math you learned along the way..."},
            {"type": "insult", "content": "🐍 A snake jumps out! Hiss! Nothing here but disappointment!"},
            {"type": "clue", "content": "📜 Ancient wisdom: Try a different box, young adventurer!"},
            {"type": "insult", "content": "🕷️ Just cobwebs and spider webs. This box has been empty for centuries!"}
        ]
        
        self.setup_welcome_screen()
    
    def setup_welcome_screen(self):
        self.clear_screen()
        
        title_label = tk.Label(self.root, text="🏴‍☠️ MATHEMATICAL TREASURE HUNT 🏴‍☠️", 
                             font=("Arial", 20, "bold"), fg="gold", bg="#2c3e50")
        title_label.pack(pady=30)
        
        intro_text = """
        Welcome, brave treasure hunter! 
        
        You must solve 5 interconnected mathematical puzzles
        to unlock the treasure chamber.
        
        Each answer will lead you to the next puzzle.
        Only the wisest can claim the golden treasure!
        
        Are you ready to begin your quest?
        """
        
        intro_label = tk.Label(self.root, text=intro_text, font=("Arial", 12), 
                             fg="white", bg="#2c3e50", justify="center")
        intro_label.pack(pady=20)
        
        start_button = tk.Button(self.root, text="🚀 START ADVENTURE", 
                               font=("Arial", 14, "bold"), bg="gold", fg="black",
                               command=self.start_puzzles, padx=20, pady=10)
        start_button.pack(pady=30)
    
    def start_puzzles(self):
        self.game_phase = "puzzles"
        self.current_puzzle = 0
        self.show_puzzle()
    
    def show_puzzle(self):
        self.clear_screen()
        
        # Progress indicator
        progress_text = f"Puzzle {self.current_puzzle + 1} of {len(self.puzzles)}"
        progress_label = tk.Label(self.root, text=progress_text, font=("Arial", 12), 
                                fg="gold", bg="#2c3e50")
        progress_label.pack(pady=10)
        
        # Show previous answers if any
        if self.puzzle_answers:
            prev_answers_text = "Previous answers: " + " → ".join(map(str, self.puzzle_answers))
            prev_label = tk.Label(self.root, text=prev_answers_text, font=("Arial", 10), 
                                fg="lightblue", bg="#2c3e50")
            prev_label.pack(pady=5)
        
        # Current puzzle
        puzzle = self.puzzles[self.current_puzzle]
        
        # Adjust question based on previous answers
        question = puzzle["question"]
        if "previous answer" in question.lower() and self.puzzle_answers:
            question = question.replace("X", str(self.puzzle_answers[-1]))
            question = question.replace("Y", str(self.puzzle_answers[-1]))
        
        question_label = tk.Label(self.root, text=question, font=("Arial", 14, "bold"), 
                                fg="white", bg="#2c3e50", wraplength=700)
        question_label.pack(pady=30)
        
        # Answer entry
        self.answer_var = tk.StringVar()
        answer_frame = tk.Frame(self.root, bg="#2c3e50")
        answer_frame.pack(pady=20)
        
        tk.Label(answer_frame, text="Your Answer:", font=("Arial", 12), 
                fg="white", bg="#2c3e50").pack(side=tk.LEFT, padx=5)
        
        answer_entry = tk.Entry(answer_frame, textvariable=self.answer_var, 
                              font=("Arial", 14), width=10, justify="center")
        answer_entry.pack(side=tk.LEFT, padx=10)
        answer_entry.focus()
        
        # Bind Enter key
        answer_entry.bind('<Return>', lambda e: self.check_answer())
        
        # Buttons
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=30)
        
        submit_button = tk.Button(button_frame, text="✅ Submit Answer", 
                                font=("Arial", 12), bg="green", fg="white",
                                command=self.check_answer, padx=15)
        submit_button.pack(side=tk.LEFT, padx=10)
        
        hint_button = tk.Button(button_frame, text="💡 Show Hint", 
                              font=("Arial", 12), bg="orange", fg="white",
                              command=self.show_hint, padx=15)
        hint_button.pack(side=tk.LEFT, padx=10)
    
    def show_hint(self):
        puzzle = self.puzzles[self.current_puzzle]
        messagebox.showinfo("Hint", puzzle["hint"])
    
    def check_answer(self):
        try:
            user_answer = int(self.answer_var.get())
            correct_answer = self.puzzles[self.current_puzzle]["answer"]
            
            # Allow some tolerance for square root calculations
            if self.current_puzzle == 2:  # Square root puzzle
                if abs(user_answer - correct_answer) <= 2:
                    user_answer = correct_answer
            
            if user_answer == correct_answer:
                self.puzzle_answers.append(user_answer)
                self.solved_puzzles.append(self.current_puzzle)
                
                messagebox.showinfo("Correct! 🎉", f"Excellent work! The answer is {correct_answer}")
                
                self.current_puzzle += 1
                if self.current_puzzle < len(self.puzzles):
                    self.show_puzzle()
                else:
                    self.show_treasure_room()
            else:
                messagebox.showerror("Incorrect ❌", 
                                   f"That's not correct. Try again!\nYour answer: {user_answer}")
                self.answer_var.set("")
                
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number!")
            self.answer_var.set("")
    
    def show_treasure_room(self):
        self.clear_screen()
        self.game_phase = "treasure"
        
        # Make window larger for treasure room
        self.root.geometry("900x700")
        
        title_label = tk.Label(self.root, text="🏛️ THE TREASURE CHAMBER 🏛️", 
                             font=("Arial", 18, "bold"), fg="gold", bg="#2c3e50")
        title_label.pack(pady=10)
        
        instructions = f"""
        🎉 Congratulations! You have solved all puzzles! 🎉
        Your keys are: {' - '.join(map(str, self.puzzle_answers))}
        
        📦 Choose one of the 6 treasure boxes below! 📦
        Only one contains the real treasure!
        """
        
        instruction_label = tk.Label(self.root, text=instructions, font=("Arial", 12, "bold"), 
                                   fg="white", bg="#2c3e50", justify="center")
        instruction_label.pack(pady=10)
        
        # Create treasure boxes - Make them more prominent
        boxes_label = tk.Label(self.root, text="👇 CLICK A TREASURE BOX BELOW 👇", 
                             font=("Arial", 14, "bold"), fg="yellow", bg="#2c3e50")
        boxes_label.pack(pady=5)
        
        box_frame = tk.Frame(self.root, bg="#2c3e50")
        box_frame.pack(pady=20)
        
        self.box_buttons = []
        for i in range(6):
            row = i // 3
            col = i % 3
            
            box_button = tk.Button(box_frame, text=f"📦\nBox {i+1}", 
                                 font=("Arial", 14, "bold"), bg="brown", fg="gold",
                                 width=12, height=5,
                                 command=lambda box_num=i: self.open_treasure_box(box_num),
                                 relief="raised", bd=5)
            box_button.grid(row=row, col=col, padx=20, pady=20)
            self.box_buttons.append(box_button)
    
    def open_treasure_box(self, box_num):
        # Add some suspense
        self.box_buttons[box_num].config(text="🔓\nOpening...", state="disabled")
        self.root.after(1000, lambda: self.reveal_box_content(box_num))
    
    def reveal_box_content(self, box_num):
        # Randomly assign treasure box contents
        contents = self.treasure_boxes.copy()
        random.shuffle(contents)
        
        # Ensure at least one reward exists
        if not any(content["type"] == "reward" for content in contents[:6]):
            contents[0] = {"type": "reward", "content": "🏆 CONGRATULATIONS! You found the legendary Golden Treasure! 💰"}
        
        selected_content = contents[box_num]
        
        # Update button appearance based on content
        if selected_content["type"] == "reward":
            self.box_buttons[box_num].config(text="💰\nTREASURE!", bg="gold", fg="black")
        elif selected_content["type"] == "clue":
            self.box_buttons[box_num].config(text="📜\nCLUE", bg="blue", fg="white")
        else:
            self.box_buttons[box_num].config(text="💩\nEMPTY", bg="gray", fg="black")
        
        # Show result
        messagebox.showinfo("Box Contents", selected_content["content"])
        
        # Ask if they want to try another box or finish
        if selected_content["type"] == "reward":
            self.show_victory_screen()
        else:
            result = messagebox.askyesno("Continue?", "Would you like to try another box?")
            if not result:
                self.show_results_screen()
    
    def show_victory_screen(self):
        self.clear_screen()
        
        victory_label = tk.Label(self.root, text="🎊 VICTORY! 🎊", 
                               font=("Arial", 24, "bold"), fg="gold", bg="#2c3e50")
        victory_label.pack(pady=50)
        
        message = f"""
        Congratulations, Master Treasure Hunter!
        
        You successfully solved all {len(self.puzzles)} mathematical puzzles:
        {' → '.join(map(str, self.puzzle_answers))}
        
        And you found the legendary treasure!
        Your mathematical skills have proven worthy!
        
        🏆 You are now a certified Mathematical Treasure Hunter! 🏆
        """
        
        message_label = tk.Label(self.root, text=message, font=("Arial", 12), 
                               fg="white", bg="#2c3e50", justify="center")
        message_label.pack(pady=30)
        
        self.add_restart_button()
    
    def show_results_screen(self):
        self.clear_screen()
        
        title_label = tk.Label(self.root, text="🎯 QUEST COMPLETE 🎯", 
                             font=("Arial", 18, "bold"), fg="gold", bg="#2c3e50")
        title_label.pack(pady=30)
        
        message = f"""
        Well done, adventurer!
        
        You solved all {len(self.puzzles)} mathematical puzzles:
        Your journey: {' → '.join(map(str, self.puzzle_answers))}
        
        Though you didn't find the main treasure this time,
        your mathematical skills have grown stronger!
        
        Try again for another chance at glory!
        """
        
        message_label = tk.Label(self.root, text=message, font=("Arial", 12), 
                               fg="white", bg="#2c3e50", justify="center")
        message_label.pack(pady=30)
        
        self.add_restart_button()
    
    def add_restart_button(self):
        restart_button = tk.Button(self.root, text="🔄 Play Again", 
                                 font=("Arial", 14, "bold"), bg="green", fg="white",
                                 command=self.restart_game, padx=20, pady=10)
        restart_button.pack(pady=30)
    
    def restart_game(self):
        self.current_puzzle = 0
        self.puzzle_answers = []
        self.solved_puzzles = []
        self.game_phase = "welcome"
        self.setup_welcome_screen()
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TreasureHuntGame()
    game.run()
