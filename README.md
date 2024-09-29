# Snake Game

## Project Overview
This project is a modern, web-based Snake Game built with **Python**, **Flask**, **HTML/CSS**, and **JavaScript**. The game features real-time score submission, dynamic obstacles, power-ups, and a leaderboard to track high scores.

### Features:
- **Snake Movement**: Control the snake using arrow keys (up, down, left, right).
- **Food and Score**: Collect food to grow the snake and increase your score.
- **Power-Ups**: Special items like speed boosts, extra growth, and score multipliers.
- **Obstacles**: Avoid obstacles while navigating the snake.
- **Pause Functionality**: Pause and resume the game at any time.
- **Settings Menu**: Adjust grid size, difficulty, and snake skin color before starting the game.
- **Leaderboard**: Track top 5 high scores.
- **Game Over Modal**: Save your name and score after the game ends.

## Technology Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Game Logic**: JavaScript for snake movement and rendering, with Flask handling the score submission and leaderboard.
  
## Installation & Setup

### Prerequisites:
- **Python 3.x**
- **Flask**
  
### Setup Instructions:
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/marianbt554/snake-game.git
   cd snake-game
2. Install the requiered Python packages: pip install Flask
3. Run the Flask application: python snake.py
4. Open your web browser and go to http://127.0.0.1:5000/ to play the game.

### How to play
1. Press any arrow key to start the game.
2. Control the snake using the arrow keys.
3. Collect food to increase your score and grow the snake.
4. Avoid obstacles and the walls.
5. Power-Ups:
Speed Boost (Blue): Temporarily increases snake speed.
Growth (Orange): Grow the snake by an additional segment.
Score Boost (Green): Adds 10 extra points.
5. After the game ends, enter your name to save your score on the leaderboard.
6. The top 5 high scores will be displayed on the leaderboard.
