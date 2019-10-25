from django.http import HttpResponse
from django.shortcuts import render, redirect


def welcome(request):
    if request.user.is_authenticated:
        print(request.user)
        return redirect('player_home')
    else:
    # return HttpResponse("Hello World")
        return render(request, 'tictactoe/welcome.html')