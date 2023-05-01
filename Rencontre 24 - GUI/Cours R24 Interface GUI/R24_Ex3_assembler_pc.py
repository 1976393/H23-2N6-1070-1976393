# Programme pour créer un 
# GUI avec le module customtkinter 
import customtkinter as ctk
import tkinter as tk

# pour l'apparence de la fenêtre  (choix Light, Dark, System)
ctk.set_appearance_mode("Dark")

# pour l'apparence des composants graphiques dans la fenêtre
# choix possibles: green, dark-blue, blue
ctk.set_default_color_theme("green")

# Dimensions de la fenêtre
appWidth, appHeight = 800, 400
appPrix = {"AMD Ryzen 9 5950X         ":669.98,
           "AMD Ryzen 7 5800X3        ":438.98,
           "Intel Core i9 12900 K     ":569.99,
           "Intel Core i7 12700 K     ":428.99,
           "GeForce RTX 3090Ti        ":2379.99,
           "GeForce RTX 3080Ti        ":1639.99,
           "GeForce RTX 3070Ti        ":819.99,
           "Radeon RX 6950 XT         ":610.99,
           "G.SKILL Trident Z5        ":670.29,
           "CORSAIR Dominator         ":284.99,
           "CORSAIR Vengeance         ":310.99,
           "G.SKILL Ripjaws V         ":119.59  }

# App Class
class App(ctk.CTk):
    # ta play liste
    ls_chansons = []
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # titre de la fenêtre
        self.title("Assemble ton PC!")
        # applique les dimensions de la fenêtre
        self.geometry(f"{appWidth}x{appHeight}")
        self.grid_rowconfigure((0,1,2,3,4), weight=1)  # configure grid system
        self.grid_columnconfigure((0,1,2), weight=1, uniform="column")
        
        # CTkLabel pour directive
        self.lbl_directive = ctk.CTkLabel(self,
                                    text="CHOISIS tes composantes",width=150,
                               height=25 ,fg_color='red')
        self.lbl_directive.grid(row=0, column=0,columnspan=3,
                                padx=20, pady=(0,5) ,sticky="ew")  #enlevé sticky="ew"       
        # CTkOptionMenu  pour les choix de processeurs
        self.choix_processeur = ctk.CTkOptionMenu(self,
                                    values=[
                                    "Choisis ton processeur    ",
                                    "AMD Ryzen 9 5950X         ",
                                    "AMD Ryzen 7 5800X3        ",
                                    "Intel Core i9 12900 K     ",
                                    "Intel Core i7 12700 K     "],width=200,
                               height=25)
        self.choix_processeur.grid(row=1, column=0,
                                    padx=(0,20), pady=(0,5),
                                     sticky="e")
        # CTkOptionMenu  pour les choix de carte graphique
        self.choix_carte_graphique = ctk.CTkOptionMenu(self,
                                    values=[
                                    "Choisis ta carte graphique",
                                    "GeForce RTX 3090Ti        ",
                                    "GeForce RTX 3080Ti        ",
                                    "GeForce RTX 3070Ti        ",
                                    "Radeon RX 6950 XT         "],width=200,
                               height=25)
        self.choix_carte_graphique.grid(row=1, column=1,
                                    padx=20, pady=(0,5),
                                     sticky="e")
        # CTkOptionMenu pour les choix de barrettes RAM
        self.choix_RAM = ctk.CTkOptionMenu(self,
                                    values=[
                                    "Choisis ta RAM            ",
                                    "G.SKILL Trident Z5        ",
                                    "CORSAIR Dominator         ",
                                    "CORSAIR Vengeance         ",
                                    "G.SKILL Ripjaws V         "],width=200,
                               height=25)
        self.choix_RAM.grid(row=1, column=2,
                                    padx=20, pady=(0,5),
                                     sticky="e")
  
        # CTkButton estimer
        self.btn_estimer = ctk.CTkButton(self,
                                        text="Obtenir estimé",
                                        width=200,
                               height=25)
        self.btn_estimer.grid(row=3, column=1,
                                         padx=60,
                                        pady=(0,5), sticky="w")


        # CTkLabel pour messages
        self.lbl_message = ctk.CTkLabel(self,
                                    text="Commence par choisir tes composantes",width=200,
                               height=25)
        self.lbl_message.grid(row=4, column=1,
                                padx=5,pady=(0,5) ,sticky="ew")  #enlevé sticky="ew"
    # Pour obtenir un estimé
    def estimer(self):
        pass             


if __name__ == "__main__":
    app = App()
    # Used to run the application
    app.mainloop()    
