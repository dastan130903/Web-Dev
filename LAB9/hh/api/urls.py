from django.urls import path
from .views import (
    CompanyListCreateView,
    CompanyDetailView,
    CompanyVacanciesView,
    VacancyListCreateView,
    VacancyDetailView,
    vacancies_top_ten
)

urlpatterns = [
    # /api/companies
    path('companies/', CompanyListCreateView.as_view(), name='company-list'),
    # /api/companies/<int:id>/
    path('companies/<int:id>/', CompanyDetailView.as_view(), name='company-detail'),
    # /api/companies/<int:id>/vacancies/
    path('companies/<int:id>/vacancies/', CompanyVacanciesView.as_view(), name='company-vacancies'),

    # /api/vacancies/
    path('vacancies/', VacancyListCreateView.as_view(), name='vacancy-list'),
    # /api/vacancies/<int:id>/
    path('vacancies/<int:id>/', VacancyDetailView.as_view(), name='vacancy-detail'),

    # /api/vacancies/top_ten/
    path('vacancies/top_ten/', vacancies_top_ten, name='vacancies-top-ten'),
]
