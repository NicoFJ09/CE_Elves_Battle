import tkinter as tk

class ScreenManager:
    def __init__(self, root):
        """
        Initializes the ScreenManager with a root Tkinter window.
        """
        self.root = root
        self.screens = {}
        self.current_screen = None  # Track the currently displayed screen

    def add_screen(self, name, screen):
        """
        Adds a screen to the manager.
        :param name: The name of the screen (string).
        :param screen: A callable that returns a Tkinter Frame.
        """
        self.screens[name] = screen

    def show_screen(self, name):
        """
        Switches to the specified screen.
        :param name: The name of the screen to show (string).
        """
        # Destroy the current screen if it exists
        if self.current_screen is not None:
            self.current_screen.destroy()

        # Create and display the new screen
        self.current_screen = self.screens[name]()
        self.current_screen.pack(expand=True, fill="both")