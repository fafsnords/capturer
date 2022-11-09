# usr/bin/env/python
# coding utf-8

import mysql.connector
from django.shortcuts import render, redirect
from . models import Cipher, Stegano, ReverseEngr, Analysis, DirListing, Recon

db = mysql.connector.connect(
    host = '',
    port = '',
    database = '',
    username = '',
    password = ''
)

controldb = db.cursor()

def index(request):
    return render(request, 'web/index.html')

def about(request):
    return render(request, 'web/about.html')

def sign_up(request):
    if request.method == 'POST':
      username = request.POST['user']
      password = request.POST['pass']

      controldb.execute('SELECT username FROM info')

      for uname in controldb.fetchall():
         # check if the username is already registered then its not added to a database.
         if username in uname:
           return render(request, 'web/register.html', {'data':'<div class="error-register"><p>username already exists</p></div>'})
      else:
        request.session['user'] = username
        request.session['pass'] = password
        controldb.execute('INSERT INTO info (username, password) VALUES ("{0}", "{1}")'.format(username, password))
        db.commit()

        return redirect('/challenge')

    return render(request, 'web/register.html')

def sign_in(request):
    if request.method == 'POST':
      username = request.POST['user']
      password = request.POST['pass']

      controldb.execute('SELECT username, password FROM info')

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

        controldb.execute('SELECT username, password FROM info')

        for data in controldb.fetchall():
           # change username
           if current_username in data and password in data:
             controldb.execute('UPDATE info SET username = "{0}" WHERE username = "{1}"'.format(new_username, current_username))
             db.commit()
             return render(request, 'web/settings.html', {'success':'<div class="success"><p>Username change Successfully</p></div>'})
           
           # change password
           if username in data and current_password in data:
             controldb.execute('UPDATE info SET password = "{0}" WHERE username = "{1}" AND password = "{2}"'.format(new_password, username, current_password))
             db.commit()
             return render(request, 'web/settings.html', {'success':'<div class="success"><p>Password change Successfully</p></div>'})
           
           # delete account
           if del_username in data and del_password in data:
             controldb.execute('DELETE FROM info WHERE username = "{0}" AND password = "{1}"'.format(del_username, del_password))
             db.commit()
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
          Cipher(cipher = solver).save()
          return render(request, 'web/flag.html', {'success':'<div class="success"><p>flag submitted</p></div>'})

        elif flag == 'ctf{y0u_c4n_4lways_f1nd}':
          Stegano(stegano = solver).save()
          return render(request, 'web/flag.html', {'success':'<div class="success"><p>flag submitted</p></div>'})

        elif flag == 'ctf{py_g0ds}':
          ReverseEngr(reverseengr = solver).save()
          return render(request, 'web/flag.html', {'success':'<div class="success"><p>flag submitted</p></div>'})

        elif flag == 'ctf{sh4rp_3ye_l1ke_a_h4wk}':
          Analysis(analysis = solver).save()
          return render(request, 'web/flag.html', {'success':'<div class="success"><p>flag submitted</p></div>'})

        elif flag == 'ctf{f1nd_a_r1ght_p4th}':
          DirListing(dirlisting = solver).save()
          return render(request, 'web/flag.html', {'success':'<div class="success"><p>flag submitted</p></div>'})

        elif flag == 'ctf{th3_g0d_4ccess}':
          Recon(recon = solver).save()
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
