from pymongo import MongoClient
from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    # Get the username and password from the request
    username = request.POST.get('username', 'default')
    password = request.POST.get('password', 'default')

    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['textutils']  # Replace 'your_database_name' with your actual database name
    collection = db['username_and_passeords']

    # Insert the username and password into MongoDB
    user_data = {'username': username, 'password': password}
    collection.insert_one(user_data)

    # Render a template after processing
    return render(request, 'removepunc.html')

def home(request):
    # Render the home page template
    return render(request, 'index.html')

def finalOutput(request):
    # Your existing code for text processing
    doit = request.GET.get('removePunctuations', 'Error')
    doit2 = request.GET.get('removeExtraLines', 'Error')
    doit3 = request.GET.get('upperCase', 'Error')
    sentence = request.GET.get('sentence', 'Error')
    print(sentence)

    
    if doit3 == 'on':
        # Code to convert sentence to uppercase
        finalOutput = ""
        for char in sentence:
            finalOutput += char.upper()
        params = {'sentsentence': finalOutput}
        sentence = finalOutput

    if doit2 == 'on':
        # Code to remove extra lines
        sentence_without_extraLines = ""
        for char in sentence:
            if char != '\n' and char!= '\r':
                sentence_without_extraLines += char
            else:
                print("not possible")
        
        params = {'sentsentence': sentence_without_extraLines}
        sentence = sentence_without_extraLines

    if doit == 'on':
        # Code to remove punctuations
        puntuations = ['<', '>', '.', ',', '?', '!', ':', ';', "'", '"', '(', ')', '[', ']', '{', '}', '...', '-', '/', '&', '*']
        sentence_without_punctuations = ""
        for char in sentence:
            if char not in puntuations:
                sentence_without_punctuations += char
        params = {'sentsentence': sentence_without_punctuations}
        sentence =sentence_without_punctuations 
    if doit != 'on' and doit3 != 'on' and doit2 != 'on' :
        return HttpResponse("ERROR!!!SELECT SOMETHING LAUDE")

   
    return render(request, 'result.html', params)