"""
Unit tests for the Subnet Calculator CLI application.
"""

import unittest
from main import calculate_subnets, calculate_subnet_masks


class TestSubnetCalculator(unittest.TestCase):
    """Test cases for subnet calculation functions."""

    def test_calculate_subnets_valid(self):
        network = "192.168.0.0"
        cidr = "24"
        departments = [50, 20]
        output = calculate_subnets(network, cidr, departments)
        self.assertIn("Department 1:", output)
        self.assertIn("Subnet Mask:", output)
        self.assertIn("Broadcast Address:", output)

    def test_calculate_subnets_invalid_network(self):
        result = calculate_subnets("invalid", "24", [30])
        self.assertIn("Error:", result)

    def test_calculate_subnets_invalid_mask(self):
        result = calculate_subnets("192.168.1.0", "abc", [30])
        self.assertIn("Error:", result)

    def test_calculate_masks_valid(self):
        result = calculate_subnet_masks([30, 100])
        self.assertIn("/27", result)
        self.assertIn("/25", result)

    def test_calculate_masks_zero_hosts(self):
        result = calculate_subnet_masks([0])
        self.assertIn("Error:", result)

    def test_calculate_masks_negative_hosts(self):
        result = calculate_subnet_masks([-5])
        self.assertIn("Error:", result)


if __name__ == "__main__":
    unittest.main()
