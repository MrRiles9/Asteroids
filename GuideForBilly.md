Step 1: Install the Required Software
Before you start, make sure you have Git and Python installed on your computer.

1. Install Git
Git is used to download (clone) your project from GitHub.

Windows: Download and install Git for Windows.
Mac: Git comes pre-installed on macOS. If not, install it via Homebrew:
bash
Copy
Edit
brew install git
Linux (Debian/Ubuntu):
bash
Copy
Edit
sudo apt update && sudo apt install git
After installing, check if Git works by opening Command Prompt (Windows) or Terminal (Mac/Linux) and running:

bash
Copy
Edit
git --version
If it prints a version number (e.g., git version 2.34.1), you're good to go.

2. Install Python
Your game is written in Python, so you need Python 3 installed.

Windows & Mac: Download and install Python from the official site.
During installation, check the box that says "Add Python to PATH" (important!).
Linux (Debian/Ubuntu):
bash
Copy
Edit
sudo apt update && sudo apt install python3 python3-pip
To check if Python is installed, open a terminal and run:

bash
Copy
Edit
python --version
or

bash
Copy
Edit
python3 --version
If you see something like Python 3.10.5, you're all set!

Step 2: Clone the GitHub Repository
Now, you need to download your project from GitHub.

1. Open a Terminal
Windows: Open Command Prompt or Git Bash.
Mac/Linux: Open Terminal.
2. Navigate to a Folder Where You Want to Download the Game
For example, if you want to save it in the "Documents" folder, run:

bash
Copy
Edit
cd Documents
(This changes the working directory to Documents.)

3. Clone the Repository
Now, download the project by running:

bash
Copy
Edit
git clone https://github.com/MrRiles9/Asteroids.git
This will create a folder called "Asteroids" with all your game files inside.

4. Move Into the Project Folder
Once it's downloaded, move into the project directory:

bash
Copy
Edit
cd Asteroids
(This ensures you're inside the folder where the game files are.)

Step 3: Install Dependencies
Your game likely has some required Python libraries, like pygame.

1. Create a Virtual Environment (Recommended)
To avoid conflicts with other Python projects, create a virtual environment:

bash
Copy
Edit
python -m venv venv
Then activate it:

Windows:
bash
Copy
Edit
venv\Scripts\activate
Mac/Linux:
bash
Copy
Edit
source venv/bin/activate
(You should now see (venv) before your terminal prompt.)

2. Install Required Libraries
Run:

bash
Copy
Edit
pip install -r requirements.txt
If you don’t have a requirements.txt file, you might need to install pygame manually:

bash
Copy
Edit
pip install pygame
Step 4: Run the Game
Once everything is set up, start the game by running:

bash
Copy
Edit
python main.py
(Use python3 main.py if python doesn't work.)

Troubleshooting
"python is not recognized" → Restart your computer and ensure Python is installed.
"pygame module not found" → Try:
bash
Copy
Edit
pip install pygame
Game window doesn’t open? → Check for errors in the terminal and send them here.
