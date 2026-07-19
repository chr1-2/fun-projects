import math
import random
import sys
import time

while True:
    b = input("\nEnter first name (or type 'q' to exit): ")
    if b.lower() == 'q':
        print("Goodbye!")
        break
        
    c = input("Enter second name : ")
    
    print("\nAnalyzing...", end="", flush=True)
    
    # Creates a moving loading bar animation
    for _ in range(60):
        time.sleep(0.1)
        print("█", end="", flush=True)
    print(" Done!\n")

    a = random.random()
    percentage = (a * 100)

    print(f"{b} and {c} are {percentage:.2f}% likely to be gay.\n")
    print("-" * 30)
