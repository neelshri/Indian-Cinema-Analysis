# IndianCinemaAnalysis
To analyse the different film industry within the indian cinema.

Under this project I am using websctaping libraries
Such as bs4/BeautifulSoup and request to scrape IMDB website.

I have written this bollywood.py file using the VS code editor as it felt easier and later I moved to conda/Jupyter notebooks.
Later I have written similar but not exactly the same code to extract data for different indian cinemas.

The data is being collected for 7 different film industries within the Indian cinema.
1. Bollywood-  Mumbai based hindi film industry
2. Pollywood- Punjabi  film industry
3. Chollywood- Chattisgarhi  film industry
4. Tollywood- Telgu  film industry
5. Kollywood- Tamil  film industry
6. Ollywood- Odiya  film industry
7. Dhollywood- Gujrati film industry

Now, the data was started to get collected however, the format was not the one relevant for analysis
hence, I wrote some different set of lopps and blocks to fix that to get that data upon which the analysis can be worked.

An unclean xlsx file was generated with the help of the python script I wrote. The name of this unclean file is 
"Indian Cinema.xlsx"

Now with the help of a tool Alteryx(attached 2 sample images from the several workflows of the data) I cleaned most of the data 
for irregularities and duplicate records and then the results were fed into a new xlsx file i.e. "Cleaned_Indian_cinema.xlsx"

Now, moving back to analysis using python. 

Use the data visualization libraries to showcase the results
via charts and graph.

Also, saved the data scraped in to the My Sql data base to be later represented using Tableau
