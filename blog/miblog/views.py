from django.shortcuts import render

# Create your views here.
#views based on functions (for now)
def index(request):
    return render(request, 'miblog/index.html')