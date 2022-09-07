#IMPORTING LIBRARIES

from cgitb import text
from typing import AnyStr
from unicodedata import name
from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv
import pandas as pd
###----BOLLYWOOD----###

#MAKING VARIABLES AS LIST

movie_name_bw = []
movie_year_bw = []
movie_rating_bw = []
movie_time_bw = []
movie_genre_bw =[]
movie_metascore_bw =[]
movie_votes_bw = []




#COLLECT MOVIE NAMES

for page in (1,3,1):
    #GETTING RESPONSE FROM THE WEBSITE AND STORING THE RESPONSE IN THE GIVEN VARIABLE

    html_bw=requests.get('https://www.imdb.com/list/ls056464416/?st_dt=&mode=detail&page='+str(page)+'&sort=user_rating,desc')

    #RAISE STATUS FOR ANY ISSUES WITH THE WEBSITE

    html_bw.raise_for_status()

    #STORING THE HTML RESPONSE IN TEXT FORMAT IN THE GIVEN VARIABLE
    
    soup_bw=BeautifulSoup(html_bw.text,'lxml')

    movie_data_bw=soup_bw.findAll('div',attrs={'class':'lister-item mode-detail'})

    for store in movie_data_bw:
        
        movie_name_bollywood=store.h3.a.text 
        movie_name_bw.append(movie_name_bollywood)

        movie_year_bollywood=store.h3.find('span',attrs={'lister-item-year text-muted unbold'}).text.replace('(',"").replace(')',"")
        movie_year_bw.append(movie_year_bollywood)

        movie_rating1_bollywood=store.find('span',attrs={'ipl-rating-star__rating'})
        
        movie_rating_bw.append(movie_rating1_bollywood)
        # if len(movie_rating1_bollywood) is None :
        #     movie_rating1_bollywood='null'
        # movie_rating_bw.append(movie_rating1_bollywood)

        movie_time_bollywood=store.find('span',attrs={'runtime'}).text.replace('min','')
        movie_time_bw.append(movie_time_bollywood)
        
        movie_genre_bollywood=store.find('span',attrs={'genre'}).text.replace(' ','')
        movie_genre_bw.append(movie_genre_bollywood)
        

        movie_metascore_bollywood=store.find('div',attrs={'inline-block ratings-metascore'}).span.text  if store.find('span',class_='metascore') else 'null'
        movie_metascore_bw.append(movie_metascore_bollywood)

        movie_votes_bollywood=store.find('span',attrs={'name':'nv'}).text.replace(',','')

        movie_votes_bw.append(movie_votes_bollywood)
    
    

    movie_rating_bw = ['' if i is None else i for i in movie_rating_bw]

movies_bollywood=pd.DataFrame({"Movie Name":movie_name_bw, 
"Movie Release Year":movie_year_bw,
"Movie IMDB Rating":movie_rating_bw,
"Movies Runtime":movie_time_bw,
"Movie Genre":movie_genre_bw,
"Movie Votes":movie_votes_bw,
"Movie Metascore":movie_metascore_bw})


print(movies_bollywood)



    



