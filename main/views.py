from django.shortcuts import render
from .models import *
def index_view(request):
    word= request.GET.get('word')
    correct=None
    incorrects=None
    message=None

    if word is not None:

        if 'x' not in word.lower() and 'h' not in word.lower():
            message='Soz tarkibida Xx yoki Hh mavjud emas'


        corrects=Correct.objects.filter(word=word)
        if corrects.exists():
            correct=corrects.first()
            incorrects=correct.incorrect_set.all()
        else:
            incorrects=InCorrect.objects.filter(word=word)
            if incorrects.exists():
                correct=incorrects.first().correct
                incorrects=correct.incorrect_set.all()
            else:
                message="Bunday soz mavjud emas"
    context={
        'correct':correct,
        'incorrects':incorrects,
        'message':message
    }
    return render(request,'index.html',context)
