from tkinter import *
from PIL import Image, ImageTk
from pygame import *
from time import *


#=================================================================================================================================================================
#Finalizado 30/10/2025 04:54 made by:Lucas, Vicenzo
#===================================================================================================================================================================

#==================================================================================================================
#CODIGO DE CLASSE DISCOS AQUI
class discos:

    codex = []    # array para o disco importa o padrao de codificaçao
    idex = 0      # indicatico de rotaçao do disco
    pos = 0       # indicativo de pos sequencial na maquina
    rot = 0       # indicativo onde o rotor deve girar o proximo
    
    assem = []    #codex exclusivo para o ETW 
    mirror = []   #codex exclusivo para o UKW importar

    def entrada(self, inpt):
        saida = self.codex[inpt]
        return saida

    def retorno(self, inpt):
        saida = self.codex.index(inpt)
        return saida
    
    def ford(self, alt=0):

        if alt == 1:
            buffer = self.codex[0]

            for x in range(len(self.codex)):
                if x < len(self.codex)-1:
                    self.codex[x] = self.codex[x+1]

            self.codex[len(self.codex)-1] = buffer
            
            if self.idex <= 26:
                self.idex = self.idex+1
            else:
                self.idex = 0
                
            if self.codex[0] == self.rot:
                return 1
            else:
                return 0
        
         
#====================================================================================
#talvez isso seja uma pessima ideia mas vamor ver se funciona
#classe discos ficou um pouco generica sem metodo __init__  afim de poder integrar o ETW e UKW e nao ter que criar outra classe e etc etc etc

    def traduz(self, inpt):
        
        if(type(inpt) == str):
        
            letra = self.assem.index(inpt)
        
        else:
        
            letra = self.assem[inpt]
            if letra == " ":
                letra = "-"

        

        return letra
    
    def espelho(self, inpt):
         
         saida = self.mirror[inpt]
         
         return saida

#=============================================================================================================================================================
#CODGIO FORA DA CLASSE AQUI V

pinoIndex = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Ç","-"] #array para indicar pos de rotaçao do disco
pinos = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ç"," "] #array para o obj ETW importar

