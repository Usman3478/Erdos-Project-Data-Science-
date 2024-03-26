import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
import tqdm
import requests
from bs4 import BeautifulSoup


#Importing data 
data = pd.read_csv('Movie data.csv')

#Look at the data 
data.head()

data.columns()

#We are trying to fetch the data such as "production company" from imdb api.

# Function to get the data from imdb api
!pip install imdbpy
from imdb import IMDb

#Function:
def get_production_company(movie_title):
    try:
        movies = ia.search_movie(movie_title)
        if movies:
            movie = movies[0]
            ia.update(movie)
            companies = movie.get('production companies')
            if isinstance(companies, list):
                return [company.get('name') for company in companies]
            elif isinstance(companies, str):
                return [companies]
            else:
                return None
        else:
            return None
    except Exception as e:
        return None
        
#The above function will return production company for a given movie title, given that it exists in the IMDb website

#Now, we can use the function for our data
from tqdm import tqdm
data['companies'] = data['production_companies'] # generate a new column to compare with the old production companies
for index, row in tqdm(data.iterrows(),total=len(data)):
    if pd.isnull(row['companies']):
        data.at[index,'companies'] = get_production_company(row['title'])




