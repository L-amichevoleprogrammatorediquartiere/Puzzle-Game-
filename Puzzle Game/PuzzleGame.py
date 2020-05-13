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
          if self.imlistc==self.seq:
               self.vittoria()
     def tabtre(self):
          for i in range(25):
               try:
                    self.blist[i].destroy()
               except:
                    pass
          self.image.destroy()
          self.pun=self.pdu=-1
          self.seq=[0,1,2,3,4,5,6,7,8]
          self.immagine()
          cd=[-163,0,0,163]
          self.imlist=[]
          self.imlistc=[]  
          self.blist=[]
          xbot=45 
          ybot=6
          for i in range(3):
               for x in range(3):
                    cd[2]+=163
                    cd[0]+=163
                    r=self.img.crop((cd[0],cd[1],cd[2],cd[3])) 
                    self.jpg=ImageTk.PhotoImage(r)
                    self.imlist.append(self.jpg)
                    if x>1:
                         cd[1]+=163
                         cd[0]=-163
                         cd[3]+=163
                         cd[2]=0
          for i in range(9):
               v=random.choice(self.seq)
               self.seq.remove(v)
               self.imlistc.append(v)
               self.x=Button(image=self.imlist[v],width=163,height=163,command= lambda i=i: self.spostat(i))
               self.x.image=self.imlist[v]
               self.x.place(x=xbot,y=ybot)
               self.blist.append(self.x)
               xbot+=173
               if xbot>392:
                    xbot=45
                    ybot+=173
          self.seq=[0,1,2,3,4,5,6,7,8]

     def tabquattro(self):
          self.pun=self.pdu=-1
          for i in range(25):
               try:
                    self.blist[i].destroy()
               except:
                    pass
          self.image.destroy()
          self.seq=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
          self.immagine()
          cd=[0,0,122,122]
          self.imlist=[]
          self.imlistc=[]  
          self.blist=[]
          xbot=40 
          ybot=6
          for i in range(4):
               for x in range(4):
                    r=self.img.crop((cd[0],cd[1],cd[2],cd[3]))
                    self.jpg=ImageTk.PhotoImage(r)
                    self.imlist.append(self.jpg)
                    cd[0]+=122
                    cd[2]+=122
               cd[0]=0
               cd[1]+=122
               cd[2]=122
               cd[3]+=122
          for i in range(16):
               v=random.choice(self.seq)
               self.seq.remove(v)
               self.imlistc.append(v)
               self.i=Button(image=self.imlist[v],width=122,height=122,command= lambda i=i: self.spostat(i))
               self.i.image=self.imlist[v]
               self.i.place(x=xbot,y=ybot)
               self.blist.append(self.i)
               xbot+=132
               if xbot>437:
                    xbot=40
                    ybot+=132
          self.seq=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
     def tabcinque(self):
          self.pun=self.pdu=-1
          for i in range(25):
               try:
                    self.blist[i].destroy()
               except:
                    pass
          self.image.destroy()
          self.seq=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
          self.immagine()
          cd=[0,0,98,98]
          self.imlist=[]
          self.imlistc=[]  
          self.blist=[]
          xbot=35
          ybot=6
          for i in range(5):
               for x in range(5):
                    r=self.img.crop((cd[0],cd[1],cd[2],cd[3]))
                    self.jpg=ImageTk.PhotoImage(r)
                    self.imlist.append(self.jpg)
                    cd[0]+=98
                    cd[2]+=98
               cd[0]=0
               cd[1]+=98
               cd[2]=98
               cd[3]+=98
          for i in range(25):
               v=random.choice(self.seq)
               self.seq.remove(v)
               self.imlistc.append(v)
               self.i=Button(image=self.imlist[v],width=98,height=98,command= lambda i=i: self.spostat(i))
               self.i.image=self.imlist[v]
               self.i.place(x=xbot,y=ybot)
               self.blist.append(self.i)
               xbot+=108
               if xbot>500:
                    xbot=35
                    ybot+=108
          self.seq=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
     def ciao(self):
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
          self.ciao()
          self.menubar=Menu(root,tearoff=0)
          self.gioco =Menu(self.menubar,tearoff=0)
          self.tabella= Menu(self.gioco,tearoff=0)
          self.tabella.add_command(label='Easy 3x3',command=lambda root=root:self.tabtre())
          self.tabella.add_command(label='Medium 4x4',command=lambda root=root:self.tabquattro())
          self.tabella.add_command(label='Difficult 5x5',command=lambda root=root:self.tabcinque())
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
