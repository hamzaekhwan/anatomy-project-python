import customtkinter as ctk

from PIL import Image

class Start:

    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("sacT")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/firstT.jpg"),
                                               size=(width,height))
        
        
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)

        start_button = ctk.CTkButton(self.root, text="Start Learning",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_sac)
        start_button.place(x=700, y=470, width=200, height=60)
        
        
    def go_to_sac(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sac()
        pba.root.mainloop()

##################start of sac #################
class Sac:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("sacT")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/sacT.jpg"),
                                               size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)
         
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_start)

        btn.place(x=10, y=10, width=25, height=25) 

         

        head_button = ctk.CTkButton(self.root, text="The Head",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_head)
        head_button.place(x=620, y=130, width=120, height=60)

        Vertebral_coulmn_button = ctk.CTkButton(self.root, text="Vertebral coulmn",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_Vertebral)
        Vertebral_coulmn_button.place(x=280, y=170, width=180, height=60)

        shoulder_button = ctk.CTkButton(self.root, text="Shoulder girdel",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_shoulder)
        shoulder_button.place(x=640, y=200, width=160, height=60)

        Thoracic_cage_button = ctk.CTkButton(self.root, text="Thoracic cage",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_thoracic)
        Thoracic_cage_button.place(x=255, y=240, width=160, height=60)

        Upper_limb_button = ctk.CTkButton(self.root, text="Upper limb",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_upper)
        Upper_limb_button.place(x=660, y=270, width=160, height=60)

        plivice_button = ctk.CTkButton(self.root, text="Plvice girdel",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_plivice)
        plivice_button.place(x=275, y=420, width=160, height=60)
        
        lowerlimb_button = ctk.CTkButton(self.root, text="Lower limb",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_lower)
        lowerlimb_button.place(x=660, y=435, width=160, height=60)

    def forword_to_start(self):

        self.root.destroy()  # close the students window
       
        pba = Start()
        pba.root.mainloop()
    def go_to_head(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = The_head()
        pba.root.mainloop()
    def go_to_Vertebral(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Vertebral_coulmn()
        pba.root.mainloop()
    def go_to_shoulder(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sholder_girdel()
        pba.root.mainloop()
    def go_to_thoracic(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Thoracic_cage()
        pba.root.mainloop()
    def go_to_upper(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Upper_limb()
        pba.root.mainloop()

    def go_to_plivice(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Plvice_girdel()
        pba.root.mainloop()    

    def go_to_lower(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Lower_limb()
        pba.root.mainloop() 

#############################end of sac ############################

##################start of LOWER_LIMP #################
class Lower_limb:  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("sacT")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Lower limb/Lower limb rigions.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)

        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_sac)
        btn.place(x=10, y=10, width=25, height=25) 
        Femur_button = ctk.CTkButton(self.root, text="Femur",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_Femur)
        Femur_button.place(x=680, y=220, width=100, height=45)

        metatarsals_and_phalanges_button = ctk.CTkButton(self.root, text="metatarsals and phalanges",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_metatarsals_and_phalanges)
        metatarsals_and_phalanges_button.place(x=680, y=460, width=280, height=35)

        patella_button = ctk.CTkButton(self.root, text="patella ",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_patella )
        patella_button.place(x=680, y=275, width=100, height=45)

        tarsals_button = ctk.CTkButton(self.root, text="tarsals",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_tarsals )
        tarsals_button.place(x=690, y=410, width=100, height=35)

        tibia_and_fibula_button = ctk.CTkButton(self.root, text="tibia and fibula",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_tibia_and_fibula )
        tibia_and_fibula_button.place(x=680, y=350, width=180, height=45)

    def go_to_Femur(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Femur()
        pba.root.mainloop()

    def go_to_metatarsals_and_phalanges(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Metatarsals_And_Phalanges()
        pba.root.mainloop()   
    def go_to_patella(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = patella()
        pba.root.mainloop()      

    def go_to_tarsals(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Tarsals()
        pba.root.mainloop()   
    def go_to_tibia_and_fibula(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Tibia_And_Fibula()
        pba.root.mainloop()  

    def forword_to_sac(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sac()
        pba.root.mainloop()    

class Femur:  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Femur")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Lower limb/Femur .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)    

        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_lower_limp)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_lower_limp(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Lower_limb()
        pba.root.mainloop()
class Metatarsals_And_Phalanges:  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Metatarsals_And_Phalanges")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Lower limb/metatarsals and phalanges .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)     

        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_lower_limp)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_lower_limp(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Lower_limb()
        pba.root.mainloop()

class patella:  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("patella")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Lower limb/patella .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0) 

        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_lower_limp)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_lower_limp(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Lower_limb()
        pba.root.mainloop() 

class Tarsals :  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Tarsals")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Lower limb/tarsals .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0) 
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_lower_limp)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_lower_limp(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Lower_limb()
        pba.root.mainloop()
class Tibia_And_Fibula :  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Tibia_And_Fibula")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Lower limb/tibia and fibula .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)  

        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_lower_limp)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_lower_limp(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Lower_limb()
        pba.root.mainloop()

##################END of LOWER_LIMP #################        
##################start of Plvice_girdel #################
class Plvice_girdel:  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Plvice_girdel")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Plvice girdel/Plvice rigions.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_sac)
        btn.place(x=10, y=10, width=25, height=25) 

        Ilium_button = ctk.CTkButton(self.root, text="Ilium",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_Ilium)
        Ilium_button.place(x=715, y=240, width=100, height=45)

        Ischium_button = ctk.CTkButton(self.root, text="Ischium",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_Ischium)
        Ischium_button.place(x=255, y=350, width=100, height=45)

        Pubis_button = ctk.CTkButton(self.root, text="Pubis",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_Pubis)
        Pubis_button.place(x=732, y=380, width=100, height=45)

    def go_to_Ilium(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Ilium()
        pba.root.mainloop()

    def go_to_Ischium(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Ischium()
        pba.root.mainloop()   
    def go_to_Pubis(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Pubis()
        pba.root.mainloop()       
    def forword_to_sac(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sac()
        pba.root.mainloop() 
class Ilium:  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Ilium")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Plvice girdel/Ilium.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_plivice)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_plivice(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Plvice_girdel()
        pba.root.mainloop()

class Ischium:  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Ischium")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Plvice girdel/Ischium.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_plivice)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_plivice(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Plvice_girdel()
        pba.root.mainloop()

class Pubis:  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Pubis")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Plvice girdel/Pubis.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)  
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_plivice)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_plivice(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Plvice_girdel()
        pba.root.mainloop()      
##################end of Plvice girdel #################
##################start of shoulder #################

class Sholder_girdel:  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Sholder_girdel")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Sholder girdel/Sholder girdel rigions.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)        
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_sac)
        btn.place(x=10, y=10, width=25, height=25) 

        clavicle_button = ctk.CTkButton(self.root, text="clavicle",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_clavicle)
        clavicle_button.place(x=580, y=110, width=100, height=45)

        scapula_button = ctk.CTkButton(self.root, text="scapula",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_scapula)
        scapula_button.place(x=240, y=400, width=100, height=45)


    def go_to_clavicle(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Clavicle()
        pba.root.mainloop()

    def go_to_scapula(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Scapula()
        pba.root.mainloop()    
    def forword_to_sac(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sac()
        pba.root.mainloop() 
class Scapula:
    def __init__(self):  
            self.root = ctk.CTk()
            self.root.title("Scapula")
            width=1050
            height=600
            self.root.geometry("{}x{}+20+20".format(width,height))
            self.root.resizable(0, 0)
            self.root.configure(fg_color='white')
            self.bg_image = ctk.CTkImage(Image.open("Data/Sholder girdel/scapula.jpg"),
                                                    size=(width,height))
            self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
            self.bg_image_label.place(x=0, y=0)  
            self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
            btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_shoulder)

            btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_shoulder(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sholder_girdel()
        pba.root.mainloop()

class Clavicle:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Clavicle")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Sholder girdel/clavicle .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)    
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_shoulder)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_shoulder(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sholder_girdel()
        pba.root.mainloop()    
    
##################end of shouldwe #################
##################start of head#######################
class The_head:  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("sacT")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/The head/The head rigions.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)   
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_sac)
        btn.place(x=10, y=10, width=25, height=25) 

        cranial_button = ctk.CTkButton(self.root, text="Cranial",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_cranial)
        cranial_button.place(x=450, y=130, width=120, height=60)

        facial_button = ctk.CTkButton(self.root, text="Facial",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_facial)
        facial_button.place(x=695, y=385, width=120, height=60)


    def go_to_cranial(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Cranial()
        pba.root.mainloop()

    def go_to_facial(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Facial()
        pba.root.mainloop()
    def forword_to_sac(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sac()
        pba.root.mainloop() 
#############start of faciaL /###########################
class Facial:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Cranial")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/The head/facial/facial rgions.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)   
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_head)
        btn.place(x=10, y=10, width=25, height=25)

        nasal_button = ctk.CTkButton(self.root, text="nasal",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_nasal)
        nasal_button.place(x=695, y=160, width=120, height=60)

        maxilla_button = ctk.CTkButton(self.root, text="maxilla",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_maxilla)
        maxilla_button.place(x=720, y=230, width=120, height=60)

        zigomatic_button = ctk.CTkButton(self.root, text="zigomatic",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_zigomatic)
        zigomatic_button.place(x=250, y=240, width=120, height=60)

        Mandible_button = ctk.CTkButton(self.root, text="mandible",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_mandible)
        Mandible_button.place(x=220, y=340, width=120, height=60)
        
        
    def go_to_nasal(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Nasal()
        pba.root.mainloop()

    def go_to_maxilla(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Maxilla()
        pba.root.mainloop()

    def go_to_zigomatic(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Zigomatic()
        pba.root.mainloop()

    def go_to_mandible(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Mandible()
        pba.root.mainloop()

    def forword_to_head(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = The_head()
        pba.root.mainloop()

class Mandible:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Zigomatic")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/The head/facial/Mandible .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0) 
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_facial)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_facial(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Facial()
        pba.root.mainloop()

class Zigomatic:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Zigomatic")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/The head/facial/zigomatic.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0) 
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_facial)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_facial(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Facial()
        pba.root.mainloop()



class Maxilla:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Maxilla")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/The head/facial/maxilla .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0) 
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                   
                            hover_color=("gray70", "gray30"),
                           
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_facial)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_facial(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Facial()
        pba.root.mainloop()

class Nasal:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Nasal")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/The head/facial/nasal .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)   
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_facial)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_facial(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Facial()
        pba.root.mainloop()
######################end of facial #########################

class Cranial:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Cranial")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/The head/cranial/cranial rgions .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)   
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_head)
        btn.place(x=10, y=10, width=25, height=25)

        frontal_button = ctk.CTkButton(self.root, text="frontal",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                        command=self.go_to_frontal)
        frontal_button.place(x=675, y=170, width=120, height=60)
        
        occipital_button = ctk.CTkButton(self.root, text="occipital",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                        command=self.go_to_occipital)
        occipital_button.place(x=230, y=400, width=120, height=60)

        parietal_button = ctk.CTkButton(self.root, text="parietal",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                        command=self.go_to_parietal)
        parietal_button.place(x=235, y=170, width=120, height=60)

        sphinoid_button = ctk.CTkButton(self.root, text="sphinoid ",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                        command=self.go_to_sphinoid)
        sphinoid_button.place(x=685, y=260, width=120, height=60)

        temporal_button = ctk.CTkButton(self.root, text="temporal",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                        command=self.go_to_temporal)
        temporal_button.place(x=400, y=470, width=120, height=60)

    def go_to_frontal(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Frontal()
        pba.root.mainloop()    

    def go_to_occipital(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Occipital()
        pba.root.mainloop() 

    def go_to_parietal(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Parietal()
        pba.root.mainloop() 

    def go_to_sphinoid(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sphinoid()
        pba.root.mainloop()

    def go_to_temporal(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Temporal()
        pba.root.mainloop()
    def forword_to_head(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = The_head()
        pba.root.mainloop()
class Temporal:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Temporal")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/The head/cranial/temporal part.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_cranial)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_cranial(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Cranial()
        pba.root.mainloop()


class Sphinoid:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Sphinoid")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/The head/cranial/sphinoid part .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_cranial)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_cranial(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Cranial()
        pba.root.mainloop()

class Parietal:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Occipital")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/The head/cranial/parietal part.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_cranial)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_cranial(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Cranial()
        pba.root.mainloop()
                 

class Occipital:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Occipital")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/The head/cranial/occipital part .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_cranial)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_cranial(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Cranial()
        pba.root.mainloop()

class Frontal:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Frontal")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/The head/cranial/frontal part.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)   
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_cranial)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_cranial(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Cranial()
        pba.root.mainloop()


####################end of cranial###############################
######################end of head ###################################

################start of thoaracic cage ##########################################
class Thoracic_cage:  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("sacT")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Thoracic cage/Thoracic cage rigions.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)   
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_sac)
        btn.place(x=10, y=10, width=25, height=25) 


        False_ribs_button = ctk.CTkButton(self.root, text="False ribs",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_False_ribs)
        False_ribs_button.place(x=670, y=290, width=120, height=40)

        True_ribs_button = ctk.CTkButton(self.root, text="True ribs",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_True_ribs)
        True_ribs_button.place(x=675, y=350, width=120, height=40)

        floating_ribs_button = ctk.CTkButton(self.root, text="floating ribs",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_floating_ribs)
        floating_ribs_button.place(x=320, y=400, width=140, height=40)

        sternum_button = ctk.CTkButton(self.root, text="Sternum",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_sternum)
        sternum_button.place(x=313, y=222, width=100, height=40)
    

    def go_to_False_ribs(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = FalseRibs()
        pba.root.mainloop()

    def go_to_True_ribs(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = TrueRibs()
        pba.root.mainloop()

    def go_to_floating_ribs(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = FloatingRibs()
        pba.root.mainloop()

    def go_to_sternum(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sternum()
        pba.root.mainloop()
    def forword_to_sac(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sac()
        pba.root.mainloop()
class FalseRibs:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("FalseRibs")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Thoracic cage/False ribs .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)   
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_Thoracic_cage)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_Thoracic_cage(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Thoracic_cage()
        pba.root.mainloop()

class TrueRibs:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("TrueRibs")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Thoracic cage/True ribs .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)  
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_Thoracic_cage)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_Thoracic_cage(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Thoracic_cage()
        pba.root.mainloop()

class FloatingRibs:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("FloatingRibs")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Thoracic cage/floating ribs .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)   
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_Thoracic_cage)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_Thoracic_cage(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Thoracic_cage()
        pba.root.mainloop()

class Sternum:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Sternum")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Thoracic cage/Sternum.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)  
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_Thoracic_cage)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_Thoracic_cage(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Thoracic_cage()
        pba.root.mainloop()

#####################end of thoaracic cage ###########################

################start of upper_limb ##########################################
class Upper_limb:  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("sacT")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Upper limb/Upper limb rigions.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0) 
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))  
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            
                            command=self.forword_to_sac)
        btn.place(x=10, y=10, width=25, height=25)

        carbals_button = ctk.CTkButton(self.root, text="Carbals",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_Carbals)
        carbals_button.place(x=510, y=415, width=120, height=40)

        Humerus_button = ctk.CTkButton(self.root, text="Humerus",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_Humerus)
        Humerus_button.place(x=550, y=200, width=120, height=40)

        metacarpals_and_phalanges_button = ctk.CTkButton(self.root, text="metacarpals and phalanges ",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_metacarpals_and_phalanges)
        metacarpals_and_phalanges_button.place(x=510, y=472, width=290, height=40)

        Radius_and_ulna_button = ctk.CTkButton(self.root, text="Radius and ulna",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_Radius_and_ulna)
        Radius_and_ulna_button.place(x=530, y=330, width=200, height=40)         
    

    def go_to_Carbals(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Carbals()
        pba.root.mainloop()

    def go_to_Humerus(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Humerus()
        pba.root.mainloop()

    def go_to_metacarpals_and_phalanges(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Metacarpals_And_Phalanges()
        pba.root.mainloop()

    def go_to_Radius_and_ulna(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Radius_And_Ulna()
        pba.root.mainloop()

    def forword_to_sac(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sac()
        pba.root.mainloop()
class Carbals:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Carbals")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Upper limb/carbals .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0) 
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            # fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), #font=('Arial', 16),
                            command=self.forword_to_upper)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_upper(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Upper_limb()
        pba.root.mainloop()  

class Humerus:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Humerus")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Upper limb/Humerus .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)  
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20)) 
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                           
                            command=self.forword_to_upper)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_upper(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Upper_limb()
        pba.root.mainloop() 

class Metacarpals_And_Phalanges:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Metacarpals_And_Phalanges")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Upper limb/metacarpals and phalanges .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)  
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20)) 
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            
                            command=self.forword_to_upper)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_upper(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Upper_limb()
        pba.root.mainloop() 

class Radius_And_Ulna:
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Radius_And_Ulna")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Upper limb/Radius and ulna .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0) 
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            
                            command=self.forword_to_upper)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_upper(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Upper_limb()
        pba.root.mainloop() 
#####################end of Upper_limb ###########################
################start of vertebal ##########################################
class Vertebral_coulmn:  
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Vertebral_coulmn")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Vertebral coulmn/Vertebral coulmn region.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)   
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                           
                            command=self.forword_to_sac)
        btn.place(x=10, y=10, width=25, height=25)

        cervical_button = ctk.CTkButton(self.root, text="Cervical",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_cervical)
        cervical_button.place(x=630, y=140, width=120, height=60)

        coccyx_button = ctk.CTkButton(self.root, text="Coccyx",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_Coccyx)
        coccyx_button.place(x=500, y=450, width=120, height=60)

        Lumber_button = ctk.CTkButton(self.root, text="Lumber",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_Lumber)
        Lumber_button.place(x=655, y=345, width=120, height=60)

        sacrum_button = ctk.CTkButton(self.root, text="sacrum",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_sacrum)
        sacrum_button.place(x=655, y=410, width=120, height=60)

        ThoracicV_button = ctk.CTkButton(self.root, text="Thoracic",text_color="black", font=ctk.CTkFont(size=20, weight="bold"),
                         command=self.go_to_Thoracic)
        
        ThoracicV_button.place(x=655, y=250, width=120, height=60)

    def go_to_cervical(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Cervical()
        pba.root.mainloop()    

    def go_to_Coccyx(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Coccyx()
        pba.root.mainloop() 

    def go_to_Lumber(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Lumber()
        pba.root.mainloop() 

    def go_to_sacrum(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sacrum()
        pba.root.mainloop() 

    def go_to_Thoracic(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Thoracic()
        pba.root.mainloop()
    def forword_to_sac(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Sac()
        pba.root.mainloop()
class Cervical :
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Cervical")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Vertebral coulmn/Cervical.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0) 
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            
                            command=self.forword_to_vertebral)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_vertebral(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Vertebral_coulmn()
        pba.root.mainloop()   

class Coccyx :
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Coccyx")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Vertebral coulmn/Coccyx.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0)  
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            
                            command=self.forword_to_vertebral)





        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_vertebral(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Vertebral_coulmn()
        pba.root.mainloop()   
             
class Sacrum :
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Sacrum")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Vertebral coulmn/sacrum.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0) 
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                            
                            command=self.forword_to_vertebral)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_vertebral(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Vertebral_coulmn()
        pba.root.mainloop() 
             
class Lumber :
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Lumber")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Vertebral coulmn/Lumber .jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0) 
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                           
                            command=self.forword_to_vertebral)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_vertebral(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Vertebral_coulmn()
        pba.root.mainloop() 

class Thoracic :
    def __init__(self):  
        self.root = ctk.CTk()
        self.root.title("Thoracic")
        width=1050
        height=600
        self.root.geometry("{}x{}+20+20".format(width,height))
        self.root.resizable(0, 0)
        self.root.configure(fg_color='white')
        self.bg_image = ctk.CTkImage(Image.open("Data/Vertebral coulmn/ThoracicV.jpg"),
                                                size=(width,height))
        self.bg_image_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        self.bg_image_label.place(x=0, y=0) 
        self.forword = ctk.CTkImage(Image.open("Data/forword.png"), size=(20, 20))
        btn = ctk.CTkButton(self.root, text="", font=ctk.CTkFont(size=18, weight="bold"),
                            fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"),
                            image=self.forword, anchor="w",
                           
                            command=self.forword_to_vertebral)

        btn.place(x=10, y=10, width=25, height=25) 
    def forword_to_vertebral(self):
        self.root.destroy()  # close the login window
            # start the main window
        pba = Vertebral_coulmn()
        pba.root.mainloop() 

#######################end of vertebral ################################

pba = Start()
pba.root.mainloop()        
        
