from django_filters import FilterSet, CharFilter, NumberFilter
from django.contrib.auth import get_user_model
from django import forms
from quizapp.models import Result

User = get_user_model()



class ResultFilter(FilterSet):
    score_min = NumberFilter(field_name='total', lookup_expr=['gt', 'lt'],
                             label='Score', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Result
        fields = {
            'total': ['gt', 'lt'],
        }


class UserFilter(FilterSet):
    first_name = CharFilter(lookup_expr='icontains', label='first_name',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = CharFilter(lookup_expr='icontains', label='last_name',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains']
        }