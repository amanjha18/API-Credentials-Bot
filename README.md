# AI Bot for Finding API Credentials

## Overview

This Python script is designed to build an AI bot that can find API credentials (specifically a merchant ID and a secret key) from a given URL. It utilizes the `requests` library for making HTTP requests and the `BeautifulSoup` library for parsing HTML content.

## Usage

1. Clone or download the repository.
2. Install the required libraries using the following command:

pip install -r requirements.txt
3. Run the script using a Python interpreter:

python app.py
4. Enter the URL of the webpage from which you want to extract API credentials.
5. The script will process the URL and display the extracted API credentials (if present).

## Code Explanation

The script defines a function `find_credentials(url)` that performs the following steps:
- Makes an HTTP GET request to the provided URL using the `requests` library.
- Parses the HTML content of the response using `BeautifulSoup`.
- Searches for input fields with the names 'merchant_id' and 'secret_key' and extracts their values.

The main part of the script prompts the user to enter a URL and processes the URL using the `find_credentials` function. It then prints the extracted API credentials.

## Note

- Ensure that the provided URL has input fields with the names 'merchant_id' and 'secret_key' for the script to work effectively.
- Handle exceptions and errors appropriately, and consider adding error checking for robust functionality.

## Author

[aman]

Feel free to use and modify this script as needed for your projects!


