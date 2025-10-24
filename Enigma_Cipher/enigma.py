from tkinter import *
from PIL import Image, ImageTk
from pygame import *


tela = Tk()




class interface():

    def __init__(self):
        self.tela = tela
        self.menu()
        self.frames_menu()
        self.buttons_menu()
        self.images_menu()
        self.labels_menu()
        self.setlbl()
        self.go_to_settings()
        
    
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
        self.enigma.geometry("652x756")
        self.enigma.resizable(False, False)
        self.enigma_image()
        self.enigma_label()
        self.io()
        self.jumpers()
        self.createlbs()
        
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

    #Background da página da enigma
    def enigma_label(self):
        self.lb_bg = Label(self.enigma, image=self.bg_image)
        self.lb_bg.place(relwidth= 1, relheight=1)

    #Imput/Output
    def io(self):

        #Settings Button
        self.start = Button(self.enigma, image=self.set_image, command=self.go_to_settings)
        self.start.place(relx=0.785, rely=0.15, width=50, height=50)

        #Rotors Labels
        self.txt_r1 = "A"
        self.lb_r1 = Label(self.enigma, text=self.txt_r1, font="Arial, 14")
        self.lb_r1.place(relx=0.165, rely=0.185, width=23, height=23)
        
        self.txt_r2 = "B"
        self.lb_r2 = Label(self.enigma, text=self.txt_r2, font="Arial, 14")
        self.lb_r2.place(relx=0.2665, rely=0.185, width=23, height=23)

        self.txt_r3 = "C"
        self.lb_r3 = Label(self.enigma, text=self.txt_r3, font="Arial, 14")
        self.lb_r3.place(relx=0.368, rely=0.187, width=23, height=23)

        self.txt_r4 = "D"
        self.lb_r4 = Label(self.enigma, text=self.txt_r4, font="Arial, 14")
        self.lb_r4.place(relx=0.47, rely=0.187, width=23, height=23)

        self.txt_r5 = "E"
        self.lb_r5 = Label(self.enigma, text=self.txt_r5, font="Arial, 14")
        self.lb_r5.place(relx=0.57, rely=0.187, width=23, height=23)


        #Rotors Buttons
        self.bt_up1 = Button(self.enigma, text="+")
        self.bt_up1.place(relx=0.1678, rely=0.1315, width=20, height=20)
        self.bt_dn1 = Button(self.enigma, text="-")
        self.bt_dn1.place(relx=0.1678, rely=0.2436, width=20, height=20)
        
        self.bt_up2 = Button(self.enigma, text="+")
        self.bt_up2.place(relx=0.2695, rely=0.1315, width=20, height=20)
        self.bt_dn2 = Button(self.enigma, text="-")
        self.bt_dn2.place(relx=0.2695, rely=0.2436, width=20, height=20)

        self.bt_up3 = Button(self.enigma, text="+")
        self.bt_up3.place(relx=0.371, rely=0.1315, width=20, height=20)
        self.bt_dn3 = Button(self.enigma, text="-")
        self.bt_dn3.place(relx=0.371, rely=0.2436, width=20, height=20)

        self.bt_up4 = Button(self.enigma, text="+")
        self.bt_up4.place(relx=0.472, rely=0.1315, width=20, height=20)
        self.bt_dn4 = Button(self.enigma, text="-")
        self.bt_dn4.place(relx=0.472, rely=0.2436, width=20, height=20)

        self.bt_up5 = Button(self.enigma, text="+")
        self.bt_up5.place(relx=0.573, rely=0.1315, width=20, height=20)
        self.bt_dn5 = Button(self.enigma, text="-")
        self.bt_dn5.place(relx=0.573, rely=0.2436, width=20, height=20)


        #Rotors ID
        self.txt_id_r1 = "1"
        self.lb_id_r1 = Label(self.enigma, text=self.txt_id_r1)
        self.lb_id_r1.place(relx=0.1678, rely=0.08, width=20, height=20)

        self.txt_id_r2 = "2"
        self.lb_id_r2 = Label(self.enigma, text=self.txt_id_r2)
        self.lb_id_r2.place(relx=0.2695, rely=0.08, width=20, height=20)

        self.txt_id_r3 = "3"
        self.lb_id_r3 = Label(self.enigma, text=self.txt_id_r3)
        self.lb_id_r3.place(relx=0.371, rely=0.08, width=20, height=20)

        self.txt_id_r4 = "4"
        self.lb_id_r4 = Label(self.enigma, text=self.txt_id_r4)
        self.lb_id_r4.place(relx=0.472, rely=0.08, width=20, height=20)

        self.txt_id_r5 = "5"
        self.lb_id_r5 = Label(self.enigma, text=self.txt_id_r5)
        self.lb_id_r5.place(relx=0.573, rely=0.08, width=20, height=20)


        #Entrada
        self.lb_ent = Label(self.enigma, text="Entrada")
        self.lb_ent.place(relx=0.1, rely= 0.32, width= 50, height = 25)
        
        self.ent = Entry(self.enigma)
        self.ent.place(relx=0.2, rely= 0.32, width= 500, height = 25)

        #Saida
        self.lb_extt = Label(self.enigma, text="Saida")
        self.lb_extt.place(relx=0.1, rely= 0.38, width= 50, height = 25)

        self.lb_ext = Label(self.enigma, text="Esperando Criptografia")
        self.lb_ext.place(relx=0.2, rely= 0.38, width= 500, height = 25)

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
            self.j_z = Label(self.enigma, text="_")
            self.j_z.place(relx= 0.88, rely= 0.77, width=17, height=17)

            self.e_z = Entry(self.enigma)
            self.e_z.place(relx= 0.88, rely= 0.86, width=17, height=17)

    #Função para abrir a tela de configurações    
    def go_to_settings(self):
        settings = Toplevel()
        self.settings = settings
        self.settings.title("Settings")
        self.settings.configure(background="#FFFFFF")
        self.settings.geometry("350x350")
        self.settings_bg()
        self.settings_io()

    #Frames da settings
    def settings_bg(self):
        self.rotors_frame = Frame(self.settings, bg="#9FA1AD")
        self.rotors_frame.place(relx= 0.05, rely= 0.05, width= 180, height= 210)

        self.lbl_rotor_title = Label(self.settings, text="Selecione um rotor para cada slot")
        self.lbl_rotor_title.place(relx= 0.05, rely=0.05, width= 180, height= 20)

        self.ukw_frame = Frame(self.settings, bg="#FD6161")
        self.ukw_frame.place(relx= 0.6, rely= 0.05, width=120, height= 210 )

        self.volume_frame = Frame(self.settings, bg="#AEF705")
        self.volume_frame.place(relx = 0.05, rely=0.7, width = 180, heigh= 80)

        self.check_frame = Frame(self.settings, bg="#F179B1")
        self.check_frame.place(relx=0.6, rely=0.7, width= 120, height= 37 )

        self.save_frame = Frame(self.settings, bg="#7CEE4F")
        self.save_frame.place(relx= 0.6, rely= 0.82, width=120, height=37)

    def settings_io(self):
        self.lbl_r1s = Label(self.settings, text="Selecione o rotor")
        self.lbl_r1s.place(relx+)



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
        self.a_label.place(**self.a_place_args)

    def toggle_a(self):
        if self.a_visivel:
            self.a_label.place_forget()
            self.a_visivel = False
        else:
            self.a_label.place(**self.a_place_args)
            self.a_visivel = True

    #B -----
    def create_lbl_b(self):
        bimage_path = r"Enigma_Cipher\images\letters\B.jpeg"
        bimg = Image.open(bimage_path)
        bimg = bimg.resize((44, 44), Image.LANCZOS)
        self.b_photo = ImageTk.PhotoImage(bimg) 
       
       
        self.b_label = Label(self.enigma, image=self.b_photo)
        self.b_place_args = {'relx': 0.544, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}
        self.b_label.place(**self.b_place_args)

    def toggle_b(self):
        if self.b_visivel:
            self.b_label.place_forget()
            self.b_visivel = False
        else:
            self.b_label.place(**self.b_place_args)
            self.b_visivel = True

    #C -----
    def create_lbl_c(self):
        cimage_path = r"Enigma_Cipher\images\letters\C.jpeg"
        cimg = Image.open(cimage_path)
        cimg = cimg.resize((44, 44), Image.LANCZOS)
        self.c_photo = ImageTk.PhotoImage(cimg) 
       
       
        self.c_label = Label(self.enigma, image=self.c_photo)
        self.c_place_args = {'relx': 0.35, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}
        self.c_label.place(**self.c_place_args)

    def toggle_c(self):
        if self.c_visivel:
            self.c_label.place_forget()
            self.c_visivel = False
        else:
            self.c_label.place(**self.c_place_args)
            self.c_visivel = True

    #D -----
    def create_lbl_d(self):
        dimage_path = r"Enigma_Cipher\images\letters\D.jpeg"
        dimg = Image.open(dimage_path)
        dimg = dimg.resize((44, 44), Image.LANCZOS)
        self.d_photo = ImageTk.PhotoImage(dimg) 
       
       
        self.d_label = Label(self.enigma, image=self.d_photo)
        self.d_place_args = {'relx': 0.321, 'rely': 0.531, 'relwidth': 0.065, 'relheight': 0.058}
        self.d_label.place(**self.d_place_args)
        
    def toggle_d(self):
        if self.d_visivel:
            self.d_label.place_forget()
            self.d_visivel = False
        else:
            self.d_label.place(**self.d_place_args)
            self.d_visivel = True

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
        self.f_label.place(**self.f_place_args)

    def toggle_f(self):
        if self.f_visivel:
            self.f_label.place_forget()
            self.f_visivel = False
        else:
            self.f_label.place(**self.f_place_args)
            self.f_visivel = True

    #G -----
    def create_lbl_g(self):
        gimage_path = r"Enigma_Cipher\images\letters\G.jpeg"
        gimg = Image.open(gimage_path)
        gimg = gimg.resize((44, 44), Image.LANCZOS)
        self.g_photo = ImageTk.PhotoImage(gimg) 
       
       
        self.g_label = Label(self.enigma, image=self.g_photo)
        self.g_place_args = {'relx': 0.515, 'rely': 0.53, 'relwidth': 0.065, 'relheight': 0.058}
        self.g_label.place(**self.g_place_args)

    def toggle_g(self):
        if self.g_visivel:
            self.g_label.place_forget()
            self.g_visivel = False
        else:
            self.g_label.place(**self.g_place_args)
            self.g_visivel = True

    #H -----
    def create_lbl_h(self):
        himage_path = r"Enigma_Cipher\images\letters\H.jpeg"
        himg = Image.open(himage_path)
        himg = himg.resize((44, 44), Image.LANCZOS)
        self.h_photo = ImageTk.PhotoImage(himg) 
       
       
        self.h_label = Label(self.enigma, image=self.h_photo)
        self.h_place_args = {'relx': 0.61, 'rely': 0.531, 'relwidth': 0.065, 'relheight': 0.058}
        self.h_label.place(**self.h_place_args)

    def toggle_h(self):
        if self.h_visivel:
            self.h_label.place_forget()
            self.h_visivel = False
        else:
            self.h_label.place(**self.h_place_args)
            self.h_visivel = True

    #I -----
    def create_lbl_i(self):
        iimage_path = r"Enigma_Cipher\images\letters\I.jpeg"
        iimg = Image.open(iimage_path)
        iimg = iimg.resize((44, 44), Image.LANCZOS)
        self.i_photo = ImageTk.PhotoImage(iimg) 
       
       
        self.i_label = Label(self.enigma, image=self.i_photo)
        self.i_place_args = {'relx': 0.776, 'rely': 0.4573, 'relwidth': 0.065, 'relheight': 0.058}
        self.i_label.place(**self.i_place_args)

    def toggle_i(self):
        if self.i_visivel:
            self.i_label.place_forget()
            self.i_visivel = False
        else:
            self.i_label.place(**self.i_place_args)
            self.i_visivel = True

    #J -----
    def create_lbl_j(self):
        jimage_path = r"Enigma_Cipher\images\letters\J.jpeg"
        jimg = Image.open(jimage_path)
        jimg = jimg.resize((44, 44), Image.LANCZOS)
        self.j_photo = ImageTk.PhotoImage(jimg) 
       
       
        self.j_label = Label(self.enigma, image=self.j_photo)
        self.j_place_args = {'relx': 0.707, 'rely': 0.53, 'relwidth': 0.065, 'relheight': 0.058}
        self.j_label.place(**self.j_place_args)

    def toggle_j(self):
        if self.j_visivel:
            self.j_label.place_forget()
            self.j_visivel = False
        else:
            self.j_label.place(**self.j_place_args)
            self.j_visivel = True

    #K -----
    def create_lbl_k(self):
        kimage_path = r"Enigma_Cipher\images\letters\K.jpeg"
        kimg = Image.open(kimage_path)
        kimg = kimg.resize((44, 44), Image.LANCZOS)
        self.k_photo = ImageTk.PhotoImage(kimg) 
       
       
        self.k_label = Label(self.enigma, image=self.k_photo)
        self.k_place_args = {'relx': 0.804, 'rely': 0.53, 'relwidth': 0.065, 'relheight': 0.058}
        self.k_label.place(**self.k_place_args)

    def toggle_k(self):
        if self.k_visivel:
            self.k_label.place_forget()
            self.k_visivel = False
        else:
            self.k_label.place(**self.k_place_args)
            self.k_visivel = True

    #L -----
    def create_lbl_l(self):
        limage_path = r"Enigma_Cipher\images\letters\L.jpeg"
        limg = Image.open(limage_path)
        limg = limg.resize((44, 44), Image.LANCZOS)
        self.l_photo = ImageTk.PhotoImage(limg) 
       
       
        self.l_label = Label(self.enigma, image=self.l_photo)
        self.l_place_args = {'relx': 0.834, 'rely': 0.603, 'relwidth': 0.065, 'relheight': 0.058}
        self.l_label.place(**self.l_place_args)

    def toggle_l(self):
        if self.l_visivel:
            self.l_label.place_forget()
            self.l_visivel = False
        else:
            self.l_label.place(**self.l_place_args)
            self.l_visivel = True

    #M -----
    def create_lbl_m(self):
        mimage_path = r"Enigma_Cipher\images\letters\M.jpeg"
        mimg = Image.open(mimage_path)
        mimg = mimg.resize((44, 44), Image.LANCZOS)
        self.m_photo = ImageTk.PhotoImage(mimg) 
       
       
        self.m_label = Label(self.enigma, image=self.m_photo)
        self.m_place_args = {'relx': 0.7349, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}
        self.m_label.place(**self.m_place_args)

    def toggle_m(self):
        if self.m_visivel:
            self.m_label.place_forget()
            self.m_visivel = False
        else:
            self.m_label.place(**self.m_place_args)
            self.m_visivel = True

    #N -----
    def create_lbl_n(self):
        nimage_path = r"Enigma_Cipher\images\letters\N.jpeg"
        nimg = Image.open(nimage_path)
        nimg = nimg.resize((44, 44), Image.LANCZOS)
        self.n_photo = ImageTk.PhotoImage(nimg) 
       
       
        self.n_label = Label(self.enigma, image=self.n_photo)
        self.n_place_args = {'relx': 0.640, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}
        self.n_label.place(**self.n_place_args)

    def toggle_n(self):
        if self.n_visivel:
            self.n_label.place_forget()
            self.n_visivel = False
        else:
            self.n_label.place(**self.n_place_args)
            self.n_visivel = True

    #O -----
    def create_lbl_o(self):
        oimage_path = r"Enigma_Cipher\images\letters\O.jpeg"
        oimg = Image.open(oimage_path)
        oimg = oimg.resize((44, 44), Image.LANCZOS)
        self.o_photo = ImageTk.PhotoImage(oimg) 
       
       
        self.o_label = Label(self.enigma, image=self.o_photo)
        self.o_place_args = {'relx': 0.872, 'rely': 0.4573, 'relwidth': 0.065, 'relheight': 0.058}
        self.o_label.place(**self.o_place_args)

    def toggle_o(self):
        if self.o_visivel:
            self.o_label.place_forget()
            self.o_visivel = False
        else:
            self.o_label.place(**self.o_place_args)
            self.o_visivel = True

    #P -----
    def create_lbl_p(self):
        pimage_path = r"Enigma_Cipher\images\letters\P.jpeg"
        pimg = Image.open(pimage_path)
        pimg = pimg.resize((44, 44), Image.LANCZOS)
        self.p_photo = ImageTk.PhotoImage(pimg) 
       
       
        self.p_label = Label(self.enigma, image=self.p_photo)
        self.p_place_args = {'relx': 0.064, 'rely': 0.603, 'relwidth': 0.065, 'relheight': 0.058}
        self.p_label.place(**self.p_place_args)

    def toggle_p(self):
        if self.p_visivel:
            self.p_label.place_forget()
            self.p_visivel = False
        else:
            self.p_label.place(**self.p_place_args)
            self.p_visivel = True

    #Q -----
    def create_lbl_q(self):
        qimage_path = r"Enigma_Cipher\images\letters\Q.jpeg"
        qimg = Image.open(qimage_path)
        qimg = qimg.resize((44, 44), Image.LANCZOS)
        self.q_photo = ImageTk.PhotoImage(qimg) 
       
       
        self.q_label = Label(self.enigma, image=self.q_photo)
        self.q_place_args = {'relx': 0.1, 'rely': 0.4574, 'relwidth': 0.065, 'relheight': 0.058}
        self.q_label.place(**self.q_place_args)

    def toggle_q(self):
        if self.q_visivel:
            self.q_label.place_forget()
            self.q_visivel = False
        else:
            self.q_label.place(**self.q_place_args)
            self.q_visivel = True

    #R -----
    def create_lbl_r(self):
        rimage_path = r"Enigma_Cipher\images\letters\R.jpeg"
        rimg = Image.open(rimage_path)
        rimg = rimg.resize((44, 44), Image.LANCZOS)
        self.r_photo = ImageTk.PhotoImage(rimg) 
       
       
        self.r_label = Label(self.enigma, image=self.r_photo)
        self.r_place_args = {'relx': 0.3889, 'rely': 0.4574, 'relwidth': 0.065, 'relheight': 0.058}
        self.r_label.place(**self.r_place_args)

    def toggle_r(self):
        if self.r_visivel:
            self.r_label.place_forget()
            self.r_visivel = False
        else:
            self.r_label.place(**self.r_place_args)
            self.r_visivel = True

    #S -----
    def create_lbl_s(self):
        simage_path = r"Enigma_Cipher\images\letters\S.jpeg"
        simg = Image.open(simage_path)
        simg = simg.resize((44, 44), Image.LANCZOS)
        self.s_photo = ImageTk.PhotoImage(simg) 
       
       
        self.s_label = Label(self.enigma, image=self.s_photo)
        self.s_place_args = {'relx': 0.2249668, 'rely': 0.531, 'relwidth': 0.065, 'relheight': 0.058}
        self.s_label.place(**self.s_place_args)

    def toggle_s(self):
        if self.s_visivel:
            self.s_label.place_forget()
            self.s_visivel = False
        else:
            self.s_label.place(**self.s_place_args)
            self.s_visivel = True

    #T -----
    def create_lbl_t(self):
        timage_path = r"Enigma_Cipher\images\letters\T.jpeg"
        timg = Image.open(timage_path)
        timg = timg.resize((44, 44), Image.LANCZOS)
        self.t_photo = ImageTk.PhotoImage(timg) 
       
       
        self.t_label = Label(self.enigma, image=self.t_photo)
        self.t_place_args = {'relx': 0.486, 'rely': 0.4574, 'relwidth': 0.065, 'relheight': 0.058}
        self.t_label.place(**self.t_place_args)

    def toggle_t(self):
        if self.t_visivel:
            self.t_label.place_forget()
            self.t_visivel = False
        else:
            self.t_label.place(**self.t_place_args)
            self.t_visivel = True

    #U -----
    def create_lbl_u(self):
        uimage_path = r"Enigma_Cipher\images\letters\U.jpeg"
        uimg = Image.open(uimage_path)
        uimg = uimg.resize((44, 44), Image.LANCZOS)
        self.u_photo = ImageTk.PhotoImage(uimg) 
       
       
        self.u_label = Label(self.enigma, image=self.u_photo)
        self.u_place_args = {'relx': 0.6793, 'rely': 0.4576, 'relwidth': 0.065, 'relheight': 0.058}
        self.u_label.place(**self.u_place_args)

    def toggle_u(self):
        if self.u_visivel:
            self.u_label.place_forget()
            self.u_visivel = False
        else:
            self.u_label.place(**self.u_place_args)
            self.u_visivel = True

    #V -----
    def create_lbl_v(self):
        vimage_path = r"Enigma_Cipher\images\letters\V.jpeg"
        vimg = Image.open(vimage_path)
        vimg = vimg.resize((44, 44), Image.LANCZOS)
        self.v_photo = ImageTk.PhotoImage(vimg) 
       
       
        self.v_label = Label(self.enigma, image=self.v_photo)
        self.v_place_args = {'relx': 0.4469, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}
        self.v_label.place(**self.v_place_args)

    def toggle_v(self):
        if self.v_visivel:
            self.v_label.place_forget()
            self.v_visivel = False
        else:
            self.v_label.place(**self.v_place_args)
            self.v_visivel = True

    #W -----
    def create_lbl_w(self):
        wimage_path = r"Enigma_Cipher\images\letters\W.jpeg"
        wimg = Image.open(wimage_path)
        wimg = wimg.resize((44, 44), Image.LANCZOS)
        self.w_photo = ImageTk.PhotoImage(wimg) 
       
       
        self.w_label = Label(self.enigma, image=self.w_photo)
        self.w_place_args = {'relx': 0.197005, 'rely': 0.4576, 'relwidth': 0.065, 'relheight': 0.058}
        self.w_label.place(**self.w_place_args)

    def toggle_w(self):
        if self.w_visivel:
            self.w_label.place_forget()
            self.w_visivel = False
        else:
            self.w_label.place(**self.w_place_args)
            self.w_visivel = True

    #X -----
    def create_lbl_x(self):
        ximage_path = r"Enigma_Cipher\images\letters\X.jpeg"
        ximg = Image.open(ximage_path)
        ximg = ximg.resize((44, 44), Image.LANCZOS)
        self.x_photo = ImageTk.PhotoImage(ximg) 
       
       
        self.x_label = Label(self.enigma, image=self.x_photo)
        self.x_place_args = {'relx': 0.254, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}
        self.x_label.place(**self.x_place_args)

    def toggle_x(self):
        if self.x_visivel:
            self.x_label.place_forget()
            self.x_visivel = False
        else:
            self.x_label.place(**self.x_place_args)
            self.x_visivel = True

    #Y -----
    def create_lbl_y(self):
        yimage_path = r"Enigma_Cipher\images\letters\Y.jpeg"
        yimg = Image.open(yimage_path)
        yimg = yimg.resize((44, 44), Image.LANCZOS)
        self.y_photo = ImageTk.PhotoImage(yimg) 
       
       
        self.y_label = Label(self.enigma, image=self.y_photo)
        self.y_place_args = {'relx': 0.159, 'rely': 0.602, 'relwidth': 0.065, 'relheight': 0.058}
        self.y_label.place(**self.y_place_args)

    def toggle_y(self):
        if self.y_visivel:
            self.y_label.place_forget()
            self.y_visivel = False
        else:
            self.y_label.place(**self.y_place_args)
            self.y_visivel = True

    #Z -----
    def create_lbl_z(self):
        zimage_path = r"Enigma_Cipher\images\letters\Z.jpeg"
        zimg = Image.open(zimage_path)
        zimg = zimg.resize((44, 44), Image.LANCZOS)
        self.z_photo = ImageTk.PhotoImage(zimg) 
       
       
        self.z_label = Label(self.enigma, image=self.z_photo)
        self.z_place_args = {'relx': 0.583, 'rely': 0.4573, 'relwidth': 0.065, 'relheight': 0.058}
        self.z_label.place(**self.z_place_args)

    def toggle_z(self):
        if self.z_visivel:
            self.z_label.place_forget()
            self.z_visivel = False
        else:
            self.z_label.place(**self.z_place_args)
            self.z_visivel = True

    #Ç -----
    def create_lbl_ç(self):
        çimage_path = r"Enigma_Cipher\images\letters\Ç.jpeg"
        çimg = Image.open(çimage_path)
        çimg = çimg.resize((44, 44), Image.LANCZOS)
        self.ç_photo = ImageTk.PhotoImage(çimg) 
       
       
        self.ç_label = Label(self.enigma, image=self.ç_photo)
        self.ç_place_args = {'relx': 0.9, 'rely': 0.53, 'relwidth': 0.065, 'relheight': 0.058}
        self.ç_label.place(**self.ç_place_args)

    def toggle_ç(self):
        if self.ç_visivel:
            self.ç_label.place_forget()
            self.ç_visivel = False
        else:
            self.ç_label.place(**self.ç_place_args)
            self.ç_visivel = True

    #Leertarste -----
    def create_lbl_leer(self):
        leerimage_path = r"Enigma_Cipher\images\letters\Leertaste.jpeg"
        leerimg = Image.open(leerimage_path)
        leerimg = leerimg.resize((345, 44), Image.LANCZOS)
        self.leer_photo = ImageTk.PhotoImage(leerimg) 
       
       
        self.leer_label = Label(self.enigma, image=self.leer_photo)
        self.leer_place_args = {'relx': 0.192, 'rely': 0.674, 'width': 345, 'height': 44}
        self.leer_label.place(**self.leer_place_args)

    def toggle_leer(self):
        if self.leer_visivel:
            self.leer_label.place_forget()
            self.leer_visivel = False
        else:
            self.leer_label.place(**self.leer_place_args)
            self.leer_visivel = True

        
   
interface() 



