import json
import os
from datetime import datetime, timedelta

WINDOW_SIZE = 10
NUMBER_OF_EVENTS = 7


# Function to generate events and write them to a file
def generate_events_file(test_events, current_time):
    translation_events = [
        {
            "timestamp": (current_time - timedelta(minutes=(i*3))).strftime('%Y-%m-%d %H:%M:%S.%f'),
            "translation_id": f"5aa5b2f39f7254a75aa{i}",
            "source_language": "en",
            "target_language": "fr",
            "client_name": "airliberty",
            "event_name": "translation_delivered",
            "nr_words": 30,
            "duration": 20 + i
        }
        for i in reversed(range(NUMBER_OF_EVENTS))
    ]

    # Create a path for the events file inside the data directory
    test_events_path = os.path.join('data', test_events)
    with open(test_events_path, 'w') as file:
        for event in translation_events:
            file.write(json.dumps(event) + '\n')


if __name__ == "__main__":
    test_events = 'test_events.json'
    current_time = datetime.now()
    generate_events_file(test_events, current_time)
