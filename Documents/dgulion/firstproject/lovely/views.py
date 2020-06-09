from django.shortcuts import render


def happy(request):
    return render(request, 'lovely/happy.html')


def no(request):
    return render(request, 'lovely/no.html')


def yes(request):
    return render(request, 'lovely/yes.html')


def yes2(request):
    return render(request, 'lovely/yes2.html')


def yes3(request):
    return render(request, 'lovely/yes3.html')


def yes4(request):
        return render(request, 'lovely/yes4.html')

def star(request):
            return render(request, 'lovely/star.html')

def two(request):
            return render(request, 'lovely/two.html')

def three(request):
            return render(request, 'lovely/three.html')


            
