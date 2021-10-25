### Background
- FIFA22 is a popular video game where players can create a team of professional soccer players. Each professional soccer player 
is given attributes which describe his abilities. I wanted to practice creating a plotly-dash app to analyze the players.
- the data set can be found here: https://www.kaggle.com/cashncarry/fifa-22-complete-player-dataset


### Basic Goal/Demo
- Create a Choropleth Graph of the top 20 FIFA22 Clubs and their players from Plotly Dash
- When the user selects or types in a club into the drop down menu, the map displays which countries the club's players come from
  and their names


### What is a Choropleth graph?
- A Choropleth Map is a map composed of colored polygons. It is used to represent spatial variations of a quantity. 
- https://plotly.com/python/choropleth-maps/ for documentation


### Steps to Open App
- in command prompt or the console, type python3 app.py
- navigate to http://127.0.0.1:8050/

### Current Step in Project
![] (images/fc_barcelona.png?raw = True)

![] (images/manchester_city.png?raw = True)

### Additional Information
- data was intially cleaned using PySpark for PySpark Practice. The data for the app was wrangled using Pandas.


### Further Steps to Demo
- implement app for entire data set. Had questions about dash drop downs with accents and compatibility with standard English letters