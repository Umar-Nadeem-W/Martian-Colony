
# Martian Colony Survival Simulation

---

## Project Overview
The **Martian Colony Survival Simulation** is a Python-based terminal game that uses NumPy to simulate resource management, random events, and competitive survival among four fictional Martian colonies. Each colony starts with a predefined set of resources and must endure 10 rounds of events like storms, resource growth, and wars to emerge victorious.

The project was created to help practice and reinforce **basic NumPy skills**, including:
- Array creation and manipulation.
- Indexing and slicing.
- Element-wise operations.
- Randomization and logic implementation.

---

## Features
1. **Colonies and Resources**:
   - Each colony is represented as a row in a NumPy array, with resources for food, weapons, oxygen, population, and event assignments.
   - Names of colonies are stored separately for user-friendly output.

2. **Random Events**:
   - **Storms**: Affects one colony by reducing all its resources.
   - **Resource Growth**: Increases resources for one colony by 20%.
   - **Wars**: Two colonies compete, with resources transferred based on a weighted scoring system (weapons are given more importance).

3. **Victory Condition**:
   - After 10 rounds, the colony with the most resources is declared the winner.

---

## How It Works
1. **Initialization**:
   - A NumPy array `Colonies` initializes resources for each colony.
   - Random events (`Eventsholder`) are assigned to each colony at the start of every round.

2. **Rounds**:
   - Each round consists of:
     1. Assigning random events to colonies.
     2. Executing events:
        - Storms reduce resources.
        - Resource growth boosts resources.
        - Wars cause resource redistribution.
     3. Displaying the current state of all colonies after the round.

3. **Victory**:
   - After 10 rounds, the colony with the highest total resources is declared the winner.

---

## Code Highlights
1. **NumPy Practice**:
   - **Array Creation**: Colonies and resources are stored in a structured NumPy array.
   - **Indexing & Slicing**: Access and update specific resources for each colony.
   - **Element-Wise Operations**: Efficiently modify resources during events (e.g., storms, growth, wars).
   - **Randomization**: Assign events randomly using `np.random.randint`.

2. **Logic Building**:
   - Event handling ensures dynamic gameplay with a balance of randomness and strategic updates.
   - Weighted scoring in wars emphasizes logic-driven resource redistribution.

---

## How to Run
1. Install Python (>= 3.6) and NumPy.
2. Copy the code into a `.py` file (e.g., `martian_colony.py`).
3. Run the file in your terminal:
   ```bash
   python martian_colony.py
