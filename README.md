# web-scraping-challenge.

This repository contains my solution of the Web Scraping Homework  - Mission to Mars of the GATECH Data Science and Analytics Bootcamp which has been completed in 2 steps:

# Step1:

Completed the initial scraping using [Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter](/Missions_to_Mars/mission_to_mars.ipynb) as follows:
* Scraped the [Mars News Site](https://redplanetscience.com/) and collected the latest News Title and Paragraph Text. Assigned the text to variables.
* Scraped the url for the Featured Space Image site of https://spaceimages-mars.com/ and saved the completed url string for that image.
* Scraped the table containing facts about the planet including Diameter, Mass, etc. on https://galaxyfacts-mars.com/ and converted the data to a HTML table string.
* Scraped the https://marshemispheres.com/ to got the image url and image title for each hemisphere and saved them to a list of dictionary.

# Step2:

a) Converted my Jupyter notebook into a Python script called [scrape_mars.py](/Missions_to_Mars/scrape_mars.py) with a function called scrape that executes all of my scraping code from above and returns one Python dictionary containing all of the scraped data.

b) Used MongoDB with [Flask templating](/Missions_to_Mars/app.py) to create a new [HTML page](/Missions_to_Mars/templates/index.html) that displays all of the information that was scraped from the URLs above. 2 routes were created:

* `/scrape` that imports my [scrape_mars.py](/Missions_to_Mars/scrape_mars.py) script, calls my scrape function, then stores the return value in Mongo as a Python dictionary.

* `/` that queries my Mongo database and passes the mars data into an HTML template to display the data.

Bellow is a screenshot of the final application.
![Final App Screenshot](/Missions_to_Mars/Final_App_Screenshot.PNG)
