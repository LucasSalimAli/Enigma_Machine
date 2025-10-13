from tkinter import *
from PIL import Image, ImageTk



tela = Tk()



class interface():

    def __init__(self):
        self.tela = tela
        self.menu()
        self.frames_menu()
        self.buttons_menu()
        self.images_menu()
        self.labels_menu()
        
        tela.mainloop()

        
    #Menu Inicial
    def menu(self):
        self.tela.title("Digital Enigma Machine")
        self.tela.configure(background= "#2CAA2C")
        self.tela.geometry("300x300")
        self.tela.resizable(False, False)
        

    #Função para chamar a imagem da Logo
    def images_menu(self):
        image_path = "Enigma_Cipher\images\sign3.jpeg"
        img = Image.open(image_path)
        img = img.resize((300, 150), Image.LANCZOS)
        self.image = (img)
        self.title_image = ImageTk.PhotoImage(self.image)


    #Detalhes em volta da logo e dos botões
    def frames_menu(self):

        #frame title
        self.frame_title = Frame(self.tela, bg="#7015BB", bd = 4, highlightbackground= '#ffffff', highlightthickness=2)  

        self.frame_title.place(relx= 0.05, rely= 0.13, relwidth= 0.9, relheight=0.5)

        #frame btns
        self.frame_button1 = Frame(self.tela, bg="#227900", bd = 4, highlightbackground= '#ffffff', highlightthickness=2)

        self.frame_button1.place(relx= 0.05, rely= 0.75, relwidth=0.9, height=50)


    #Botões
    def buttons_menu(self):
        self.bt_start = Button(self.tela, text="Start", font=("Arial", 20), command= self.go_to_enigma)
        self.bt_start.place(relx= 0.61, rely=0.763, width=100, height=43)
        

        self.bt_exit = Button(self.tela, text="Exit", font=("Arial", 20), command= exit)
        self.bt_exit.place(relx= 0.061, rely=0.763, width=100, height=43)
        

    #Imagem da Lobo
    def labels_menu(self):
        self.lb_title = Label(self.frame_title, text= "ENIGMA", image=self.title_image, font=("Arial", 30))
        self.lb_title.place(relx= 0.001, rely= 0.03, relwidth= 1, relheight=0.95)




    #Função para abrir a janela da Enigma
    def go_to_enigma(self):
        enigma = Toplevel()
        self.enigma = enigma
        self.enigma.title("Enigma Simulator")
        self.enigma.geometry("600x620")
        self.enigma_image()
        self.enigma_label()

    
    #Função para chamar as imagem da tela da Enigma
    def enigma_image(self):
        bgimage_path = "Enigma_Cipher\images\protorype enigma.jpeg"
        bgimg = Image.open(bgimage_path)
        bgimg = bgimg.resize((600, 620), Image.LANCZOS)
        self.bgimage = (bgimg)
        self.bg_image = ImageTk.PhotoImage(self.bgimage)


    #Labels e background da página da enigma
    def enigma_label(self):
        self.lb_bg = Label(self.enigma, image=self.bg_image)
        self.lb_bg.place(relwidth= 1, relheight=1)

   
interface()