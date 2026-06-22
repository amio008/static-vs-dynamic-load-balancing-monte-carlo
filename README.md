# Parallel Monte Carlo Pi Estimation using Python Multiprocessing

## Overview

This project investigates the performance impact of different parallelization strategies when estimating the value of π (Pi) using the Monte Carlo method.

Three execution models were implemented and compared:

1. **Sequential Execution**
2. **Static Parallel Scheduling**
3. **Dynamic Parallel Scheduling**

The goal is to evaluate how workload distribution affects execution time, speedup, efficiency, and estimation accuracy when utilizing multiple CPU cores.

---

## Objectives

* Implement Monte Carlo Pi estimation in Python.
* Compare sequential and parallel execution models.
* Evaluate Static vs Dynamic task scheduling.
* Measure:

  * Execution Time
  * Speedup
  * Parallel Efficiency
  * Estimation Accuracy
* Analyze scalability across multiple CPU cores.

---

## Technologies Used

* Python 3
* Multiprocessing Module
* Pandas
* Matplotlib

---

## Project Structure

```text
├── src/
│   ├── sequential_pi.py
│   ├── parallel_static_pi.py
│   ├── parallel_dynamic_pi.py
│   ├── seq_exp.py
│   ├── static_exp.py
│   └── dynamic_exp.py
│
├── experiments/
│   └── run_experiments.py
│
├── analysis/
│   ├── analysis_accuracy.py
│   ├── analysis_speedup_efficiency.py
│   └── analysis_time_scaling.py
│
├── results/
│   ├── results.csv
│   ├── Figure_1.png
│   ├── Figure_2.png
│   ├── Figure_3.png
│   ├── Figure_4.png
│   ├── Figure_5.png
│   └── Figure_6.png
│
└── test_mp.py
```

---

## Monte Carlo Method

The Monte Carlo approach estimates π by randomly generating points inside a unit square.

A point is considered inside the quarter circle if:

```math
x² + y² ≤ 1
```

The value of π is estimated as:

```math
π ≈ 4 × (Points Inside Circle / Total Points)
```

Increasing the number of samples improves accuracy.

---

## Parallelization Approaches

### 1. Sequential Execution

All samples are processed by a single CPU core.

Characteristics:

* Simple implementation
* No multiprocessing overhead
* Slowest execution time

---

### 2. Static Scheduling

The total number of samples is divided equally among workers.

Example:

```text
5,000,000 samples
4 workers

Worker 1 → 1,250,000
Worker 2 → 1,250,000
Worker 3 → 1,250,000
Worker 4 → 1,250,000
```

Advantages:

* Low scheduling overhead
* Easy implementation

Limitations:

* Potential load imbalance in uneven workloads

---

### 3. Dynamic Scheduling

Work is divided into smaller chunks and assigned dynamically.

Example:

```text
Chunk Size = 50,000

Worker requests next chunk when finished.
```

Advantages:

* Better load balancing
* Higher resource utilization
* Improved scalability

Limitations:

* Additional scheduling overhead

---

## Experimental Setup

| Parameter              | Value            |
| ---------------------- | ---------------- |
| Samples                | 5,000,000        |
| Workers Tested         | 1–6              |
| Runs per Configuration | 3                |
| Scheduling Types       | Static & Dynamic |
| Language               | Python           |

---

## Results Summary

### Execution Time

Observations:

* Parallel approaches significantly reduced execution time.
* Dynamic scheduling produced the fastest execution times at higher worker counts.
* Best performance was achieved using 6 workers.

### Speedup

Speedup is calculated as:

```math
Speedup = Sequential Time / Parallel Time
```

Results showed near-linear improvement as worker count increased.

### Efficiency

Parallel efficiency is:

```math
Efficiency = Speedup / Number of Workers
```

Dynamic scheduling generally maintained higher efficiency due to better workload distribution.

### Accuracy

All approaches produced estimates close to the actual value of π:

```text
π = 3.141592653589793...
```

Errors remained extremely small, confirming that parallelization improved performance without sacrificing accuracy.

---

## Running the Project

### Install Dependencies

```bash
pip install pandas matplotlib
```

### Run Experiments

```bash
python experiments/run_experiments.py
```

### Generate Analysis Graphs

```bash
python analysis/analysis_time_scaling.py

python analysis/analysis_speedup_efficiency.py

python analysis/analysis_accuracy.py
```

---

## Key Findings

* Parallel computing significantly accelerates Monte Carlo simulations.
* Dynamic scheduling outperformed static scheduling at higher core counts.
* Multiprocessing effectively utilizes available CPU resources.
* Accuracy remained consistent across all implementations.
* Dynamic load balancing provided the best trade-off between scalability and execution efficiency.

---

## Future Improvements

* Test larger sample sizes (10M–100M+).
* Implement distributed computing using MPI.
* Compare Python multiprocessing with OpenMP/C++ implementations.
* Evaluate performance on cloud and multi-node environments.
* Investigate GPU acceleration using CUDA.

---

## Author

Undergraduate Project – Parallel Computing and Performance Analysis

Focus Areas:

* High Performance Computing (HPC)
* Parallel Processing
* Load Balancing
* Performance Optimization
* Monte Carlo Simulation
