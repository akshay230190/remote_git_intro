import tkinter as tk
import pickle
from PIL import ImageTk,Image

print(".......................loading model.........................")
with open('mpg.pkl','rb')as fp:
    model=pickle.load(fp)
    fp.close()
print("....................... sucefully loaded.........................")
root=tk.Tk()
horse=tk.DoubleVar()
weight=tk.DoubleVar()
dis=tk.DoubleVar()
img1=ImageTk.PhotoImage(Image.open('imgs/horse.png'))
img2=ImageTk.PhotoImage(Image.open('imgs/weight.png'))
img3=ImageTk.PhotoImage(Image.open('imgs/displace.png'))
def clear():
    horse.set('')
    weight.set('')
    dis.set('')
clear()
f1=tk.Frame(root)
l1=tk.Label(f1,image=img1,text="Horsepower".center(20)+":")
l1.config(bg='white',fg='black',font=('monospace',25,'bold'))
l1.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)

e1=tk.Entry(f1,textvariable=horse)
e1.config(bg='white',fg='black',font=('monospace',15,'bold'))
e1.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)
e1.focus()
f1.pack(fill=tk.BOTH,expand=tk.YES,padx=20,pady=20)

f2=tk.Frame(root)
l2=tk.Label(f2,image=img2,text="Weight".center(20)+":")
l2.config(bg='white',fg='black',font=('monospace',25,'bold'))
l2.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)

e2=tk.Entry(f2,textvariable=weight)
e2.config(bg='white',fg='black',font=('monospace',15,'bold'))
e2.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)
f2.pack(fill=tk.BOTH,expand=tk.YES,padx=20,pady=20)

f3=tk.Frame(root)
l3=tk.Label(f3,image=img3,text="Discplacement".center(20)+":")
l3.config(bg='white',fg='black',font=('monospace',25,'bold'))
l3.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)

e3=tk.Entry(f3,textvariable=dis)
e3.config(bg='white',fg='black',font=('monospace',15,'bold'))
e3.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)
f3.pack(fill=tk.BOTH,expand=tk.YES,padx=20,pady=20)

b1=tk.Button(root,text='Predict Milage',command=lambda:predict())
b1.config(fg='white',bg='purple',font=('monospace',15,'bold'))
b1.pack(fill=tk.X,expand=tk.YES)

b2=tk.Button(root,text='Exit',command=lambda:root.quit())
b2.config(fg='white',bg='purple',font=('monospace',15,'bold'))
b2.pack(fill=tk.X,expand=tk.YES)

def predict():
    h=horse.get()
    w=weight.get()
    d=dis.get()
    feature=[[h,w,d]]
    clear()
    milage=model.predict(feature)[0]
    print("Milage of car:",milage)
    win=tk.Toplevel(root)
    win.grab_set()
    text=f"""
    
    _____________________
    #HorsePower :  {h:.2f}
    weight      :  {w:.2f}
    Displacement:  {d:.2f}
    ______________________
    Milage      : {milage:.2f}

    
    """
    msg=tk.Message(win,text=text)
    msg.config(bg='#eeeeee',fg='#333333',font=('monospace', 25, 'bold'))
    msg.pack(fill=tk.BOTH,expand=tk.YES)
    eb=tk.Button(win,text='Exit',command=lambda:win.destroy())
    eb.config(fg='white', bg='red', font=('monospace', 25, 'bold'))
    eb.pack(fill=tk.X, expand=tk.YES)
    e1.focus()
root.title('Calculate Milage of car')
root.mainloop()
