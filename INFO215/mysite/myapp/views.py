
import random
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    quotes = ['The greatest glory in living lies not in never falling, but inrising every time we fall. - Nelson Mandela', 'The way to get started is to quit talking and begin doing. -Walt Disney',
                    'If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt',
                                         'If you set your goals ridiculously high and it\'s a failure, you will fail above everyone else \'s success. -James Cameron']
    quote = random.choice(quotes)
    context = {
        'quote': quote
    }
    return render(request, 'blog_list.html', context)