# parametro de codificaçao dos discos, NAO APAGAR
pinos1 = [5, 11, 13, 6, 12, 7, 4, 17, 22, 26, 14, 20, 15, 23, 25, 8, 24, 21, 19, 16, 1, 9, 2, 18, 3, 10, 27, 0]
pinos2 = [1, 10, 4, 11, 19, 9, 18, 21, 24, 2, 12, 8, 23, 20, 13, 3, 17, 7, 26, 14, 16, 25, 6, 22, 15, 5, 27, 0]
pinos3 = [2, 4, 6, 8, 10, 12, 3, 16, 18, 20, 24, 22, 26, 14, 25, 5, 9, 23, 7, 1, 11, 13, 21, 19, 17, 15, 27, 0]
pinos4 = [5, 19, 15, 22, 2, 26, 10, 1, 25, 17, 21, 9, 18, 8, 24, 12, 14, 6, 20, 7, 11, 4, 3, 13, 23, 16, 27, 0]
pinos5 = [22, 26, 2, 18, 7, 9, 20, 25, 21, 16, 19, 4, 14, 8, 12, 24, 1, 23, 13, 10, 17, 15, 6, 5, 3, 11, 27, 0]
pinos6 = [27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
pinos7 = [16, 24, 6, 14, 8, 20, 3, 12, 9, 25, 26, 23, 5, 2, 15, 27, 18, 7, 13, 10, 22, 17, 4, 1, 19, 21, 0, 11]

colecao = [pinos1,pinos2,pinos3,pinos4,pinos5,pinos6,pinos7]

ukwa = [4, 9, 12, 25, 0, 11, 24, 23, 21, 1, 22, 5, 2, 17, 16, 20, 14, 13, 19, 18, 15, 8, 10, 7, 6, 3, 27, 26]
ukwb = [24, 17, 20, 7, 27, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 26, 1, 5, 25, 2, 22, 21, 9, 0, 19, 16, 4]
ukwc = [5, 27, 15, 9, 8, 0, 14, 24, 4, 3, 17, 25, 23, 22, 6, 2, 19, 10, 20, 16, 18, 26, 13, 12, 7, 11, 21, 1]

espelhos = {  #dict para vincular um index int com um array e depois o obj UKW importa isso como o codex
    0:ukwa,
    1:ukwb,
    2:ukwc
}

disco = {} #dict para vincular um index int com obj disco

ukw = discos()
etw = discos()
etw.assem = pinos

#============================================================================================
#FUNÇOES PUBLICAS AQUI
def escolher(lugar,discoinp):
    global disco
    disco[lugar] = discos()
    disco[lugar].codex = list(colecao[discoinp])
    disco[lugar].idex = 0
    disco[lugar].pos = lugar
    disco[lugar].rot = disco[lugar].codex[0]
    print(disco[lugar].codex)
             
def refletor(ukwinp):
    global espelhos, ukw
    ukw.mirror = espelhos[ukwinp]

def cripto(texto):
    global disco, espelhos, etw
    saida = ""

    for i in texto:
        a = etw.traduz(i)
        a = disco[0].entrada(a)
        a = disco[1].entrada(a)
        a = disco[2].entrada(a)
        a = disco[3].entrada(a)
        a = disco[4].entrada(a)
        a = ukw.espelho(a)
        a = disco[4].retorno(a)
        a = disco[3].retorno(a)
        a = disco[2].retorno(a)
        a = disco[1].retorno(a)
        a = disco[0].retorno(a)
        a = etw.traduz(a)
        disco[4].ford(disco[3].ford(disco[2].ford(disco[1].ford(disco[0].ford(1)))))
        saida = saida + a
    
    return saida


#=============================================================================
#         CODIGO INTERFACE AQUI
tela = Tk()
mixer.init()


class interface():

    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ç", " "]
    letrasBkp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ç", " "]
    
    #Inicia os parâmetros base da Interface
    def __init__(self):
        self.tela = tela
        self.audio()
        self.menu()
        self.images_menu()
        self.labels_menu()
        self.buttons_menu()
        self.setlbl()
        self.ukw_selection = 0
        self.md_selection = 1
        self.sttp_m = 1
        self.btns_sound = 1
        self.settings_music_m = 0

        self.togg = {
            "a": self.toggle_a,
            "b": self.toggle_b,
            "c": self.toggle_c,
            "d": self.toggle_d,
            "e": self.toggle_e,
            "f": self.toggle_f,
            "g": self.toggle_g,
            "h": self.toggle_h,
            "i": self.toggle_i,
            "j": self.toggle_j,
            "k": self.toggle_k,
            "l": self.toggle_l,
            "m": self.toggle_m,
            "n": self.toggle_n,
            "o": self.toggle_o,
            "p": self.toggle_p,
            "q": self.toggle_q,
            "r": self.toggle_r,
            "s": self.toggle_s,
            "t": self.toggle_t,
            "u": self.toggle_u,
            "v": self.toggle_v,
            "w": self.toggle_w,
            "x": self.toggle_x,
            "y": self.toggle_y,
            "z": self.toggle_z,
            "ç": self.toggle_ç,
            " ": self.toggle_leer
        }

        refletor(0)
        escolher(0,0)
        escolher(1,1)
        escolher(2,2)
        escolher(3,3)
        escolher(4,4)
        
        tela.mainloop()

    #Menu Inicial
    def menu(self):
        self.tela.title("Digital Enigma Machine")
        self.tela.geometry("300x300")
        self.tela.resizable(False, False)
        self.startup_sound.play()
        
    #Função para chamar a imagem da Logo
    def images_menu(self):
        image_path = "Enigma_Cipher\images\menu_bg.png"
        img = Image.open(image_path)
        img = img.resize((400, 300), Image.LANCZOS)
        self.image = (img)
        self.title_image = ImageTk.PhotoImage(self.image)

        st_image_path = "Enigma_Cipher\images\start.jpeg"
        st_img = Image.open(st_image_path)
        st_img = st_img.resize((120, 47), Image.LANCZOS)
        self.st_image = (st_img)
        self.start_image = ImageTk.PhotoImage(self.st_image)

        ex_image_path = "Enigma_Cipher\images\exit.jpeg"
        ex_img = Image.open(ex_image_path)
        ex_img = ex_img.resize((117, 47), Image.LANCZOS)
        self.ex_image = (ex_img)
        self.exit_image = ImageTk.PhotoImage(self.ex_image)

    #Botões
    def buttons_menu(self):
        self.bt_start = Button(self.tela, image=self.start_image, borderwidth=0, command= self.go_to_enigma)
        self.bt_start.place(relx= 0.3, rely=0.55, width=117, height=47)
        
        self.bt_exit = Button(self.tela, image=self.exit_image, borderwidth=0, command= exit)
        self.bt_exit.place(relx= 0.3, rely=0.77, width=117, height=47)
        
    #Imagem da bg
    def labels_menu(self):
        self.lb_title = Label(self.tela, image=self.title_image)
        self.lb_title.place(relx= 0, rely= 0, relwidth= 1, relheight=1)

    #Função para abrir a janela da Enigma
    def go_to_enigma(self):
        enigma = Toplevel()
        self.enigma = enigma
        self.enigma.geometry("652x756")
        self.enigma.resizable(False, False)
        self.enigma_image()
        self.enigma_label()
        self.io()
        self.jumpers()
        self.jumperConfig()
        self.createlbs()
        self.enigma_op.play()
        
    #Função para chamar as imagem da tela da Enigma
    def enigma_image(self):
       
       #Background Image
        bgimage_path = "Enigma_Cipher\images\protorype enigma.jpeg"
        bgimg = Image.open(bgimage_path)
        bgimg = bgimg.resize((652, 756), Image.LANCZOS)
        self.bgimage = (bgimg)
        self.bg_image = ImageTk.PhotoImage(self.bgimage)

        #Settings Button
        setimage_path = "Enigma_Cipher\images\settings.jpeg"
        setimg = Image.open(setimage_path)
        setimg = setimg.resize((50, 50), Image.LANCZOS)
        self.setimage = (setimg)
        self.set_image = ImageTk.PhotoImage(self.setimage)

        #Push Button
        poffimage_path = "Enigma_Cipher\images\PushOff.jpeg"
        poffimg = Image.open(poffimage_path)
        poffimg = poffimg.resize((100, 44), Image.LANCZOS)
        self.poffimage = (poffimg)
        self.poff_image = ImageTk.PhotoImage(self.poffimage)

        ponimage_path = "Enigma_Cipher\images\PushOn.jpeg"
        ponimg = Image.open(ponimage_path)
        ponimg = ponimg.resize((100, 44), Image.LANCZOS)
        self.ponimage = (ponimg)
        self.pon_image = ImageTk.PhotoImage(self.ponimage)

        #Copy Button
        coffimage_path = "Enigma_Cipher\images\CopyOff.jpeg"
        coffimg = Image.open(coffimage_path)
        coffimg = coffimg.resize((40, 25), Image.LANCZOS)
        self.coffimage = (coffimg)
        self.coff_image = ImageTk.PhotoImage(self.coffimage)

        conimage_path = "Enigma_Cipher\images\CopyOn.jpeg"
        conimg = Image.open(conimage_path)
        conimg = conimg.resize((40, 25), Image.LANCZOS)
        self.conimage = (conimg)
        self.con_image = ImageTk.PhotoImage(self.conimage)

        #Replay Buton
        roffimage_path = "Enigma_Cipher\images\ReplayOff.jpeg"
        roffimg = Image.open(roffimage_path)
        roffimg = roffimg.resize((40, 25), Image.LANCZOS)
        self.roffimage = (roffimg)
        self.roff_image = ImageTk.PhotoImage(self.roffimage)

        ronimage_path = "Enigma_Cipher\images\ReplayOn.jpeg"
        ronimg = Image.open(ronimage_path)
        ronimg = ronimg.resize((40, 25), Image.LANCZOS)
        self.ronimage = (ronimg)
        self.ron_image = ImageTk.PhotoImage(self.ronimage)

    #Background da página da enigma
    def enigma_label(self):
        self.lb_bg = Label(self.enigma, image=self.bg_image)
        self.lb_bg.place(relwidth= 1, relheight=1)

    #Buttons change image
    def btns_press(self,event,btn,img,state):
        if state == 1:
            btn.config(image = img )
        if state == 2:
             btn.config(image = img )

    #Imput/Output
    def io(self):

        #Settings Button
        self.start = Button(self.enigma, image=self.set_image, command=self.go_to_settings)
        self.start.place(relx=0.785, rely=0.15, width=50, height=50)

        #Rotors Labels
        self.txt_r1 = "A"
        self.lb_r1 = Label(self.enigma, text=self.txt_r1, font="Arial, 14")
        self.lb_r1.place(relx=0.165, rely=0.185, width=23, height=23)
        
        self.txt_r2 = "A"
        self.lb_r2 = Label(self.enigma, text=self.txt_r2, font="Arial, 14")
        self.lb_r2.place(relx=0.2665, rely=0.185, width=23, height=23)

        self.txt_r3 = "A"
        self.lb_r3 = Label(self.enigma, text=self.txt_r3, font="Arial, 14")
        self.lb_r3.place(relx=0.368, rely=0.187, width=23, height=23)

        self.txt_r4 = "A"
        self.lb_r4 = Label(self.enigma, text=self.txt_r4, font="Arial, 14")
        self.lb_r4.place(relx=0.47, rely=0.187, width=23, height=23)

        self.txt_r5 = "A"
        self.lb_r5 = Label(self.enigma, text=self.txt_r5, font="Arial, 14")
        self.lb_r5.place(relx=0.57, rely=0.187, width=23, height=23)


        #Rotors Buttons
        self.bt_up1 = Button(self.enigma, text="+", command= lambda: self.manualRotor(4,1))
        self.bt_up1.place(relx=0.1678, rely=0.135, width=20, height=20)
        self.bt_dn1 = Button(self.enigma, text="-", command= lambda: self.manualRotor(4,2))
        self.bt_dn1.place(relx=0.1678, rely=0.247, width=20, height=20)
        
        self.bt_up2 = Button(self.enigma, text="+", command= lambda: self.manualRotor(3,1))
        self.bt_up2.place(relx=0.2695, rely=0.135, width=20, height=20)
        self.bt_dn2 = Button(self.enigma, text="-", command= lambda: self.manualRotor(3,2))
        self.bt_dn2.place(relx=0.2695, rely=0.247, width=20, height=20)

        self.bt_up3 = Button(self.enigma, text="+", command= lambda: self.manualRotor(2,1))
        self.bt_up3.place(relx=0.371, rely=0.135, width=20, height=20)
        self.bt_dn3 = Button(self.enigma, text="-", command= lambda: self.manualRotor(2,2))
        self.bt_dn3.place(relx=0.371, rely=0.247, width=20, height=20)

        self.bt_up4 = Button(self.enigma, text="+", command= lambda: self.manualRotor(1,1))
        self.bt_up4.place(relx=0.472, rely=0.135, width=20, height=20)
        self.bt_dn4 = Button(self.enigma, text="-", command= lambda: self.manualRotor(1,2))
        self.bt_dn4.place(relx=0.472, rely=0.247, width=20, height=20)

        self.bt_up5 = Button(self.enigma, text="+", command= lambda: self.manualRotor(0,1))
        self.bt_up5.place(relx=0.573, rely=0.135, width=20, height=20)
        self.bt_dn5 = Button(self.enigma, text="-", command= lambda: self.manualRotor(0,2))
        self.bt_dn5.place(relx=0.573, rely=0.247, width=20, height=20)

        #Rotors ID
        self.lb_id_r1 = Label(self.enigma, text="1")
        self.lb_id_r1.place(relx=0.1678, rely=0.08, width=20, height=20)

        self.lb_id_r2 = Label(self.enigma, text="2")
        self.lb_id_r2.place(relx=0.2695, rely=0.08, width=20, height=20)

        self.lb_id_r3 = Label(self.enigma, text="3")
        self.lb_id_r3.place(relx=0.371, rely=0.08, width=20, height=20)

        self.lb_id_r4 = Label(self.enigma, text="4")
        self.lb_id_r4.place(relx=0.472, rely=0.08, width=20, height=20)

        self.lb_id_r5 = Label(self.enigma, text="5")
        self.lb_id_r5.place(relx=0.573, rely=0.08, width=20, height=20)

        #UKW_badge
        self.txt_ukw_id = "UKW"
        self.ukw_badge_id = Label(self.enigma, text=self.txt_ukw_id)
        self.ukw_badge_id.place(relx=0.045, rely=0.08, width=45, height=20)

        self.txt_ukw_badge = "A"
        self.ukw_badge = Label(self.enigma, text=self.txt_ukw_badge, font="Arial, 14")
        self.ukw_badge.place(relx=0.059, rely=0.177, width=23, height=23)

        #Entrada
        self.lb_ent = Label(self.enigma, text="Entrada")
        self.lb_ent.place(relx=0.1, rely= 0.32, width= 50, height = 25)
        
        self.ent = Entry(self.enigma)
        self.ent.place(relx=0.2, rely= 0.32, width= 500, height = 25)
        self.ent.bind("<Key>", self.teclas)# verifiacor de "/r" precionado para dar input na criptografia

        #Saida
        self.lb_extt = Label(self.enigma, text="Saida")
        self.lb_extt.place(relx=0.1, rely= 0.38, width= 50, height = 25)

        self.lb_ext = Label(self.enigma, text="Esperando Criptografia")
        self.lb_ext.place(relx=0.2, rely= 0.38, width= 500, height = 25)

        #Push Button
        self.p_btn = Button(self.enigma, image=self.poff_image, border=0, command= lambda: self.jumperConfig())
        self.p_btn.place(relx = 0.4, rely = 0.796, width = 100, height= 44)
        self.p_btn.bind("<Button-1>", lambda event: self.btns_press(event,self.p_btn,self.pon_image,1))
        self.p_btn.bind("<ButtonRelease-1>", lambda event: self.btns_press(event, self.p_btn, self.poff_image,2))

        #Copy 
        self.copy_btn = Button(self.enigma, image=self.coff_image,  border=0, highlightthickness=0, command=self.copiometro)
        self.copy_btn.place(relx = 0.02, rely= 0.38, width = 40, height = 25)
        self.copy_btn.bind("<Button-1>", lambda event: self.btns_press(event,self.copy_btn,self.con_image,1))
        self.copy_btn.bind("<ButtonRelease-1>", lambda event: self.btns_press(event, self.copy_btn, self.coff_image,2))

        #Replay
        self.replay_btn = Button(self.enigma, image=self.roff_image, relief="flat", border=0, highlightthickness=0, command=self.lapnspadas)
        self.replay_btn.place(relx = 0.02, rely= 0.32, width = 40, height = 25)
        self.replay_btn.bind("<Button-1>", lambda event: self.btns_press(event,self.replay_btn,self.ron_image,1))
        self.replay_btn.bind("<ButtonRelease-1>", lambda event: self.btns_press(event, self.replay_btn, self.roff_image,2))

    #Jumpers Section
    def jumpers(self):

            #A
            self.j_a = Label(self.enigma, text="A")
            self.j_a.place(relx= 0.07, rely= 0.77, width=17, height=17)

            self.e_a = Entry(self.enigma)
            self.e_a.place(relx= 0.07, rely= 0.86, width=17, height=17)

            #B
            self.j_b = Label(self.enigma, text="B")
            self.j_b.place(relx= 0.1, rely= 0.77, width=17, height=17)

            self.e_b = Entry(self.enigma)
            self.e_b.place(relx= 0.1, rely= 0.86, width=17, height=17)

            #C
            self.j_c = Label(self.enigma, text= "C")
            self.j_c.place(relx= 0.13, rely= 0.77, width=17, height=17)

            self.e_c = Entry(self.enigma)
            self.e_c.place(relx= 0.13, rely= 0.86, width=17, height=17)

            #D
            self.j_d = Label(self.enigma, text="D")
            self.j_d.place(relx= 0.16, rely= 0.77, width=17, height=17)

            self.e_d = Entry(self.enigma)
            self.e_d.place(relx= 0.16, rely= 0.86, width=17, height=17)

            #E
            self.j_e = Label(self.enigma, text="E")
            self.j_e.place(relx= 0.19, rely= 0.77, width=17, height=17)

            self.e_e = Entry(self.enigma)
            self.e_e.place(relx= 0.19, rely= 0.86, width=17, height=17)

            #F
            self.j_f = Label(self.enigma, text="F")
            self.j_f.place(relx= 0.22, rely= 0.77, width=17, height=17)

            self.e_f = Entry(self.enigma)
            self.e_f.place(relx= 0.22, rely= 0.86, width=17, height=17)

            #G
            self.j_g = Label(self.enigma, text="G")
            self.j_g.place(relx= 0.25, rely= 0.77, width=17, height=17)

            self.e_g = Entry(self.enigma)
            self.e_g.place(relx= 0.25, rely= 0.86, width=17, height=17)

            #H
            self.j_h = Label(self.enigma, text="H")
            self.j_h.place(relx= 0.28, rely= 0.77, width=17, height=17)

            self.e_h = Entry(self.enigma)
            self.e_h.place(relx= 0.28, rely= 0.86, width=17, height=17)

            #I
            self.j_i = Label(self.enigma, text="I")
            self.j_i.place(relx= 0.31, rely= 0.77, width=17, height=17)

            self.e_i = Entry(self.enigma)
            self.e_i.place(relx= 0.31, rely= 0.86, width=17, height=17)

            #J
            self.j_j = Label(self.enigma, text="J")
            self.j_j.place(relx= 0.34, rely= 0.77, width=17, height=17)

            self.e_j = Entry(self.enigma)
            self.e_j.place(relx= 0.34, rely= 0.86, width=17, height=17)

            #K
            self.j_k = Label(self.enigma, text="K")
            self.j_k.place(relx= 0.37, rely= 0.77, width=17, height=17)

            self.e_k = Entry(self.enigma)
            self.e_k.place(relx= 0.37, rely= 0.86, width=17, height=17)

            #L
            self.j_l = Label(self.enigma, text="L")
            self.j_l.place(relx= 0.40, rely= 0.77, width=17, height=17)

            self.e_l = Entry(self.enigma)
            self.e_l.place(relx= 0.40, rely= 0.86, width=17, height=17)

            #M
            self.j_m = Label(self.enigma, text="M")
            self.j_m.place(relx= 0.43, rely= 0.77, width=17, height=17)

            self.e_m = Entry(self.enigma)
            self.e_m.place(relx= 0.43, rely= 0.86, width=17, height=17)

            #N
            self.j_n = Label(self.enigma, text="N")
            self.j_n.place(relx= 0.46, rely= 0.77, width=17, height=17)
            
            self.e_n = Entry(self.enigma)
            self.e_n.place(relx= 0.46, rely= 0.86, width=17, height=17)

            #O
            self.j_o = Label(self.enigma, text="O")
            self.j_o.place(relx= 0.49, rely= 0.77, width=17, height=17)
            
            self.e_o = Entry(self.enigma)
            self.e_o.place(relx= 0.49, rely= 0.86, width=17, height=17)
            
            #P
            self.j_p = Label(self.enigma, text="P")
            self.j_p.place(relx= 0.52, rely= 0.77, width=17, height=17)

            self.e_p = Entry(self.enigma)
            self.e_p.place(relx= 0.52, rely= 0.86, width=17, height=17)

            #Q
            self.j_q = Label(self.enigma, text="Q")
            self.j_q.place(relx= 0.55, rely= 0.77, width=17, height=17)

            self.e_q = Entry(self.enigma)
            self.e_q.place(relx= 0.55, rely= 0.86, width=17, height=17)

            #R
            self.j_r = Label(self.enigma, text="R")
            self.j_r.place(relx= 0.58, rely= 0.77, width=17, height=17)

            self.e_r = Entry(self.enigma)
            self.e_r.place(relx= 0.58, rely= 0.86, width=17, height=17)

            #S
            self.j_s = Label(self.enigma, text="S")
            self.j_s.place(relx= 0.61, rely= 0.77, width=17, height=17)

            self.e_s = Entry(self.enigma)
            self.e_s.place(relx= 0.61, rely= 0.86, width=17, height=17)
            
            #T
            self.j_t = Label(self.enigma, text="T")
            self.j_t.place(relx= 0.64, rely= 0.77, width=17, height=17)

            self.e_t = Entry(self.enigma)
            self.e_t.place(relx= 0.64, rely= 0.86, width=17, height=17)

            #U
            self.j_u = Label(self.enigma, text="U")
            self.j_u.place(relx= 0.67, rely= 0.77, width=17, height=17)

            self.e_u = Entry(self.enigma)
            self.e_u.place(relx= 0.67, rely= 0.86, width=17, height=17)

            #V
            self.j_v = Label(self.enigma, text="V")
            self.j_v.place(relx= 0.70, rely= 0.77, width=17, height=17)

            self.e_v = Entry(self.enigma)
            self.e_v.place(relx= 0.70, rely= 0.86, width=17, height=17)

            #W
            self.j_w = Label(self.enigma, text="W")
            self.j_w.place(relx= 0.73, rely= 0.77, width=17, height=17)

            self.e_w = Entry(self.enigma)
            self.e_w.place(relx= 0.73, rely= 0.86, width=17, height=17)

            #X
            self.j_x = Label(self.enigma, text="X")
            self.j_x.place(relx= 0.76, rely= 0.77, width=17, height=17)

            self.e_x = Entry(self.enigma)
            self.e_x.place(relx= 0.76, rely= 0.86, width=17, height=17)

            #Y
            self.j_y = Label(self.enigma, text="Y")
            self.j_y.place(relx= 0.79, rely= 0.77, width=17, height=17)
            
            self.e_y = Entry(self.enigma)
            self.e_y.place(relx= 0.79, rely= 0.86, width=17, height=17)

            #Z
            self.j_z = Label(self.enigma, text="Z")
            self.j_z.place(relx= 0.82, rely= 0.77, width=17, height=17)

            self.e_z = Entry(self.enigma)
            self.e_z.place(relx= 0.82, rely= 0.86, width=17, height=17)

            #Ç
            self.j_ç = Label(self.enigma, text="Ç")
            self.j_ç.place(relx= 0.85, rely= 0.77, width=17, height=17)

            self.e_ç = Entry(self.enigma)
            self.e_ç.place(relx= 0.85, rely= 0.86, width=17, height=17)

            #leer
            self.j_leer = Label(self.enigma, text="-")
            self.j_leer.place(relx= 0.88, rely= 0.77, width=17, height=17)

            self.e_leer = Entry(self.enigma)
            self.e_leer.place(relx= 0.88, rely= 0.86, width=17, height=17)  
            
    #Função para abrir a tela de configurações    
    def go_to_settings(self):
        settings = Toplevel()
        self.settings = settings
        self.settings.title("Settings")
        self.settings.geometry("365x365")
        self.settings.configure(background= "#2E462E")
        self.settings_bg()
        self.settings_io()
        self.settings_sound.play()
        self.menu_still()
        
    #Frames da settings
    def settings_bg(self):

        self.rotors_frame = Frame(self.settings, bg="#9FA1AD")
        self.rotors_frame.place(relx= 0.04, rely= 0.05, width= 205, height= 220)

        self.lbl_rotor_title = Label(self.rotors_frame, text="Selecione um rotor para cada slot")
        self.lbl_rotor_title.place(relx= 0, rely=0, width= 205, height= 30)

        self.volume_frame = Frame(self.settings, bg="#FD6161")
        self.volume_frame.place(relx= 0.64, rely= 0.05, width=120, height= 220 )

        self.lbl_volume_tittle = Label(self.volume_frame, text= "Configuração de Sons")
        self.lbl_volume_tittle.place(relx= 0, rely= 0, width= 120, height= 30)

        self.ukw_frame = Frame(self.settings, bg="#AEF705")
        self.ukw_frame.place(relx = 0.04, rely=0.7, width = 205, height= 80)

        self.lbl_ukw_title = Label(self.ukw_frame, text="Selecione o UKW")
        self.lbl_ukw_title.place(relx=0, rely= 0, width=205, height=20)

        self.modes_frame = Frame(self.settings, bg="#F179B1")
        self.modes_frame.place(relx=0.64, rely=0.7, width= 120, height= 47 )

        self.modes_title = Label(self.modes_frame, text="Selecione o Modo")
        self.modes_title.place(relx = 0, rely=0, width= 120, height= 20)
        
    def settings_io(self):

        #Labels Rotores
        self.lbl_r1s = Label(self.rotors_frame, text="Slot Rotor 01")
        self.lbl_r1s.place(relx= 0, rely = 0.25, width= 70, height=17)

        self.lbl_r2s = Label(self.rotors_frame, text="Slot Rotor 02")
        self.lbl_r2s.place(relx= 0, rely = 0.40, width= 70, height=17)

        self.lbl_r3s = Label(self.rotors_frame, text="Slot Rotor 03")
        self.lbl_r3s.place(relx= 0, rely = 0.55, width= 70, height=17)

        self.lbl_r4s = Label(self.rotors_frame, text="Slot Rotor 04")
        self.lbl_r4s.place(relx= 0, rely = 0.70, width= 70, height=17)

        self.lbl_r5s = Label(self.rotors_frame, text="Slot Rotor 05")
        self.lbl_r5s.place(relx= 0, rely = 0.85, width= 70, height=17)

        
        #Rotors Select Buttons
        self.slot1_sel_clr = "#E21F1F"
        self.slot2_sel_clr = "#CEE21F"
        self.slot3_sel_clr = "#00A84C"
        self.slot4_sel_clr = "#3C1FE2"
        self.slot5_sel_clr = "#A10030"

        self.slot1_og_clr = "#f08b8b"
        self.slot2_og_clr = "#b8f08b"
        self.slot3_og_clr = "#6f9fa5"
        self.slot4_og_clr = "#9d8bf0"
        self.slot5_og_clr = "#f08bce"
        
        alt = 15

        #Slot 1
        self.slt1_1 = Button(self.rotors_frame, text="1", bg= self.slot1_sel_clr, command=lambda: self.slot_rotor(1,1))
        self.slt1_1.place(relx= 0.37, rely= 0.25, width= alt, height= alt)

        self.slt1_2 = Button(self.rotors_frame, text="2", bg= self.slot2_sel_clr, command=lambda: self.slot_rotor(1,2))
        self.slt1_2.place(relx= 0.46, rely= 0.25, width= alt, height= alt)

        self.slt1_3 = Button(self.rotors_frame, text="3", bg= self.slot3_sel_clr, command=lambda: self.slot_rotor(1,3))
        self.slt1_3.place(relx= 0.55, rely= 0.25, width= alt, height= alt)

        self.slt1_4 = Button(self.rotors_frame, text="4", bg= self.slot4_sel_clr, command=lambda: self.slot_rotor(1,4))
        self.slt1_4.place(relx= 0.64, rely= 0.25, width= alt, height= alt)

        self.slt1_5 = Button(self.rotors_frame, text="5", bg= self.slot5_sel_clr, command=lambda: self.slot_rotor(1,5))
        self.slt1_5.place(relx= 0.73, rely= 0.25, width= alt, height= alt)

        self.slt1_6 = Button(self.rotors_frame, text="6", bg= self.slot1_og_clr, command=lambda: self.slot_rotor(1,6))
        self.slt1_6.place(relx= 0.82, rely= 0.25, width= alt, height= alt)

        self.slt1_7 = Button(self.rotors_frame, text="7", bg= self.slot1_og_clr, command=lambda: self.slot_rotor(1,7))
        self.slt1_7.place(relx= 0.91, rely= 0.25, width= alt, height= alt)


        #Slot 2
        self.slt2_1 = Button(self.rotors_frame, text="1", bg= self.slot1_sel_clr, command=lambda: self.slot_rotor(2,1))
        self.slt2_1.place(relx= 0.37, rely= 0.40, width= alt, height= alt)

        self.slt2_2 = Button(self.rotors_frame, text="2", bg= self.slot2_sel_clr, command=lambda: self.slot_rotor(2,2))
        self.slt2_2.place(relx= 0.46, rely= 0.40, width= alt, height= alt)

        self.slt2_3 = Button(self.rotors_frame, text="3", bg= self.slot3_sel_clr, command=lambda: self.slot_rotor(2,3))
        self.slt2_3.place(relx= 0.55, rely= 0.40, width= alt, height= alt)

        self.slt2_4 = Button(self.rotors_frame, text="4", bg= self.slot4_sel_clr, command=lambda: self.slot_rotor(2,4))
        self.slt2_4.place(relx= 0.64, rely= 0.40, width= alt, height= alt)

        self.slt2_5 = Button(self.rotors_frame, text="5", bg= self.slot5_sel_clr, command=lambda: self.slot_rotor(2,5))
        self.slt2_5.place(relx= 0.73, rely= 0.40, width= alt, height= alt)

        self.slt2_6 = Button(self.rotors_frame, text="6", bg= self.slot2_og_clr, command=lambda: self.slot_rotor(2,6))
        self.slt2_6.place(relx= 0.82, rely= 0.40, width= alt, height= alt)

        self.slt2_7 = Button(self.rotors_frame, text="7", bg= self.slot2_og_clr, command=lambda: self.slot_rotor(2,7))
        self.slt2_7.place(relx= 0.91, rely= 0.40, width= alt, height= alt)


        #Slot 3
        self.slt3_1 = Button(self.rotors_frame, text="1", bg= self.slot1_sel_clr, command=lambda: self.slot_rotor(3,1))
        self.slt3_1.place(relx= 0.37, rely= 0.55, width= alt, height= alt)

        self.slt3_2 = Button(self.rotors_frame, text="2", bg= self.slot2_sel_clr, command=lambda: self.slot_rotor(3,2))
        self.slt3_2.place(relx= 0.46, rely= 0.55, width= alt, height= alt)

        self.slt3_3 = Button(self.rotors_frame, text="3", bg= self.slot3_sel_clr, command=lambda: self.slot_rotor(3,3))
        self.slt3_3.place(relx= 0.55, rely= 0.55, width= alt, height= alt)

        self.slt3_4 = Button(self.rotors_frame, text="4", bg= self.slot4_sel_clr, command=lambda: self.slot_rotor(3,4))
        self.slt3_4.place(relx= 0.64, rely= 0.55, width= alt, height= alt)

        self.slt3_5 = Button(self.rotors_frame, text="5", bg= self.slot5_sel_clr, command=lambda: self.slot_rotor(3,5))
        self.slt3_5.place(relx= 0.73, rely= 0.55, width= alt, height= alt)

        self.slt3_6 = Button(self.rotors_frame, text="6", bg= self.slot3_og_clr, command=lambda: self.slot_rotor(3,6))
        self.slt3_6.place(relx= 0.82, rely= 0.55, width= alt, height= alt)

        self.slt3_7 = Button(self.rotors_frame, text="7", bg= self.slot3_og_clr, command=lambda: self.slot_rotor(3,7))
        self.slt3_7.place(relx= 0.91, rely= 0.55, width= alt, height= alt)


        #Slot 4
        self.slt4_1 = Button(self.rotors_frame, text="1", bg= self.slot1_sel_clr, command=lambda: self.slot_rotor(4,1))
        self.slt4_1.place(relx= 0.37, rely= 0.7, width= alt, height= alt)

        self.slt4_2 = Button(self.rotors_frame, text="2", bg= self.slot2_sel_clr, command=lambda: self.slot_rotor(4,2))
        self.slt4_2.place(relx= 0.46, rely= 0.7, width= alt, height= alt)

        self.slt4_3 = Button(self.rotors_frame, text="3", bg= self.slot3_sel_clr, command=lambda: self.slot_rotor(4,3))
        self.slt4_3.place(relx= 0.55, rely= 0.7, width= alt, height= alt)

        self.slt4_4 = Button(self.rotors_frame, text="4", bg= self.slot4_sel_clr, command=lambda: self.slot_rotor(4,4))
        self.slt4_4.place(relx= 0.64, rely= 0.7, width= alt, height= alt)

        self.slt4_5 = Button(self.rotors_frame, text="5", bg= self.slot5_sel_clr, command=lambda: self.slot_rotor(4,5))
        self.slt4_5.place(relx= 0.73, rely= 0.7, width= alt, height= alt)

        self.slt4_6 = Button(self.rotors_frame, text="6", bg= self.slot4_og_clr, command=lambda: self.slot_rotor(4,6))
        self.slt4_6.place(relx= 0.82, rely= 0.7, width= alt, height= alt)

        self.slt4_7 = Button(self.rotors_frame, text="7", bg= self.slot4_og_clr, command=lambda: self.slot_rotor(4,7))
        self.slt4_7.place(relx= 0.91, rely= 0.7, width= alt, height= alt)


        #Slot 5
        self.slt5_1 = Button(self.rotors_frame, text="1", bg= self.slot1_sel_clr, command=lambda: self.slot_rotor(5,1))
        self.slt5_1.place(relx= 0.37, rely= 0.85, width= alt, height= alt)

        self.slt5_2 = Button(self.rotors_frame, text="2", bg= self.slot2_sel_clr, command=lambda: self.slot_rotor(5,2))
        self.slt5_2.place(relx= 0.46, rely= 0.85, width= alt, height= alt)

        self.slt5_3 = Button(self.rotors_frame, text="3", bg= self.slot3_sel_clr, command=lambda: self.slot_rotor(5,3))
        self.slt5_3.place(relx= 0.55, rely= 0.85, width= alt, height= alt)

        self.slt5_4 = Button(self.rotors_frame, text="4", bg= self.slot4_sel_clr, command=lambda: self.slot_rotor(5,4))
        self.slt5_4.place(relx= 0.64, rely= 0.85, width= alt, height= alt)

        self.slt5_5 = Button(self.rotors_frame, text="5", bg= self.slot5_sel_clr, command=lambda: self.slot_rotor(5,5))
        self.slt5_5.place(relx= 0.73, rely= 0.85, width= alt, height= alt)

        self.slt5_6 = Button(self.rotors_frame, text="6", bg= self.slot5_og_clr, command=lambda: self.slot_rotor(5,6))
        self.slt5_6.place(relx= 0.82, rely= 0.85, width= alt, height= alt)

        self.slt5_7 = Button(self.rotors_frame, text="7", bg= self.slot5_og_clr, command=lambda: self.slot_rotor(5,7))
        self.slt5_7.place(relx= 0.91, rely= 0.85, width= alt, height= alt)


        # Criação do sistema de seleção
        self.rotor_state = {r: 0 for r in range(1, 8)}
        self.slot_state = {s: 0 for s in range(1, 6)}

        self.slot_sel_clrs = [None, self.slot1_sel_clr, self.slot2_sel_clr, self.slot3_sel_clr, self.slot4_sel_clr, self.slot5_sel_clr]

        self.slot_og_clrs = [None, self.slot1_og_clr, self.slot2_og_clr, self.slot3_og_clr, self.slot4_og_clr, self.slot5_og_clr]

        self.all_slt_buttons = [
            None,  # Placeholder para Slot 0
            [None, self.slt1_1, self.slt1_2, self.slt1_3, self.slt1_4, self.slt1_5, self.slt1_6, self.slt1_7], # Slot 1 
            [None, self.slt2_1, self.slt2_2, self.slt2_3, self.slt2_4, self.slt2_5, self.slt2_6, self.slt2_7], # Slot 2
            [None, self.slt3_1, self.slt3_2, self.slt3_3, self.slt3_4, self.slt3_5, self.slt3_6, self.slt3_7], # Slot 3
            [None, self.slt4_1, self.slt4_2, self.slt4_3, self.slt4_4, self.slt4_5, self.slt4_6, self.slt4_7], # Slot 4
            [None, self.slt5_1, self.slt5_2, self.slt5_3, self.slt5_4, self.slt5_5, self.slt5_6, self.slt5_7]  # Slot 5
            ]


        #UKW Selector
        self.ukw_sel_clr = "#F85B5B"

        self.ukw_a_og_clr = "#3CA1DB"
        self.ukw_a = Button(self.ukw_frame, text="A", bg=self.ukw_sel_clr, command=lambda: self.ukw_selector(0))
        self.ukw_a.place(relx= 0.1, rely=0.4, width=30, height=30)

        self.ukw_b_og_clr = "#3ADA2C"
        self.ukw_b = Button(self.ukw_frame, text="B", bg=self.ukw_b_og_clr, command=lambda: self.ukw_selector(1))
        self.ukw_b.place(relx= 0.4, rely=0.4, width=30, height=30)
                         
        self.ukw_c_og_clr = "#C9B6E7"
        self.ukw_c = Button(self.ukw_frame, text="C", bg=self.ukw_c_og_clr, command=lambda: self.ukw_selector(2))
        self.ukw_c.place(relx= 0.7, rely=0.4, width=30, height=30)


        #Sound System
        self.on_clr = "#07c700"
        self.off_clr = "#9C2323"
        vlmsize = 23

        self.startup_lbl = Label(self.volume_frame, text="Startup Sound")
        self.startup_lbl.place(relx=0.08, rely= 0.2, width = 100, height=20)
        self.startup_on = Button(self.volume_frame, text= "On ", bg= self.on_clr, command=lambda: self.audio_control(1,1))
        self.startup_on.place(relx = 0.2, rely = 0.31, width = vlmsize, height = vlmsize)
        self.startup_off = Button(self.volume_frame, text= "Off ", bg=self.off_clr, command=lambda: self.audio_control(1,0))
        self.startup_off.place(relx = 0.6, rely = 0.31, width = vlmsize, height = vlmsize)

        self.btns_lbl = Label(self.volume_frame, text= "Buttons/Typing")
        self.btns_lbl.place(relx= 0.08, rely= 0.45, width=100, heigh= 20)
        self.btns_sound_on = Button(self.volume_frame, text= "On ", bg= self.on_clr, command=lambda: self.audio_control(2,1))
        self.btns_sound_on.place(relx = 0.2, rely = 0.56, width = vlmsize, height = vlmsize)
        self.btns_sound_off = Button(self.volume_frame, text= "Off ", bg= self.off_clr, command=lambda: self.audio_control(2,0))
        self.btns_sound_off.place(relx = 0.6, rely = 0.56, width = vlmsize, height = vlmsize)

        self.setm_lbl = Label(self.volume_frame, text= "Music")
        self.setm_lbl.place(relx= 0.08, rely= 0.7, width=100, heigh= 20)
        self.setm_on = Button(self.volume_frame, text= "On ", bg= self.off_clr, command=lambda: self.audio_control(3,1))
        self.setm_on.place(relx = 0.2, rely = 0.81, width = vlmsize, height = vlmsize)
        self.setm_off = Button(self.volume_frame, text= "Off ", bg=self.on_clr, command=lambda: self.audio_control(3,0))
        self.setm_off.place(relx = 0.6, rely = 0.81, width = vlmsize, height = vlmsize)

        #Modes Selector
        self.mode_sel_clr = "#FFFFFF"

        self.classic_mode_og_clr = "#F8F674"
        self.classic_mode_btn = Button(self.modes_frame, text="CLASSIC", bg= self.mode_sel_clr, command=lambda: self.modes_selection(1))
        self.classic_mode_btn.place(relx = 0.05, rely = 0.47, width=50, height=20)

        self.digital_mode_og_clr = "#958AF8"
        self.digital_mode_btn = Button(self.modes_frame, text="DIGITAL", bg= self.digital_mode_og_clr, command=lambda: self.modes_selection(2))
        self.digital_mode_btn.place(relx = 0.55, rely = 0.47, width=50, height=20)


        #Close Button
        self.close_btn = Button(self.settings, text = "Fechar", font="15", bg="#7CEE4F", command=self.back_from_settings)
        self.close_btn.place(relx= 0.64, rely= 0.85, width=120, height=24)



        self.slot1 = 0
        self.slot2 = 0
        self.slot3 = 0
        self.slot4 = 0
        self.slot5 = 0

    def back_from_settings(self):
        self.back_from_sound.play()
        self.settings.destroy()

    #UKW selection
    def ukw_selector(self, md):

        if md == 0:
            self.ukw_a.config(bg=self.ukw_sel_clr)
            self.ukw_b.config(bg=self.ukw_b_og_clr)
            self.ukw_c.config(bg=self.ukw_c_og_clr)
            self.ukw_badge.config(text=pinoIndex[0])
            self.ukw_selection = 0
            print("UKW:", self.ukw_selection)
            refletor(0)
        
        if md == 1:
            self.ukw_a.config(bg=self.ukw_a_og_clr)
            self.ukw_b.config(bg=self.ukw_sel_clr)
            self.ukw_c.config(bg=self.ukw_c_og_clr)
            self.ukw_badge.config(text=pinoIndex[1])
            self.ukw_selection = 1
            print("UKW:", self.ukw_selection)
            refletor(1)

        if md == 2:
            self.ukw_a.config(bg=self.ukw_a_og_clr)
            self.ukw_b.config(bg=self.ukw_b_og_clr)
            self.ukw_c.config(bg=self.ukw_sel_clr)
            self.ukw_badge.config(text=pinoIndex[2])
            print("UKW:", self.ukw_selection)
            self.ukw_selection = 2
            refletor(2)

    #Modes selection
    def modes_selection(self, mode):
        
        if mode == 1:
            self.md_selection = 1
            self.classic_mode_btn.config(bg=self.mode_sel_clr)
            self.digital_mode_btn.config(bg=self.digital_mode_og_clr)
            print("MD:", self.md_selection)

        if mode == 2:
            self.md_selection = 2
            self.classic_mode_btn.config(bg=self.classic_mode_og_clr)
            self.digital_mode_btn.config(bg=self.mode_sel_clr)
            print("MD:", self.md_selection)

#=========================================================================AREA DE CONTEÇÃO==========================
    #REPOSITORIO DE CODIGO COELHO DELTA
    
    def teclas(self,event):
        if event.keysym == "Return" and self.md_selection == 2:
            self.input_texto()

        if event.keysym != "Return" and self.md_selection == 1 and event.keysym != "BackSpace":
            

            if event.keysym == "ccedilla":
                buffer = (self.codigoJumper(cripto(self.codigoJumper("ç"))))
            
            elif event.keysym == "space":
                buffer = (self.codigoJumper(cripto(self.codigoJumper(" "))))
            
            else:
                buffer = (self.codigoJumper(cripto(self.codigoJumper(event.keysym))))           
                          
            print(buffer)

            self.lb_r5.config(text=pinoIndex[disco[0].idex])
            self.lb_r4.config(text=pinoIndex[disco[1].idex])
            self.lb_r3.config(text=pinoIndex[disco[2].idex])
            self.lb_r2.config(text=pinoIndex[disco[3].idex])
            self.lb_r1.config(text=pinoIndex[disco[4].idex])

            self.togg[str(buffer)]()
            self.enigma.update()
            sleep(1.35)
            self.togg[str(buffer)]()
            self.enigma.update()

    
    def input_texto(self):
        self.lb_ext.config(text=(self.codigoJumper(cripto(self.codigoJumper(self.ent.get())))))
        self.lapnspadas()
        self.enigma.update_idletasks()
    
        self.lb_r5.config(text=pinoIndex[disco[0].idex])
        self.lb_r4.config(text=pinoIndex[disco[1].idex])
        self.lb_r3.config(text=pinoIndex[disco[2].idex])
        self.lb_r2.config(text=pinoIndex[disco[3].idex])
        self.lb_r1.config(text=pinoIndex[disco[4].idex])

    def manualRotor(self, pos, metodo):             #recebe posiçao de qual rotor o botao foi pressionado, metodo1 para avançar, metodo2 para regredir

        if metodo == 1:

            print(disco[pos].idex)
            print(disco[pos].codex)

            buffer = disco[pos].codex[0]

            for x in range(len(disco[pos].codex)):
                if x < len(disco[pos].codex)-1:
                    disco[pos].codex[x] = disco[pos].codex[x+1]

            disco[pos].codex[len(disco[pos].codex)-1] = buffer
            
            if disco[pos].idex <= 26:
                disco[pos].idex = disco[pos].idex+1
            else:
                disco[pos].idex = 0

            print(disco[pos].idex)
            print(disco[pos].codex)

        elif metodo == 2:

            print(disco[pos].idex)
            print(disco[pos].codex)

            buffer = disco[pos].codex[27]

            for x in range(27,-1,-1):
                if x > 0:
                    disco[pos].codex[x] = disco[pos].codex[x-1]

            disco[pos].codex[0] = buffer
            
            if disco[pos].idex >= 1:
                disco[pos].idex = disco[pos].idex-1
            else:
                disco[pos].idex = 27
            
            print(disco[pos].idex)
            print(disco[pos].codex)


        self.rotor_change.play()

        self.lb_r5.config(text=pinoIndex[disco[0].idex])
        self.lb_r4.config(text=pinoIndex[disco[1].idex])
        self.lb_r3.config(text=pinoIndex[disco[2].idex])
        self.lb_r2.config(text=pinoIndex[disco[3].idex])
        self.lb_r1.config(text=pinoIndex[disco[4].idex])

    def codigoJumper(self,texto):                   #codigo de leitura do array letras(que ser configurado nos jumpers)
        
        buffer = []
        buffer2 = ""

        for x in list(texto):                       #tratamento para espaços
            if(x == "-"):
                buffer.append(self.letras.index(" "))
            else:
                buffer.append(self.letras.index(x))

        print(buffer)#depuraçao

        for x in buffer:
            buffer2 = buffer2 + self.letrasBkp[x]

        print(buffer2)#depuraçao
        return buffer2

    def jumperConfig(self):
        self.letras[0] = self.e_a.get()
        self.letras[1] = self.e_b.get()
        self.letras[2] = self.e_c.get()
        self.letras[3] = self.e_d.get()
        self.letras[4] = self.e_e.get()
        self.letras[5] = self.e_f.get()
        self.letras[6] = self.e_g.get()
        self.letras[7] = self.e_h.get()
        self.letras[8] = self.e_i.get()
        self.letras[9] = self.e_j.get()
        self.letras[10] = self.e_k.get()
        self.letras[11] = self.e_l.get()
        self.letras[12] = self.e_m.get()
        self.letras[13] = self.e_n.get()
        self.letras[14] = self.e_o.get()
        self.letras[15] = self.e_p.get()
        self.letras[16] = self.e_q.get()
        self.letras[17] = self.e_r.get()
        self.letras[18] = self.e_s.get()
        self.letras[19] = self.e_t.get()
        self.letras[20] = self.e_u.get()
        self.letras[21] = self.e_v.get()
        self.letras[22] = self.e_w.get()
        self.letras[23] = self.e_x.get()
        self.letras[24] = self.e_y.get()
        self.letras[25] = self.e_z.get()
        self.letras[26] = self.e_ç.get()
        self.letras[27] = self.e_leer.get()

        for x in range(0,28):                               #tratamento do input dos jumpers, se input nulo entao nao troca 
            if self.letras[x] == "":
                self.letras[x] = self.letrasBkp[x]
                
            
            if self.letras[x] == "-":                       #tratamento do input dos jumpers, para trocar "-" por " "
                self.letras[x] = " "

        
        for x in range(0,28):                               #tramento do input jumper para ser reversivel, Se A = B entao B = A
            letra1 = self.letras[x]
            posO = self.letrasBkp.index(letra1)
            self.letras[posO] = self.letrasBkp[x]

        
        print(self.letras)

    def copiometro(self):
        self.enigma.update_idletasks()
        buffer = self.lb_ext.cget("text")
        print(buffer)
        self.enigma.clipboard_clear()
        self.enigma.clipboard_append(buffer)
        self.enigma.update()

    def lapnspadas(self):
        buffer = self.lb_ext.cget("text")
        for x in buffer:
            print(x)
            self.togg[str(x)]()
            self.enigma.update()
            sleep(0.155)
            self.togg[str(x)]()
            self.enigma.update()
            
#====================================================================================================================
    # Cor do Selection do Rotor
    def slot_rotor(self, slot, rotor):
        
        escolher(slot-1,rotor-1)

        rotor_anterior = self.slot_state[slot]
        new_rotor_sel = self.rotor_state[rotor]

        if slot == 1 and rotor == 1:
            self.slot1 = 0
            self.lb_id_r1.config(text="1")

        if slot == 1 and rotor == 2:
            self.slot1 = 1
            self.lb_id_r1.config(text="2")

        if slot == 1 and rotor == 3:
            self.slot1 = 2
            self.lb_id_r1.config(text="3")

        if slot == 1 and rotor == 4:
            self.slot1 = 3
            self.lb_id_r1.config(text="4")

        if slot == 1 and rotor == 5:
            self.slot1 = 4
            self.lb_id_r1.config(text="5")
        
        if slot == 1 and rotor == 6:
            self.slot1 = 5
            self.lb_id_r1.config(text="6")
        
        if slot ==1 and rotor == 7:
            self.slot1 = 6
            self.lb_id_r1.config(text="7")
        
        if slot == 2 and rotor == 1:
            self.slot2 = 0
            self.lb_id_r2.config(text="1")

        if slot == 2 and rotor == 2:
            self.slot2 = 1
            self.lb_id_r2.config(text="2")

        if slot == 2 and rotor == 3:
            self.slot2 = 2
            self.lb_id_r2.config(text="3")

        if slot == 2 and rotor == 4:
            self.slot2 = 3
            self.lb_id_r2.config(text="4")

        if slot == 2 and rotor == 5:
            self.slot2 = 4
            self.lb_id_r2.config(text="5")
        
        if slot == 2 and rotor == 6:
            self.slot2 = 5
            self.lb_id_r2.config(text="6")
        
        if slot ==2 and rotor == 7:
            self.slot2 = 6
            self.lb_id_r2.config(text="7")

        if slot == 3 and rotor == 1:
            self.slot3 = 0
            self.lb_id_r3.config(text="1")

        if slot == 3 and rotor == 2:
            self.slot3 = 1
            self.lb_id_r3.config(text="2")

        if slot == 3 and rotor == 3:
            self.slot3 = 2
            self.lb_id_r3.config(text="3")

        if slot == 3 and rotor == 4:
            self.slot3 = 3
            self.lb_id_r3.config(text="4")

        if slot == 3 and rotor == 5:
            self.slot3 = 4
            self.lb_id_r3.config(text="5")
        
        if slot == 3 and rotor == 6:
            self.slot3 = 5
            self.lb_id_r3.config(text="6")
        
        if slot == 3 and rotor == 7:
            self.slot3 = 6
            self.lb_id_r3.config(text="7")

        if slot == 4 and rotor == 1:
            self.slot4 = 0
            self.lb_id_r4.config(text="1")

        if slot == 4 and rotor == 2:
            self.slot4 = 1
            self.lb_id_r4.config(text="2")

        if slot == 4 and rotor == 3:
            self.slot4 = 2
            self.lb_id_r4.config(text="3")

        if slot == 4 and rotor == 4:
            self.slot4 = 3
            self.lb_id_r4.config(text="4")

        if slot == 4 and rotor == 5:
            self.slot4 = 4
            self.lb_id_r4.config(text="5")
        
        if slot == 4 and rotor == 6:
            self.slot4 = 5
            self.lb_id_r4.config(text="6")
        
        if slot == 4 and rotor == 7:
            self.slot4 = 6
            self.lb_id_r4.config(text="7")

        if slot == 5 and rotor == 1:
            self.slot5 = 0
            self.lb_id_r5.config(text="1")

        if slot == 5 and rotor == 2:
            self.slot5 = 1
            self.lb_id_r5.config(text="2")

        if slot == 5 and rotor == 3:
            self.slot5 = 2
            self.lb_id_r5.config(text="3")

        if slot == 5 and rotor == 4:
            self.slot5 = 3
            self.lb_id_r5.config(text="4")

        if slot == 5 and rotor == 5:
            self.slot5 = 4
            self.lb_id_r5.config(text="5")
        
        if slot == 5 and rotor == 6:
            self.slot5 = 5
            self.lb_id_r5.config(text="6")
        
        if slot == 5 and rotor == 7:
            self.slot5 = 6
            self.lb_id_r5.config(text="7")

    
        print("Slot1: {}".format(self.slot1))
        print("Slot2: {}".format(self.slot2))
        print("Slot3: {}".format(self.slot3))
        print("Slot4: {}".format(self.slot4))
        print("Slot5: {}\n".format(self.slot5))

        
        if new_rotor_sel == slot:
            self.rotor_state[rotor] = 0
            self.slot_state[slot] = 0
            
        else:
            
            if rotor_anterior != 0:
                
                self.rotor_state[rotor_anterior] = 0
    
           
            if new_rotor_sel != 0:
                
                self.slot_state[new_rotor_sel] = 0
            
            self.rotor_state[rotor] = slot  
            self.slot_state[slot] = rotor  


        for s in range(1, 6):
            cor_original_do_slot = self.slot_og_clrs[s]
            
            for r in range(1, 8):
                button = self.all_slt_buttons[s][r]
                
                slot_novo = self.rotor_state[r]
                
                if slot_novo != 0:
                    
                    cor_realce = self.slot_sel_clrs[slot_novo]
                    button.config(bg=cor_realce) 
                
                else:
                   
                    button.config(bg=cor_original_do_slot)

    #Faz com que os menus continuem acesos caso entre e saia da settings
    def menu_still(self):

        
        if self.ukw_selection == 0:
            self.ukw_a.config(bg=self.ukw_sel_clr)
            self.ukw_b.config(bg=self.ukw_b_og_clr)
            self.ukw_c.config(bg=self.ukw_c_og_clr)
        if self.ukw_selection == 1:
            self.ukw_a.config(bg=self.ukw_a_og_clr)
            self.ukw_b.config(bg=self.ukw_sel_clr)
            self.ukw_c.config(bg=self.ukw_c_og_clr)
        if self.ukw_selection == 2:
            self.ukw_a.config(bg=self.ukw_a_og_clr)
            self.ukw_b.config(bg=self.ukw_b_og_clr)
            self.ukw_c.config(bg=self.ukw_sel_clr)

        if self.md_selection == 1:
            self.classic_mode_btn.config(bg=self.mode_sel_clr)
            self.digital_mode_btn.config(bg=self.digital_mode_og_clr)
        if self.md_selection == 2:
            self.classic_mode_btn.config(bg=self.classic_mode_og_clr)
            self.digital_mode_btn.config(bg=self.mode_sel_clr)

        if self.sttp_m == 1:
            self.startup_on.config(bg=self.on_clr)
            self.startup_off.config(bg=self.off_clr)
        if self.sttp_m == 0:
            self.startup_on.config(bg=self.off_clr)
            self.startup_off.config(bg=self.on_clr)

        if self.btns_sound == 1:
            self.btns_sound_on.config(bg=self.on_clr)
            self.btns_sound_off.config(bg=self.off_clr)
        if self.btns_sound == 0:
            self.btns_sound_on.config(bg=self.off_clr)
            self.btns_sound_off.config(bg=self.on_clr)
            
        if self.settings_music_m == 1:
            self.setm_on.config(bg=self.on_clr)
            self.setm_off.config(bg=self.off_clr)
        if self.settings_music_m == 0:
            self.setm_on.config(bg=self.off_clr)
            self.setm_off.config(bg=self.on_clr)

    #Audio

    #Inicia os players
    def audio(self):

        #Startup
        self.startup_sound = mixer.Sound("Enigma_Cipher\sounds\Ps1 startup sound(MP3_320K).mp3")

        #Enigma Opening
        self.enigma_op = mixer.Sound("Enigma_Cipher\sounds\Jingle.mp3")

        #Typing
        self.tiping = mixer.Sound("Enigma_Cipher\sounds\Typewriter.mp3")

        #Changing Rotor Position
        self.rotor_change = mixer.Sound("Enigma_Cipher\sounds\Ding.mp3")

        #Settings Button
        self.settings_sound = mixer.Sound("Enigma_Cipher\sounds\Piston Out.mp3")

        #Settings Out
        self.back_from_sound = mixer.Sound("Enigma_Cipher\sounds\Piston In.mp3")

        #Settings Music
        mixer.music.load("Enigma_Cipher\sounds\Portal Radio.mp3")
    
    def audio_control(self,btn,state):

        if  btn == 1 and state == 1:
            self.startup_sound.set_volume(1)
            self.enigma_op.set_volume(1)
            self.startup_on.config(bg=self.on_clr)
            self.startup_off.config(bg=self.off_clr)
            self.sttp_m = 1
            print(state)

        if  btn == 1 and state == 0:
            self.startup_sound.set_volume(0)
            self.enigma_op.set_volume(0)
            self.startup_on.config(bg=self.off_clr)
            self.startup_off.config(bg=self.on_clr)
            self.sttp_m= 0
            print(state)

        if btn == 2 and state == 1:
            self.tiping.set_volume(1)
            self.settings_sound.set_volume(1)
            self.back_from_sound.set_volume(1)
            self.rotor_change.set_volume(1)
            self.btns_sound_on.config(bg=self.on_clr)
            self.btns_sound_off.config(bg=self.off_clr)
            self.btns_sound = 1
            print(state)

        if btn == 2 and state == 0:
            self.tiping.set_volume(0)
            self.settings_sound.set_volume(0)
            self.back_from_sound.set_volume(0)
            self.rotor_change.set_volume(0)
            self.btns_sound_on.config(bg=self.off_clr)
            self.btns_sound_off.config(bg=self.on_clr)
            self.btns_sound = 0
            print(state)

        if btn == 3 and state == 1:
            mixer.music.play(-1)
            self.setm_on.config(bg=self.on_clr)
            self.setm_off.config(bg=self.off_clr)
            self.settings_music_m = 1
            
            print(state)
        if btn == 3 and state == 0:
            mixer.music.stop()
            self.setm_on.config(bg=self.off_clr)
            self.setm_off.config(bg=self.on_clr)
            self.settings_music_m = 0

            
            print(state)
        
    #Letters

    #Set Visibillity Letras
    def setlbl(self):

        self.a_visivel = False
        self.a_label = None

        self.b_visivel = False
        self.b_label = None

        self.c_visivel = False
        self.c_label = None

        self.d_visivel = False
        self.d_label = None

        self.e_visivel = True
        self.e_label = None

        self.f_visivel = False
        self.f_label = None

        self.g_visivel = False
        self.g_label = None

        self.h_visivel = False
        self.h_label = None

        self.i_visivel = False
        self.i_label = None

        self.j_visivel = False
        self.j_label = None

        self.k_visivel = False
        self.k_label = None

        self.l_visivel = False
        self.l_label = None

        self.m_visivel = False
        self.m_label = None

        self.n_visivel = False
        self.n_label = None

        self.o_visivel = False
        self.o_label = None

        self.p_visivel = False
        self.p_label = None

        self.q_visivel = False
        self.q_label = None

        self.r_visivel = False
        self.r_label = None

        self.s_visivel = False
        self.s_label = None

        self.t_visivel = False
        self.t_label = None

        self.u_visivel = False
        self.u_label = None

        self.v_visivel = False
        self.v_label = None

        self.w_visivel = False
        self.w_label = None

        self.x_visivel = False
        self.x_label = None

        self.y_visivel = False
        self.y_label = None

        self.z_visivel = False
        self.z_label = None

        self.ç_visivel = False
        self.ç_label = None

        self.leer_visivel = False
        self.leer_label = None

    #Criação das Letras
    def createlbs(self):
        self.create_lbl_a()
        self.create_lbl_b()
        self.create_lbl_c()
        self.create_lbl_d()
        self.create_lbl_e()
        self.create_lbl_f()
        self.create_lbl_g()
        self.create_lbl_h()
        self.create_lbl_i()
        self.create_lbl_j()
        self.create_lbl_k()
        self.create_lbl_l()
        self.create_lbl_m()
        self.create_lbl_n()
        self.create_lbl_o()
        self.create_lbl_p()
        self.create_lbl_q()
        self.create_lbl_r()
        self.create_lbl_s()
        self.create_lbl_t()
        self.create_lbl_u()
        self.create_lbl_v()
        self.create_lbl_w()
        self.create_lbl_x()
        self.create_lbl_y()
        self.create_lbl_z()
        self.create_lbl_ç()
        self.create_lbl_leer()

    #A -----
    def create_lbl_a(self):
        aimage_path = r"Enigma_Cipher\images\letters\A.jpeg"
        aimg = Image.open(aimage_path)
        aimg = aimg.resize((44, 44), Image.LANCZOS)
        self.a_photo = ImageTk.PhotoImage(aimg) 
       
        self.a_label = Label(self.enigma, image=self.a_photo)
        self.a_place_args = {'relx': 0.131, 'rely': 0.531, 'relwidth': 0.065, 'relheight': 0.058}
        
    def toggle_a(self):
        if self.a_visivel:
            self.a_label.place_forget()
            self.a_visivel = False
        else:
            self.a_label.place(**self.a_place_args)
            self.a_visivel = True
            self.tiping.play()

    #B -----
    def create_lbl_b(self):
        bimage_path = r"Enigma_Cipher\images\letters\B.jpeg"
        bimg = Image.open(bimage_path)
        bimg = bimg.resize((44, 44), Image.LANCZOS)
        self.b_photo = ImageTk.PhotoImage(bimg) 
    
        self.b_label = Label(self.enigma, image=self.b_photo)
        self.b_place_args = {'relx': 0.544, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}
        
    def toggle_b(self):
        if self.b_visivel:
            self.b_label.place_forget()
            self.b_visivel = False
        else:
            self.b_label.place(**self.b_place_args)
            self.b_visivel = True
            self.tiping.play()

    #C -----
    def create_lbl_c(self):
        cimage_path = r"Enigma_Cipher\images\letters\C.jpeg"
        cimg = Image.open(cimage_path)
        cimg = cimg.resize((44, 44), Image.LANCZOS)
        self.c_photo = ImageTk.PhotoImage(cimg) 
       
        self.c_label = Label(self.enigma, image=self.c_photo)
        self.c_place_args = {'relx': 0.35, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}
        
    def toggle_c(self):
        if self.c_visivel:
            self.c_label.place_forget()
            self.c_visivel = False
        else:
            self.c_label.place(**self.c_place_args)
            self.c_visivel = True
            self.tiping.play()

    #D -----
    def create_lbl_d(self):
        dimage_path = r"Enigma_Cipher\images\letters\D.jpeg"
        dimg = Image.open(dimage_path)
        dimg = dimg.resize((44, 44), Image.LANCZOS)
        self.d_photo = ImageTk.PhotoImage(dimg) 
       
        self.d_label = Label(self.enigma, image=self.d_photo)
        self.d_place_args = {'relx': 0.321, 'rely': 0.531, 'relwidth': 0.065, 'relheight': 0.058}
        
    def toggle_d(self):
        if self.d_visivel:
            self.d_label.place_forget()
            self.d_visivel = False
        else:
            self.d_label.place(**self.d_place_args)
            self.d_visivel = True
            self.tiping.play()

    #E -----
    def create_lbl_e(self):
        eimage_path = r"Enigma_Cipher\images\letters\E.jpeg"
        eimg = Image.open(eimage_path)
        eimg = eimg.resize((44, 44), Image.LANCZOS)
        self.e_photo = ImageTk.PhotoImage(eimg) 
       
        self.e_label = Label(self.enigma, image=self.e_photo)
        self.e_place_args = {'relx': 0.2930, 'rely': 0.4573, 'relwidth': 0.065, 'relheight': 0.058}
        self.e_label.place(**self.e_place_args)

    def toggle_e(self):
        if self.e_visivel:
            self.e_label.place_forget()
            self.e_visivel = False
            self.tiping.play()
        else:
            self.e_label.place(**self.e_place_args)
            self.e_visivel = True
            
            
    #F -----
    def create_lbl_f(self):
        fimage_path = r"Enigma_Cipher\images\letters\F.jpeg"
        fimg = Image.open(fimage_path)
        fimg = fimg.resize((44, 44), Image.LANCZOS)
        self.f_photo = ImageTk.PhotoImage(fimg) 
       
        self.f_label = Label(self.enigma, image=self.f_photo)
        self.f_place_args = {'relx': 0.418, 'rely': 0.53, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_f(self):
        if self.f_visivel:
            self.f_label.place_forget()
            self.f_visivel = False
        else:
            self.f_label.place(**self.f_place_args)
            self.f_visivel = True
            self.tiping.play()

    #G -----
    def create_lbl_g(self):
        gimage_path = r"Enigma_Cipher\images\letters\G.jpeg"
        gimg = Image.open(gimage_path)
        gimg = gimg.resize((44, 44), Image.LANCZOS)
        self.g_photo = ImageTk.PhotoImage(gimg) 
       
        self.g_label = Label(self.enigma, image=self.g_photo)
        self.g_place_args = {'relx': 0.515, 'rely': 0.53, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_g(self):
        if self.g_visivel:
            self.g_label.place_forget()
            self.g_visivel = False
        else:
            self.g_label.place(**self.g_place_args)
            self.g_visivel = True
            self.tiping.play()

    #H -----
    def create_lbl_h(self):
        himage_path = r"Enigma_Cipher\images\letters\H.jpeg"
        himg = Image.open(himage_path)
        himg = himg.resize((44, 44), Image.LANCZOS)
        self.h_photo = ImageTk.PhotoImage(himg) 
       
        self.h_label = Label(self.enigma, image=self.h_photo)
        self.h_place_args = {'relx': 0.61, 'rely': 0.531, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_h(self):
        if self.h_visivel:
            self.h_label.place_forget()
            self.h_visivel = False
        else:
            self.h_label.place(**self.h_place_args)
            self.h_visivel = True
            self.tiping.play()

    #I -----
    def create_lbl_i(self):
        iimage_path = r"Enigma_Cipher\images\letters\I.jpeg"
        iimg = Image.open(iimage_path)
        iimg = iimg.resize((44, 44), Image.LANCZOS)
        self.i_photo = ImageTk.PhotoImage(iimg) 
       
       
        self.i_label = Label(self.enigma, image=self.i_photo)
        self.i_place_args = {'relx': 0.776, 'rely': 0.4573, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_i(self):
        if self.i_visivel:
            self.i_label.place_forget()
            self.i_visivel = False
        else:
            self.i_label.place(**self.i_place_args)
            self.i_visivel = True
            self.tiping.play()

    #J -----
    def create_lbl_j(self):
        jimage_path = r"Enigma_Cipher\images\letters\J.jpeg"
        jimg = Image.open(jimage_path)
        jimg = jimg.resize((44, 44), Image.LANCZOS)
        self.j_photo = ImageTk.PhotoImage(jimg) 
       
        self.j_label = Label(self.enigma, image=self.j_photo)
        self.j_place_args = {'relx': 0.707, 'rely': 0.53, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_j(self):
        if self.j_visivel:
            self.j_label.place_forget()
            self.j_visivel = False
        else:
            self.j_label.place(**self.j_place_args)
            self.j_visivel = True
            self.tiping.play()

    #K -----
    def create_lbl_k(self):
        kimage_path = r"Enigma_Cipher\images\letters\K.jpeg"
        kimg = Image.open(kimage_path)
        kimg = kimg.resize((44, 44), Image.LANCZOS)
        self.k_photo = ImageTk.PhotoImage(kimg) 
       
        self.k_label = Label(self.enigma, image=self.k_photo)
        self.k_place_args = {'relx': 0.804, 'rely': 0.53, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_k(self):
        if self.k_visivel:
            self.k_label.place_forget()
            self.k_visivel = False
        else:
            self.k_label.place(**self.k_place_args)
            self.k_visivel = True
            self.tiping.play()

    #L -----
    def create_lbl_l(self):
        limage_path = r"Enigma_Cipher\images\letters\L.jpeg"
        limg = Image.open(limage_path)
        limg = limg.resize((44, 44), Image.LANCZOS)
        self.l_photo = ImageTk.PhotoImage(limg) 
       
        self.l_label = Label(self.enigma, image=self.l_photo)
        self.l_place_args = {'relx': 0.834, 'rely': 0.603, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_l(self):
        if self.l_visivel:
            self.l_label.place_forget()
            self.l_visivel = False
        else:
            self.l_label.place(**self.l_place_args)
            self.l_visivel = True
            self.tiping.play()

    #M -----
    def create_lbl_m(self):
        mimage_path = r"Enigma_Cipher\images\letters\M.jpeg"
        mimg = Image.open(mimage_path)
        mimg = mimg.resize((44, 44), Image.LANCZOS)
        self.m_photo = ImageTk.PhotoImage(mimg) 
       
        self.m_label = Label(self.enigma, image=self.m_photo)
        self.m_place_args = {'relx': 0.7349, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_m(self):
        if self.m_visivel:
            self.m_label.place_forget()
            self.m_visivel = False
        else:
            self.m_label.place(**self.m_place_args)
            self.m_visivel = True
            self.tiping.play()

    #N -----
    def create_lbl_n(self):
        nimage_path = r"Enigma_Cipher\images\letters\N.jpeg"
        nimg = Image.open(nimage_path)
        nimg = nimg.resize((44, 44), Image.LANCZOS)
        self.n_photo = ImageTk.PhotoImage(nimg) 
       
        self.n_label = Label(self.enigma, image=self.n_photo)
        self.n_place_args = {'relx': 0.640, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_n(self):
        if self.n_visivel:
            self.n_label.place_forget()
            self.n_visivel = False
        else:
            self.n_label.place(**self.n_place_args)
            self.n_visivel = True
            self.tiping.play()

    #O -----
    def create_lbl_o(self):
        oimage_path = r"Enigma_Cipher\images\letters\O.jpeg"
        oimg = Image.open(oimage_path)
        oimg = oimg.resize((44, 44), Image.LANCZOS)
        self.o_photo = ImageTk.PhotoImage(oimg) 
       
        self.o_label = Label(self.enigma, image=self.o_photo)
        self.o_place_args = {'relx': 0.872, 'rely': 0.4573, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_o(self):
        if self.o_visivel:
            self.o_label.place_forget()
            self.o_visivel = False
        else:
            self.o_label.place(**self.o_place_args)
            self.o_visivel = True
            self.tiping.play()

    #P -----
    def create_lbl_p(self):
        pimage_path = r"Enigma_Cipher\images\letters\P.jpeg"
        pimg = Image.open(pimage_path)
        pimg = pimg.resize((44, 44), Image.LANCZOS)
        self.p_photo = ImageTk.PhotoImage(pimg) 
       
        self.p_label = Label(self.enigma, image=self.p_photo)
        self.p_place_args = {'relx': 0.064, 'rely': 0.603, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_p(self):
        if self.p_visivel:
            self.p_label.place_forget()
            self.p_visivel = False
        else:
            self.p_label.place(**self.p_place_args)
            self.p_visivel = True
            self.tiping.play()

    #Q -----
    def create_lbl_q(self):
        qimage_path = r"Enigma_Cipher\images\letters\Q.jpeg"
        qimg = Image.open(qimage_path)
        qimg = qimg.resize((44, 44), Image.LANCZOS)
        self.q_photo = ImageTk.PhotoImage(qimg) 
       
        self.q_label = Label(self.enigma, image=self.q_photo)
        self.q_place_args = {'relx': 0.1, 'rely': 0.4574, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_q(self):
        if self.q_visivel:
            self.q_label.place_forget()
            self.q_visivel = False
        else:
            self.q_label.place(**self.q_place_args)
            self.q_visivel = True
            self.tiping.play()

    #R -----
    def create_lbl_r(self):
        rimage_path = r"Enigma_Cipher\images\letters\R.jpeg"
        rimg = Image.open(rimage_path)
        rimg = rimg.resize((44, 44), Image.LANCZOS)
        self.r_photo = ImageTk.PhotoImage(rimg) 
       
        self.r_label = Label(self.enigma, image=self.r_photo)
        self.r_place_args = {'relx': 0.3889, 'rely': 0.4574, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_r(self):
        if self.r_visivel:
            self.r_label.place_forget()
            self.r_visivel = False
        else:
            self.r_label.place(**self.r_place_args)
            self.r_visivel = True
            self.tiping.play()

    #S -----
    def create_lbl_s(self):
        simage_path = r"Enigma_Cipher\images\letters\S.jpeg"
        simg = Image.open(simage_path)
        simg = simg.resize((44, 44), Image.LANCZOS)
        self.s_photo = ImageTk.PhotoImage(simg) 
       
        self.s_label = Label(self.enigma, image=self.s_photo)
        self.s_place_args = {'relx': 0.2249668, 'rely': 0.531, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_s(self):
        if self.s_visivel:
            self.s_label.place_forget()
            self.s_visivel = False
        else:
            self.s_label.place(**self.s_place_args)
            self.s_visivel = True
            self.tiping.play()

    #T -----
    def create_lbl_t(self):
        timage_path = r"Enigma_Cipher\images\letters\T.jpeg"
        timg = Image.open(timage_path)
        timg = timg.resize((44, 44), Image.LANCZOS)
        self.t_photo = ImageTk.PhotoImage(timg) 

        self.t_label = Label(self.enigma, image=self.t_photo)
        self.t_place_args = {'relx': 0.486, 'rely': 0.4574, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_t(self):
        if self.t_visivel:
            self.t_label.place_forget()
            self.t_visivel = False
        else:
            self.t_label.place(**self.t_place_args)
            self.t_visivel = True
            self.tiping.play()

    #U -----
    def create_lbl_u(self):
        uimage_path = r"Enigma_Cipher\images\letters\U.jpeg"
        uimg = Image.open(uimage_path)
        uimg = uimg.resize((44, 44), Image.LANCZOS)
        self.u_photo = ImageTk.PhotoImage(uimg) 
    
        self.u_label = Label(self.enigma, image=self.u_photo)
        self.u_place_args = {'relx': 0.6793, 'rely': 0.4576, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_u(self):
        if self.u_visivel:
            self.u_label.place_forget()
            self.u_visivel = False
        else:
            self.u_label.place(**self.u_place_args)
            self.u_visivel = True
            self.tiping.play()

    #V -----
    def create_lbl_v(self):
        vimage_path = r"Enigma_Cipher\images\letters\V.jpeg"
        vimg = Image.open(vimage_path)
        vimg = vimg.resize((44, 44), Image.LANCZOS)
        self.v_photo = ImageTk.PhotoImage(vimg) 
       
        self.v_label = Label(self.enigma, image=self.v_photo)
        self.v_place_args = {'relx': 0.4469, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_v(self):
        if self.v_visivel:
            self.v_label.place_forget()
            self.v_visivel = False
        else:
            self.v_label.place(**self.v_place_args)
            self.v_visivel = True
            self.tiping.play()

    #W -----
    def create_lbl_w(self):
        wimage_path = r"Enigma_Cipher\images\letters\W.jpeg"
        wimg = Image.open(wimage_path)
        wimg = wimg.resize((44, 44), Image.LANCZOS)
        self.w_photo = ImageTk.PhotoImage(wimg) 
       
        self.w_label = Label(self.enigma, image=self.w_photo)
        self.w_place_args = {'relx': 0.197005, 'rely': 0.4576, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_w(self):
        if self.w_visivel:
            self.w_label.place_forget()
            self.w_visivel = False
        else:
            self.w_label.place(**self.w_place_args)
            self.w_visivel = True
            self.tiping.play()

    #X -----
    def create_lbl_x(self):
        ximage_path = r"Enigma_Cipher\images\letters\X.jpeg"
        ximg = Image.open(ximage_path)
        ximg = ximg.resize((44, 44), Image.LANCZOS)
        self.x_photo = ImageTk.PhotoImage(ximg) 
       
        self.x_label = Label(self.enigma, image=self.x_photo)
        self.x_place_args = {'relx': 0.254, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_x(self):
        if self.x_visivel:
            self.x_label.place_forget()
            self.x_visivel = False
        else:
            self.x_label.place(**self.x_place_args)
            self.x_visivel = True
            self.tiping.play()

    #Y -----
    def create_lbl_y(self):
        yimage_path = r"Enigma_Cipher\images\letters\Y.jpeg"
        yimg = Image.open(yimage_path)
        yimg = yimg.resize((44, 44), Image.LANCZOS)
        self.y_photo = ImageTk.PhotoImage(yimg) 
       
        self.y_label = Label(self.enigma, image=self.y_photo)
        self.y_place_args = {'relx': 0.159, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_y(self):
        if self.y_visivel:
            self.y_label.place_forget()
            self.y_visivel = False
        else:
            self.y_label.place(**self.y_place_args)
            self.y_visivel = True
            self.tiping.play()

    #Z -----
    def create_lbl_z(self):
        zimage_path = r"Enigma_Cipher\images\letters\Z.jpeg"
        zimg = Image.open(zimage_path)
        zimg = zimg.resize((44, 44), Image.LANCZOS)
        self.z_photo = ImageTk.PhotoImage(zimg) 
       
        self.z_label = Label(self.enigma, image=self.z_photo)
        self.z_place_args = {'relx': 0.583, 'rely': 0.4573, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_z(self):
        if self.z_visivel:
            self.z_label.place_forget()
            self.z_visivel = False
        else:
            self.z_label.place(**self.z_place_args)
            self.z_visivel = True
            self.tiping.play()

    #Ç -----
    def create_lbl_ç(self):
        çimage_path = r"Enigma_Cipher\images\letters\Ç.jpeg"
        çimg = Image.open(çimage_path)
        çimg = çimg.resize((44, 44), Image.LANCZOS)
        self.ç_photo = ImageTk.PhotoImage(çimg) 
       
        self.ç_label = Label(self.enigma, image=self.ç_photo)
        self.ç_place_args = {'relx': 0.9, 'rely': 0.53, 'relwidth': 0.065, 'relheight': 0.058}

    def toggle_ç(self):
        if self.ç_visivel:
            self.ç_label.place_forget()
            self.ç_visivel = False
        else:
            self.ç_label.place(**self.ç_place_args)
            self.ç_visivel = True
            self.tiping.play()

    #Leertarste -----
    def create_lbl_leer(self):
        leerimage_path = r"Enigma_Cipher\images\letters\Leertaste.jpeg"
        leerimg = Image.open(leerimage_path)
        leerimg = leerimg.resize((345, 44), Image.LANCZOS)
        self.leer_photo = ImageTk.PhotoImage(leerimg) 
       
        self.leer_label = Label(self.enigma, image=self.leer_photo)
        self.leer_place_args = {'relx': 0.192, 'rely': 0.674, 'width': 345, 'height': 44}

    def toggle_leer(self):
        if self.leer_visivel:
            self.leer_label.place_forget()
            self.leer_visivel = False
        else:
            self.leer_label.place(**self.leer_place_args)
            self.leer_visivel = True
            self.tiping.play()


screen_obj = interface()
