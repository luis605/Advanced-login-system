try:
    import tkinter as tk
    from tkinter import*
    import tkinter
except:
    try:
        import Tkinter as tk
        from Tkinter import *
        import Tkinter
    except:
        print("Erro 1: um dos módulos importantes, não pode ser executado.")


try:
    import sqlite3
except:
    print("Erro 1: um dos módulos importantes, não pode ser executado.")




def line():



    #############################################################
    #####################GUARDA DADOS############################
    #############################################################


    def guarda_dados():
        banco = sqlite3.connect('banco.db')
        cursor = banco.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS %s (x INT, y INT)" %nome)
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS %s (x INT, y INT)" %nome)
        except:
            aviso = tkinter.Tk()
            Label(text="Avisei que a idade tinha de ser por extenso").pack()
            aviso.mainloop()



    #############################################################
    #############################################################
    #############################################################


    def repete():

        jan=tkinter.Tk()

        # configurações da jan
        jan.geometry("500x500")
        jan.configure(bg="white")
        jan.title("Login")


        # textos e botões

        a = Label(text="Nome:", bg ="white")
        a.place(x=5, y=70)

        b = Button(text="click me", fg="red", command=line)
        b.place(x=400, y=450)

        cadastro_nome = Entry(jan, bd=5, bg="white")
        cadastro_nome.place(x=135, y=70)


        d = Label(text="Idade:", bg ="white")
        d.place(x=5, y=130)

        cadastro_idade = Entry(jan, bd=5, bg="white")
        cadastro_idade.place(x=135, y=130)

        jan.mainloop()
    ###############Opções nos botẽs de escolha###############



    def apagar():
        nega.destroy()
        repete()

        #
        ####
        #import database
        ####
        #




        
        
    
    

    ###ACEITA###

    def aceita():
        aceita=tkinter.Tk()
        aceita.geometry("300x150")
        aceita.title("Concorda")
        aceita.configure(bg="white")

        continuar_text = Label(aceita, text="Deseja continuar?\nSe aceitar os efeitos serão irreversíveis!!!", bg="white")
        continuar_text.pack()

        concordo = Button(aceita, text="concordo", bg="blue", fg="green", command=guarda_dados)
        concordo.place(x=5, y=100)

        def discordo_aceita():
                aceita.destroy()

                
        discordo = Button(aceita, text="discordo", bg="blue", fg="red", command=discordo_aceita)
        discordo.place(x=200, y=100)


    ###NEGA###


    def nega():

        def discordo_nega():
            nega.destroy()
        nega=tkinter.Tk()
        nega.geometry("300x150")
        nega.title("Recusa")
        nega.configure(bg="white")

        continuar_text = Label(text="Deseja continuar?\nSe aceitar os efeitos serão irreversíveis!!!", bg="white")
        continuar_text.pack()


        concordo = Button(text="concordo", bg="blue", fg="green", command=apagar)
        concordo.place(x=5, y=100)

        discordo = Button(text="discordo", bg="blue", fg="red", command=discordo_nega)
        discordo.place(x=200, y=100)




    
    botao=tkinter.Tk()
    botao.geometry("600x300")
    botao.title("Login")
    botao.configure(bg="white")


    nome = (str(cadastro_nome.get()))
    idade = (str(cadastro_idade.get()))

    if nome in '':
        cadastro_nome["bg"]="red"
        nome_sim = 0

    else:
        cadastro_nome["bg"]="white"
        nome_sim = 1
        

    if idade in '':
        cadastro_idade["bg"]="red"
        idade_sim = 0

    else:
        cadastro_idade["bg"]="white"
        idade_sim = 1

    if nome_sim == 1 and idade_sim == 1:
        jan.destroy()
        mostra_nome = Label(botao, text="O seu nome é: " + nome, bg="white")
        mostra_nome.pack()

        mostra_idade = Label(botao, text="A sua idade é: " + idade, bg="white")
        mostra_idade.pack()

        aceita = Button(botao, text="Aceita", fg="green", command=aceita)
        aceita.place(x=100, y=100)

        nega = Button(botao, text="Negar", fg="red", command=nega)
        nega.place(x=400, y=100)
    else:
        botao.destroy()
        
    botao.mainloop()
    
jan=tkinter.Tk()

# configurações da jan
jan.geometry("500x500")
jan.configure(bg="white")
jan.title("Login")


# textos e botões

a = Label(text="Nome:", bg ="white")
a.place(x=5, y=70)

b = Button(text="click me", fg="red", command=line)
b.place(x=400, y=450)

cadastro_nome = Entry(jan, bd=5, bg="white")
cadastro_nome.place(x=135, y=70)


d = Label(text="Idade:", bg ="white")
d.place(x=5, y=130)

cadastro_idade = Entry(jan, bd=5, bg="white")
cadastro_idade.place(x=135, y=130)

Label (text = "A idade tem de ser escrita por extenso", bg = "grey", width = "300", height = "2", font = ("calibri", 13,)).pack()

jan.mainloop()
