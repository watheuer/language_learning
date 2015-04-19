from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from models import Document, Word, VocabList


def index(request):
    documents = Document.objects.all()
    lists = VocabList.objects.filter(user=request.user)

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