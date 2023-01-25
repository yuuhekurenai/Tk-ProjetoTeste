from tkinter import *

#Criando janelas e configurações
window = Tk()
window.title("Widget Examplos")
window.minsize(width=500, height=500)

#Labels
label = Label(text="Esse é o texto antigo")
label.config(text="Esse é o texto novo")
label.pack()

#Buttons
def action():
    print("Faça Algo")

#chama action quando pressionado
button = Button(text="Click aqui!", command=action)
button.pack()

#Entry ou Caixa de texto
entry = Entry(width=30)
#Adiciona o texto que começa com.
entry.insert(END, string="O texto começa com...")
#Recebe o texto de entrada
print(entry.get())
entry.pack()

#Texto
text = Text(height=5, width=30)
#Ativar o texto na caixa de texto
text.focus()
#Adiciona o texto que começa com
text.insert(END, "Exemplo de multiplas linhas na entrada")
#Recebe o valor atual na textbox na primeira linha 1, caracter 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #Recebe o valor atual da spinbox
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Chama o valor atual da scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Printa 1 se o botão estiver checado , se não 0
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Está Ligado?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variaável para segurar o estado  do  radio
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Opção1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Opção2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Retorna a seleção atual da list box
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Maçã", "Pera", "Laranja", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
