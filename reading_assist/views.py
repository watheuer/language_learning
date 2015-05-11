from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from models import Document, Word, VocabList
from definitions import definition
import json


def index(request):
    documents = Document.objects.all()
    user = User.objects.get(id=request.user.id)
    lists = VocabList.objects.filter(user=user)

    context = {
        'documents': documents,
        'lists': lists
    }

    return render(request, 'reading_assist/index.html', context)


def document(request, pk):
    document = get_object_or_404(Document, pk=pk)

    context = {
        'document': document
    }

    return render(request, 'reading_assist/read.html', context)


def vocab_list(request, pk):
    list = get_object_or_404(VocabList, pk=pk)

    context = {
        'list': list
    }

    return render(request, 'reading_assist/vocab.html', context)


def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')

        document = Document(title=title, body=body)
        document.save()

        return redirect('reading:index')

    return render(request, 'reading_assist/new.html', {})


# TODO: error checking
def get_definitions(request):
    word = request.GET.get('word')
    definitions = definition(word)
    response_data = {}

    new_word = Word(text=word)
    if len(definitions) >= 1:
        new_word.definition1 = definitions[0]
    if len(definitions) >= 2:
        new_word.definition2 = definitions[1]
    if len(definitions) >= 3:
        new_word.definition3 = definitions[2]
    new_word.save()

    for i in range(len(definitions)):
        response_data[i] = definitions[i]

    return HttpResponse(json.dumps(response_data), content_type='application/json')
