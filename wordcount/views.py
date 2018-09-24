from django.http import HttpResponse
from django.shortcuts import render
import operator

#def home(request):
#    return render(request, 'home.html',{'hithere':'this is me'})

def home(request):
    return render(request,'home.html')

#def eggs(request):
   # return HttpResponse('<h1>Eggs are given free today</h1>')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split() #converts the full text into list.

    worddictionary = {}


    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1

        else:
            #add to the dictionary
            worddictionary[word] = 1



    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'wd':worddictionary.items()})


def youtube(request):
    return render(request,'youtube.html')