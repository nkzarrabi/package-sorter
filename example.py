#!/usr/bin/env python3
"""
Package Sorter - Example Usage

This script demonstrates how to use the package sorting function.
"""

from package_sorter import sort


def main():
    """Demonstrate package sorting with various examples"""
    
    print("Package Sorter - Example Usage")
    print("=" * 40)
    
    # Example packages
    packages = [
        {"desc": "Small standard package", "width": 10, "height": 10, "length": 10, "mass": 5},
        {"desc": "Heavy small package", "width": 10, "height": 10, "length": 10, "mass": 25},
        {"desc": "Large volume package", "width": 100, "height": 100, "length": 100, "mass": 15},
        {"desc": "Long thin package", "width": 200, "height": 5, "length": 5, "mass": 10},
        {"desc": "Heavy and bulky package", "width": 100, "height": 100, "length": 100, "mass": 30},
        {"desc": "Boundary case - exactly bulky", "width": 150, "height": 10, "length": 10, "mass": 19},
        {"desc": "Boundary case - exactly heavy", "width": 50, "height": 50, "length": 50, "mass": 20},
    ]
    
    for package in packages:
        result = sort(package["width"], package["height"], package["length"], package["mass"])
        print(f"{package['desc']}: {package['width']}x{package['height']}x{package['length']} cm, {package['mass']} kg -> {result}")


if __name__ == "__main__":
    main()