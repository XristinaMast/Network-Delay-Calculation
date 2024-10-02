# Network-Delay-Calculation.


This project calculates the delay in a network based on several user inputs, including the average size of a package, the number of nodes, the bit-rate, fragmentation, and other relevant parameters. The formula used in this code takes into account different network conditions and returns the calculated delay time.

## Table of Contents
- [Overview](#overview)
- [How It Works](#how-it-works)
- [Inputs](#inputs)
- [Formula](#formula)
- [Installation](#installation)
- [Usage](#usage)


## Overview
The goal of this project is to calculate the network delay based on inputs provided by the user. The delay is calculated by considering parameters such as package size, number of nodes, bit-rate, fragmentation, and header size. The user is prompted to input these values, and the program will ensure that no negative values are entered before proceeding with the calculation.

## How It Works
1. The user is prompted to enter values for:
   - Average size of the package (L)
   - Number of nodes (N)
   - Bit-rate (R)
   - Fragmentation (F)
   - Header size (H)
   
2. If a negative value is entered, the user will be asked to re-enter the value until a valid, positive number is provided.
   
3. Once valid inputs are provided, the program calculates the delay based on different conditions:
   - If fragmentation and header size are both zero
   - If fragmentation is zero but header size is not
   - If neither are zero

4. The calculated delay is then displayed with precision up to 10 decimal places.

## Inputs
The following parameters are used to calculate the delay:

1. **L (Package Size)**: The average size of the package in bits.
   - Example: 1000 (bits)

2. **N (Number of Nodes)**: The number of nodes in the network.
   - Example: 5

3. **R (Bit-Rate)**: The bit-rate of the nodes in bits per second (bps).
   - Example: 5000 (bps)

4. **F (Fragmentation)**: The size of the fragments, used in cases where data is fragmented.
   - Example: 500 (bits)

5. **H (Header Size)**: The size of the header in bits.
   - Example: 100 (bits)

## Formula
The program uses the following formulas to calculate the delay, depending on the conditions:

1. **When F = 0 and H = 0**:
   \[
   \text{Delay} = \frac{(N - 1) \times L}{R}
   \]

2. **When F = 0 and H ≠ 0**:
   \[
   \text{Delay} = \frac{L}{R} + (N - 2) \times \frac{H}{R}
   \]

3. **When F ≠ 0**:
   \[
   \text{Delay} = \frac{(L / F) \times (F + H)}{R} + \frac{(N - 2) \times (F + H)}{R}
   \]

The result is displayed in seconds with a precision of 10 decimal places.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/network-delay-calculator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd network-delay-calculator
   ```

3. Make sure Python 3.x is installed on your system. The script does not require any additional dependencies.

## Usage
1. Run the Python script:
   ```bash
   python network_delay_calculator.py
   ```

2. Enter the required inputs when prompted:
   - Average size of the package (L)
   - Number of nodes (N)
   - Bit-rate (R)
   - Fragmentation (F)
   - Header size (H)

3. The calculated delay will be displayed in the console.

### Example:
```
Please enter the average size of the package (L): 
L: 1000
Please enter the number of the nodes during (T1,T2) (N): 
N: 4
Please enter the Bit-Rate of the nodes (R) : 
R: 5000
Now please enter the value of the fragmentation (F): 
F: 200
And last but not least, please enter the height value of the title (H): 
H: 50
The delay is: 0.0400000000
```
