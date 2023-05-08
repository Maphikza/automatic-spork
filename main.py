import time
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from googlesearch import search
from newspaper import Article


def search_news(name: str) -> List[str]:
    query = f"{name} news"
    results = []
    for result in search(query, num_results=15, lang="en"):
        results.append(result)
    return results


def extract_text(url: str) -> str:
    article = Article(url)
    article.download()
    article.parse()

    return article.text


def extract_text_selenium(url):
    # Initialize the WebDriver (change the path if necessary)
    service = Service(executable_path=r"C:\Users\stapi\PycharmProjects\chromedriver")
    driver = webdriver.Chrome(service=service)

    # Open the URL
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Extract text content from the page
    scraped_text = driver.find_element(By.TAG_NAME, "body").text

    # Close the WebDriver
    driver.quit()

    return scraped_text


if __name__ == "__main__":
    celebrity_name = input("Enter the celebrity name: ")
    celeb_news = search_news(celebrity_name)
    for news in celeb_news:
        text = extract_text_selenium(news)
        time.sleep(2)
        print(text)
        # print(extract_text(news))
        print("_________")
