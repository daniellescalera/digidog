🛠️ Setup Instructions

1. Clone the Repository:

Open your terminal or command prompt and run:

    git clone https://github.com/daniellescalera/digidog.git
    cd digidog

2. Create a Virtual Environment:

To keep dependencies isolated, create a virtual environment.

▶ On macOS/Linux/WSL:
    python3 -m venv venv
    source venv/bin/activate

▶ On Windows:
    python -m venv venv
    venv\Scripts\activate

⚠️ If you're using **Python 3.12 or higher on Linux/WSL**, pip may show an “externally-managed-environment” error.
To resolve this, use:
    
    pip install --break-system-packages -r requirements.txt

If installing individually:
    
    pip install --break-system-packages pygame

Make sure your virtual environment is correctly activated. You can confirm this by running:

    which pip

It should return a path ending in `/venv/bin/pip` (not `/usr/bin/pip`).

3. Install Dependencies:

With your virtual environment activated, install the required packages:

    pip install -r requirements.txt


🚀 Running the Application

Once everything is installed, run the application with:

    python src/main.py

A window will open displaying the DigiDog simulation.

---

🎮 Controls and Interactions

- **Arrow Keys**: Move DigiDog around the environment
- **F**: Feed the dog
- **P**: Play with the dog
- **S**: Put the dog to sleep
- **C**: Command the dog to sit

🔒 Note: The program uses synchronization to ensure only one action occurs at a time. You must wait for an action to complete before starting a new one.


🧠 Operating System Concepts Demonstrated

- **Multithreading**: Each action runs in a separate thread to prevent UI freezing.
- **Synchronization**: `threading.Lock()` ensures only one action can occur at a time.
- **Process & Thread States**: The dog’s `state` (idle, sleeping, playing, etc.) represents OS thread states.
- **Timed Actions**: Each behavior has a set duration (e.g., 5–30 seconds) to simulate thread runtime.


📝 Additional Notes

- Ensure **Python 3.10+** is installed on your system
- If you're using WSL, you may need to use `python3` instead of `python`
- The `venv` folder is intentionally excluded from the repository — users must create their own virtual environment
- If you encounter pip issues, check that you're using the correct version of pip inside your virtual environment

📦 GitHub Repository:
https://github.com/daniellescalera/digidog

