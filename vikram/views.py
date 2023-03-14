from django.shortcuts import render

# Create your views here.
def vikram(request):
    d={'movie_name':'VIKRAM','hero_name':'KAMALHASAN'}
    return render(request,'multiverse.html',context=d)
