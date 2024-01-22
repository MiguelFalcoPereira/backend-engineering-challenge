# Backend Engineering Challenge


## Translation Analysis Tool

This tool analyzes translation events and calculates the moving average delivery time for the last X minutes.


### Requirements

- Python (3.7.x or higher recommended)


### Installation

1. Clone the repository:
```bash
git clone https://github.com/MiguelFalcoPereira/backend-engineering-challenge.git
```


### Usage
Run the main script to analyze all the translation delivered events within the specified time.

    analyze_translation.py --input_file events.json --window_size 10
    
Replace `events.json` with the path to your input file and adjust other parameters as needed:

- `--input_file`: Path to the input file containing translation events (required).
- `--window_size`: Size of the time window in minutes (default: 10).
- `--output_file`: Path to the output file to store the results (default: output_file.json).


If you don't have an input file prepared, you can quickly create a new one by doing:
    
    python data/generate_translation_events.py

### Testing
To run the tests use the following command:
    
    python test_analyze_translation.pypython -m unittest tests.test_analyze_translation
    
### Notes

- I opted to use a **binary search algorithm** because it works more efficiently on already sorted data, while also reducing the total time spent to find the first `translation_delivery` event within the past `window_size` minutes. 
Also, this algorithm minimizes the search space by eliminating the need to check if every event happened after the last `window_size` minutes (maximum of half of the total events per iteration).


## Challenge Objective

Your mission is to build a simple command line application that parses a stream of events and produces an aggregated output. In this case, we're interested in calculating, for every minute, a moving average of the translation delivery time for the last X minutes.

If we want to count, for each minute, the moving average delivery time of all translations for the past 10 minutes we would call your application like (feel free to name it anything you like!).

	unbabel_cli --input_file events.json --window_size 10
	
The input file format would be something like:

	{"timestamp": "2018-12-26 18:11:08.509654","translation_id": "5aa5b2f39f7254a75aa5","source_language": "en","target_language": "fr","client_name": "airliberty","event_name": "translation_delivered","nr_words": 30, "duration": 20}
	{"timestamp": "2018-12-26 18:15:19.903159","translation_id": "5aa5b2f39f7254a75aa4","source_language": "en","target_language": "fr","client_name": "airliberty","event_name": "translation_delivered","nr_words": 30, "duration": 31}
	{"timestamp": "2018-12-26 18:23:19.903159","translation_id": "5aa5b2f39f7254a75bb3","source_language": "en","target_language": "fr","client_name": "taxi-eats","event_name": "translation_delivered","nr_words": 100, "duration": 54}

Assume that the lines in the input are ordered by the `timestamp` key, from lower (oldest) to higher values, just like in the example input above.

The output file would be something in the following format.

```
{"date": "2018-12-26 18:11:00", "average_delivery_time": 0}
{"date": "2018-12-26 18:12:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:13:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:14:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:15:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:16:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:17:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:18:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:19:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:20:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:21:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:22:00", "average_delivery_time": 31}
{"date": "2018-12-26 18:23:00", "average_delivery_time": 31}
{"date": "2018-12-26 18:24:00", "average_delivery_time": 42.5}
```

#### Notes

Before jumping right into implementation we advise you to think about the solution first. We will evaluate, not only if your solution works but also the following aspects:

+ Simple and easy to read code. Remember that [simple is not easy](https://www.infoq.com/presentations/Simple-Made-Easy)
+ Comment your code. The easier it is to understand the complex parts, the faster and more positive the feedback will be
+ Consider the optimizations you can do, given the order of the input lines
+ Include a README.md that briefly describes how to build and run your code, as well as how to **test it**
+ Be consistent in your code. 

Feel free to, in your solution, include some your considerations while doing this challenge. We want you to solve this challenge in the language you feel most comfortable with. Our machines run Python (3.7.x or higher) or Go (1.16.x or higher). If you are thinking of using any other programming language please reach out to us first 🙏.

Also, if you have any problem please **open an issue**. 

Good luck and may the force be with you
