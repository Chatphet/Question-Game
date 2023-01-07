from tkinter import *


answers=["go",  #เฉลย
         "love",
         "eat",
         "math",
         "box"]

exams=["ไป",    #โจทย์
       "รัก",
       "กิน",
       "คณิตศาสตร์",
       "กล่อง"]


def win2():
    def win3():
        mywin2.destroy()#################################################################
        your_input=[]
        your_input.append(your_input1.get())
        your_input.append(your_input2.get())
        your_input.append(your_input3.get())
        your_input.append(your_input4.get())
        your_input.append(your_input5.get())
        Name=name.get()
        mywin3=Tk()
        mywin3.config(bg="#F4A5A1")
        score=0
        for i in range(5):
            if your_input[i]==answers[i]:
                score+=1
        score=Label(mywin3,text="{} your score is {}".format(Name,score),font="Tahoma 30 bold",bg="#F4A5A1").grid()
        
    #PAGE 2
    mywin1.destroy() ##################################################################
    e=10
    mywin2=Tk()
    mywin2.config(bg="#F4A5A1")
    mywin2.minsize(450,350)
    your_input1=StringVar()
    your_input2=StringVar()
    your_input3=StringVar()
    your_input4=StringVar()
    your_input5=StringVar()
    


    HEAD=Label(mywin2,text="จงเติมคำภาษาอังกฤษ",font="Tahoma 20 bold",bg="#F4A5A1").place(x=90,y=20)
    

    for i in range(5):
        exam=Label(mywin2,text=("{}".format(exams[i])),font="Tahoma 10 bold",bg="#F4A5A1").place(x=90,y=70+e)
        i+=1
        e+=30
    
    enter=Entry(mywin2,textvariable=your_input1).place(x=220,y=80)
    enter=Entry(mywin2,textvariable=your_input2).place(x=220,y=110)
    enter=Entry(mywin2,textvariable=your_input3).place(x=220,y=140)
    enter=Entry(mywin2,textvariable=your_input4).place(x=220,y=170)
    enter=Entry(mywin2,textvariable=your_input5).place(x=220,y=200)
    bt_ok=Button(mywin2,text="Let's Check",command=win3).place(x=220,y=270)
    bt_close=Button(mywin2,text="CLOSE",command=mywin2.destroy).place(x=160,y=270)
    
    

    
    mywin2.mainloop()
    
#PAGE 1
e=10
mywin1=Tk()
name=StringVar()
mywin1.config(bg="#F4A5A1")
mywin1.minsize(450,200)
head=Label(mywin1,text="Input name",font="Tahoma 30 bold",bg="#F4A5A1").place(x=90,y=10)
namebox=Entry(mywin1,textvariable=name).place(x=150,y=80)
bt_next=Button(mywin1,text="NEXT",command=win2).place(x=150,y=120)
bt_close=Button(mywin1,text="CLOSE",command=mywin1.destroy).place(x=230,y=120)
mywin1.mainloop()


