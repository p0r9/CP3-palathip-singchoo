from tkinter import*
import math

def calculateBMI(event):
    LabelResult.configure(text=float(textboxw.get())/math.pow(float(textboxh.get())/100,2))
    bmi = (float(textboxw.get())/math.pow(float(textboxh.get())/100,2))
    if  bmi < 18.5 :
         LabelText.configure (text='ผอมเกินไป',font=('arial,30'),fg='red')
    elif  bmi > 29.9 :
          LabelText.configure (text='อ้วนมาก',font=('arial,30'),fg='red')
    elif  bmi > 24.9 :
         LabelText.configure (text='อ้วน',font=('arial,30',),fg='red')
    elif  bmi > 22.9 :
         LabelText.configure (text='น้ำหนักเกิน',font=('arial,30'),fg='red')
    elif  bmi > 18.5 :
         LabelText.configure (text='น้ำหนักปกติเหมาะสม',font=('arial,30'),fg='red')
    



MainWindow = Tk()
LabelHeight = Label(MainWindow,text='ส่วนสูง (cm.)',font=('arial,30'))
LabelHeight.grid(row=0,column=0)
textboxh = Entry(MainWindow)
textboxh.grid(row=0,column=1)
LabelWeight = Label(MainWindow,text='น้ำหนัก (kg.)',font=('arial,30'))
LabelWeight.grid(row=1,column=0)
textboxw = Entry(MainWindow)
textboxw.grid(row=1,column=1)
calculatebutton = Button(MainWindow,text='คำนวณ',font=('arial,30'))
calculatebutton.grid(row=2)
calculatebutton.bind('<Button-1>',calculateBMI)
LabelResult = Label(MainWindow,text='ผลลัพธ์',font=('arial,30'))
LabelResult.grid(row=2,column=1)
LabelText = Label(MainWindow,text='ระดับ',font=('arial,30'))
LabelText.grid(row=3,column=1)
MainWindow.mainloop()