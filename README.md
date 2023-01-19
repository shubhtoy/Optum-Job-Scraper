
# Optum Job Scraper

This script is a web scraper that uses the Python library `requests` to scrape job listings from the Optum job search website.

## Getting Started

### Prerequisites

-   Python 3
-   `requests` library
-   `json` library

### Installing

1.  Clone the repository

    `git clone https://github.com/shubhtoy/Optum-Job-Scraper.git` 

2.  Install the required libraries

    `pip install requests` 

3.  Run the script


    `python Optum-Job-Scraper.py` 

### How it works

The script starts by defining some global variables, including the `OUTPUT` variable which sets the filename for the output JSON file.

The headers and parameters for the API request are also defined. The `requests.get()` method is used to make the API request with the defined headers and parameters.

The script then uses a callback function to replace the callback function in the API response with a valid json object.

The script then uses a for loop to iterate through the pages and extract the job listings. The job listings are then stored in a list called `all_jobs`.

Finally, the script uses the `json.dump()` method to write the job listings to a JSON file in the specified format.

## Authors

-   **Shubhtoy** - _Initial work_ - [shubhtoy](https://github.com/shubhtoy)

## License

This project is licensed under the MIT License.

## Acknowledgments

-   API endpoint and parameters are specific to Optum and may change over time.
-   API endpoint may be restricted to authorized parties only.
-   API endpoint may be subject to rate limits.
-   Always make sure to use appropriate headers, parameters and respect rate limits when scraping.
-   Do not scrape websites without permission from the website owner.



