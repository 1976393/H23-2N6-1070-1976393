from cgitb import text
from operator import index, truediv
import tkinter
from xmlrpc.client import FastMarshaller
import customtkinter
import time

class MyFrameAfficher(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0,1), weight=1)  # configure grid system
        self.grid_columnconfigure((0,1,2), weight=1)
        
        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self, text="Employe Courant")
        self.label.grid(row=0, column=1, padx=5, pady=5)
        
        self.btn_precedent = customtkinter.CTkButton( master=self, text="Précédent", font = ("inter",14), command=self.aller_au_precedent)
        self.btn_precedent.grid(row=1, column=0, padx=5, pady=5)
        
        self.nom = customtkinter.CTkEntry(master=self,  font = ("inter",14),width=300)
        self.nom.grid(row=1, column=1, padx=5, pady=5)
        self.nom.insert(0,ls_employes[0])
        
        self.btn_suivant = customtkinter.CTkButton( master=self, text="Suivant", font = ("inter",14),command=self.aller_au_suivant)
        self.btn_suivant.grid(row=1, column=2, padx=5, pady=5)
        
     
    def aller_au_precedent(self):
        global index_courant
        if index_courant - 1 < 0:
            index_courant = len(ls_employes)-1
            self.nom.delete(0,len(self.nom.get()))
            self.nom.insert(0,ls_employes[index_courant])
        else:
            index_courant -= 1
            self.nom.delete(0,len(self.nom.get()))
            self.nom.insert(0,ls_employes[index_courant])
        
                
    def aller_au_suivant(self):
        global index_courant
        if index_courant + 1 > len(ls_employes)-1:
            index_courant = 0
            self.nom.delete(0,len(self.nom.get()))
            self.nom.insert(0,ls_employes[index_courant])
        else:
            index_courant +=1
            self.nom.delete(0,len(self.nom.get()))
            self.nom.insert(0,ls_employes[index_courant])
            

        
               
class MyFrameModifier(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0,1,2,3), weight=1)  # configure grid system
        self.grid_columnconfigure((0,1,2), weight=1)
        
        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self, text="Ajouter/Enlever un employé")
        self.label.grid(row=0, column=1, padx=5, pady=5)
       
     
        self.btn_ajouter = customtkinter.CTkButton( master=self, text="Ajouter", font = ("inter",14),command=self.ajouter)
        self.btn_ajouter.grid(row=1, column=1, padx=5, pady=5)
        
        self.nouveau_nom = customtkinter.CTkEntry(master=self, placeholder_text="Entrez un nom d'employé",width=400 ,font = ("inter",14))
        self.nouveau_nom.grid(row=2, column=1, padx=5, pady=5, columnspan=1, sticky="nsew")  
        
        self.avertissement = customtkinter.CTkLabel(self, text=" ", width=180 )
        self.avertissement.grid(row=3, column=1, padx=5, pady=5)
        
        self.btn_enlever = customtkinter.CTkButton( master=self, text="Enlever", font = ("inter",14),command=self.enlever)
        self.btn_enlever.grid(row=4, column=1, padx=5, pady=5)     

    def ajouter(self):
        new_name = self.nouveau_nom.get()
        if len(new_name) < 2:
            self.avertissement.configure(text= f'"{new_name}" est invalide car il n\'est pas assez long!')
            return
        in_list = False
        for i in ls_employes:
            if i == new_name:
                in_list = True
        if in_list == False:
                ls_employes.append(new_name)
                self.nouveau_nom.delete(0,len(self.nouveau_nom.get()))
                self.avertissement.configure(text= f'"{new_name}" a été ajouté à la liste')
        if in_list == True:
            self.avertissement.configure(text= f'"{new_name}" est déjà dans la liste')
             
     
    def enlever(self):
        in_list = False
        if len(self.nouveau_nom.get()) <2:
            self.avertissement.configure(text = f'"{self.nouveau_nom.get()}" n\'est pas assez long')
            return
        for i in ls_employes:
            if i == self.nouveau_nom.get():
                in_list = True
                ls_employes.remove(i)
                self.nouveau_nom.delete(0,len(self.nouveau_nom.get()))
                self.avertissement.configure(text = f'"{i}" a été enlevé de la liste')
        if in_list == False:
            self.avertissement.configure(text = f'"{self.nouveau_nom.get()}" n\'existe pas dans la liste')
            

          

        
                
class App(customtkinter.CTk):
    global ls_employes
    ls_employes = ['Pierre-Paul Gallant', 'Maxime Pelletier']
    global index_courant
    index_courant = 0
         
    def __init__(self):
        super().__init__()
        self.geometry("450x300")
        self.title="Liste des employés"
        self.resizable(False, False)   #On ne peut pas changer la grandeur de la fenêtre
        self.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)  # configure grid system
        self.grid_columnconfigure((0,1,2,3), weight=1)
        
         
        self.pour_afficher = MyFrameAfficher(master=self,width=600, corner_radius=0)
        self.pour_afficher.grid(row=0, column=0, padx=2, pady=2)
        
        self.pour_modifier = MyFrameModifier(master=self,width=600, corner_radius=0)
        self.pour_modifier.grid(row=6, column=0, padx=30, pady=2 , sticky="EW")


app = App()

app.mainloop()