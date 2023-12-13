from django.shortcuts import render

# Create your views here.
def home(request):
    # dictionary form ah backend teka data nia aste hoy
    d = {'author':"arif","age":20,'List':['python','programming','language'] }
    return render(request,'home.html',{'data':d})