#!/usr/bin/env python3
"""Module doc"""

from windowify import find_step
def main():
    """Main function"""
    for window_size in [300,500]:
        print(f"window_size={window_size}")
        for height in [3000, 4096]:
            print(f"\theight={height}")
            for d in range(0,10):
                print(f"\t\td={d}")
                print("\t\t\t", find_step(height=height, window_size=window_size, d=d))
    

if __name__ == "__main__":
    main()


