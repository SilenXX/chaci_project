from django.shortcuts import render
from django.http import HttpResponse

from .models import Word
# Create your views here.
def index(request):
    all_word_list = Word.objects.order_by('-word_num')
    context = {'all_word_list': all_word_list}
    return render(request, 'record/index.html', context)

def add(request):
    add_word = request.GET['word']
    try:
        result = Word.objects.get(word_text=add_word)
        result.word_num = result.word_num + 1
        result.save()
        return HttpResponse("existed!")
    except:
        result = Word(word_text=add_word, word_num=1)
        result.save()
        return HttpResponse("created!")