from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "notas/index.html")

def user_login(request):
    pass
