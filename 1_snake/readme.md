![Snake](image/banner.png)
# Snake: Recreated with python

## Project Structure

```
1_snake/
|── image/                  # assets, images, font, etc
│── music/                  # music 
│── snake_v1.py             # simple game script
│── snake_v2.py             # final game script
│── readme.md
```

## How to use
### 1. Download the project
**Option A — Download ONLY this folder**<br>
If you want just the Snake project (not the entire 100_Games_With_Python repo):
1. Copy this folder link: https://github.com/guoweier/100_Games_With_Python/tree/main/1_snake
2. Go to: https://download-directory.github.io/
3. Paste → download ZIP
4. Unzip and open the folder


**Option B — Download the entire repo**<br>
Click the green Code button → Download ZIP.<br>


### 2. Requirements
- Python 3.10+
- Pygame

**MacOS**
1. Go to the [Python website](https://www.python.org/downloads/), follow the steps to download python.
2. Use Command + Space and type "Terminal"
3. Ensure you have python3 installed by typing `python3 --version`
4. Install pygame by running the following command:
```
pip install pygame 
```

**Windows**
1. Go to the [python website](https://www.python.org/downloads/), follow the steps to download python. 
2. Click the Windows Start button, type cmd (or powershell) in the serach bar. Click on the Command Prompt (or PowerShell) application to open it. 
3. In the window, type the following command and press Enter to install pygame:
```
pip install pygame 
```

**Linux**
1. Most Linux distributions come with python3 pre-installed. Open Terminal and run the following command to confirm python3 installation:
```
python3 --version
```
2. Ensure pip are installed:
```
# install pip if not yet
sudo apt install python3-pip
# check pip installation
pip3 --version
```
3. Use a virtual environment
```
# create a virtual environment 
python3 -m venv .venv 
# activate environment 
source .venv/bin/activate
```
4. With the virtual environment activated, install pygame:
```
pip install pygame
```


### 3. Run the Game
**MacOS / Linux**
1. Go into the project folder
```
cd path/to/folder/
```
For example:
```
cd ~/Downloads/1_snake
```
2. run
```
python3 snake_v2.py
```

**Windows**
1. Go into the project folder
```
cd path\to\folder
```
For example:
```
cd C:\Users\YourName\Downloads\1_snake
```
2. Run
```
python snake_v2.py
```
If Windows opens the Microsoft Store or shows Python errors:<br>
```
py snake_v2.py
```


## Support
If you enjoy this project, please consider starring the repo ⭐️ <br>
It helps support 100_GAMES_WITH_PYTHON and encourages future mini-games!
