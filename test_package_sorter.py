import unittest
from package_sorter import sort


class TestPackageSorter(unittest.TestCase):
    
    def test_standard_packages(self):
        """Test packages that should go to STANDARD stack"""
        # Small, light package
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")
        
        # Just under bulky threshold
        self.assertEqual(sort(99, 99, 99, 5), "STANDARD")
        self.assertEqual(sort(149, 10, 10, 5), "STANDARD")
        
        # Just under heavy threshold
        self.assertEqual(sort(10, 10, 10, 19.9), "STANDARD")
    
    def test_special_packages_heavy_only(self):
        """Test packages that are heavy but not bulky"""
        # Heavy but small
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
        self.assertEqual(sort(10, 10, 10, 25), "SPECIAL")
        
        # Heavy, just under bulky volume threshold
        self.assertEqual(sort(99, 99, 99, 20), "SPECIAL")
        
        # Heavy, just under bulky dimension threshold
        self.assertEqual(sort(149, 10, 10, 20), "SPECIAL")
    
    def test_special_packages_bulky_only(self):
        """Test packages that are bulky but not heavy"""
        # Large volume but light
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
        
        # Large dimension but light
        self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")
        self.assertEqual(sort(10, 150, 10, 10), "SPECIAL")
        self.assertEqual(sort(10, 10, 150, 10), "SPECIAL")
        
        # Way over dimension threshold but light
        self.assertEqual(sort(200, 10, 10, 10), "SPECIAL")
        
        # Bulky by volume, just under heavy threshold
        self.assertEqual(sort(100, 100, 100, 19.9), "SPECIAL")
    
    def test_rejected_packages(self):
        """Test packages that are both heavy and bulky"""
        # Both heavy and bulky by volume
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        
        # Both heavy and bulky by dimension
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")
        self.assertEqual(sort(10, 150, 10, 20), "REJECTED")
        self.assertEqual(sort(10, 10, 150, 20), "REJECTED")
        
        # Way over both thresholds
        self.assertEqual(sort(200, 200, 200, 50), "REJECTED")
    
    def test_boundary_conditions(self):
        """Test exact boundary values"""
        # Exact bulky volume threshold
        self.assertEqual(sort(100, 100, 100, 19.9), "SPECIAL")  # Bulky only
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")   # Both
        
        # Exact bulky dimension threshold
        self.assertEqual(sort(150, 10, 10, 19.9), "SPECIAL")    # Bulky only
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")     # Both
        
        # Exact heavy threshold
        self.assertEqual(sort(149, 10, 10, 20), "SPECIAL")      # Heavy only
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")     # Both
        
        # Just under all thresholds
        self.assertEqual(sort(149, 10, 10, 19.9), "STANDARD")
    
    def test_edge_cases(self):
        """Test edge cases and unusual inputs"""
        # Zero dimensions
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")
        
        # One zero dimension (volume becomes 0)
        self.assertEqual(sort(0, 100, 100, 10), "STANDARD")
        
        # Large dimension with zero mass
        self.assertEqual(sort(200, 10, 10, 0), "SPECIAL")
        
        # Fractional values
        self.assertEqual(sort(99.9, 99.9, 99.9, 19.9), "STANDARD")
        self.assertEqual(sort(150.1, 10, 10, 10), "SPECIAL")


if __name__ == "__main__":
    unittest.main()