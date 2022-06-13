from tkinter import *
from tkinter.ttk import Combobox
from ast import literal_eval

class Conversion_System:
    def __init__(self,app):
        self.app = app
        cb1 = Combobox(app,values=["Dec","Hex","Oct","Bin"])
        cb1.place(x=30,y=40)
        cb1.current(0)
        t1 = Entry(app, bd=2, relief=GROOVE, font=("Arial", 10,"bold"))
        t1.place(x=30, y=100)
    
        cb2 = Combobox(app,values=["Dec","Hex","Oct","Bin"])

        cb2.place(x=220, y=40)
        cb2.current(0)
        t2 = Entry(app, bd=2, relief=GROOVE, font=("Arial", 10, "bold"))
        t2.insert(0, "0000")
        t2.place(x=220, y=100)
        t2.config(state='disabled')

        btn = Button(text="Convert",command=lambda:self.convert(cb1,cb2,t1,t2),font=("Arial", 10, "bold"))
        btn.place(x=170, y=180)

    def callbackFunc(self,event):
        print(self.cb1.get())

    def decimal_to_hexadecimal(self,dec):
         return hex(dec)

    def decimal_to_octal(self,dec):
        return oct(dec)

    def decimal_to_binary(self,dec):
        return bin(dec)

    def DecimalToBinary(self,num):

        if num > 1:
            self.DecimalToBinary(num // 2)
        v = num % 2
        print(num % 2, end='')

    def binaryToDecimal(self,n):
        return int(n, 2)

    def convert(self,cmbox1,cmbox2,t1,t2):
        self.cmbox1 = cmbox1
        self.cmbox2 = cmbox2
        self.t1 = t1
        self.t2 = t2
        str1 = self.cmbox1.get()
        str2 = self.cmbox2.get()
                # From Dec
        if (str1 == "Dec" and str2 == "Dec"):
            val = int(self.Text1.get())
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, val)
            t2.config(state='disabled')

        elif(str1 == "Dec" and str2 == "Hex"):
            val = int(self.t1.get())
            r = self.decimal_to_hexadecimal(val)
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0,r)
            t2.config(state='disabled')

        elif(str1 == "Dec" and str2 == "Oct"):
            val = int(self.t1.get())
            r = self.decimal_to_octal(val)
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, r)
            rt2.config(state='disabled')

        elif (str1 == "Dec" and str2 == "Bin"):
            val = int(self.t1.get())
            r = self.decimal_to_binary(val)
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, str(r))
            t2.config(state='disabled')

                # From Hex
        elif (str1 == "Hex" and str2 == "Hex"):
            val = self.t1.get()
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, val)
            t2.config(state='disabled')

        elif (str1 == "Hex" and str2 == "Dec"):
            val = "0x"+self.t1.get()
            res = literal_eval(val)
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, str(res))
            t2.config(state='disabled')

        elif (str1 == "Hex" and str2 == "Oct"):

            val = self.t1.get()
            res = oct(int(val))
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, str(res))
            t2.config(state='disabled')

        elif (str1 == "Hex" and str2 == "Bin"):
            print(str1," and ",str2)
            res = bin(int(self.t1.get(), 16)).zfill(8)
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, str(res))
            t2.config(state='disabled')

            # From Oct
        elif (str1 == "Oct" and str2 == "Oct"):
            val = str(self.t1.get())
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, val)
            t2.config(state='disabled')

        elif (str1 == "Oct" and str2 == "Dec"):
            print(str1, " and ", str2)
            res = str(int(self.t1.get(), 8))
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, str(res))
            t2.config(state='disabled')

        elif (str1 == "Oct" and str2 == "Hex"):
            dec = str(int(self.t1.get(), 8))
            decm = int(dec)
            res = str(hex(decm))
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, str(res))
            t2.config(state='disabled')

        elif (str1 == "Oct" and str2 == "Bin"):
            dec = str(int(self.t1.get(), 8));
            decm = int(dec);
            res = str(bin(decm))
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, str(res))
            t2.config(state='disabled')

                # From Bin
        elif (str1 == "Bin" and str2 == "Bin"):
            val = str(self.t1.get())
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, val)
            t2.config(state='disabled')

        elif (str1 == "Bin" and str2 == "Dec"):
            val = self.t1.get()
            print("V : ", val)
            ret = self.binaryToDecimal(val)
            t2.config(state='normal')
            self.t2.delete(0,END)
            self.t2.insert(0,str(ret))
            t2.config(state='disabled')

        elif (str1 == "Bin" and str2 == "Hex"):
            temp = int(self.t1.get(), 2)
            ret = str(hex(temp))
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, str(ret))
            t2.config(state='disabled')

        elif (str1 == "Bin" and str2 == "Oct"):
            temp = int(self.t1.get(), 2);
            ret = str(oct(temp))
            t2.config(state='normal')
            self.t2.delete(0, END)
            self.t2.insert(0, str(ret))
            t2.config(state='disabled')
        else:
            print("Not",str1,str2)


root = Tk()
root.geometry("400x250+400+200")
root.title("Conversion System")
data = Conversion_System(root)
root.mainloop()
