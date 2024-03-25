# Script Tag Keyword Search

This Python script provides a simple yet effective tool for searching specific keywords within the `<script>` tags of HTML files. It's particularly useful for analyzing web pages to identify references to features like 'Continue Watching' lists or other significant JavaScript variables and functions related to user interactions and preferences.

## Features

- **Keyword Search in `<script>` Tags**: Scans HTML content for specified keywords within `<script>` tags, aiding in quick identification of relevant JavaScript code.
- **Support for Multiple Files**: Allows batch processing of HTML files to search for keywords, enhancing efficiency in analyzing multiple web pages.
- **Customizable Keyword List**: Users can easily modify the list of keywords according to their specific search criteria.

## Prerequisites

Before running this script, ensure you have Python installed on your system. Additionally, you'll need the `BeautifulSoup` library for parsing HTML content:

```bash
pip install beautifulsoup4
Usage
Prepare Your HTML Files: Place the HTML files you want to analyze in an accessible directory.

Customize Your Keyword List: Modify the keywords list in the script to include the specific keywords you're interested in searching within the script tags.

python
Copy code
keywords = ['continue-watching', 'resume-watching', ...]
Specify Your HTML Files: Update the html_files list with the paths to the HTML files you intend to analyze.
python
Copy code
html_files = [
    'path\\to\\your\\html_file1.html', 
    ...
]
```

## Run the Script: Execute the script in your terminal or command prompt.
- bash
- Copy code
- python path_to_script.py
- Review the Results: The script will output the results in the terminal, indicating each keyword found and a snippet of the script content where it was discovered.

## Customization
- This script can be easily customized to fit various needs:
- Adjust the keywords list to search for different terms.
- Expand the html_files list to analyze additional HTML files.
- Modify the output formatting or the details provided about found keywords for specific reporting needs.
