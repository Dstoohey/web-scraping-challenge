from splinter import Browser
from bs4 import BeautifulSoup 
import time
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # mars nasa
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    list_item = soup.select_one("ul.item_list li.slide")
    content_title = list_item.find("div", class_='content_title').get_text()
    text_body = list_item.find("div", class_='article_teaser_body').get_text()
    
    #Jet Propulsion Lab at CalTech.

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # mars facts

    mars_facts = pd.read_html('https://space-facts.com/mars/')
    mars_table = mars_facts[0]
    mars_html_table = mars_table.to_html()
    mars_html_table = mars_html_table.replace("\n", "")
    
    # mars hemispheres

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemispheres_url = []
    links = browser.find_by_css("a.product-item h3")




    
    # Store data in a dictionary
    mars_data_dict = {
        "title": content_title,
        "body": text_body,
        "hemispheres": hemispheres_url,
        "table": mars_html_table
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data_dict



