from tkinter import *
import random
import time
from PIL import Image,ImageTk
class puzzle:
     def immagine(self):
          try:
               y=Image.open(self.dire.get())
               if y.width>490:
                    self.img=y.crop((0,0,490,490))
               else:
                    self.img=y
          except:
               self.img=Image.open("Default img/prov.jpg")
     def vittoria(self):
          for i in range(25):
               try:
                    self.blist[i].destroy()
               except:
                    pass
          for i in range(9):
               self.blist[i].destroy()
          self.jpg=ImageTk.PhotoImage(self.img)
          image=Label(self.root,image=self.jpg)
          image.place(x=55,y=6)
     def spostat(self,t):
          if self.pun==-1:
               self.pun=t             
          elif self.pdu==-1:
               self.pdu=t
               self.blist[self.pun].config(image=self.imlist[self.imlistc[self.pdu]])
               self.blist[self.pun].image=self.imlist[self.imlistc[self.pdu]]
               self.blist[self.pdu].config(image=self.imlist[self.imlistc[self.pun]])
               self.blist[self.pdu].image=self.imlist[self.imlistc[self.pun]]
               uno=self.imlistc[self.pun]
               due=self.imlistc[self.pdu]
               self.imlistc[self.pdu]=uno
               self.imlistc[self.pun]=due
               self.pun=self.pdu=-1
               if self.imlistc ==sorted(self.imlistc):
                     self.vittoria()
     def tab(self,t):
          if t==3:
               k=163
               xb=45 
               yb=6
               pm=392
               p=173
          elif t==4:
               k=132
               xb=45 
               yb=6
               pm=490
               p=132
          elif t==5:
               k=98
               xb=45 
               yb=6
               pm=500
               p=108
          for i in range(25):
               try:
                    self.blist[i].destroy()
               except:
                    pass
          self.image.destroy()
          self.pun=self.pdu=-1
          self.immagine()
          cd=[0,0,k,k]
          self.imlist=[]
          self.imlistc=random.sample(range(t*t),len(range(t*t)))  
          self.blist=[]
          xbot=xb
          ybot=yb
          for i in range(t):
               for x in range(t):
                    self.jpg=ImageTk.PhotoImage(self.img.crop((cd[0],cd[1],cd[2],cd[3])))
                    cd[0]+=k
                    cd[2]+=k
                    self.imlist.append(self.jpg)
               cd[1]+=k
               cd[0]=0
               cd[3]+=k
               cd[2]=k
          for i in range(t*t):
               self.x=Button(image=self.imlist[self.imlistc[i]],width=p-10,height=p-10,command= lambda i=i: self.spostat(i))
               self.x.image=self.imlist[self.imlistc[i]]
               self.x.place(x=xbot,y=ybot)
               self.blist.append(self.x)
               xbot+=p
               if xbot>pm:
                    xbot=xb
                    ybot+=p
     def hello(self):
          self.img=Image.open("Default img/Logo.jpg")
          self.jpg=ImageTk.PhotoImage(self.img)
          self.image=Label(self.root,image=self.jpg)
          self.image.place(x=37,y=6)
     def __init__(self,root):
          self.root=root
          info=Label(text="Insert directory",font='Arial 12')
          info.place(x=25,y=540)
          self.dire=Entry(root,width=60,font='Arial 11')
          self.dire.place(x=25,y=568)
          self.hello()
          self.menubar=Menu(root,tearoff=0)
          self.gioco =Menu(self.menubar,tearoff=0)
          self.tabella= Menu(self.gioco,tearoff=0)
          self.tabella.add_command(label='Easy 3x3',command=lambda root=root:self.tab(3))
          self.tabella.add_command(label='Medium 4x4',command=lambda root=root:self.tab(4))
          self.tabella.add_command(label='Difficult 5x5',command=lambda root=root:self.tab(5))
          self.gioco.add_cascade(label='Tabella',menu=self.tabella)
          self.menubar.add_cascade(label='Gioco',menu=self.gioco)
          root.config(menu=self.menubar)
def main():
     root=Tk()
     root.title('Puzzle Game')
     root.geometry('600x600+400+50')
     puzzle(root)
     root.mainloop()
main()
