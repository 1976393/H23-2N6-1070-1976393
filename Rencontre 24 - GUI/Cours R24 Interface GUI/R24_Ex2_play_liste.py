# Programme pour créer un 
# GUI avec le module customtkinter 
import customtkinter
import tkinter as tk


# Dimensions de la fenêtre
appWidth, appHeight = 800, 400


# App Class
class MyFrameChoisir(customtkinter.CTkFrame):
 
    ls_chansons = []
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0,1), weight=1)  # configure grid system
        self.grid_columnconfigure((0,1,2), weight=1)
        
        # CTkEntry pour le nom
        self.nom = customtkinter.CTkEntry(self,
        placeholder_text="Entre ton nom ici",width=580,
                               height=25)
        self.nom.grid(row=0, column=1,
                        columnspan=3, padx=100,
                        pady=5, sticky="w")     #, sticky="ew"



        # CTkOptionMenu  pour les choix des chansons
        self.choix_chansons = customtkinter.CTkOptionMenu(self,
                                values=["Choisis parmi ces chansons pop:",
                                "'Drivers License' by Olivia Rodrigo",
                                "'Mood' by 24kGoldn",
                                "'Blinding Lights' by The Weeknd",
                                "'Levitating' by Dua Lipa",
                                "'Save Your Tears' by The Weeknd",
                                "'Up' by Cardi B",
                                "'Peaches' by Justin Bieber",
                                "'Kiss Me More' by Doja Cat",
                                "'Good 4 U' by Olivia Rodrigo",
                                "'Montero (Call Me By Your Name)' by Lil Nas X",
                                "'Heat Waves' by Glass Animals",
                                "'Industry Baby' by Lil Nas X",
                                "'Deja Vu' by Olivia Rodrigo",
                                "'Astronaut In The Ocean' by Masked Wolf",],width=580,
                               height=25)
        self.choix_chansons.grid(row=4, column=1,
                                padx=100, pady=5,
                                columnspan=2, sticky="w")

        # CTkButton Ajouter à ta liste
        self.btn_Ajouter = customtkinter.CTkButton(self,
                            text="Ajouter à la liste",
                            width=580,
                               height=25)
        self.btn_Ajouter.grid(row=5, column=1,
                            columnspan=2, padx=100,
                            pady=5, sticky="w")

        # CTkTextbox pour ta play liste
        self.ta_play_liste = customtkinter.CTkTextbox(self,
                            width=640,
                            height=200, state="disabled")
        self.ta_play_liste.grid(row=6, column=1,
                            columnspan=2, padx=100,
                            pady=20)
  
        # CTkLabel pour message pour le nombre de chansons ajoutées
        self.lbl_nb_chansons = customtkinter.CTkLabel(self,
        text="Il y a présentement 0 chansons dans ta play liste",font = ("inter",16),width=580,
                               height=25)
        self.lbl_nb_chansons.grid(row=7, column=1,
                                    padx=50, pady=5,sticky="ew")  #enlevé sticky="ew"

    # Pour ajouter la chanson sélectionnée à la play liste
    def ajouter(self):
        pass

           

class App(customtkinter.CTk):
         
    def __init__(self):
        super().__init__()
        
        # titre de la fenêtre
        self.title("Ta play liste")
        # applique les dimensions de la fenêtre
        self.geometry(f"{appWidth}x{appHeight}")

        # pour l'apparence de la fenêtre  (choix Light, Dark, System)
        customtkinter.set_appearance_mode("Dark")

        # pour l'apparence des composants graphiques dans la fenêtre
        # choix possibles: green, dark-blue, blue
        customtkinter.set_default_color_theme("green")
  
        self.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)  # configure grid system
        self.grid_columnconfigure((0,1,2,3), weight=1)
        
         
        self.pour_choisir = MyFrameChoisir(master=self,width=600, corner_radius=0)
        self.pour_choisir.grid(row=0, column=0, padx=2, pady=2)
        



app = App()
app.mainloop()