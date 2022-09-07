
#IMPORTING LIBRARIES

from cgitb import text
from typing import AnyStr
from unicodedata import name
from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv

###----POLLYWOOD----###

#MAKING VARIABLES AS LIST

movie_name_pw = []
movie_year_pw = []
movie_rating_pw = []
movie_time_pw = []
movie_genre_pw =[]
movie_metascore_pw =[]
movie_votes_pw = []




#COLLECT MOVIE NAMES

for page in (1,2,1):
    #GETTING RESPONSE FROM THE WEBSITE AND STORING THE RESPONSE IN THE GIVEN VARIABLE

    html_pw=requests.get('https://www.imdb.com/list/ls023440410/?st_dt=&mode=detail&page='+str(page)+'&sort=user_rating,desc')

    #RAISE STATUS FOR ANY ISSUES WITH THE WEBSITE

    html_pw.raise_for_status()

    #STORING THE HTML RESPONSE IN TEXT FORMAT IN THE GIVEN VARIABLE
    
    soup_pw=BeautifulSoup(html_pw.text,'lxml')

    movie_data_pw=soup_pw.findAll('div',attrs={'class':'lister-item mode-detail'})

    for store in movie_data_pw:
        
        movie_name_pollywood=store.h3.a.text 
        movie_name_pw.append(movie_name_pollywood)

        movie_year_pollywood=store.h3.find('span',attrs={'lister-item-year text-muted unbold'}).text.replace('(',"").replace(')',"")
        movie_year_pw.append(movie_year_pollywood)

        movie_rating1_pollywood=store.find('span',attrs={'ipl-rating-star__rating'})
        
        movie_rating_pw.append(movie_rating1_pollywood)
        # if len(movie_rating1_bollywood) is None :
        #     movie_rating1_bollywood='null'
        # movie_rating_bw.append(movie_rating1_bollywood)

        movie_time_pollywood=store.find('span',attrs={'class':'runtime'}).text.replace('min','') if store.find('span',class_='runtime') else 'null'
        movie_time_pw.append(movie_time_pollywood)
        
        movie_genre_pollywood=store.find('span',attrs={'genre'}).text.replace(' ','')
        movie_genre_pw.append(movie_genre_pollywood)
        

        movie_metascore_pollywood=store.find('div',attrs={'inline-block ratings-metascore'}).span.text  if store.find('span',class_='metascore') else 'null'
        movie_metascore_pw.append(movie_metascore_pollywood)

        movie_votes_pollywood=store.find('span',attrs={'name':'nv'}).text.replace(',','')

        movie_votes_pw.append(movie_votes_pollywood)
    
    

    movie_rating_pw = ['' if i is None else i for i in movie_rating_pw]

movies_pollywood=pd.DataFrame({"PW Movie Name":movie_name_pw, 
"PW Movie Release Year":movie_year_pw,
"PW Movie IMDB Rating":movie_rating_pw,
"PW Movies Runtime":movie_time_pw,
"PW Movie Genre":movie_genre_pw,
"PW Movie Votes":movie_votes_pw})

print(movies_pollywood)


   
#print(movies_pollywood['Movie IMDB Rating'])


    



