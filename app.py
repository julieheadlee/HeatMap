import os
import psycopg2
from flask import Flask
from flask import render_template_string
from flask import render_template
import csv
import pandas as pd
import folium
from folium.plugins import HeatMapWithTime
from flask import Markup

app = Flask(__name__)
# # Menu(app=app)


# # DATABASE_URL will contain the database connection string: HEROKU
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # Connects to the database using the app config
# # db = SQLAlchemy(app)

@app.route("/")
def timelapse():
    # use the csv for now to generate the map

    # session = Session(engine)
    # histData = session.query(airQuality.AQI, airQuality.Defining_Parameter, airQuality.Date ).\
    #     join(sites, airQuality.site_no == sites.site_no). \
    #     join(counties, counties.county_code == sites.County_Code). \
    #     filter(airQuality.Date >= '2010-01-01' and airQuality.Date <= '2020-10-31' and \
    #         airQuality.Defining_Parameter == 'PM2.5')
    file = "Data/all_data.csv"
    param = "Ozone"
    # get the data
    histData = pd.read_csv(file, parse_dates=['Date'])

    histData['year'] = (histData['Date'].dt.year)
    histData['month'] = (histData['Date'].dt.month)
    histData['day'] = 1
    histData['newDate'] = pd.to_datetime(histData[['year', 'month', 'day']])

    #Reorder columns
    columns = ['newDate', 'Latitude', 'Longitude', 'AQI', 'Defining_Parameter','county_name']
    reorderData = histData[columns]
    
    # Get only the data for the parameter
    paramData = reorderData.loc[reorderData['Defining_Parameter'] == param]

    sortedhistData = paramData.sort_values(by=['newDate'])

    newhistData = sortedhistData.reset_index()
    newhistData.drop(columns=['index'], inplace=True)

    mapData=newhistData[["newDate", "Latitude", "Longitude", "AQI", 'Defining_Parameter']]
    # Create list of lists, with the "key" of the list being the date, and the "value" being all measurements for that date.
    # 1. Need list of date
    mapTime = mapData["newDate"].sort_values().unique()


    # 2. create the lists
    mapData_list = []
    
    # Weight must be between 0 and 1.  Divide AQI by max value to get correct data
    minAQI = mapData["AQI"].min()
    maxAQI = mapData['AQI'].max()

    mapData["AQI_adj"] = mapData["AQI"]/maxAQI
    
    for date in mapTime:
        mapData_list.append(mapData.loc[mapData['newDate'] == date, ["Latitude", "Longitude", "AQI_adj"]].groupby(["Latitude", "Longitude"]).mean().reset_index().values.tolist())

    # create the base map
    start_coords = (36.7378, -119.7871)
    folium_map = folium.Map(location=start_coords, zoom_start=6, tiles='Stamen Terrain')

    #add the Heat Map from the data
    #HeatMap(data=mapData, radius=20).add_to(folium_map)
    HeatMapWithTime(data=mapData_list, index=mapTime, radius=20, auto_play=True, max_opacity=0.3,
                       gradient = {0.2: '#FBD973', 
                            0.4: '#fa782f', 
                            0.75: '#F16578', 
                            .9: '#782890'}).add_to(folium_map)

    # display base map with HeatMap 
    _ = folium_map._repr_html_()

    map_id = Markup(folium_map.get_root().html.render())
    hdr_txt = Markup(folium_map.get_root().header.render())
    script_txt = Markup(folium_map.get_root().script.render())

    return render_template(
        'timelapse.html',
        map_id = map_id,
        hdr_txt=hdr_txt,
        script_txt = script_txt,
        title="Timelapse Heat Map - January 2010 - October 2020"
    )
@app.route("/yearlyvpop")
def yearlyvpop():
    return render_template("yearlyvpop.html")




# @app.after_request
# def add_header(r):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     return r

# def tmpl_show_menu():
#     return render_template_string(
#         """
#         {%- for item in current_menu.children %}
#             {% if item.active %}*{% endif %}{{ item.text }}
#         {% endfor -%}
#         """)

# @app.route('/')
# @register_menu(app, '.', 'Home')
# def index():
#     return tmpl_show_menu()

# @app.route('/first')
# @register_menu(app, '.first', 'First', order=0)
# def first():
#     return tmpl_show_menu()

# @app.route('/second')
# @register_menu(app, '.second', 'Second', order=1)
# def second():
#     return tmpl_show_menu()

if __name__ == '__main__':
    app.run(debug=True)