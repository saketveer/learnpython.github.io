from django.shortcuts import render
from course.models import Student


# Create your views here.


def home(request):
    return render(request, 'home.html', {'title': 'Home Page'})  # the page getting from gs15 templates


def pagetwo(request):
    return render(request, 'page2.html', {'title': 'Page2'})  # the page getting from gs15 templates


def result(request):
    return render(request, 'result.html', {'title': 'Result'})


def studentinfo(request):
    global i
    stud = Student.objects.all()

    for i in stud:   # for self test only
     print(i.stuid, i.stuname, i.stuemail, i.stupass)  # for self test only

    return render(request, 'student.html', {'stu': stud})


def pythonintroduction(request):
    return render(request, 'pythonintroduction.html', {'title': 'Python Introduction'})

def pythongettingstarted(request):
    return render(request, 'pythongettingstarted.html', {'title': 'Python Getting Started'})

def pythonsyntax(request):
    return render(request, 'pythonsyntax.html', {'title': 'Python Syntax'})

def pythonvariable(request):
    return render(request, 'pythonvariable.html', {'title': 'Python Variable'})

def pythondatatype(request):
    return render(request, 'pythondatatype.html', {'title': 'Python Data Types'})

def pythonnumbers(request):
    return render(request, 'pythonnumbers.html', {'title': 'Python Numbers'})

def pythoncasting(request):
    return render(request, 'pythoncasting.html', {'title': 'Python Casting'})

def pythonoperators(request):
    return render(request, 'pythonoperators.html', {'title': 'Python Operators'})

def pythonlists(request):
    return render(request, 'pythonlists.html', {'title': 'Python Lists'})

def pythontuples(request):
    return render(request, 'pythontuples.html', {'title': 'Python Tuples'})

def pythonsets(request):
    return render(request, 'pythonsets.html', {'title': 'Python Sets'})

def pythondictionary(request):
    return render(request, 'pythondictionary.html', {'title': 'Python Dictionary'})

def pythonarray(request):
    return render(request, 'pythonarray.html', {'title': 'Python Array'})

def pythonuserinput(request):
    return render(request, 'pythonuserinput.html', {'title': 'Python User Input'})

def pythonifelse(request):
    return render(request, 'pythonifelse.html', {'title': 'Python If..else'})

def pythonwhileloops(request):
    return render(request, 'pythonwhileloops.html', {'title': 'Python While Loops'})

def pythonforloops(request):
    return render(request, 'pythonforloops.html', {'title': 'Python For Loops'})

def pythonfunctions(request):
    return render(request, 'pythonfunctions.html', {'title': 'Python Functions'})

def pythonclassobjects(request):
    return render(request, 'pythonclassobjects.html', {'title': 'Python Class & Objects'})
