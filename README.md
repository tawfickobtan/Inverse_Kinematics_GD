# Solving Inverse Kinematics using Gradient Descent (Playground) 🤖
### This `README.md` file is AI-generated but fact check by me 😁

Welcome to the **Solving Inverse Kinematics using Gradient Descent (Playground)** repository! This project is a playful experiment in simulating a robotic arm with inverse kinematics using Pygame, Python, and gradient descent. Watch as the arm continuously adjusts its joints to follow your mouse cursor, all while exploring the fundamentals of robotics and optimization! 🖱️✨

---

## 📋 Overview

- **What it does:**  
  Simulates a multi-jointed arm that dynamically adjusts its position to reach your mouse cursor using gradient descent.
- **Key Features:**  
  - User-defined number of joints and segment length 🔧  
  - Inverse kinematics powered by gradient descent with a hint of randomness for organic movement 🌪️  
  - Real-time graphical rendering with Pygame 🎨

---

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/repo-name.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd repo-name
   ```

3. **Install dependencies:**

   - Ensure you have Python 3 installed 🐍  
   - Install Pygame:

     ```bash
     pip install pygame
     ```

---

## 🚀 Usage

1. **Run the script:**

   ```bash
   python script.py
   ```

2. **Input Settings:**  
   - When prompted, enter the **number of joints** for your arm.  
   - Enter the **length of each segment** (in pixels).

3. **Interact:**  
   - Move your mouse around the window and watch as the arm adjusts its position to follow your cursor! 🎯

---

## 🤓 How It Works

- **Joint Calculation:**  
  The script computes joint positions using trigonometric functions based on user-defined angles.
  
- **Inverse Kinematics with Gradient Descent:**  
  It employs gradient descent to minimize the error between the arm's tip and the mouse position.  
  - **Loss Function:** Measures the squared error between the desired and actual positions.  
  - **Angle Update:** Adjusts the joint angles with a small learning rate and a touch of randomness to simulate natural movement.

- **Rendering:**  
  The arm is rendered with lines for segments and circles for joints, with vibrant colors to enhance visual clarity.

---
# Have fun!! 😁♥️


