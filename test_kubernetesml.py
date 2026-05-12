# test_kubernetesml.py
"""
Tests for KubernetesML module.
"""

import unittest
from kubernetesml import KubernetesML

class TestKubernetesML(unittest.TestCase):
    """Test cases for KubernetesML class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KubernetesML()
        self.assertIsInstance(instance, KubernetesML)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KubernetesML()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
