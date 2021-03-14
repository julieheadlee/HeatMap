import os
import psycopg2
from flask import Flask
from flask import render_template_string
from flask import render_template
import csv
import pandas as pd
import folium
from folium.plugins import HeatMap
from folium.plugins import HeatMapWithTime

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
    # get the data
    histData = pd.read_csv(file)

    mapTime=pd.to_datetime(histData['Date'], format='%Y-%m-%d')

    mapData=histData[["Latitude", "Longitude", "AQI"]]
    # create the base map
    start_coords = (36.7378, -119.7871)
    folium_map = folium.Map(location=start_coords, zoom_start=6, tiles='Stamen Terrain')
    # mapData.write_csv("Data/mapdata.csv")
    #add the Heat Map from the data
    #HeatMap(data=mapData, radius=20).add_to(folium_map)
    HeatMapWithTime(data=mapData, index=mapTime, radius=20,scale_radius=True).add_to(folium_map)
 
    # display base map with HeatMap 
    return folium_map._repr_html_()    
    #return render_template("timelapse.html", map_id=folium_map._repr_html_())
    

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