import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

class GameLauncher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎮 Treasure Hunt Game Launcher")
        self.root.geometry("600x500")
        self.root.configure(bg='#2c3e50')
        
        self.setup_launcher()
    
    def setup_launcher(self):
        # Title
        title_label = tk.Label(self.root, text="🏴‍☠️ MATHEMATICAL TREASURE HUNT 🏴‍☠️", 
                             font=("Arial", 18, "bold"), fg="gold", bg="#2c3e50")
        title_label.pack(pady=30)
        
        subtitle_label = tk.Label(self.root, text="Choose Your Adventure!", 
                                font=("Arial", 14), fg="white", bg="#2c3e50")
        subtitle_label.pack(pady=10)
        
        # Game options
        options_frame = tk.Frame(self.root, bg="#2c3e50")
        options_frame.pack(pady=40)
        
        # Basic Version
        basic_frame = tk.Frame(options_frame, bg="#34495e", relief="ridge", bd=3)
        basic_frame.pack(pady=20, padx=40, fill="x")
        
        basic_title = tk.Label(basic_frame, text="🎯 CLASSIC VERSION", 
                             font=("Arial", 14, "bold"), fg="lightblue", bg="#34495e")
        basic_title.pack(pady=(10,5))
        
        basic_desc = """
• Simple and clean interface
• 5 interconnected math puzzles
• 6 treasure boxes to choose from
• Perfect for beginners
• Quick and fun gameplay
        """
        
        basic_label = tk.Label(basic_frame, text=basic_desc, font=("Arial", 10), 
                             fg="white", bg="#34495e", justify="left")
        basic_label.pack(pady=(0,10))
        
        basic_button = tk.Button(basic_frame, text="🚀 PLAY CLASSIC", 
                               font=("Arial", 12, "bold"), bg="green", fg="white",
                               command=self.launch_basic, padx=20, pady=8)
        basic_button.pack(pady=(0,15))
        
        # Advanced Version
        advanced_frame = tk.Frame(options_frame, bg="#8b4513", relief="ridge", bd=3)
        advanced_frame.pack(pady=20, padx=40, fill="x")
        
        advanced_title = tk.Label(advanced_frame, text="⚡ ADVANCED EDITION", 
                                font=("Arial", 14, "bold"), fg="gold", bg="#8b4513")
        advanced_title.pack(pady=(10,5))
        
        advanced_desc = """
• Enhanced visual effects and themes
• More complex mathematical challenges
• 8 treasure boxes with rarities
• Score tracking and statistics
• Hint system with penalties
• Built-in calculator
        """
        
        advanced_label = tk.Label(advanced_frame, text=advanced_desc, font=("Arial", 10), 
                                fg="white", bg="#8b4513", justify="left")
        advanced_label.pack(pady=(0,10))
        
        advanced_button = tk.Button(advanced_frame, text="⚔️ PLAY ADVANCED", 
                                  font=("Arial", 12, "bold"), bg="darkred", fg="white",
                                  command=self.launch_advanced, padx=20, pady=8)
        advanced_button.pack(pady=(0,15))
        
        # Footer
        footer_text = "Created by Math Pirates Team | Choose wisely, adventurer!"
        footer_label = tk.Label(self.root, text=footer_text, font=("Arial", 9), 
                              fg="lightgray", bg="#2c3e50")
        footer_label.pack(side="bottom", pady=20)
    
    def launch_basic(self):
        try:
            self.root.withdraw()  # Hide launcher
            subprocess.run([sys.executable, "treasure_hunt_game.py"], 
                         cwd=os.path.dirname(os.path.abspath(__file__)))
            self.root.deiconify()  # Show launcher again
        except Exception as e:
            messagebox.showerror("Error", f"Could not launch basic game: {str(e)}")
            self.root.deiconify()
    
    def launch_advanced(self):
        try:
            self.root.withdraw()  # Hide launcher
            subprocess.run([sys.executable, "advanced_treasure_hunt.py"], 
                         cwd=os.path.dirname(os.path.abspath(__file__)))
            self.root.deiconify()  # Show launcher again
        except Exception as e:
            messagebox.showerror("Error", f"Could not launch advanced game: {str(e)}")
            self.root.deiconify()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    launcher = GameLauncher()
    launcher.run()
