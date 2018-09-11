from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Comment, CommentForm
import datetime

@csrf_exempt
def index(request):
    comments = Comment.objects.order_by('id')
    template = loader.get_template('openComment/index.html')
    comments = comments.reverse()
    context = {
        'comments': comments,
    }
    if(len(request.POST)!=0):
        x = datetime.datetime.now()
        print(request.POST)
        pref = request.POST.copy()
        pref['time'] = str(x.strftime("%c"))
        if pref['author'] == '': 
            pref['author'] = 'anon'
        if pref['comment'] == '': 
            pref['comment'] = 'nothing'

        cmm = CommentForm(pref)
        print(cmm)
        cmm.save()
    return HttpResponse(template.render(context, request))

# Create your views here.
