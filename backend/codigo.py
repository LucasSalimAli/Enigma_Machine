# teste para criação dos discos utilizando classes. OwO
class discos:

    codex = []    # array para o disco importa o padrao de codificaçao
    idex = 0      # indicatico de rotaçao do disco
    pos = 0       # indicativo de pos sequencial na maquina
    rot = 0
    

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
            
            if self.idex != 29:
                self.idex = self.idex+1
            else:
                self.idex = 0
                
            if self.codex[0] == self.rot:
                return 1
            else:
                return 0
            

    def conf(self,pino):

        buffer2 = pino[self.idex]
        print(pino)
        print(buffer2)
        while self.codex[0] != buffer2:

            buffer = self.codex[0]
            for x in range(len(self.codex)):
                if x < len(self.codex)-1:
                    self.codex[x] = self.codex[x+1]

            self.codex[len(self.codex)-1] = buffer
         


#====================================================================================
#talvez isso seja uma pessima ideia mas vamor ver se funciona
#classe discos ficou um pouco generica sem metodo __init__  afim de poder integrar o ETW e UKW e nao ter que criar outra classe e etc etc etc

    def traduz(self, inpt):
        
        if(type(inpt) == str):
        
            letra = self.assem.index(inpt)
        
        else:
        
            letra = self.assem[inpt]

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

def escolher():
    global disco
    for i in range(5):
        disco[i] = discos()
        disco[i].codex = list(colecao[int(input("Informe o disco para posiçao {}: ".format(i+1)))-1])
        disco[i].idex = 0
        disco[i].pos = i
        disco[i].rot = disco[i].codex[0]
        print(disco[i].codex)

def config():
    global disco
    for i in range(5):
        disco[i].idex = pinos.index(input("Informe o indice de configuraçao do disco {} (A - Z): ".format(i+1)))
        print(disco[i].codex)
        disco[i].conf(colecao[disco[i].pos])
        print(disco[i].codex)     

def refletor():
    global espelhos, ukw
    ukw.mirror = espelhos[(int(input("Informe o refletor que desejas adicionar: ")))-1]

def cripto():
    global disco, espelhos, etw

    texto = input()
    a = 0
    while texto != "/sair":

        if(texto == "/get"):
            print(disco[0].codex)
            print(disco[1].codex)
            print(disco[2].codex)
            print(disco[3].codex)
            print(disco[4].codex)

        else:
            texto = list(texto)

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
                print(a,end="")
            
            print("\n")
        texto = input()

            
def teste():
    print(pinos1)


def sair():
    global resp
    resp = 0

menu = {

    1:escolher,
    2:config,
    3:sair, #def de sair por enquanto - PRECISA FAZR O SISTEMA DE JUMPER OwO
    4:refletor,
    5:cripto,
    6:sair,
    7:teste

}


resp = 1
while resp > 0:

    print("Escolha a operaçao que deseja realizar")
    print("1 - Escolher discos")
    print("2 - Configurar index dos discos")
    print("3 - Configurar Jumpers")
    print("4 - Escolher o refletor")
    print("5 - Criptografar")
    print("6 - Sair")

    menu[int(input())]()

     





