from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_user(request):
    print(request.POST)
    return redirect('/info')

def show_info(request):
    name = (request.POST['name'])
    location = (request.POST['location'])
    language = (request.POST['language'])
    comment = (request.POST['comment'])
    context = {
        'name' : name,
        'location' : location,
        'language' : language,
        'comment' : comment 
    }
    return render(request, 'info.html', context)