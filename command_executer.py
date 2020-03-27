#-*-coding:UTF-8 -*
#import random
from tkinter import *
from PIL import ImageTk, Image
#import curses
import os
from os import path,environ,chdir,system
from os.path import dirname,join
import sys

#filename ="phrase.txt"

#if hasattr(sys, '_MEIPASS'):
    # PyInstaller >= 1.6
    #chdir(sys._MEIPASS)
    #filename = join(sys._MEIPASS, filename)
#elif '_MEIPASS2' in environ:
    # PyInstaller < 1.6 (tested on 1.5 only)
    #chdir(environ['_MEIPASS2'])
    #filename = join(environ['_MEIPASS2'], filename)
#else:
    #chdir(dirname(sys.argv[0]))
    #filename = join(dirname(sys.argv[0]), filename)
#import time
#import math
#import pygame
import subprocess
from tkinter.font import Font
from subprocess import Popen, PIPE
#import traceback
#from threading import Thread, Event
#from queue import Queue
#from time import sleep
from base64 import *

class Window():

    def __init__(self):
        self.fenetre=Tk()
        self.fenetre.title("Command Executer V 1.3")
        self.fenetre.geometry("1250x650")

        #filename="icone.ico"
        #if hasattr(sys, '_MEIPASS'):
            # PyInstaller >= 1.6
            #chdir(sys._MEIPASS)
            #filename = join(sys._MEIPASS, filename)
        #elif '_MEIPASS2' in environ:
            # PyInstaller < 1.6 (tested on 1.5 only)
            #chdir(environ['_MEIPASS2'])
            #filename = join(environ['_MEIPASS2'], filename)
        #else:
            #chdir(dirname(sys.argv[0]))
            #filename = join(dirname(sys.argv[0]), filename) rttrtrt
        #self.img = IMageTk.PhotoImage(Image.open("icone.ico"))
        #self.fenetre.call('wm', 'iconphoto', self.fenetre._w, img)
        self.fenetre.iconbitmap("icone.ico")

        os.environ["COMSPEC"]="C:\\Windows\\system32\\cmd.exe"


        #filename="command_executer_credits.dat"
        #if hasattr(sys, '_MEIPASS'):
            # PyInstaller >= 1.6
            #chdir(sys._MEIPASS)
            #filename = join(sys._MEIPASS, filename)
        #elif '_MEIPASS2' in environ:
            # PyInstaller < 1.6 (tested on 1.5 only)
            #chdir(environ['_MEIPASS2'])
            #filename = join(environ['_MEIPASS2'], filename)
        #else:
            #chdir(dirname(sys.argv[0]))
            #filename = join(dirname(sys.argv[0]), filename)


        with open("command_executer_credits.dat","r") as f:
            self.credits=b64decode(str(f.read()).encode()).decode()
            self.credits=self.credits.split(";")



        self.canvas=Canvas()
        self.canvas.create_line(625,0,625,40,fill="#224147")
        self.canvas.create_line(0,400,625,400,fill="#0f440d")
        self.canvas.create_line(0,585,625,585,fill="#0f440d")
        self.canvas.pack(fill=BOTH,expand=1)

        self.frame_out=Frame(self.fenetre,bg="black",width=1000,height=1000)
        self.frame_out.pack_propagate(0)
        self.frame_out.pack()
        self.frame_out.place(x=625,y=40)


        self.blazed=Font(family="Blazed.ttf",weight="bold",size=10)
        self.underfont=Font(family="afont.ttf",weight="bold",size=18,underline=True)
        self.label1=Label(self.fenetre,text="Enter a command :",font=("Blaed.ttf",30),fg="blue",)
        self.commande=StringVar()
        self.entry=Entry(self.fenetre,textvariable=self.commande,width=35)
        self.bouton=Button(self.fenetre,text="EXECUTE",command=self.execute,height=2,width=15,font=("helv36",20))
        self.boutonde=Button(self.fenetre,text="QUIT",command=self.fenetre.quit,heigh=2,width=15,font=("helv36",20))
        self.label3=Label(self.fenetre,text=self.credits[0],font=("Blazed.ttf",9),fg="green")
        self.label4=Label(self.fenetre,text=self.credits[1],font=("Blazed.ttf",9),fg="green")
        self.label_output=Label(self.fenetre,text="Output",font=self.underfont)
        self.label1.pack()
        self.label1.place(x=92,y=25)
        self.entry.pack()
        self.entry.place(x=165,y=115)
        self.bouton.pack()
        self.bouton.place(x=155,y=145)
        self.boutonde.pack()
        self.boutonde.place(x=155,y=255)
        self.label3.pack()
        self.label3.place(x=200,y=590)
        self.label4.pack()
        self.label4.place(x=250,y=620)
        self.label_output.pack()
        self.label_output.place(x=630,y=3)
        self.fenetre.mainloop()

     
    def launch(self):

        pass
     

    def execute(self):
        
        try:
            a=Popen(self.commande.get(),stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=True)
            output,err=a.communicate(b"")
            self.output=output.decode()
            if self.output=="":
                try:
                    a=Popen(self.commande.get(),stdin=PIPE,stdout=PIPE,stderr=PIPE)
                    self.err_msg.destroy()
                    self.text_output.destroy()
                    self.output="The command was succesfully executed !"
                    self.text_output=Label(self.fenetre,text=self.output,font=("yoo",10),fg="white",bg="black")
                    self.text_output.place(x=650,y=50)
                except:

                    self.output=self.commande.get()+" "+"is not a valid windows command !"
                    self.err_msg=Label(self.fenetre,text=self.output,fg="red",font=("ee",10))
                    self.err_msg.pack()
                    self.err_msg.place(x=145,y=360)
                    self.fenetre.update()
                    self.fenetre.update_idletasks()
            else:

                try:
                    self.err_msg.destroy()
                except:
                    pass
            

                try:
                    self.text_output.destroy()
                except:
                    pass
          
                self.text_output=Label(self.fenetre,text=self.output,font=("yoo",10),fg="white",bg="black")
                self.text_output.place(x=630,y=40)
            
            self.fenetre.update()
            self.fenetre.update_idletasks()


            

        except:
            pass



        
if __name__=="__main__":
    exec=Window()
    exec.launch()

