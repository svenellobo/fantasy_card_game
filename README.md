# Fantasy Card Game

A desktop fantasy card game built with Python and [customtkinter](https://github.com/TomSchimansky/CustomTkinter), based on a Fantasy Realms board game that was created by Bruce Glassco and published by WizKids.

---

## Features

- **Player vs CPU**: Play against a computer-controlled opponent with unique logic.
- **Drag & Drop**: Rearrange cards in your hand by clicking and dragging.
- **Card Library**: Browse all available cards with images and descriptions.
- **Score Screen**: See a detailed breakdown of both hands and the winner at the end.
- **Responsive UI**: Works on Windows and Linux, with adaptive scaling and scrollbars.
- **Instructions**: In-game help and instructions for new players.
- **Custom Theming**: Modern dark mode and color highlights for game phases and results.

---

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/svenellobo/fantasy_card_game.git
    cd fantasy_card_game
    ```

2. **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Dependencies include: `customtkinter`, `Pillow` (PIL), and standard Python libraries.*

---

## Running the Game

```bash
python main.py
```

- The game window will open in maximized mode, adapting to your OS (Windows or Linux).
- All resources (images, etc.) are loaded using a utility function that works both in development and when packaged (e.g., with PyInstaller).

---

## How to Play

- **Start a new game** from the main menu.
- **Draw cards** from the deck or discard area during your turn.
- **Discard unwanted cards** by double-clicking them.
- **End your turn** and let the CPU play.
- **View the card library** or instructions at any time from the menu.
- **Game ends** when the discard pile reaches a certain size; the winner is shown with a detailed score breakdown.

---

## Project Structure

```
fantasy_card_game/
│
├── main.py                # Application entry point and main window
├── game.py                # Game logic and turn management
├── gui/
│   ├── game_screen.py     # Main game UI
│   ├── score_screen.py    # End-of-game score display
│   ├── card_widget.py     # Card widget with drag-and-drop
│   ├── card_library.py    # Card library browser
│   ├── instructions.py    # In-game instructions/help
│   ├── player_choice_screen.py # Player options and navigation
│   └── ...                # Other GUI components
├── card_library/
│   ├── wild/
│   │   ├── mirage.py
│   │   └── doppelganger.py
│   ├── wizard/
│   │   └── necromancer.py
│   └── ...                # Other card types
├── cpu_player.py          # CPU player logic
├── utility.py             # Resource path utility for packaging
├── requirements.txt       # Python dependencies
└── README.md              # (You are here)
```

---

## Notes

- **Cross-platform:** The game is tested on Windows and Linux. Font scaling and window maximization are handled per-OS.
- **Resource Management:** The `resource_path` function ensures images and other resources are found whether running from source or as a packaged executable.
- **CustomTkinter:** All UI is built with [customtkinter](https://github.com/TomSchimansky/CustomTkinter) for a modern look and feel.
- **Extensible:** Card logic is modular; new cards can be added by creating new classes in the `card_library` directory.

---

## Troubleshooting

- If you see errors about fonts, make sure you use a single font name string (e.g., `"Arial"`, not a tuple).
- If images do not appear, check that the `images/` directory exists and paths are correct.
- For packaging (e.g., with PyInstaller), all resource loading is handled via `utility.py`.

---



## Credits

- Developed by [svenellobo](https://github.com/svenellobo)
- Uses [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) and [Pillow](https://python-pillow.org/)

---

Enjoy the game!
