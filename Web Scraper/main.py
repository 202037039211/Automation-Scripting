import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape data from a given URL
def scrape_data(url):
    # Send HTTP request to the website
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")  # Log the HTTP response status

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example scraping: Extracting the page title and the first three paragraphs
    title = soup.find('h1', id="firstHeading").text if soup.find('h1', id="firstHeading") else "N/A"
    paragraphs = [p.text for p in soup.find_all('p')[:3]]  # Get the first three paragraphs

    # Organize the scraped data into a dictionary
    data = {
        "Title": [title],
        "Paragraph 1": [paragraphs[0] if len(paragraphs) > 0 else "N/A"],
        "Paragraph 2": [paragraphs[1] if len(paragraphs) > 1 else "N/A"],
        "Paragraph 3": [paragraphs[2] if len(paragraphs) > 2 else "N/A"],
    }

    # Convert the data into a pandas DataFrame for better structure
    df = pd.DataFrame(data)
    print("Scraped data:\n", df)

    # Save the scraped data to a CSV file (this simulates updating a CRM system)
    df.to_csv('scraped_data.csv', index=False)
    print("Data saved to scraped_data.csv")

# Main function to prompt the user for the URL and start the scraping process
def main():
    url = input("Enter the URL of the page to scrape: ")
    scrape_data(url)

# Ensure the script is executed directly (not imported)
if __name__ == "__main__":
    main()
