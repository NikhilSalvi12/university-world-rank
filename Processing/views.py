from django.shortcuts import render
import pickle
import sklearn
import pandas as pd


# Create your views here.

# Passes the homepage
def userpannel(request):
    return render(request, "index.html",{"Rank":""})


#calculate the rank from the predicted values
def getrank(request):
    Institute_name = request.GET["Institute_name"]
    Country = request.GET["Country"]
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

    df = pd.DataFrame([{'national_rank': National_rank,
                       'quality_of_education': Edu_quality, 'alumni_employment': Alumni,
                       'quality_of_faculty': Faculty, 'publications': Publication, 'influence': Influence,
                       'citations': citations, 'broad_impact': broad_impact, 'patents': patents,
                       'score': score, 'year': year}])

    norm = pickle.load(open(r'Universityrank\sav_files\normalize.sav', 'rb'))
    df_norm = norm.transform(df)

    model = pickle.load(open(r'Universityrank\sav_files\finalized_model.sav', 'rb'))
    prediction = model.predict(df_norm)
    prediction = prediction[0].round()

    return render(request, "index.html", {"Rank": prediction, "Name": Institute_name})


#the reference data file
def data(request):
    #Ref_data = pd.read_csv(){"CSVFile": r'static\data.csv'}
    return render(request,'Reference_Data.html')

