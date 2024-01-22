import argparse
import json
from datetime import datetime, timedelta

from .analyze_translation_tool.utils import parse_timestamp, format_number

"""
    Binary search to find the index of the nearest timestamp after or equal to the target (lower-bound_time).
"""
def binary_search_nearest(events, target):
    low, high = 0, len(events) - 1
    closest_event_index = None

    while low <= high:
        mid = (low + high) // 2
        mid_timestamp = parse_timestamp(events[mid]['timestamp'])

        if mid_timestamp >= target:
            # Update closest event based on distance
            if closest_event_index is None or mid_timestamp < parse_timestamp(events[closest_event_index]['timestamp']):
                closest_event_index = mid

            high = mid - 1
        else:
            low = mid + 1

    return closest_event_index


"""
    Get the correct slot for the given timestamp based on the seconds of the intervals timestamps.
"""
def get_correct_slot(timestamp, interval_seconds):
    if timestamp.second < interval_seconds:
        new_timestamp = timestamp.replace(second=interval_seconds)
    else:
        new_timestamp = timestamp.replace(second=interval_seconds, minute=timestamp.minute+1)
    return new_timestamp


"""
    Creates the output file with the calculated average delivery times for each minute in the time window.
"""
def create_output_file(time_dict, window_size, lower_bound_time, file_name):
    with open(file_name, 'w') as file:
        current_key = lower_bound_time
        last_delivery_average = 0
        for window in range(window_size):
            if current_key.strftime('%Y-%m-%d %H:%M:%S') in time_dict:
                last_delivery_average = time_dict[current_key.strftime('%Y-%m-%d %H:%M:%S')]
            entry = {
                "date": current_key.strftime('%Y-%m-%d %H:%M:%S'),
                "average_delivery_time": last_delivery_average
            }
            file.write(json.dumps(entry)+"\n")
            current_key += timedelta(minutes=1)


def main():
    parser = argparse.ArgumentParser(description='Calculate moving average delivery time for translations.',
                                     epilog="Example: python analyze_translation.py --input_file events.json --window_size 10")
    parser.add_argument('--input_file', type=str, required=True, help='Path to the input file')
    parser.add_argument('--output_file', type=str, default="output_file.json", help='Path to the output file')
    parser.add_argument('--window_size', type=int, default=10, help='Size of the time window in minutes')
    args = parser.parse_args()
    try:
        # Read the events from the input file
        with open(args.input_file, 'r') as file:
            events = [json.loads(line.strip()) for line in file]

        total_duration = 0
        num_events = 0
        current_time = datetime.now()
        # Do a binary search for the nearest timestamp after or equal to the lower bound of the time window
        lower_bound_time = current_time - timedelta(minutes=args.window_size)
        start_index = binary_search_nearest(events, lower_bound_time)
        time_dict = {}
        if start_index:
            # Iterate through the relevant events within the time window
            for event in events[start_index:]:
                timestamp = parse_timestamp(event['timestamp'])
                duration = event['duration']
                # Confirm if the event is within the time window
                if timestamp <= current_time:
                    total_duration += duration
                    num_events += 1
                    average_delivery_time = total_duration / num_events
                    # Get the corresponding slot for the event
                    slot = get_correct_slot(timestamp, lower_bound_time.second).strftime('%Y-%m-%d %H:%M:%S')
                    # Update time_dict with the calculated average delivery time for each event
                    time_dict[slot] = format_number(average_delivery_time)
        # Create the output file with calculated average delivery times for every minute within the time window
        create_output_file(time_dict, args.window_size, lower_bound_time, args.output_file)
        print(f"Output file created.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == '__main__':
    main()
