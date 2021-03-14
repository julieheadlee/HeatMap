// Create our map, start with the center of the US.  Show US zoom level.
var myMap = L.map("map-id", {
    timeDimensionControl: true,
    timeDimensionControlOptions: {
        timeSliderDragUpdate: true,
        loopButton: true,
        autoPlay: true,
        playerOptions: {
            transitionTime: 1000,
            loop: true
        }
    },
    timeDimension: true,
    timeDimensionOptions: {
        timeInterval: "2010-01-01/2020-09-30",
        period: "P1M"  //1 month intervals -- data will be averaged for each month
    },
    center: [36.7378, -119.7871],
    zoom: 6
  });
  
  // Adding a tile layer (the background map image) to our map
  // We use the addTo method to add objects to our map
  L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
  }).addTo(myMap);

// get the data to create the historical data
