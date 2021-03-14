# Importing Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time as tm
import pandas as pd

# Function for Excel File
def city_data():
    # Reading in File
    filePath = "../Data/ca_sites.csv"
    f = pd.read_csv(filePath)
    # Creating DataFrame
    dfCASites = pd.DataFrame(f)
    
    # Rename Column
    dfCASites = dfCASites.rename(columns = {'City Name': 'City'}) 
    # Drop Duplicates
    dfCASites = dfCASites.drop_duplicates(subset=['City'])

    city = dfCASites['City'].tolist()
    
    return city 

# Function for Browser
def init_browser():
    # Setting Up Splinter
    executable_path = {'executable_path': "C:/Windows/chromedriver"}
    return Browser('chrome', **executable_path, headless=False)

def scrape_info():
    # Calling init_browser Function
    browser = init_browser()
    
    # Calling city_list Function
    city_list = city_data()
    
    # Creating List of Current AQI Data
    currentAQI = []
    
    baseUrl = 'https://www.airnow.gov/?'
    state = 'CA'
    country = 'USA'
    
    for city in city_list:
        # Building URL Query
        url_air_now = baseUrl + 'city=' + city + '&state=' + state + '&country=' + country

        # Visiting URL 
        browser.visit(url_air_now)
        # Visiting the URL Takes Some Time, Using the Time Module to Slow Down the Run
        tm.sleep(1)

        # Scrape page into Soup
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        
        
        try:
            # Scraping Date & Time
            aqUpdateTime = soup.find('span', class_='aq-updated-time')
            currentDateTime = aqUpdateTime.text
            currentTime = currentDateTime.rsplit('PST')[0] + 'PST'
            currentDate = currentDateTime.rsplit('PST')[1]

            # Scraping Current Pollutant
            aqiItem = soup.find('div', class_='aqi')
            aqi = aqiItem.find('b').text
            pollutantItem = soup.find('div', class_='pollutant')
            pollutant = pollutantItem.find('b').text

            # Appending Dictionary to List
            currentAQI.append({"City": city, "Time": currentTime, "Date": currentDate,
                              "Current AQI Value": aqi, "Current Pollutant": pollutant})
        except IndexError:
            next
            
    # Closing Browser
    browser.quit()
  
    # Creating DataFrame of currentAQI
    dfAQI = pd.DataFrame(currentAQI)
    # Removing White Space at the End of City Column
    dfAQI['City'] = dfAQI['City'].str.strip()
    
    # Reading in ca-sites File
    filePath = "../Data/ca_sites.csv"
    f = pd.read_csv(filePath)
    # Creating DataFrame
    dfCASites = pd.DataFrame(f)
    # Renaming Column to Help with Merge
    dfCASites = dfCASites.rename(columns = {'City Name': 'City'}) 
    # Dropping Duplicates
    dfCASites = dfCASites.drop_duplicates(subset=['City'])
    
    # Merging DataFrames
    dfMerge = pd.merge(dfCASites, dfAQI, how='left', on='City')
    # Dropping NaN
    dfMerge = dfMerge.dropna()
    
    # Renaming Column Headers
    dfMerge = dfMerge.rename(columns={"Defining Site" : "DefiningSite", "Land Use" : "LandUse",
                                      "Location Setting" : "LocationSetting", "State Name": "StateName", 
                                      "County Name" : "CountyName", "County Code" : "CountyCode",
                                     "CBSA Name" : "CBSAName", "Current AQI Value" : "CurrentAQIValue",
                                     "Current Pollutant" : "CurrentPollutant"})
    
    # Creating New CSV
    dfMerge.to_csv('../Data/currentAQIData.csv')

# We want the scrape_info() to Update Every Hour
# Use tm.sleep(3600) to achieve this
# This will continue to run as long as the Server is Open
def sleeper():
    scrape_info()
while True:
  sleeper()
  tm.sleep(3600)

