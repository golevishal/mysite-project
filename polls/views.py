# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.template import loader


def index(request):
	return HttpResponse("Hello world!! You are at the polls index.")


def detail(request, question_id):
	latest_questions = Question.objects.order_by('-pub_date')
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_questions,
	}
	return HttpResponse(template.render(context, request))


def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
