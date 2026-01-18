# test_algospark.py
"""
Tests for AlgoSpark module.
"""

import unittest
from algospark import AlgoSpark

class TestAlgoSpark(unittest.TestCase):
    """Test cases for AlgoSpark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AlgoSpark()
        self.assertIsInstance(instance, AlgoSpark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AlgoSpark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
