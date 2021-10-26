import dash
from dash import dcc, html
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from helper_functions import t20_club_players_iso, t20_clubs
from data_cleaning import t20_paid_clubs


app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1('App to Display Player\'s Nationality by Selected Club from FIFA22', style = {'text-align': 'center'}),
    html.Div(['Please enter a team you\'re interested in from the Top 20 Soccer Clubs',
            dcc.Dropdown(id = 'select_team',
           options = t20_clubs,
           value = t20_paid_clubs()[0])
     ]),

    html.Div(id ='output_container', children = []),
    html.Br(),

    dcc.Graph(id = 't20_players_map', figure = {})
    
])

@app.callback(
    [Output(component_id = 'output_container', component_property = 'children'),
    Output(component_id = 't20_players_map', component_property = 'figure')],
    [Input(component_id = 'select_team', component_property = 'value')]
)
# call back function always refers to component_property 'value'
def update_options(search_value):
    
    #the container used here is just to print the below statement
    container = 'Hover over countries to see players!'

    dff = t20_club_players_iso.copy()
    dff = dff[dff['Club'] == search_value]


    # choropleth build
    fig = px.choropleth(
        data_frame = dff,
        locations = 'natl_iso',
        locationmode = 'ISO-3',
        scope = 'world',
        hover_name = 'Club',
        hover_data= ['FullName'],
        title = 'Where are {}\'s Players From?'.format(search_value),
        width= 1500,
        height= 700)
        #projection = 'mercator')
    

    # fig.update are additional options for customizing the fig
    # fig by itself is pretty barebones

    # shows country borders
    fig.update_geos(showcountries = True,
                    resolution = 50,
                    visible = False


    )
    # modifies layout of the country     
    fig.update_layout(title = dict(x = 0.5, xanchor = 'center'),
                        margin = dict(l=30, r=30, t=30, b=10))
        



    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)