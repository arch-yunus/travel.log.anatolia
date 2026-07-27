import unittest
import os
import shutil
import tempfile
from analytics import TravelLogAnalytics

class TestTravelLogAnalytics(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory structure for testing
        self.test_dir = tempfile.mkdtemp()
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir)
        
        # Setup fake regions
        self.region_name = "01_Marmara"
        os.makedirs(os.path.join(self.test_dir, self.region_name, "Istanbul", "Ayasofya"))
        os.makedirs(os.path.join(self.test_dir, "02_Ege")) # Empty region

    def tearDown(self):
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir)

    def test_scan_region_populated(self):
        analytics = TravelLogAnalytics(root_dir=self.test_dir)
        result = analytics.scan_region(self.region_name)
        
        self.assertEqual(result["cities"], 1)
        self.assertEqual(result["locations"], 1)

    def test_scan_region_empty(self):
        analytics = TravelLogAnalytics(root_dir=self.test_dir)
        result = analytics.scan_region("02_Ege")
        
        self.assertEqual(result["cities"], 0)
        self.assertEqual(result["locations"], 0)

    def test_scan_region_nonexistent(self):
        analytics = TravelLogAnalytics(root_dir=self.test_dir)
        result = analytics.scan_region("99_Uzay")
        
        self.assertIsNone(result)
        
    def test_scan_region_with_readme(self):
        # Create a mock README.md marking only Istanbul as visited
        with open("README.md", "w", encoding="utf-8") as f:
            f.write("# 🇹🇷 TRAVEL LOG\n\n- ✅ **Istanbul**\n- ❌ Bursa\n")
            
        os.makedirs(os.path.join(self.test_dir, self.region_name, "Bursa", "Ulu_Cami"))
        
        analytics = TravelLogAnalytics(root_dir=self.test_dir)
        result = analytics.scan_region(self.region_name)
        
        # Istanbul is in README and has folder -> counted
        # Bursa has folder but is NOT in README -> not counted
        self.assertEqual(result["cities"], 1)
        self.assertEqual(result["locations"], 1)

if __name__ == '__main__':
    unittest.main()
