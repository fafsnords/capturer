# usr/bin/env/python
# coding utf-8

from django.shortcuts import render, redirect
from . models import Cipher, Stegano, ReverseEngr, Analysis, DirListing, Recon
from django.db import connection

controldb = connection.cursor()

def index(request):
    return render(request, 'web/index.html')

def about(request):
    return render(request, 'web/about.html')

def sign_up(request):
    if request.method == 'POST':
      username = request.POST['user']
      password = request.POST['pass']

      controldb.execute('SELECT username FROM server_data')

      for uname in controldb.fetchall():
         # check if the username is already registered then its not added to a database.
         if username in uname:
           return render(request, 'web/register.html', {'data':'<div class="error-register"><p>username already exists</p></div>'})
      else:
        request.session['user'] = username
        request.session['pass'] = password
        controldb.execute('INSERT INTO server_data (username, password) VALUES ("{0}", "{1}")'.format(username, password))

        return redirect('/challenge')

    return render(request, 'web/register.html')

def sign_in(request):
    if request.method == 'POST':
      username = request.POST['user']
      password = request.POST['pass']

      controldb.execute('SELECT username, password FROM server_data')

      for data in controldb.fetchall():
         # if username and password is match its successfully redirected into a ctf zone.
         if username in data and password in data:
           request.session['user'] = username
           request.session['pass'] = password

           return redirect('/challenge')
      else:
        return render(request, 'web/login.html', {'data':'<div class="error-login"><p>incorrect username </br>or password try again</p></div>'})
    return render(request, 'web/login.html')

def challenge(request):
    if request.session.get('user') and request.session.get('pass'):
      # session provided to access in ctf games.
      return render(request, 'web/challenge.html')
    else:
      return redirect('/sign_in')

def settings(request):
    if request.session.get('user') and request.session.get('pass'):
      if request.method == 'POST':
        new_username = request.POST.get('new_username')
        current_username = request.POST.get('current_username')
        password = request.POST.get('pass')
        username = request.POST.get('user')
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        del_username = request.POST.get('del_username')
        del_password = request.POST.get('del_password')

        controldb.execute('SELECT username, password FROM server_data')

        for data in controldb.fetchall():
           # change username
           if current_username in data and password in data:
             controldb.execute('UPDATE server_data SET username = "{0}" WHERE username = "{1}"'.format(new_username, current_username))
             return render(request, 'web/settings.html', {'success':'<div class="success"><p>Username change Successfully</p></div>'})
           
           # change password
           if username in data and current_password in data:
             controldb.execute('UPDATE server_data SET password = "{0}" WHERE username = "{1}" AND password = "{2}"'.format(new_password, username, current_password))
             return render(request, 'web/settings.html', {'success':'<div class="success"><p>Password change Successfully</p></div>'})
           
           # delete account
           if del_username in data and del_password in data:
             controldb.execute('DELETE FROM server_data WHERE username = "{0}" AND password = "{1}"'.format(del_username, del_password))
             del request.session['user']
             del request.session['pass']
             return redirect('/sign_in')
        else:
          return render(request, 'web/settings.html', {'error':'<div class="error"><p>Incorrect Username or Password Try Again</p></div>'})
      return render(request, 'web/settings.html')
    else:
      return redirect('/sign_in')

def flag(request):
    if request.session.get('user') and request.session.get('pass'):
      if request.method == 'POST':
        solver = request.POST.get('leet')
        flag = request.POST.get('flag')

        '''
         if the solver is solve the challenge 
         then a solvers leet/codename is added into a separate database
         depends on the type of flag that represent on challenge.
        '''

        if flag == 'ctf{the_leg3nd4ry_c0de_bre4ker}':
          controldb.execute('INSERT INTO server_cipher (cipher) VALUES ("{0}")'.format(solver))
          return render(request, 'web/flag.html', {'success':'<div class="success"><p>flag submitted</p></div>'})

        elif flag == 'ctf{h1de_4nd_s33k}':
          controldb.execute('INSERT INTO server_stegano (stegano) VALUES ("{0}")'.format(solver))
          return render(request, 'web/flag.html', {'success':'<div class="success"><p>flag submitted</p></div>'})

        elif flag == 'ctf{l0gin_Suc3ssFully}':
          controldb.execute('INSERT INTO server_reverseengr (reverseengr) VALUES ("{0}")'.format(solver))
          return render(request, 'web/flag.html', {'success':'<div class="success"><p>flag submitted</p></div>'})

        elif flag == 'ctf{ch1lds_pl4y}':
          controldb.execute('INSERT INTO server_analysis (analysis) VALUES ("{0}")'.format(solver))
          return render(request, 'web/flag.html', {'success':'<div class="success"><p>flag submitted</p></div>'})

        elif flag == 'ctf{f1nd_a_r1ght_p4th}':
          controldb.execute('INSERT INTO server_dirlisting (dirlisting) VALUES ("{0}")'.format(solver))
          return render(request, 'web/flag.html', {'success':'<div class="success"><p>flag submitted</p></div>'})

        elif flag == 'ctf{s1mple_g4me}':
          controldb.execute('INSERT INTO server_recon (recon) VALUES ("{0}")'.format(solver))
          return render(request, 'web/flag.html', {'success':'<div class="success"><p>flag submitted</p></div>'})
        else:
          return render(request, 'web/flag.html', {'error':'<div class="error"><p>incorrect flag</p></div>'})
      else:
        return render(request, 'web/flag.html')
    else:
      return redirect('/sign_in')

def solvers(request):
    return render(request, 'web/solvers.html', {'Cipher':Cipher.objects.all().values, 'Stegano':Stegano.objects.all().values, 'ReverseEngr':ReverseEngr.objects.all().values, 'Analysis':Analysis.objects.all().values, 'DirListing':DirListing.objects.all().values, 'Recon':Recon.objects.all().values})

def log_out(request):
    try:
      del request.session['user']
      del request.session['pass']
    except:
      pass
    return redirect('/sign_in')