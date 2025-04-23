import tkinter as tk

def create_main_menu(root, show_game_screen, show_help_screen):
    """
    Creates the main menu screen.
    """
    main_menu_frame = tk.Frame(root)

    title_label = tk.Label(
        main_menu_frame,
        text="Battle Elves",
        font=("Arial", 36, "bold")
    )
    title_label.pack(pady=40)

    start_button = tk.Button(
        main_menu_frame,
        text="Start Game",
        font=("Arial", 18),
        width=20,
        height=2,
        command=show_game_screen
    )
    start_button.pack(pady=20)

    help_button = tk.Button(
        main_menu_frame,
        text="Help",
        font=("Arial", 18),
        width=20,
        height=2,
        command=show_help_screen
    )
    help_button.pack(pady=20)

    quit_button = tk.Button(
        main_menu_frame,
        text="Quit",
        font=("Arial", 18),
        width=20,
        height=2,
        command=root.quit
    )
    quit_button.pack(pady=20)

    return main_menu_frame