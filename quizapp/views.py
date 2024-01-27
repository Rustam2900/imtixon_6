# from random import shuffle, sample
#
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model
# from django.shortcuts import render
# from django.core.cache import cache
#
# from .models import Question, Result, QuizType
# from .utils import check_answer
#
# User = get_user_model()
#
#
# def qiuz(request):
#     quizs = QuizType.objects.all()
#     context = {
#         'quizs': quizs
#     }
#     return render(request, 'home.html', context)
#
#
# @login_required(login_url='login')
# def question(request, pk):
#     questions = Question.objects.filter(quiz_id=pk)
#     if questions.count() > 5:
#         questions = sample(list(questions), 5)
#     else:
#         questions = sample(list(questions), questions.count())
#     if request.method == "POST":
#         context = check_answer(request)
#         cache.delete('questions')
#         return render(request, 'quizapp/result.html', context)
#
#     if not cache.get('questions'):
#         cache.set('questions', questions, timeout=360)
#     questions = cache.get('questions')
#     context = {
#         'questions': questions,
#     }
#     return render(request, 'quizapp/question.html', context)
#
#
# def result_list(request):
#     results = Result.objects.all()
#     context = {
#         'results': results
#     }
#     return render(request, 'quizapp/result_list.html', context)
#
#
from random import shuffle, sample


from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect

from django.core.cache import cache
from django_filters.views import FilterView
from .forms import QuizTypeForm
from .filters import UserFilter, ResultFilter

from .forms import SignUP
from .models import Question, Result, QuizType
from .utils import check_answer
from .mixins import Base
User = get_user_model()



class BlogListView(Base, FilterView):
    model = Result
    template_name = 'result_list.html'
    filterset_class = ResultFilter
def quiz_type_create(request):
    form = QuizTypeForm()
    context = {
        "form": form
    }
    return render(request, 'quizapp/quiz_type_create.html', context)


# def get_queryset(self):
#     qr = super().get_queryset()
#     search = self.request.GET.get('search')
#     if search is not None:
#         return qr.filter(first_name__icontains=search, last_name__icontains=search, score_min__icontains=search,
#                          score_max__icontains=search)
#     return qr




def qiuz(request):
    quizs = QuizType.objects.all()
    context = {
        'quizs': quizs
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def question(request, pk):
    questions = Question.objects.filter(quiz_id=pk)
    if questions.count() > 5:
        questions = sample(list(questions), 5)
    else:
        questions = sample(list(questions), questions.count())
    if request.method == "POST":
        context = check_answer(request)
        cache.delete('questions')
        return render(request, 'quizapp/result.html', context)

    if not cache.get('questions'):
        cache.set('questions', questions, timeout=360)
    questions = cache.get('questions')
    context = {
        'questions': questions,
    }
    return render(request, 'quizapp/question.html', context)


def result_list(request):
    results = Result.objects.all()
    context = {
        'results': results
    }
    return render(request, 'quizapp/result_list.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = SignUP(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are registered')
            return redirect('quizapp:login')
        messages.warning(request, 'Please retry again')
    form = SignUP()
    context = {
        'form': form
    }

    return render(request, 'registration/signup.html', context)


def login_quiz(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        last_login = request.POST.get('last_login')
        is_superuser = request.POST.get('is_superuser')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        date_joined = request.POST.get('date_joined')
        first_name = request.POST.get('first_name')
        user = authenticate(request, username=username, password=password, last_login=last_login,
                            is_superuser=is_superuser,
                            last_name=last_name, email=email, date_joined=date_joined, first_name=first_name)
        if not user:
            messages.error(request, 'User not found')
            return render(request, 'registration/login.html')
        login(request, user)
        messages.info(request, 'Login successfully')
        return redirect('quizapp:qiuz')

    return render(request, 'registration/login.html')


def logout_quiz(request):
    logout(request)
    messages.success(request, 'Log out successfully')
    return redirect('quizapp:login')