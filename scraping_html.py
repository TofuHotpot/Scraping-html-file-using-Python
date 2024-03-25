from bs4 import BeautifulSoup

def search_keyword_in_scripts(html_content, keywords):
    soup = BeautifulSoup(html_content, 'html.parser')
    found_keywords = {}

    # Searching for keywords in 'script' tags
    for script in soup.find_all('script'):
        script_content = script.string if script.string else ""
        for keyword in keywords:
            if keyword.lower() in script_content.lower():
                if keyword not in found_keywords:
                    found_keywords[keyword] = []
                found_keywords[keyword].append(script_content)

    return found_keywords

# List of keywords to search for
keywords = ['continue-watching', 'resume-watching', 'continueWatching', 'ResumeWatching', 'Watch History', 'Continue Watching', 'viewedItems']

# List of your HTML files
html_files = [
    'C:\\Users\\nicole.chung\\desktop\\hackAIthon\\html_files\\itvx.html', 
    'C:\\Users\\nicole.chung\\desktop\\hackAIthon\\html_files\\appleTV.html',
    'C:\\Users\\nicole.chung\\desktop\\hackAIthon\\html_files\\netflix.html',
]

# Search for keywords in each HTML file
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
        found_keywords = search_keyword_in_scripts(html_content, keywords)
        
        print(f"Results for {file_path}:")
        for keyword, scripts in found_keywords.items():
            print(f"\nKeyword '{keyword}' found in the following script(s):")
            for script in scripts:
                print(f"\nScript content (truncated): {script[:100000]}...")  # Print first 500 characters
        print("\n" + "="*50)
