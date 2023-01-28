from tkinter import *

#Função para calcular milhas em kilometros.
def miles_to_km():
    milhas = float(milhas_input.get())
    Km = round(milhas * 1.609)
    kilometros_result_label.config(text=f'{Km}')

janela = Tk()
janela.title("Milhas em Kilometros")
janela.config(padx=20, pady=20)

milhas_input = Entry(width=7)
milhas_input.grid(column=1 , row= 0)

milhas_label = Label(text="Milhas")
milhas_label.grid(column=2, row=0)

e_igual_label = Label(text="É igual á")
e_igual_label.grid(column=0, row=1)

kilometros_result_label = Label(text="0")
kilometros_result_label.grid(column=1, row=1)

kilometros_label = Label(text="Km")
kilometros_label.grid(column=2, row=1)

calculo_btn = Button(text="Calcular", command=miles_to_km)
calculo_btn.grid(column=1, row=2)


janela.mainloop()