# Air_Quality_Analysis
Tell your story web visualization Project 2

## **Inspiration:**
>- Analyze Air Quality in California by county & compare to demographic information from the Census data. Information can be useful for businesses to make saftey decisions on outdoor working employee's health.

## **Team members:** *(Git Hub user name)*
>- **Julia Headlee**  [Git Hub: julieheadlee](https://github.com/julieheadlee)
>- **Melanie Nolker** [Git Hub: mnolker](https://github.com/mnolker)
>- **Alicia Perez** [Git Hub: AliciaAPerez](https://github.com/AliciaAPerez)
>- **Kayla St. Germain** [Git Hub: KStG1992](https://github.com/KStG1992)

## **Data sets:**
>- Air Quality current: https://docs.airnowapi.org/HistoricalObservationsByLatLon/docs
>>- scrape current data for visualization of current air quality
>- Air Quality historical data: https://aqs.epa.gov/aqsweb/airdata/download_files.html
>>- csv to database (cleanse using pandas); Use Python flask route to pass data from PostgressSQL database
>- US Census:  
    * by county: https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html 
    * by city: https://www.census.gov/data/datasets/time-series/demo/popest/2010s-total-cities-and-towns.html
>>- Use Python flask route to pass data from PostgressSQL database

## **Visuals:**
>- Topical graph with heatmap of Air Quality
>- Add layer to map to include demographic data
>- make interactive graph by picking date / county
>- Interactive map of air quality over time D3 folium JS library ? https://python-visualization.github.io/folium/
