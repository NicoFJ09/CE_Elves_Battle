import tkinter as tk
from screens.main_menu import create_main_menu
from screens.game_screen import create_game_screen
from screens.screen_manager import ScreenManager

def main():
    root = tk.Tk()
    root.title("Battle Elves")

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate 90% of screen dimensions
    window_width = int(screen_width * 0.9)
    window_height = int(screen_height * 0.9)

    # Center the window on the screen
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Set the window size and position
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Initialize the ScreenManager
    screen_manager = ScreenManager(root)

    # Register screens with the ScreenManager
    screen_manager.add_screen("main_menu", lambda: create_main_menu(root, lambda: screen_manager.show_screen("game_screen"), lambda: print("Help screen clicked!")))
    screen_manager.add_screen("game_screen", lambda: create_game_screen(root, lambda: screen_manager.show_screen("main_menu")))

    # Show the main menu initially
    screen_manager.show_screen("main_menu")

    root.mainloop()

if __name__ == "__main__":
    main()