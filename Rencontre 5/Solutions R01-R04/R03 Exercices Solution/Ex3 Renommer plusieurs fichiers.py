import os

os.chdir('G:\Python\Scripts\R2 Exercices Solution\Ex3 Videos')
#print(os.getcwd())#
for f in os.listdir():
    print(f)#
    print( os.path.splitext(f))
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('_')
    
    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(2)
    
    new_names = '{}_{}{}'.format(f_num, f_title,f_ext)
    
    os.rename(f, new_names)
