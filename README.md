# BlueCruise Live Vehicle Manuever Animations

This repository contains tools and scripts for analyzing BlueCruise live vehicle testing data. The main components include a Jupyter Notebook for identifying vehicle dynamics and a Python script for generating animations of specific maneuvers.

## Table of Contents

- [Setup](#setup)
- [Virtual Environment](#virtual-environment)
- [Installing Requirements](#installing-requirements)
- [Usage](#usage)
  - [Identifying Vehicle Dynamics](#identifying-vehicle-dynamics)
  - [Generating Maneuver Animations](#generating-maneuver-animations)
- [Data](#data)
- [Output](#output)

## Simple Comand Line Commands

- `cd <repository-directory>`: change to the repository directory
- `cd ..`: change to the parent directory
- `ls`: list files in the current directory
- `pwd`: print working directory

## Setup

1. **Clone the Repository**:
    First change to the directory where you want to clone the repository
   ```bash
   git clone https://github.com/DonavenLobo/GatechxFord-Near-Miss-Maneuver-Animations.git
   cd https://github.com/DonavenLobo/GatechxFord-Near-Miss-Maneuver-Animations.git
   ```

2. **Ensure you have Python 3.9 or later installed**. You can check your Python version with:
   ```bash
   python --version
   ```

## Virtual Environment

1. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - **On Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **On macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

## Installing Requirements

Once the virtual environment is activated, install the required packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Project Structure (ASCII)
```
BlueCruise_LiveVehicleTesting/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   ├── trip1_data_mike_Nov15.csv
│   └── trip2_data_mike_Nov15.csv
│
├── scripts/
│   ├── BC_LiveVehicleTesting_ManueverAnimations.py
│   └── gifs/
│
├── BlueCruise_LiveVehicleTesting_Manuevers_Ayyan.ipynb
└── BlueCruise_LiveVehicleTesting_Manuevers_Isabel.ipynb
```

## Usage

### Identifying Vehicle Dynamics

1. **Open the Jupyter Notebook**:
   - Launch Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Open `BlueCruise_LiveVehicleTesting_Manuevers.ipynb`.

2. **Run the Notebook**:
   - Follow the instructions in the notebook to analyze vehicle dynamics.
   - Use the notebook to identify and pinpoint exact sequences and times of interest.

### Generating Maneuver Animations

1. **Run the Python Script**:
   - After identifying the timestamps of interest using the notebook, run the script:
     ```bash
     python scripts/BC_LiveVehicleTesting_ManueverAnimations.py
     ```
   - Enter the trip number when prompted (1 [Ayyan] or 2 [Isabel])
   - Enter the start and end timestamps when prompted.

2. **Output**:
   - The script will generate a GIF of the vehicle dynamics for the specified time range.
   - The GIF will be saved in the `gifs` directory.

## Data

- The necessary data files should be placed in the `data` directory.
- You can find the required data in the "Near Miss Research" channel on our Teams platform.
- A zip file containing all maneuver recordings is also available in the same location.

## Output

- The output GIFs will be stored in the `gifs` folder.
- Ensure the `gifs` directory exists or is created by the script.

---