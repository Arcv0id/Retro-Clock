from tkinter import Label, Tk
import time

janela = Tk()
janela.title("Retro Clock")    #window name
janela.geometry("360x100")     #window size
janela.configure(bg="#0f380f") #background color
janela.resizable(False, False) #Prevents the window from expanding

font_pixel = ("Early GameBoy", 30, "bold") #font

relogio = Label(
    janela,
    font=font_pixel,
    bg="#0f380f",   #Font color 
    fg="#8bac0f",   #Border width   
    bd=10,          #Border width
    relief="ridge"  #border style
)
relogio.pack(pady=10)  #graphical interface library

def atualizar_relogio():
    hora = time.strftime("%H:%M:%S")        #Set the Time to 23:59:59.
    relogio.config(text=hora)               #Change the Label text
    relogio.after(1000, atualizar_relogio)  #Every second the clock is changed


atualizar_relogio()    #Start the clock
janela.mainloop()      #keep the window open
