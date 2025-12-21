# 🚀 Asteroids Game

A modern, open-source recreation of the classic arcade space shooter, developed by **Pinnheads**. Navigate through treacherous asteroid fields, blast space rocks into dust, and avoid enemy saucers in this retro-inspired challenge.

## 🎮 About The Project

This project is a clone of the legendary 1979 Atari arcade game **Asteroids**. It captures the essential vector-style gameplay where physics, inertia, and precision aiming are key to survival.

**Key Features:**

- **Classic Gameplay:** Authentic physics-based movement (thrust, drift, and rotation).
- **Wrap-around World:** Screen edges wrap objects to the opposite side.
- **Progressive Difficulty:** Asteroids split into smaller, faster pieces when destroyed.
- **Score Tracking:** High score system to challenge your friends.
- **Modular Design:** Clean code architecture separating game logic (`asteroidfield`, `player`, `shot`).

## 🛠️ Built With

- [**Python**](https://www.python.org/) - Core programming language.
- [**Pygame**](https://www.pygame.org/) - Game development library.
- [**uv**](https://github.com/astral-sh/uv) - Extremely fast Python package installer and resolver.

## 📂 Project Structure

| **File**           | **Description**                                              |
| ------------------ | ------------------------------------------------------------ |
| `main.py`          | The entry point of the game; initializes the window and game loop. |
| `player.py`        | Handles ship movement, rotation, and shooting logic.         |
| `asteroid.py`      | Defines asteroid behavior, splitting mechanics, and physics. |
| `asteroidfield.py` | Manages the spawning waves and distribution of asteroids.    |
| `shot.py`          | Logic for projectiles fired by the player.                   |
| `circleshape.py`   | Base class handling circular collision detection for game objects. |
| `constants.py`     | Global configuration (screen dimensions, colors, speeds).    |

## 🏁 Getting Started

Follow these instructions to get a local copy of the game up and running.

### Prerequisites

- **Python 3.8+** installed.
- **git** installed.

### Installation

1. **Clone the repository**

   ```
   git clone [https://github.com/pinnheads/asteroids-game.git](https://github.com/pinnheads/asteroids-game.git)
   cd asteroids-game
   ```

2. **Install Dependencies**

   This project uses `pyproject.toml`. You can install dependencies using **pip** or **uv**.

   **Option A: Using pip (Standard)**

   ```
   pip install .
   ```

   **Option B: Using uv (Recommended for speed)**

   ```
   # If you don't have uv installed:
   pip install uv
   
   # Sync dependencies
   uv sync
   ```

### 🚀 How to Run

Execute the main script to launch the game window:

```
python main.py
```

## 🕹️ Controls

| **Key**      | **Action**                  |
| ------------ | --------------------------- |
| **W / ⬆️**    | Thrust (Accelerate forward) |
| **A / ⬅️**    | Rotate Left                 |
| **D / ➡️**    | Rotate Right                |
| **Spacebar** | Fire Weapon                 |

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Contact

[GitHub Profile](https://github.com/pinnheads) | [Website](https://utsavdeep.com)

