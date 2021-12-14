


# Import Dependecies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# Define the functions scrape
def scrape():
    
    # NASA Mars News
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Access https://redplanetscience.com/
    url_red_planet = "https://redplanetscience.com/"
    browser.visit(url_red_planet)

    # Allow the page time to load
    time.sleep(5)

    # Set the Beautiful Soup object with the fully loaded page
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')    

    # Pull news_title
    news_title=soup.find("div",class_="content_title").text

    # Pull news paragraph
    news_p=soup.find("div",class_="article_teaser_body").text

    # Print news title and paragraph
    print(f"> Title: {news_title}\n\n> Article Teaser: {news_p}")

    # Close the browser
    browser.quit()


    # JPL Mars Space Images - Featured Image
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Access https://spaceimages-mars.com/
    url_space_image = "https://spaceimages-mars.com/"
    browser.visit(url_space_image)

    # Allow the page time to load
    time.sleep(5)

    # Set the Beautiful Soup object with the fully loaded page
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')    

    # Save the first results in a variable
    results=soup.find_all("img", class_="headerimage fade-in")

    # Pull image url
    featured_image_url=f"{url_space_image}{results[0]['src']}"

    # Print the url
    print(f"Here is the link to the current Featured Mars Image: {featured_image_url}")

    # Close the browser
    browser.quit()


    # Mars Facts
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Access https://galaxyfacts-mars.com/
    url_galaxy_facts = "https://galaxyfacts-mars.com/"
    browser.visit(url_galaxy_facts)

    # Allow the page time to load
    time.sleep(5)

    # Set the Beautiful Soup object with the fully loaded page
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')    

    # Read Mars facts table and rename the columns
    mars_table = pd.read_html(url_galaxy_facts)[1]

    # Close the browser
    browser.quit()

    # Rename the columns
    mars_table.columns=["Description","Value"]

    # Reset the data frame index
    mars_table.set_index("Description")

    # Save the table in html file
    mars_table.to_html("mars_html.html")

    # Convert the data to a HTML table string
    mars_html=mars_table.to_html()


    # Mars Hemispheres
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Access https://galaxyfacts-mars.com/
    url_mars_hemi = "https://marshemispheres.com/"
    browser.visit(url_mars_hemi)

    # Allow the page time to load
    time.sleep(5)

    # Cerberus Hemisphere Enhanced
    # Click on Cerberus Hemisphere Enhanced
    browser.click_link_by_partial_text('Cerberus')

    # Create an empty list to hold the results
    image_urls=[]
    image_titles=[]

    # Set the Beautiful Soup object with the fully loaded page
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')    

    # Pull the image URL and append the url list
    cerberus_url=url_mars_hemi+soup.find("img", class_="wide-image")["src"]
    image_urls.append(cerberus_url)

    # Pull image title and append the title list
    cerberus_title=soup.find("h2", class_="title").text
    image_titles.append(cerberus_title)

    # Schiaparelli Hemisphere Enhanced
    # Go back to the home page
    browser.click_link_by_partial_text('Back')

    # Click on Schiaparelli Hemisphere Enhanced
    browser.click_link_by_partial_text('Schiaparelli')

    # Set the Beautiful Soup object with the fully loaded page
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')    

    # Pull the image URL and append the url list
    schiaparelli_url=url_mars_hemi+soup.find("img", class_="wide-image")["src"]
    image_urls.append(schiaparelli_url)

    # Pull image title and append the title list
    schiaparelli_title=soup.find("h2", class_="title").text
    image_titles.append(schiaparelli_title)

    # Syrtis Major Hemisphere Enhanced
    # Go back to the home page
    browser.click_link_by_partial_text('Back')

    # Click on Syrtis Major Hemisphere Enhanced
    browser.click_link_by_partial_text('Syrtis')

    # Set the Beautiful Soup object with the fully loaded page
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')    

    # Pull the image URL and append the url list
    syrtis_url=url_mars_hemi+soup.find("img", class_="wide-image")["src"]
    image_urls.append(syrtis_url)

    # Pull image title and append the title list
    syrtis_title=soup.find("h2", class_="title").text
    image_titles.append(syrtis_title)

    # Valles Marineris Hemisphere Enhanced
    # Go back to the home page
    browser.click_link_by_partial_text('Back')

    # Click on Valles Marineris Hemisphere Enhanced
    browser.click_link_by_partial_text('Valles')

    # Set the Beautiful Soup object with the fully loaded page
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')    

    # Pull the image URL and append the url list
    valles_url=url_mars_hemi+soup.find("img", class_="wide-image")["src"]
    image_urls.append(valles_url)

    # Pull image title and append the title list
    valles_title=soup.find("h2", class_="title").text
    image_titles.append(valles_title)

    # Close the browser
    browser.quit()

    hemisphere_image_urls=[]
    for i in range(len(image_urls)):
        hemisphere_image_urls.append({"title": image_titles[i],"img_url":image_urls[i]})
        
    mars_dict={"news_title":news_title,
               "news_paragraph":news_p,
               "featured_image":featured_image_url,
               "mars_facts":mars_html,
               "image_titles":image_titles,
               "image_urls":image_urls
               }

    return mars_dict