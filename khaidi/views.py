from django.shortcuts import render

# Create your views here.
def khaidi(request):
    d={'movie_name':'KHAIDI','hero_name':'KARTHIK'}
    return render(request,'multiverse.html',context=d)
