# usr/bin/env/python
# coding utf-8

import mysql.connector
from django.shortcuts import render, redirect
from . models import Cipher, Stegano, ReverseEngr, Analysis, DirListing, Recon

db = mysql.connector.connect(
    host = '127.0.0.1',
    port = '3306',
    database = '',
    username = '',
    password = ''
)

controldb = db.cursor()

def index(request):
    return render(request, 'web/index.html')

def sign_up(request):
    if request.method == 'POST':
      username = request.POST['user']
      password = request.POST['pass']

      controldb.execute('SELECT username FROM info')

      for uname in controldb.fetchall():
         if username in uname:
           return render(request, 'web/register.html', {'data':'<div class="error-register"><h1 class="register-message">username already exists</h1></div>'})
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
         if username in data and password in data:
           request.session['user'] = username
           request.session['pass'] = password

           return redirect('/challenge')
      else:
        return render(request, 'web/login.html', {'data':'<div class="error-login"><h1 class="login-message">incorrect username or password try again</h1></div>'})
    return render(request, 'web/login.html')

def challenge(request):
    if request.session.get('user') and request.session.get('pass'):
      return render(request, 'web/challenge.html')
    else:
      return redirect('/sign_in')

def flag(request):
    if request.session.get('user') and request.session.get('pass'):
      if request.method == 'POST':
        solver = request.POST.get('leet')
        flag = request.POST.get('submit-flag')

        if flag == 'ctf{the_leg3nd4ry_c0de_bre4ker}':
          Cipher(cipher = solver).save()
          return render(request, 'web/flag.html', {'success':'<div class="success"><h1 class="success-message">flag submitted</h1></div>'})

        elif flag == 'ctf{y0u_c4n_4lways_f1nd}':
          Stegano(stegano = solver).save()
          return render(request, 'web/flag.html', {'success':'<div class="success"><h1 class="success-message">flag submitted</h1></div>'})

        elif flag == 'ctf{py_g0ds}':
          ReverseEngr(reverseengr = solver).save()
          return render(request, 'web/flag.html', {'success':'<div class="success"><h1 class="success-message">flag submitted</h1></div>'})

        elif flag == 'ctf{sh4rp_3ye_l1ke_a_h4wk}':
          Analysis(analysis = solver).save()
          return render(request, 'web/flag.html', {'success':'<div class="success"><h1 class="success-message">flag submitted</h1></div>'})

        elif flag == 'ctf{f1nd_a_r1ght_p4th}':
          DirListing(dirlisting = solver).save()
          return render(request, 'web/flag.html', {'success':'<div class="success"><h1 class="success-message">flag submitted</h1></div>'})

        elif flag == 'ctf{th3_g0d_4ccess}':
          Recon(recon = solver).save()
          return render(request, 'web/flag.html', {'success':'<div class="success"><h1 class="success-message">flag submitted</h1></div>'})
        else:
          return render(request, 'web/flag.html', {'error':'<div class="error"><h1 class="error-message">incorrect flag</h1></div>'})
      else:
        return render(request, 'web/flag.html')
    else:
      return redirect('/sign_in')

def hall_of_fame(request):
    return render(request, 'web/hall-of-fame.html', {'Cipher':Cipher.objects.all().values, 'Stegano':Stegano.objects.all().values, 'ReverseEngr':ReverseEngr.objects.all().values, 'Analysis':Analysis.objects.all().values, 'DirListing':DirListing.objects.all().values, 'Recon':Recon.objects.all().values})

def log_out(request):
    try:
      del request.session['user']
      del request.session['pass']
    except:
      pass
    return redirect('/sign_in')
