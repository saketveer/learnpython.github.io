
from django.urls import path
from.import views


urlpatterns = [

    path('', views.home, name='home'),  # it is used to ope home page autometicaly.
    path('home', views.home, name='home'),  # it is used jum from other pages.
    path('pagetwo', views.pagetwo, name='pagetwo'),
    path('result', views.result, name='result'),

    path('stu/', views.studentinfo, name='studentinfo'),

    path('pythonintroduction', views.pythonintroduction, name='pythonintroduction'),
    path('pythongettingstarted', views.pythongettingstarted, name='pythongettingstarted'),
    path('pythonsyntax', views.pythonsyntax, name='pythonsyntax'),
    path('pythonvariable', views.pythonvariable, name='pythonvariable'),
    path('pythondatatype', views.pythondatatype, name='pythondatatype'),
    path('pythonnumbers', views.pythonnumbers, name='pythonnumbers'),
    path('pythoncasting', views.pythoncasting, name='pythoncasting'),
    path('pythonoperators', views.pythonoperators, name='pythonoperators'),
    path('pythonlists', views.pythonlists, name='pythonlists'),
    path('pythontuples', views.pythontuples, name='pythontuples'),
    path('pythonsets', views.pythonsets, name='pythonsets'),
    path('pythondictionary', views.pythondictionary, name='pythondictionary'),
    path('pythonarray', views.pythonarray, name='pythonarray'),
    path('pythonuserinput', views.pythonuserinput, name='pythonuserinput'),
    path('pythonifelse', views.pythonifelse, name='pythonifelse'),
    path('pythonwhileloops', views.pythonwhileloops, name='pythonwhileloops'),
    path('pythonforloops', views.pythonforloops, name='pythonforloops'),
    path('pythonfunctions', views.pythonfunctions, name='pythonfunctions'),
    path('pythonclassobjects', views.pythonclassobjects, name='pythonclassobjects'),






]