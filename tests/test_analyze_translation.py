import unittest
from datetime import datetime

from analyze_translation import binary_search_nearest, get_correct_slot, create_output_file
from utils import parse_timestamp


class TestBinarySearchNearest(unittest.TestCase):
    def setUp(self):
        # Create a sample of delivery events for testing
        self.events = [
            {"timestamp": "2024-01-21 15:51:10.496954", "translation_id": "5aa5b2f39f7254a75aa6", "duration": 26},
            {"timestamp": "2024-01-21 15:54:10.496954", "translation_id": "5aa5b2f39f7254a75aa5", "duration": 25},
            {"timestamp": "2024-01-21 15:57:10.496954", "translation_id": "5aa5b2f39f7254a75aa4", "duration": 24},
            {"timestamp": "2024-01-21 16:00:10.496954", "translation_id": "5aa5b2f39f7254a75aa3", "duration": 23},
            {"timestamp": "2024-01-21 16:03:10.496954", "translation_id": "5aa5b2f39f7254a75aa2", "duration": 22},
            {"timestamp": "2024-01-21 16:06:10.496954", "translation_id": "5aa5b2f39f7254a75aa1", "duration": 21},
            {"timestamp": "2024-01-21 16:09:10.496954", "translation_id": "5aa5b2f39f7254a75aa0", "duration": 20},
        ]

    def test_binary_search_nearest_found(self):
        # Target timestamp that represents the lower_bound_time
        target_timestamp = datetime.strptime("2024-01-21 16:01:00.496954", "%Y-%m-%d %H:%M:%S.%f")
        result_index = binary_search_nearest(self.events, target_timestamp)
        self.assertEqual(result_index, 4)


class TestGetCorrectSlot(unittest.TestCase):
    def setUp(self):
        # Create sample events for testing
        self.events = [
            {"timestamp": "2024-01-21 15:51:10.496954", "translation_id": "5aa5b2f39f7254a75aa6", "duration": 26},
            {"timestamp": "2024-01-21 15:54:10.496954", "translation_id": "5aa5b2f39f7254a75aa5", "duration": 25},
            {"timestamp": "2024-01-21 15:57:10.496954", "translation_id": "5aa5b2f39f7254a75aa4", "duration": 24},
            {"timestamp": "2024-01-21 16:00:10.496954", "translation_id": "5aa5b2f39f7254a75aa3", "duration": 23},
            {"timestamp": "2024-01-21 16:03:10.496954", "translation_id": "5aa5b2f39f7254a75aa2", "duration": 22},
            {"timestamp": "2024-01-21 16:06:10.496954", "translation_id": "5aa5b2f39f7254a75aa1", "duration": 21},
            {"timestamp": "2024-01-21 16:09:10.496954", "translation_id": "5aa5b2f39f7254a75aa0", "duration": 20},
        ]

    def test_get_correct_slot(self):
        lower_bound_time = datetime.strptime("2024-01-21 16:01:00.496954", "%Y-%m-%d %H:%M:%S.%f")
        event_timestamp = parse_timestamp(self.events[4]["timestamp"])
        slot = get_correct_slot(event_timestamp, lower_bound_time.second)
        expected_result = datetime.strptime("2024-01-21 16:04:00", "%Y-%m-%d %H:%M:%S")
        self.assertEqual(slot, expected_result)


if __name__ == '__main__':
    unittest.main()
