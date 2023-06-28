from django.http import HttpResponse
from django.shortcuts import render, redirect

from ormapp1.models import Game


# Create your views here.
def index_fun(request):
    return render(request, 'insertgame.html', {'msg': False})


def insert_fun(request):
    g1 = Game()
    g1.Game_Name= request.POST['game-name']
    g1.Game_type = request.POST['ddl-game-type']
    g1.Player_name = request.POST['player-name']
    g1.Player_age = request.POST['player-age']
    g1.Player_city = request.POST['player-city']
    g1.save()


    return render(request, 'insertgame.html', {'msg': True})


#Get the game table data using game model
def display_fun(request):
    data = Game.objects.all()

    return render(request, 'displaygame.html', {'Gamedata': data})

#
# def delete_fun(request):
#
#     g2 = Game()
#     g2.Game.objects.get(id=request.POST['d'])
#     g2.delete()
#     return HttpResponse("<script>alert('Data Deleted Successfully')</script>")
def update_fun(request, id):
    g1 = Game.objects.get(id=id)
    if request.method == 'POST':
        g1.Game_Name = request.POST['game-name']
        g1.Game_type = request.POST['ddl-game-type']
        g1.Player_name = request.POST['player-name']
        g1.Player_age = request.POST['player-age']
        g1.Player_city = request.POST['player-city']
        g1.save()
        return redirect('display')
    return render(request, 'update_game.html', {'data': g1})


def delete_fun(request, id):
    g1 = Game.objects.get(id=id)
    g1.delete()
    return redirect('display')
