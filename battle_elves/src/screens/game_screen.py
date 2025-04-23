import tkinter as tk
import os 
def create_game_screen(root, show_main_menu):
    """
    Creates the game screen.
    """
    game_screen_frame = tk.Frame(root)

    label = tk.Label(
        game_screen_frame,
        text="Game Screen",
        font=("Arial", 24, "bold")
    )
    label.pack(pady=40)

    back_button = tk.Button(
        game_screen_frame,
        text="Back to Main Menu",
        font=("Arial", 18),
        command=show_main_menu
    )
    back_button.pack(pady=20)

    return game_screen_frame