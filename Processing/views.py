from django.shortcuts import render
import pickle
import sklearn
import pandas as pd
from pathlib import Path


# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent


# Passes the homepage
def userpannel(request):
    return render(request, "index.html",{"Rank":""})


#calculate the rank from the predicted values
def getrank(request):
    other_country_list = ['Portugal','Greece','Hong Kong','Norway','New Zealand','Hungary','Denmark','South Africa','Czech Republic','Russia','Saudi Arabia','Egypt','Chile','Argentina','Thailand','Malaysia','Singapore','Colombia','Mexico','Slovenia','Romania','Lebanon','Croatia','Estonia','Slovak Republic','Iceland','Serbia','Bulgaria','Lithuania','Uganda','United Arab Emirates','Uruguay','Cyprus','Puerto Rico']
    Institute_name = request.GET["Institute_name"]
    Country = request.GET["Country"]
    if Country in other_country_list:
        Country = "Other"
    # values from the created model
    country_map_dic = {'USA': 0, 'China': 1,'Japan': 2,'United Kingdom': 3, 'Germany': 4,'France': 5,'Italy': 6,'Spain': 7,
                       'Canada': 8,'South Korea': 9,'Australia': 10,'Taiwan': 11,'Brazil': 12,'India': 13,'Netherlands': 14,
                       'Switzerland': 15,'Sweden': 16,'Austria': 17,'Israel': 18,'Finland': 19,'Turkey': 20,'Belgium': 21,
                       'Poland': 22,'Iran': 23,'Ireland': 24,'Other': 25}
    Country = country_map_dic[Country]
    National_rank = request.GET["National_rank"]
    Edu_quality = request.GET["Edu_quality"]
    Alumni = request.GET["Alumni"]
    Faculty = request.GET["Faculty"]
    Publication = request.GET["Publication"]
    Influence = request.GET["Influence"]
    citations = request.GET["citations"]
    broad_impact = request.GET["broad_impact"]
    if broad_impact == None:
        broad_impact = 496
    patents = request.GET["patents"]
    score = request.GET["score"]
    year = request.GET["year"]

    df = pd.DataFrame([{'country': Country,'national_rank': National_rank,
                       'quality_of_education': Edu_quality, 'alumni_employment': Alumni,
                        'quality_of_faculty': Faculty, 'publications': Publication, 'influence': Influence,
                        'citations': citations, 'broad_impact': broad_impact, 'patents': patents,
                        'score': score, 'year': year}])

    norm = pickle.load(open(BASE_DIR/r'sav_files/normalize.sav', 'rb'))
    df_norm = norm.transform(df)

    model = pickle.load(open(BASE_DIR/r'sav_files/finalized_model.sav', 'rb'))
    prediction = model.predict(df_norm)
    prediction = prediction[0].round()

    return render(request, "index.html", {"Rank": prediction, "Name": Institute_name})


#the reference data file
def data(request):
    #Ref_data = pd.read_csv(){"CSVFile": r'static\data.csv'}
    return render(request,'Reference_Data.html')

