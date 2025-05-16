# Othello
Welcome to the **Othello** game project!

![Othello Board](img/othello_board.jpg)
## Overview
This Python implementation originally featured a console-only mode for Player vs Bot. It has now been updated to include two modes of play: **Player vs Player** and **Player vs Bot**. The project also offers two interfaces: a **Console Interface** and a **Graphical User Interface (GUI)**, providing an enhanced gaming experience.


### Interfaces
- **Graphical User Interface (GUI)**

  ![Othello GUI](img/othello_gui.png)

- **Console Interface**

  ![Othello Console](img/othello_console.png)

## Recent Updates
- **21.9.2024**: Revisited and updated the project.
- **23.9.2024**: Added GUI and Player vs Player mode.
- **16.5.2025**: Migrated from setuptools to pyproject.

## Getting started

Make sure you have Python 3.10 installed on your system before running this project. 

You can check your Python version by running the following command:

```bash
python --version
```

Clone repository
```bash
git clone https://github.com/lazarnagulov/othello.git
```
*Optional*: Install virtual environment.

Install othello with pip:
```bash
pip install .
```

Run the application with the following command for the default option (GUI: Player vs Bot):
```
othello
```

## Game Customisation

You can customize your game mode with the following command-line options:
- **Console** Player vs Bot
```
othello [--console | -c] [--bot | -b]
```
- **Console** Player vs Player
```
othello [--console | -c] [--player | -p]
```
- **GUI** Player vs Bot
```
othello [--gui | -g] [--bot | -b]
```
- **GUI** Player vs Player
```
othello [--gui | -g] [--player | -p]
```
## Dependencies
- **PyQt5**: Required for the GUI.

## References
- [Othello](https://en.wikipedia.org/wiki/Reversi)
- [Heuristic Function for Othello](https://kartikkukreja.wordpress.com/2013/03/30/heuristic-function-for-reversiothello/)
