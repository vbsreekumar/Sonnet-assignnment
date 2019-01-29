from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app import sonnet_helper as shelp
from first_app import sonnet_solution_one as one
from first_app import sonnet_solution_two as two

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def keyword(request):
    if request.method=='POST':
        s = request.POST['sn1']

        if s:
            results = one.sonnet_tag(int(s))
            return render(request, 'first_app/index.html', {'res1': results})
        else:
            return HttpResponseRedirect('/index/')

    return render(request, 'first_app/index.html')

def recommend(request):
    if request.method == 'POST':
        s = request.POST['sn2']

        if s:
            results = two.sonnet_recommend(2, int(s))
            return render(request, 'first_app/index.html', {'res2': results})
        else:
            return HttpResponseRedirect('/keyword/')

    return render(request, 'first_app/index.html')


def relate(request):
    if request.method == 'POST':
        s = request.POST['sn3']

        if s:
            results = two.sonnet_recommend(1, int(s))
            return render(request, 'first_app/index.html', {'res3': results})
        else:
            return HttpResponseRedirect('/keyword/')

    return render(request, 'first_app/index.html')

def display(request):
        i = request.GET['i']
        if not i:
            return render(request, 'first_app/display.html')
        else:
            return HttpResponse(shelp.get_sonnet(int(i)))
