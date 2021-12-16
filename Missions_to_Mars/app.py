from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Create the database
db = client.mars_db
mars = db.mars_collection

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    scrape_data = mars.find()

    # Return template and data
    return render_template("index.html", html_data=scrape_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape_app():
    # Drop the previous database
    mars.drop()
    
    # Run the scrape function
    results = scrape_mars.scrape()

    # Insert the results in the database
    mars.insert_one(results)
    print(results)
    
    # Redirect back to home page
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)
