# LoGreenTech Solutions - Energy Management Software

## 🌱 Smart Grid Energy Balancing Algorithm

This project implements and compares different algorithms to solve the **Two-Sum problem** for Smart Grid energy balancing, finding two energy production surplus values that sum to a target demand value.

### 📋 Problem Statement

Your company, LoGreenTech Solutions, develops energy management software for Smart Grid districts. The system needs to dynamically balance energy supply and demand by finding two production surplus values that sum to a target demand value.

The challenge: **Real-time performance requirements** make brute force approaches unsuitable for large datasets.

## 🏗️ Project Structure

```
algo/
├── README.md                    # This file
├── docker-compose.yml          # Docker container orchestration
├── Dockerfile                  # Container configuration  
├── requirements.txt            # Python dependencies
├── app/                        # Main application
│   ├── __init__.py
│   ├── algo.py                 # Main algorithm implementation
│   ├── pyproject.toml          # Package configuration
│   └── test_docker.py          # Docker environment test
└── GreenIT_data/              # Energy production data
    ├── data_list_10.csv       # Small dataset (10 values)
    ├── data_list_100.csv      # Medium dataset (100 values)
    ├── data_list_1000.csv     # Large dataset (1K values)
    ├── data_list_10000.csv    # Very large (10K values)
    └── ... (up to 2M values)  # Extreme scale datasets
```

## 🧮 Algorithms Implemented

### 1. **Brute Force Approach** 
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Method:** Check every pair of values
- **Use case:** Small datasets only

### 2. **Hash Table Approach** 
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Method:** Single pass with complement lookup
- **Use case:** Production-ready for all dataset sizes

## 🚀 Getting Started

### Prerequisites
- Docker and Docker Compose
- Or Python 3.10+ with pip (for local development)

### Option 1: Docker Environment (Recommended)

#### 1. Build and Start Container
```bash
# Build and start the container
docker-compose up --build

# Or run in background
docker-compose up --build -d
```

#### 2. Access Jupyter Lab
Open your browser and navigate to: **http://localhost:8888**

#### 3. Test the Environment
In a Jupyter notebook cell or terminal:
```python
# Quick environment test
exec(open('test_docker.py').read())
```

#### 4. Run the Analysis
```python
# In Jupyter notebook
from algo import run_analysis_in_docker

# Run with default target sum of 0
run_analysis_in_docker()

# Run with custom target sum
run_analysis_in_docker(target=25)
```

#### 5. Command Line Usage (in Docker terminal)
```bash
# Access container terminal
docker exec -it algo bash

# Run analysis with default target (0)
python algo.py

# Run analysis with custom target
python algo.py 42

# Run comprehensive test
python test_docker.py
```

### Option 2: Local Development

#### 1. Install Dependencies
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or .venv\Scripts\activate  # Windows

# Install packages
pip install -r requirements.txt
pip install -e app[dev]
```

#### 2. Run Analysis
```bash
cd app/
python algo.py          # Default target sum = 0
python algo.py 25       # Custom target sum = 25
```

## 📊 Understanding the Results

### Performance Analysis Output
```
================================================================================
LoGreenTech Solutions - Energy Management Performance Analysis
================================================================================
Target sum: 0

Data Size    Brute Force (s) Hash Table (s)  Speedup    Result Found
--------------------------------------------------------------------------------
10           0.000003        0.000002        1.50x      Yes
100          0.000089        0.000008        11.13x     No
1000         0.008234        0.000067        122.90x    Yes
10000        0.823456        0.000623        1322.45x   Yes
100000       82.345678       0.006234        13214.5x   Yes
```

### Key Metrics Explained:
- **Data Size**: Number of energy production values
- **Brute Force (s)**: Time taken by O(n²) algorithm
- **Hash Table (s)**: Time taken by O(n) algorithm  
- **Speedup**: Performance improvement ratio
- **Result Found**: Whether a valid pair was found

### Algorithm Advantages Analysis
The tool automatically explains:
- Time complexity comparison
- Scalability benefits
- Real-time performance requirements
- Memory trade-offs
- Hash collision considerations
- Practical benefits for Smart Grid systems

## 🔧 Advanced Usage

### Custom Target Values
Test different energy demand scenarios:
```python
# Test common energy balancing scenarios
targets_to_test = [0, 25, 50, 100, -25, -50]

for target in targets_to_test:
    print(f"\n=== Testing Target: {target} kW ===")
    run_analysis_in_docker(target)
```

### Individual Algorithm Testing
```python
from algo import two_sum_brute_force, two_sum_hash_table, load_data

# Load specific dataset
data = load_data("/GreenIT_data/data_list_1000.csv")

# Test both algorithms
target = 0
bf_result = two_sum_brute_force(data, target)
ht_result = two_sum_hash_table(data, target)

print(f"Brute Force: {bf_result}")
print(f"Hash Table: {ht_result}")
```

### Benchmarking Specific Algorithms
```python
from algo import benchmark_algorithm

# Benchmark with multiple runs for accuracy
bf_time, bf_result = benchmark_algorithm(two_sum_brute_force, data, target, runs=10)
ht_time, ht_result = benchmark_algorithm(two_sum_hash_table, data, target, runs=10)

print(f"Average times over 10 runs:")
print(f"Brute Force: {bf_time:.6f}s")
print(f"Hash Table: {ht_time:.6f}s")
print(f"Speedup: {bf_time/ht_time:.2f}x")
```

## 🐳 Docker Commands Reference

```bash
# Build container
docker-compose build

# Start services
docker-compose up

# Start in background
docker-compose up -d

# View logs
docker-compose logs -f

# Execute commands in running container
docker exec -it algo bash
docker exec -it algo python algo.py

# Stop services
docker-compose down

# Rebuild and restart
docker-compose up --build --force-recreate
```

## 📁 Data Format

The CSV files contain energy production surplus data:
```csv
Value
25
-48
56
-94
33
```

- **Positive values**: Energy surplus (production > consumption)
- **Negative values**: Energy deficit (production < consumption)
- **Target sum**: Desired energy balance point

## 🎯 Expected Results

### Performance Trends:
- **Small datasets (≤100)**: Minimal difference between algorithms
- **Medium datasets (1K-10K)**: Hash table shows 10-100x speedup
- **Large datasets (100K+)**: Hash table shows 1000-10000x speedup
- **Extreme datasets (1M+)**: Brute force becomes impractical

### Real-world Impact:
- **Brute force**: Suitable only for small, non-real-time scenarios
- **Hash table**: Production-ready for Smart Grid real-time requirements

## 🔍 Troubleshooting

### Docker Issues:
```bash
# Check if container is running
docker ps

# Check container logs
docker-compose logs algo

# Restart container
docker-compose restart

# Clean rebuild
docker-compose down
docker system prune -f
docker-compose up --build
```

### Data Access Issues:
```bash
# Verify data volume mounting
docker exec -it algo ls -la /GreenIT_data

# Check file permissions
docker exec -it algo ls -la /GreenIT_data/*.csv
```

### Python Environment Issues:
```bash
# Check Python packages in container
docker exec -it algo pip list

# Reinstall packages
docker exec -it algo pip install -r requirements.txt
```

## 📝 Notes for LoGreenTech Development Team

1. **Production Deployment**: Use hash table algorithm for all production systems
2. **Performance Monitoring**: Monitor execution times in production environments
3. **Scalability**: The hash table approach scales linearly with Smart Grid expansion
4. **Memory Considerations**: O(n) space complexity is acceptable for modern systems
5. **Real-time Requirements**: Hash table ensures sub-second response times
