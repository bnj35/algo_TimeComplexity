"""
LoGreenTech Solutions - Energy Management Software
Two-Sum Algorithm Implementation for Smart Grid Energy Balancing

This module implements and compares different algorithms to find two energy
production surplus values that sum to a target demand value.
"""

import csv
import time
import os
import pandas as pd
from typing import List, Tuple, Optional
import sys


def load_data(file_path: str) -> List[int]:
    """
    Load energy production surplus data from CSV file.
    
    Args:
        file_path: Path to the CSV file containing the data
        
    Returns:
        List of integers representing production surplus values
    """
    try:
        df = pd.read_csv(file_path)
        return df['Value'].tolist()
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return []


def two_sum_brute_force(values: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Brute force approach to find two values that sum to target.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Args:
        values: List of integer values
        target: Target sum to find
        
    Returns:
        Tuple of (index1, index2) if found, None otherwise
    """
    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):
            if values[i] + values[j] == target:
                return (i, j)
    return None


def two_sum_hash_table(values: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Optimized approach using hash table for O(n) time complexity.
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    The algorithm works by:
    1. For each value, calculate what complement is needed (target - current_value)
    2. Check if this complement exists in our hash table
    3. If found, return the indices; if not, store current value and index
    
    Args:
        values: List of integer values
        target: Target sum to find
        
    Returns:
        Tuple of (index1, index2) if found, None otherwise
    """
    seen = {}  # Hash table: value -> index
    
    for i, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return (seen[complement], i)
        seen[value] = i
    
    return None


def benchmark_algorithm(algorithm, values: List[int], target: int, runs: int = 5) -> Tuple[float, Optional[Tuple[int, int]]]:
    """
    Benchmark an algorithm by running it multiple times and measuring execution time.
    
    Args:
        algorithm: The algorithm function to benchmark
        values: List of values to search
        target: Target sum
        runs: Number of runs for averaging
        
    Returns:
        Tuple of (average_time_seconds, result)
    """
    total_time = 0
    result = None
    
    for _ in range(runs):
        start_time = time.perf_counter()
        result = algorithm(values, target)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    
    return total_time / runs, result


def analyze_performance(data_dir: str = "../GreenIT_data", target: int = 0):
    """
    Analyze performance of both algorithms across different data sizes.
    
    Args:
        data_dir: Directory containing the CSV data files
        target: Target sum to search for
    """
    print("=" * 80)
    print("LoGreenTech Solutions - Energy Management Performance Analysis")
    print("=" * 80)
    print(f"Target sum: {target}")
    print()
    
    # Get all CSV files and sort by data size
    csv_files = []
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv') and 'data_list_' in filename:
            size = int(filename.replace('data_list_', '').replace('.csv', ''))
            csv_files.append((size, filename))
    
    csv_files.sort(key=lambda x: x[0])
    
    print(f"{'Data Size':<12} {'Brute Force (s)':<15} {'Hash Table (s)':<15} {'Speedup':<10} {'Result Found'}")
    print("-" * 80)
    
    for size, filename in csv_files:
        file_path = os.path.join(data_dir, filename)
        values = load_data(file_path)
        
        if not values:
            continue
            
        # Benchmark brute force
        bf_time, bf_result = benchmark_algorithm(two_sum_brute_force, values, target)
        
        # Benchmark hash table
        ht_time, ht_result = benchmark_algorithm(two_sum_hash_table, values, target)
        
        # Calculate speedup
        speedup = bf_time / ht_time if ht_time > 0 else float('inf')
        
        # Check if results match
        result_found = "Yes" if bf_result == ht_result and bf_result is not None else "No"
        
        print(f"{size:<12} {bf_time:<15.6f} {ht_time:<15.6f} {speedup:<10.2f}x {result_found}")


def explain_algorithm_advantages():
    """
    Explain why the hash table approach is superior to brute force.
    """
    print("\n" + "=" * 80)
    print("ALGORITHM ANALYSIS: Why Hash Table Approach is Superior")
    print("=" * 80)
    
    print("""
1. TIME COMPLEXITY COMPARISON:
   - Brute Force: O(n²) - For each element, check all remaining elements
   - Hash Table: O(n) - Single pass through the data with O(1) lookups
   
2. SCALABILITY:
   - With 1,000,000 energy readings:
     * Brute Force: ~1,000,000,000,000 operations (1 trillion!)
     * Hash Table: ~1,000,000 operations (1 million)
   - The difference becomes exponentially larger with more data
   
3. REAL-TIME REQUIREMENTS:
   - Smart Grid systems need sub-second response times
   - Hash table approach provides consistent performance regardless of data size
   - Critical for dynamic energy balancing in real-time scenarios
   
4. MEMORY TRADE-OFF:
   - Hash Table: O(n) space complexity - stores seen values for fast lookup
   - This is acceptable because:
     * Modern systems have abundant memory
     * Time savings far outweigh memory cost
     * O(1) average-case lookup time (without hash collisions)
   
5. HASH COLLISION CONSIDERATIONS:
   - Good hash functions minimize collisions
   - Python's dict implementation uses open addressing
   - Even with some collisions, average case remains O(1)
   - Worst case O(n) only in pathological scenarios with poor hash function
   
6. PRACTICAL BENEFITS FOR LOGREENTACH:
   - Enables real-time energy optimization
   - Supports larger smart grid networks
   - Reduces server computational costs
   - Improves customer experience with faster response times
""")


def run_analysis_in_docker(target: int = 0):
    """
    Convenience function to run analysis in Docker environment.
    This function can be called from Jupyter notebooks in the Docker container.
    
    Args:
        target: Target sum to search for (default: 0)
    """
    data_dir = "/GreenIT_data"
    print("Running LoGreenTech Energy Management Analysis in Docker Environment")
    print("=" * 80)
    
    if not os.path.exists(data_dir):
        print(f"Error: Data directory {data_dir} not found!")
        print("Make sure the GreenIT_data volume is properly mounted.")
        return
    
    analyze_performance(data_dir, target)
    explain_algorithm_advantages()
    
    print("\n" + "=" * 80)
    print("Docker analysis complete!")
    print("=" * 80)


def main():
    """
    Main function to run the energy management analysis.
    """
    if len(sys.argv) > 1:
        try:
            target = int(sys.argv[1])
        except ValueError:
            print("Error: Target must be an integer")
            return
    else:
        target = 0  # Default target sum
    
    # Run performance analysis
    # Use Docker-compatible path when running in container, local path otherwise
    if os.path.exists("/GreenIT_data"):
        data_dir = "/GreenIT_data"  # Docker environment
    else:
        data_dir = "/Users/benjaminauger/Documents/lyon/prosit/4_prosit/algo/GreenIT_data"  # Local environment
    
    analyze_performance(data_dir, target)
    
    # Explain the algorithm advantages
    explain_algorithm_advantages()
    
    print("\n" + "=" * 80)
    print("Analysis complete. The hash table approach demonstrates clear superiority")
    print("for LoGreenTech's Smart Grid energy management requirements.")
    print("=" * 80)


if __name__ == "__main__":
    main()
