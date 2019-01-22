from django.http import HttpResponse
from django.shortcuts import render
import operator
from collections import Counter


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    counter = Counter(wordlist)
    len(counter) #=> 7
    counter["world"] #=> 2

    print(type(counter))


    return render(request, 'count.html', {'fulltext': fulltext,'count': len(wordlist),'sortedwords': sortedwords,'counter':counter})


def about(request):
    return render(request, 'about.html')