🛠️ Setup Instructions
Clone the Repository:

Open your terminal or command prompt and run:

bash
Copy
Edit
git clone https://github.com/daniellescalera/digidog.git
cd digidog
Create a Virtual Environment:

To keep dependencies isolated, create a virtual environment:

On macOS/Linux or WSL:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
On Windows:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
Install Dependencies:

With the virtual environment activated, install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Running the Application
Navigate to the src directory and execute the main script:

bash
Copy
Edit
python src/main.py
Upon running, a window will open displaying the DigiDog simulation.

🎮 Controls and Interactions
Use the following keys to interact with DigiDog:

Arrow Keys: Move the dog around the environment.

F: Feed the dog

P: Play with the dog

S: Put the dog to sleep

C: Command the dog to sit

Note: The application is designed so that only one action can occur at a time. If an action is already in progress, other actions will be ignored until the current one completes. This behavior illustrates thread synchronization using locks.

🧠 Operating System Concepts Demonstrated
Multithreading: Each dog action runs in its own thread to allow concurrent execution without freezing the UI.

Synchronization: A threading lock ensures that only one action thread can run at a time, preventing overlapping actions.

Process/Thread States: The dog's state transitions (e.g., idle, sleeping, playing) mimic real OS thread states, providing a visual representation of these concepts.

Timed Actions: Each action uses a timed delay (e.g., 5–15 seconds) to simulate how long a thread might run before returning to idle.

📝 Additional Notes
Ensure that Python 3.10 or higher is installed on your system.

The venv directory is excluded from the repository to prevent environment conflicts. Users should create their own virtual environment as outlined above.

For any issues or questions, please refer to the project's GitHub repository:
https://github.com/daniellescalera/digidog
