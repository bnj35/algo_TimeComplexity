#!/usr/bin/env python3
"""
Simple test script to verify the Docker environment works correctly
"""

from algo import run_analysis_in_docker, two_sum_brute_force, two_sum_hash_table, load_data
import os

def test_docker_environment():
    """Test if the Docker environment is set up correctly"""
    print("Testing LoGreenTech Docker Environment")
    print("=" * 50)
    
    # Check if data directory exists
    data_dir = "/GreenIT_data"
    if os.path.exists(data_dir):
        print("✅ Data directory found at /GreenIT_data")
        
        # List available files
        files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
        print(f"✅ Found {len(files)} CSV files")
        
        # Test loading a small file
        test_file = os.path.join(data_dir, "data_list_10.csv")
        if os.path.exists(test_file):
            data = load_data(test_file)
            print(f"✅ Successfully loaded {len(data)} values from test file")
            
            # Test both algorithms
            target = 0
            bf_result = two_sum_brute_force(data, target)
            ht_result = two_sum_hash_table(data, target)
            
            print(f"✅ Brute force result: {bf_result}")
            print(f"✅ Hash table result: {ht_result}")
            print(f"✅ Results match: {bf_result == ht_result}")
            
        else:
            print("❌ Test file data_list_10.csv not found")
    else:
        print("❌ Data directory not found at /GreenIT_data")
        print("Make sure you've mounted the volume correctly")
        return False
    
    print("\n" + "=" * 50)
    print("Environment test complete!")
    return True

if __name__ == "__main__":
    if test_docker_environment():
        print("\nRunning full analysis...")
        run_analysis_in_docker()
    else:
        print("Environment test failed. Please check your Docker configuration.")