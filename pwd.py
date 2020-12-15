import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp850').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "Profil Tous les utilisateurs" in line]

for wifi in wifis:
   
   fichier = open("password.txt", "a")
   results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('cp850').split('\n')
   
   results= [line.split(':')[1][1:-1] for line in results if "Contenu de la clé  " in line]
   try:
       print(f'Name:{wifi}, Password: {results[0]}')
       fichier.write(f'Name:{wifi}, Password: {results[0]}\n')
   except: 
       print(f"Name:{wifi}, Password: canno't be read")
     
fichier.close()