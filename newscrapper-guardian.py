import requests
from bs4 import BeautifulSoup

def get_article_urls(base_url):
    # Send a GET request to the base URL
    response = requests.get(base_url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: {response.status_code}")
        return []
    
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find article URLs based on the specific HTML tags and classes
    # Modify these selectors according to the structure of the webpage you are scraping
    article_links = [a['href'] for a in soup.find_all('a', class_=['dcr-lv2v9o', 'dcr-jokavg', 'dcr-4cudl2'])]
    
    # Convert relative URLs to absolute URLs
    article_urls = [base_url + link if link.startswith('/') else link for link in article_links]
    
    return article_urls

def fetch_article(url):
    # Fetch the web page
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the article content
    content = '\n'.join([heading.text.strip() for heading in soup.find_all('p') if heading.text.strip()]) if soup.find_all('p') else 'N/A'

    return {
        'content': content,
        'url': url
    }

if __name__ == '__main__':
    # Base URL of the website you want to scrape
    base_url = 'https://www.theguardian.com'
    
    # Get all article URLs from the specified base URL
    article_url = get_article_urls(base_url)

with open('scraped_articles.txt', 'a', encoding='utf-8') as file:

    for url in article_url:

        article = fetch_article(url)

        # write the article into new text file
        file.write(article['content'])

    print("Scraping completed. Results saved to 'scraped_articles.txt'.")
