from django.shortcuts import render

from .models import QuestionModel,AnswerModel
# Create your views here.


def questions(request):
    Question=QuestionModel.objects.all()
    return render(request,'question.html',{'question':Question})