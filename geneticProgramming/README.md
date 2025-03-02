# Traveling Salesman Problem (TSP) using Genetic Algorithm

## 📌 Overview

This project implements a **Genetic Algorithm (GA)** to solve the **Traveling Salesman Problem (TSP)** in Python. It finds an optimized route for visiting a set of fixed cities while minimizing the total travel distance.

## 🏙️ Cities Defined

The cities are manually set with fixed (x, y) coordinates:

```
City 1: (10, 20)
City 2: (40, 80)
City 3: (70, 90)
City 4: (20, 50)
City 5: (90, 60)
City 6: (60, 30)
City 7: (50, 70)
City 8: (80, 20)
City 9: (30, 40)
City 10: (100, 10)
```

## 🚀 Features

* **Fixed Cities:** Uses predefined city coordinates.
* **Genetic Algorithm:** Implements natural selection, crossover, and mutation.
* **Elitism:** Retains the best route in each generation.
* **Tournament Selection:** Chooses the best individuals from a subset.
* **Order Crossover (OX1):** Preserves order in child solutions.
* **Mutation:** Swaps two cities to introduce diversity.
* **Visualization:** Uses Matplotlib to plot the best route.

## 🛠️ Installation & Requirements

**Requirements:** Python 3.x, NumPy, Matplotlib

Install dependencies using:

```sh
pip install numpy matplotlib
```

## 📜 Usage

Run the script:

```sh
python tsp_genetic.py
```

### 📌 Genetic Algorithm Parameters

```python
population_size = 50   # Number of candidate solutions
generations = 500      # Number of iterations
mutation_rate = 0.1    # Probability of mutation per individual
```

## 📈 Expected Output

```
Generation 0: Best Distance = 450.23
Generation 50: Best Distance = 375.48
Generation 100: Best Distance = 330.76
Generation 150: Best Distance = 290.34
...
Best Route Found: [(10, 20), (30, 40), (20, 50), (40, 80), (70, 90), ...]
Best Distance: 245.92
```

## 🖼️ Visualization

The final optimized route is plotted using  **Matplotlib** :

![TSP Route](/home/samuel/Documents/Icog-Intern/geneticProgramming/travelingSellesMan.png)

## 🛠️ How It Works

1. **Initialize Population:** Generates random routes.
2. **Evaluate Fitness:** Computes total distance for each route.
3. **Selection:** Uses tournament selection to pick parents.
4. **Crossover:** Applies order crossover (OX1) to create offspring.
5. **Mutation:** Swaps two cities in the route with a small probability.
6. **Repeat:** Runs for multiple generations until an optimal route is found.
7. **Plot Best Route:** Displays the shortest route found.

## 🚀 Future Improvements

* Increase the number of cities for more complex problems.
* Experiment with different selection and mutation strategies.
* Implement real-world city data using APIs.
* Optimize performance using parallel processing.

### 🔗 Author

Developed by **Samuel Tolossa** 🚀
