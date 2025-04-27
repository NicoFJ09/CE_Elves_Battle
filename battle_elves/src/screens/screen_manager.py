import tkinter as tk

# Global variables to manage screens
screens = {}
current_screen = None
root = None

def initialize_screen_manager(root_window):
    """
    Initializes the screen manager with the root Tkinter window.
    """
    global root
    root = root_window

def add_screen(name, screen):
    """
    Adds a screen to the manager.
    :param name: The name of the screen (string).
    :param screen: A callable that returns a Tkinter Frame.
    """
    screens[name] = screen

def show_screen(name):
    """
    Switches to the specified screen.
    :param name: The name of the screen to show (string).
    """
    global current_screen
    # Destroy the current screen if it exists
    if current_screen is not None:
        current_screen.destroy()

    # Create and display the new screen
    current_screen = screens[name]()
    current_screen.pack(expand=True, fill="both")