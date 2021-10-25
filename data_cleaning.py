import pandas as pd 


df = pd.read_csv('players_fifa22.csv')
# df.columns
df_interest = df[['FullName', 'Nationality', 'Club', 'WageEUR']]
# df_interest

# get list of top 20 best paid clubs (avg salary in EUR)
def t20_paid_clubs():
    highest_avg_pay = df_interest[['Club', 'WageEUR']].groupby(by = 'Club').mean().sort_values(by = 'WageEUR', ascending = False)
    highest_avg_pay.reset_index(inplace = True, drop = False)

    highest_avg_pay_list = highest_avg_pay.head(20)['Club'].tolist()
    return highest_avg_pay_list

# get list of players that play for the top 20 best paid clubs

def t20_players():
    df_players_interest = df_interest.loc[df_interest['Club'].isin(t20_paid_clubs())]
    df_players_interest.reset_index(inplace = True, drop = True)
    return df_players_interest

# t20_players()

# get unique countries in order from all teams

def countries_sort():
    sorted_countries = df_interest.Nationality.unique().tolist()
    #.tolist().sort()
    sorted_countries.sort()
    return sorted_countries

#print(countries_sort())



# update player nationality with country ISO 

