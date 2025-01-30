import requests
from bs4 import BeautifulSoup

def get_html(url):
    """Fetch HTML content of the URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def parse_html(html, choice):
    """Parse HTML and scrape based on user's choice."""
    soup = BeautifulSoup(html, 'html.parser')
    
    if choice == '1':  # Scrape all headings (h1, h2, h3)
        headings = soup.find_all(['h1', 'h2', 'h3'])
        for i, heading in enumerate(headings, 1):
            print(f"{i}. {heading.get_text().strip()}")
    
    elif choice == '2':  # Scrape all links
        links = soup.find_all('a', href=True)
        for i, link in enumerate(links, 1):
            print(f"{i}. {link['href']} - {link.get_text().strip()}")
    
    elif choice == '3':  # Scrape all paragraphs
        paragraphs = soup.find_all('p')
        for i, paragraph in enumerate(paragraphs, 1):
            print(f"{i}. {paragraph.get_text().strip()}")
    
    else:
        print("Invalid choice. Please enter a valid option.")

def main():
    """Main function to interactively scrape a webpage."""
    print("Welcome to the Interactive Web Scraping Tool!")
    url = input("Enter the URL of the website to scrape: ")
    html = get_html(url)

    if html:
        print("\nWhat would you like to scrape?")
        print("1. All Headings (h1, h2, h3)")
        print("2. All Links")
        print("3. All Paragraphs")

        choice = input("\nEnter your choice (1/2/3): ")
        print("\nScraping results:")
        parse_html(html, choice)

if __name__ == "__main__":
    main()
