from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):

    return render(request, 'home.html', {})

def count(request):
    fulltext = request.GET['fulltext']
    nbr_of_words = fulltext.split()
    word_freq={}
    for i in nbr_of_words:
        if i in word_freq:
            word_freq[i]+=1
        else:
            word_freq[i]=1

    sorted_words=sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
    context ={'fulltext': fulltext,
              'nbrOfWord': len(nbr_of_words),
              'wordFreq': word_freq,
              'sortedWords': sorted_words
            }

    return render(request, 'count.html', context)

