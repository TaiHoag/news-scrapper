# News Scrapper
This repository is still in progress of developing and refining

## Description
This is a News Scrapper to scrap data and text from online newspapers, news sites or any specific websites written in JS and HTML.

## Instruction

### 1. Find article URLs based on the specific HTML tags and classes:
Modify these selectors according to the structure of the webpage you are scraping to the `article_links` in the `get_article_urls` function.

Example `article_links` for CNN:
```py
article_links = [a['href'] for a in soup.find_all('a', class_=['container__link', 'container__title-url container_lead-package__title-url', 'container__link container__link--type-article container_lead-package__link container_lead-package__left container_lead-package__light', 'container__link container__link--type-live-story container_lead-package__link container_lead-package__left container_lead-package__light'])]
```

### 2. Find the wanted article content according to the type of HTML headings and paragraphs:
Modify these headings to the `content` in the  `fetch_article` function.

Example `content` for CNN:
```py
content = '\n'.join([heading.text.strip() for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hgroup', 'p', 'blockquote']) if heading.text.strip()]) if soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hgroup', 'p', 'blockquote']) else 'N/A'
```

### 3. Edit the Base URL
Get the Base URL of the website homepage, for example:
'https://edition.cnn.com' or 'https://www.theguardian.com'
Modify the URL into the `base_url`

