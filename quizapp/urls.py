from django.urls import path

from .views import question, qiuz, result_list, quiz_type_create, logout_quiz, login_quiz, sign_up

urlpatterns = [
    path('', qiuz, name='qiuz'),
    path('quiz/<int:pk>/', question, name='quistion'),
    path('results/', result_list, name='results'),
    path('quiz_type_create/', quiz_type_create, name='quiz_type_create'),
    path('signup/', sign_up, name='signup'),
    path('logout/', logout_quiz, name='logout'),
    path('login/', login_quiz, name='login')
]
