import os
from datetime import datetime

# Q1  imprimez le répertoire courant
print(f'Q1  Le répertoire courant est : {os.getcwd()}')
print(80*'_' )

# Q2   ATTENTION sous windows, la variable d'environnement équivalente à HOME de Linux est USERPROFILE
#      MALGRÉ CELA, on va toujours parler de votre HOME
#   Imprimez la variable d'environnement USERPROFILE
myHome = os.environ.get('USERPROFILE')
print (f'Q2  Mon Home est : {myHome}')
print(80*'_' )

# Q3 Déplacez-vous sur le répertoire 'Desktop' de votre HOME                            #
# Et imprimez le répertoire courant                                                     #
os.chdir(myHome)
os.chdir('Desktop')
print(f'Q3  Le répertoire courant est maintenant: {os.getcwd()}')
print(80*'_' )

# Q4   Imprimez la liste des répertoires et des fichiers qu'il y a dans votre Desktop   #
print(f'Q4 Liste des répertoires et fichiers dans mon bureau : {os.listdir()}')
print(80*'_' )


# Q5   création d'un répertoire OS-DemoQ5                                               #
# Et réimprimez les répertoires et les fichiers dans votre Desktop                      #
os.mkdir('OS-DemoQ5')
print(f'Q5 Liste des répertoires et fichiers dans mon bureau : {os.listdir()}')
print(80*'_' )

# Q6   création d'un répertoire et d'un sous-répertoire en une seule fois               #
# Et réimprimez les répertoires et les fichiers dans votre Desktop                      #
os.makedirs('OS-DemoQ6/Sub-Dir-1')
print(f'Q6 Liste des répertoires et fichiers dans mon bureau : {os.listdir()}')
print(80*'_' )

# Q7   suppression du répertoire OS-DemoQ5#
# Et réimprimez les répertoires et les fichiers dans votre bureau#
os.rmdir('OS-DemoQ5')
print(f'Q7 Liste des répertoires et fichiers dans mon bureau : {os.listdir()}')
print(80*'_' )

# Q8   suppression du répertoire OS-DemoQ6 avec rmdir#
# Et réimprimez les répertoires et les fichiers dans votre bureau#
# Observez que vous avez un message d'erreur comme quoi le répertoire n'est pas vide
os.rmdir('OS-DemoQ6')
print(f'Q8 Liste des répertoires et fichiers dans mon bureau : {os.listdir()}')
print(80*'_' )

# 9   suppression du répertoire OS-DemoQ6 avec rmdir#
# Et réimprimez les répertoires et les fichiers dans votre bureau#
# Observez que vous avez un message d'erreur comme quoi le répertoire n'est pas vide
os.rmdir('OS-DemoQ6')
print(f'Q8 Liste des répertoires et fichiers dans mon bureau : {os.listdir()}')
print(80*'_' )

# Q9 create a new file in the bureau directory 
file_path = os.path.join(os.environ.get('USERPROFILE'),'test.txt')
print(file_path)
print(f'Q7 Liste des répertoires et fichiers dans mon bureau : {os.listdir()}')
print(80*'_' )

# Q8 renommer un fichier ou un dossier #
os.rename('test.txt', 'demo.txt')
print(f'Q8 Liste des répertoires et fichiers dans mon Home : {os.listdir()}')

# Q9 trouver toutes les infos d'un fichier avec stat
print(os.stat('demo.txt'))
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))


# grab the filename of #
print(os.path.basename('/tmp/demo.txt')) #demo.txt#
print(os.path.dirname('/tmp/demo.txt'))  #/tmp#
print(os.path.split('/tmp/demo.txt'))  #('/tmp', 'demo.txt')#
print(os.path.exists('/tmp/demo.txt'))
print(os.path.isfile('/tmp/demo.txt'))
print(os.path.isdir('/tmp/demo.txt'))
print(os.path.splitext('/tmp/demo.txt'))  #('/tmp/demo', '.txt')#



