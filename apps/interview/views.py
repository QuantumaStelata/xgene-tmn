from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View
from apps.main.models import ClanInfo
from .models import Question, Answer
# Create your views here.

class Interview(View):
    def get(self, request, *args, **kwargs):
        clan = ClanInfo.objects.get()
        questions = Question.objects.filter(users=request.user.profile.play, publicate=True).prefetch_related()

        all_answers_count = {}
        for question in questions:
            all_answers_count[question.id] = 0
            for answer in question.answers.all():
                all_answers_count[question.id] += answer.users.count()

        return render(request, 'interview/interview.html', {'clan': clan, 'questions': questions, 'all_answers_count': all_answers_count})

    def post(self, request, *args, **kwargs):
        clan = ClanInfo.objects.get()
        for id in request.POST.getlist('answer'):
            answer = Answer.objects.get(id=id)
            question = Question.objects.get(answers=answer)
            answer.users.add(request.user.profile.play)
            question.users.remove(request.user.profile.play)
            answer.save()
            question.save()
        
        return HttpResponseRedirect('/interview')
