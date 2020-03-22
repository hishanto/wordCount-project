from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    return render(request, 'home.html')

def count (request):
    posts = request.GET['fulltext']
    count = posts.split()
    dic = {}
    for word in count:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    return render(request, 'count.html',{ 'fulltext': posts, 'count':len(count), 'dic':dic})
