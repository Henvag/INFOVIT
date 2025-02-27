import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Set of visited URLs to avoid revisiting
visited_urls = set()


# Function to crawl a given URL
def crawl(url):
    if url in visited_urls:
        return
    visited_urls.add(url)

    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    # Extract and print the texts using the provided XPath expression
    elements = driver.find_elements(By.XPATH, "//span[@class='C9DxTc ']")
    for element in elements:
        print(element.text)

    # Find all internal links on the page
    links = driver.find_elements(By.XPATH, "//a[@href]")
    for link in links:
        href = link.get_attribute("href")
        if href.startswith("https://sites.google.com/view/nikt2024?usp=sharing") and href not in visited_urls:
            crawl(href)


# Start crawling from the main page
start_url = "https://sites.google.com/view/nikt2024?usp=sharing"
crawl(start_url)

# Close the WebDriver
driver.quit()