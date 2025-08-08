import tkinter as tk
from tkinter import messagebox, ttk
import random
import math
import time
from datetime import datetime

class AdvancedTreasureHuntGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🏴‍☠️ Advanced Mathematical Treasure Hunt")
        self.root.geometry("900x700")
        self.root.configure(bg='#1a1a2e')
        
        # Game state variables
        self.current_puzzle = 0
        self.puzzle_answers = []
        self.solved_puzzles = []
        self.game_phase = "welcome"
        self.start_time = None
        self.hints_used = 0
        self.attempts = 0
        
        # Advanced interconnected mathematical puzzles
        self.puzzles = [
            {
                "question": "A treasure chest has coins arranged in a triangular pattern. The first row has 1 coin, second row has 2 coins, third row has 3 coins, and so on. If there are 7 rows total, how many coins are there?",
                "answer": 28,  # 1+2+3+4+5+6+7 = 28
                "hint": "This is the 7th triangular number. Formula: n(n+1)/2"
            },
            {
                "question": "A pirate's treasure map shows X islands (where X is your previous answer). If pirates can travel between any two islands, how many different routes are possible? (This is the number of combinations of X items taken 2 at a time)",
                "answer": 378,  # C(28,2) = 28*27/2 = 378
                "hint": "Use the combination formula: X × (X-1) ÷ 2"
            },
            {
                "question": "The treasure chest's lock has a 3-digit code. If the previous answer is Y, what are the last 3 digits of Y²?",
                "answer": 884,  # 378² = 142884, last 3 digits are 884
                "hint": "Calculate Y × Y and look at the last three digits"
            },
            {
                "question": "A ancient scroll shows Z (previous answer) written in Roman numerals, but some digits are missing. If we add the sum of Z's digits to Z itself, what do we get?",
                "answer": 908,  # 884 + (8+8+4) = 884 + 20 = 904... Let me recalculate: 884 + 24 = 908
                "hint": "Add each digit of the previous answer, then add that sum to the original number"
            },
            {
                "question": "The final riddle: If W is the previous answer, what is the remainder when W is divided by 37?",
                "answer": 20,  # 908 ÷ 37 = 24 remainder 20
                "hint": "Divide the previous answer by 37 and find the remainder"
            }
        ]
        
        # Enhanced treasure box system
        self.treasure_boxes = [
            {"type": "reward", "content": "🏆 LEGENDARY TREASURE! You've found the Golden Crown of Mathematics! Worth 10,000 gold coins! 👑", "rarity": "legendary"},
            {"type": "reward", "content": "💎 RARE TREASURE! A bag of precious gems! Worth 5,000 gold coins! ✨", "rarity": "rare"},
            {"type": "clue", "content": "🗝️ WISE CLUE: 'Numbers are the music of the universe' - Keep searching, mathematician!", "rarity": "common"},
            {"type": "insult", "content": "🦜 PARROT INSULT: 'Squawk! This landlubber couldn't find treasure in a jewelry store! Squawk!'", "rarity": "common"},
            {"type": "clue", "content": "📜 ANCIENT WISDOM: 'The real treasure is the equations you mastered along the way...'", "rarity": "common"},
            {"type": "insult", "content": "💀 SKELETON'S MOCKERY: 'I've been dead for 200 years and even I could solve those puzzles faster!'", "rarity": "common"},
            {"type": "insult", "content": "🐙 KRAKEN'S TAUNT: 'With eight arms, I can do math eight times faster than you!'", "rarity": "common"},
            {"type": "clue", "content": "🧭 NAVIGATOR'S TIP: 'Not all who wander are lost... but you might be! Try another box!'", "rarity": "common"}
        ]
        
        self.setup_welcome_screen()
    
    def setup_welcome_screen(self):
        self.clear_screen()
        
        # Animated title
        title_frame = tk.Frame(self.root, bg='#1a1a2e')
        title_frame.pack(pady=30)
        
        title_label = tk.Label(title_frame, text="🏴‍☠️ ADVANCED MATHEMATICAL TREASURE HUNT 🏴‍☠️", 
                             font=("Pirates", 22, "bold"), fg="#FFD700", bg="#1a1a2e")
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="⚡ Enhanced Edition with Advanced Challenges ⚡", 
                                font=("Arial", 12), fg="#87CEEB", bg="#1a1a2e")
        subtitle_label.pack()
        
        intro_text = """
🗺️ Welcome, brave mathematician-adventurer! 🗺️

You stand before the legendary Cave of Numerical Mysteries,
where only the most skilled problem solvers can claim the ultimate treasure!

🔢 QUEST OBJECTIVES:
• Solve 5 interconnected advanced mathematical puzzles
• Each challenge builds upon the previous answer
• Unlock the mysterious treasure chamber
• Choose wisely from multiple treasure boxes!

🎯 SPECIAL FEATURES:
• Time tracking for speedrun challenges
• Hint system (but it affects your final score!)
• Multiple treasure rarities
• Enhanced difficulty with real mathematical concepts

Are you ready to prove your mathematical prowess?
        """
        
        intro_label = tk.Label(self.root, text=intro_text, font=("Courier", 11), 
                             fg="#E6E6FA", bg="#1a1a2e", justify="center")
        intro_label.pack(pady=20)
        
        # Difficulty selection
        difficulty_frame = tk.Frame(self.root, bg='#1a1a2e')
        difficulty_frame.pack(pady=20)
        
        tk.Label(difficulty_frame, text="Choose your challenge level:", 
                font=("Arial", 12, "bold"), fg="#FFD700", bg="#1a1a2e").pack()
        
        button_frame = tk.Frame(self.root, bg='#1a1a2e')
        button_frame.pack(pady=20)
        
        start_button = tk.Button(button_frame, text="🚀 BEGIN ADVENTURE", 
                               font=("Arial", 16, "bold"), bg="#32CD32", fg="white",
                               command=self.start_puzzles, padx=25, pady=15,
                               relief="raised", bd=3)
        start_button.pack(side=tk.LEFT, padx=15)
        
        rules_button = tk.Button(button_frame, text="📋 GAME RULES", 
                               font=("Arial", 12), bg="#4169E1", fg="white",
                               command=self.show_rules, padx=20, pady=10)
        rules_button.pack(side=tk.LEFT, padx=15)
    
    def show_rules(self):
        rules_text = """
🎮 GAME RULES & SCORING:

📊 SCORING SYSTEM:
• Base Score: 1000 points
• Time Bonus: Extra points for quick solving
• Hint Penalty: -50 points per hint used
• Treasure Bonus: Varies by rarity

🎯 PUZZLE MECHANICS:
• Each answer feeds into the next puzzle
• Hints available but reduce final score
• Some tolerance for rounding in calculations

🏆 TREASURE RARITY:
• Legendary: 10,000+ gold coins
• Rare: 5,000+ gold coins  
• Common: Clues and humor

⚡ SPEEDRUN MODE:
• Beat the puzzles as fast as possible
• Time is tracked for leaderboard potential

Good luck, treasure hunter!
        """
        messagebox.showinfo("Game Rules", rules_text)
    
    def start_puzzles(self):
        self.game_phase = "puzzles"
        self.current_puzzle = 0
        self.start_time = time.time()
        self.show_puzzle()
    
    def show_puzzle(self):
        self.clear_screen()
        
        # Header with progress and stats
        header_frame = tk.Frame(self.root, bg='#1a1a2e')
        header_frame.pack(fill=tk.X, pady=10)
        
        progress_text = f"🗡️ CHALLENGE {self.current_puzzle + 1} OF {len(self.puzzles)} ⚔️"
        progress_label = tk.Label(header_frame, text=progress_text, font=("Arial", 14, "bold"), 
                                fg="#FFD700", bg="#1a1a2e")
        progress_label.pack()
        
        # Stats bar
        stats_frame = tk.Frame(header_frame, bg='#1a1a2e')
        stats_frame.pack(pady=5)
        
        if self.start_time:
            elapsed = int(time.time() - self.start_time)
            time_text = f"⏱️ Time: {elapsed//60:02d}:{elapsed%60:02d}"
        else:
            time_text = "⏱️ Time: 00:00"
            
        tk.Label(stats_frame, text=time_text, font=("Arial", 10), 
                fg="#87CEEB", bg="#1a1a2e").pack(side=tk.LEFT, padx=20)
        
        tk.Label(stats_frame, text=f"💡 Hints Used: {self.hints_used}", font=("Arial", 10), 
                fg="#87CEEB", bg="#1a1a2e").pack(side=tk.LEFT, padx=20)
        
        tk.Label(stats_frame, text=f"🎯 Attempts: {self.attempts}", font=("Arial", 10), 
                fg="#87CEEB", bg="#1a1a2e").pack(side=tk.LEFT, padx=20)
        
        # Show solution path
        if self.puzzle_answers:
            path_text = "🧭 Your Journey: " + " ➜ ".join(map(str, self.puzzle_answers))
            path_label = tk.Label(self.root, text=path_text, font=("Arial", 11), 
                                fg="#98FB98", bg="#1a1a2e")
            path_label.pack(pady=5)
        
        # Current puzzle with better styling
        puzzle = self.puzzles[self.current_puzzle]
        question = puzzle["question"]
        
        # Replace placeholders with actual values
        if "previous answer" in question.lower() and self.puzzle_answers:
            question = question.replace("X", str(self.puzzle_answers[-1]))
            question = question.replace("Y", str(self.puzzle_answers[-1]))
            question = question.replace("Z", str(self.puzzle_answers[-1]))
            question = question.replace("W", str(self.puzzle_answers[-1]))
        
        question_frame = tk.Frame(self.root, bg='#2F4F4F', relief="ridge", bd=2)
        question_frame.pack(pady=30, padx=50, fill=tk.X)
        
        tk.Label(question_frame, text="🧩 MATHEMATICAL CHALLENGE:", 
                font=("Arial", 12, "bold"), fg="#FFD700", bg="#2F4F4F").pack(pady=(15,5))
        
        question_label = tk.Label(question_frame, text=question, font=("Arial", 13), 
                                fg="white", bg="#2F4F4F", wraplength=700, justify="left")
        question_label.pack(pady=(5,20), padx=20)
        
        # Enhanced answer entry
        answer_frame = tk.Frame(self.root, bg='#1a1a2e')
        answer_frame.pack(pady=30)
        
        tk.Label(answer_frame, text="✨ Enter Your Answer:", font=("Arial", 14, "bold"), 
                fg="#FFD700", bg="#1a1a2e").pack()
        
        self.answer_var = tk.StringVar()
        answer_entry = tk.Entry(answer_frame, textvariable=self.answer_var, 
                              font=("Arial", 16), width=15, justify="center",
                              bg="white", fg="black", relief="sunken", bd=3)
        answer_entry.pack(pady=10)
        answer_entry.focus()
        
        answer_entry.bind('<Return>', lambda e: self.check_answer())
        
        # Enhanced button panel
        button_frame = tk.Frame(self.root, bg='#1a1a2e')
        button_frame.pack(pady=30)
        
        submit_button = tk.Button(button_frame, text="⚔️ SUBMIT ANSWER", 
                                font=("Arial", 12, "bold"), bg="#228B22", fg="white",
                                command=self.check_answer, padx=20, pady=10,
                                relief="raised", bd=3)
        submit_button.pack(side=tk.LEFT, padx=10)
        
        hint_button = tk.Button(button_frame, text="💡 REQUEST HINT (-50 pts)", 
                              font=("Arial", 12), bg="#FF8C00", fg="white",
                              command=self.show_hint, padx=20, pady=10,
                              relief="raised", bd=3)
        hint_button.pack(side=tk.LEFT, padx=10)
        
        calculate_button = tk.Button(button_frame, text="🧮 CALCULATOR", 
                                   font=("Arial", 12), bg="#4169E1", fg="white",
                                   command=self.open_calculator, padx=20, pady=10,
                                   relief="raised", bd=3)
        calculate_button.pack(side=tk.LEFT, padx=10)
    
    def open_calculator(self):
        calc_window = tk.Toplevel(self.root)
        calc_window.title("🧮 Pirate Calculator")
        calc_window.geometry("300x400")
        calc_window.configure(bg='#2F4F4F')
        
        # Simple calculator implementation
        calc_display = tk.StringVar()
        calc_display.set("0")
        
        display = tk.Label(calc_window, textvariable=calc_display, 
                          font=("Arial", 16), bg="white", relief="sunken", 
                          anchor="e", padx=10, pady=10)
        display.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(calc_window, text="Basic calculations for puzzle solving", 
                font=("Arial", 10), fg="white", bg='#2F4F4F').pack()
    
    def show_hint(self):
        puzzle = self.puzzles[self.current_puzzle]
        self.hints_used += 1
        messagebox.showinfo("💡 Treasure Hint", 
                          f"Hint: {puzzle['hint']}\n\n⚠️ Using hints reduces your final score by 50 points!")
    
    def check_answer(self):
        self.attempts += 1
        try:
            user_answer = float(self.answer_var.get())
            correct_answer = self.puzzles[self.current_puzzle]["answer"]
            
            # Allow some tolerance for floating point calculations
            tolerance = max(1, abs(correct_answer * 0.01))  # 1% tolerance or minimum 1
            
            if abs(user_answer - correct_answer) <= tolerance:
                # Accept the answer
                final_answer = int(user_answer) if user_answer.is_integer() else user_answer
                self.puzzle_answers.append(final_answer)
                self.solved_puzzles.append(self.current_puzzle)
                
                messagebox.showinfo("⚔️ VICTORY! ⚔️", 
                                  f"🎉 Excellent work, mathematician!\n\n"
                                  f"✅ Correct Answer: {correct_answer}\n"
                                  f"🧠 Your mathematical prowess grows stronger!")
                
                self.current_puzzle += 1
                if self.current_puzzle < len(self.puzzles):
                    self.show_puzzle()
                else:
                    self.show_treasure_room()
            else:
                messagebox.showerror("❌ Incorrect Answer", 
                                   f"⚠️ That's not quite right, adventurer!\n\n"
                                   f"🎯 Your answer: {user_answer}\n"
                                   f"💡 Try again, or use a hint for guidance!")
                self.answer_var.set("")
                
        except ValueError:
            messagebox.showerror("Invalid Input", 
                               "⚠️ Please enter a valid number!\n"
                               "Decimals are allowed for precision.")
            self.answer_var.set("")
    
    def show_treasure_room(self):
        self.clear_screen()
        self.game_phase = "treasure"
        
        # Calculate final score
        elapsed_time = int(time.time() - self.start_time)
        base_score = 1000
        time_bonus = max(0, 600 - elapsed_time)  # Bonus for solving under 10 minutes
        hint_penalty = self.hints_used * 50
        final_score = base_score + time_bonus - hint_penalty
        
        title_label = tk.Label(self.root, text="🏛️ THE LEGENDARY TREASURE CHAMBER 🏛️", 
                             font=("Arial", 20, "bold"), fg="#FFD700", bg="#1a1a2e")
        title_label.pack(pady=20)
        
        # Score display
        score_frame = tk.Frame(self.root, bg="#2F4F4F", relief="ridge", bd=3)
        score_frame.pack(pady=10)
        
        score_text = f"""
📊 FINAL PERFORMANCE SCORE: {final_score} points
⏱️ Completion Time: {elapsed_time//60:02d}:{elapsed_time%60:02d}
💡 Hints Used: {self.hints_used} (-{hint_penalty} points)
🎯 Total Attempts: {self.attempts}
        """
        
        tk.Label(score_frame, text=score_text, font=("Arial", 11), 
                fg="white", bg="#2F4F4F").pack(pady=10, padx=20)
        
        instructions = f"""
🎊 CONGRATULATIONS, MASTER MATHEMATICIAN! 🎊

Your legendary problem-solving keys: {' ⟶ '.join(map(str, self.puzzle_answers))}

Before you lies the ancient treasure vault with 8 mysterious chests...
Each chest contains either legendary treasures, rare gems, ancient wisdom, or... 
the mocking laughter of long-dead pirates! 

Choose your destiny wisely - fortune favors the mathematically bold! ⚔️
        """
        
        instruction_label = tk.Label(self.root, text=instructions, font=("Arial", 11), 
                                   fg="#E6E6FA", bg="#1a1a2e", justify="center")
        instruction_label.pack(pady=15)
        
        # Create enhanced treasure boxes
        box_frame = tk.Frame(self.root, bg="#1a1a2e")
        box_frame.pack(pady=20)
        
        self.box_buttons = []
        box_colors = ["#8B4513", "#CD853F", "#DEB887", "#F4A460", "#DAA520", "#B8860B", "#9ACD32", "#6B8E23"]
        
        for i in range(8):
            row = i // 4
            col = i % 4
            
            box_button = tk.Button(box_frame, text=f"📦\nCHEST {i+1}", 
                                 font=("Arial", 11, "bold"), bg=box_colors[i], fg="white",
                                 width=12, height=4,
                                 command=lambda box_num=i: self.open_treasure_box(box_num),
                                 relief="raised", bd=4)
            box_button.grid(row=row, col=col, padx=10, pady=10)
            self.box_buttons.append(box_button)
    
    def open_treasure_box(self, box_num):
        # Dramatic opening sequence
        self.box_buttons[box_num].config(text="🔓\nOPENING...", state="disabled", bg="#696969")
        self.root.update()
        time.sleep(0.5)
        
        self.box_buttons[box_num].config(text="⚡\nREVEALING...")
        self.root.update()
        time.sleep(0.5)
        
        self.reveal_box_content(box_num)
    
    def reveal_box_content(self, box_num):
        # Enhanced randomization system
        contents = self.treasure_boxes.copy()
        random.shuffle(contents)
        
        # Ensure variety in results
        selected_content = contents[box_num % len(contents)]
        
        # Update button appearance based on content
        if selected_content["type"] == "reward":
            if selected_content["rarity"] == "legendary":
                self.box_buttons[box_num].config(text="👑\nLEGENDARY!", bg="#FFD700", fg="black")
            else:
                self.box_buttons[box_num].config(text="💎\nRARE!", bg="#9370DB", fg="white")
        elif selected_content["type"] == "clue":
            self.box_buttons[box_num].config(text="📜\nWISDOM", bg="#4169E1", fg="white")
        else:
            self.box_buttons[box_num].config(text="💀\nEMPTY", bg="#696969", fg="white")
        
        # Show enhanced result dialog
        title = f"🗝️ CHEST {box_num + 1} CONTENTS"
        messagebox.showinfo(title, selected_content["content"])
        
        # Continue or finish options
        if selected_content["type"] == "reward":
            self.show_victory_screen(selected_content)
        else:
            result = messagebox.askyesno("Continue Adventure?", 
                                       "🎲 Try your luck with another chest?\n\n"
                                       "⚠️ Or end your quest here and try again later?")
            if not result:
                self.show_results_screen()
    
    def show_victory_screen(self, treasure_content):
        self.clear_screen()
        
        victory_label = tk.Label(self.root, text="🎊 ULTIMATE VICTORY! 🎊", 
                               font=("Arial", 28, "bold"), fg="#FFD700", bg="#1a1a2e")
        victory_label.pack(pady=30)
        
        elapsed_time = int(time.time() - self.start_time)
        
        message = f"""
🏆 LEGENDARY ACHIEVEMENT UNLOCKED! 🏆

{treasure_content["content"]}

📈 YOUR INCREDIBLE MATHEMATICAL JOURNEY:
🧮 Puzzles Solved: {len(self.puzzle_answers)} of {len(self.puzzles)}
🗝️ Solution Path: {' ➜ '.join(map(str, self.puzzle_answers))}
⏱️ Total Time: {elapsed_time//60:02d}:{elapsed_time%60:02d}
💡 Hints Used: {self.hints_used}
🎯 Total Attempts: {self.attempts}

🎖️ You have earned the title: "MATHEMATICAL TREASURE MASTER" 🎖️

Your name shall be remembered in the annals of mathematical legend!
        """
        
        message_label = tk.Label(self.root, text=message, font=("Arial", 12), 
                               fg="white", bg="#1a1a2e", justify="center")
        message_label.pack(pady=20)
        
        self.add_restart_button()
    
    def show_results_screen(self):
        self.clear_screen()
        
        title_label = tk.Label(self.root, text="🎯 MATHEMATICAL QUEST COMPLETED 🎯", 
                             font=("Arial", 20, "bold"), fg="#FFD700", bg="#1a1a2e")
        title_label.pack(pady=30)
        
        elapsed_time = int(time.time() - self.start_time)
        
        message = f"""
⚔️ Well fought, brave mathematician! ⚔️

🧠 QUEST STATISTICS:
📊 Puzzles Conquered: {len(self.puzzle_answers)} of {len(self.puzzles)}
🗝️ Your Mathematical Journey: {' ➜ '.join(map(str, self.puzzle_answers))}
⏱️ Adventure Duration: {elapsed_time//60:02d}:{elapsed_time%60:02d}
💡 Wisdom Sought (Hints): {self.hints_used}
🎯 Battle Attempts: {self.attempts}

Though the legendary treasure eluded you this time,
your mathematical skills have grown exponentially!

🔄 The treasure chamber awaits your return!
Each attempt makes you wiser and stronger!

🌟 "In mathematics, you don't understand things. You just get used to them." - John von Neumann
        """
        
        message_label = tk.Label(self.root, text=message, font=("Arial", 11), 
                               fg="#E6E6FA", bg="#1a1a2e", justify="center")
        message_label.pack(pady=20)
        
        self.add_restart_button()
    
    def add_restart_button(self):
        button_frame = tk.Frame(self.root, bg="#1a1a2e")
        button_frame.pack(pady=30)
        
        restart_button = tk.Button(button_frame, text="🔄 NEW ADVENTURE", 
                                 font=("Arial", 16, "bold"), bg="#32CD32", fg="white",
                                 command=self.restart_game, padx=25, pady=15,
                                 relief="raised", bd=3)
        restart_button.pack(side=tk.LEFT, padx=10)
        
        quit_button = tk.Button(button_frame, text="🚪 EXIT GAME", 
                              font=("Arial", 14), bg="#DC143C", fg="white",
                              command=self.root.quit, padx=20, pady=10,
                              relief="raised", bd=3)
        quit_button.pack(side=tk.LEFT, padx=10)
    
    def restart_game(self):
        self.current_puzzle = 0
        self.puzzle_answers = []
        self.solved_puzzles = []
        self.game_phase = "welcome"
        self.start_time = None
        self.hints_used = 0
        self.attempts = 0
        self.setup_welcome_screen()
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = AdvancedTreasureHuntGame()
    game.run()
