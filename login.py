from tkinter import *
from PIL import Image,ImageTk,ImageDraw #pip install pillow
from datetime import*
import time
from math import *
import pymysql #pip install pymysql
import os
from tkinter import messagebox,ttk
class Login_window:
    def __init__(self, root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        #======bg =====

        left_lbl=Label(self.root,bg="#08A302",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        #========frame=====
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2")
        title.place(x=250,y=50)
        email = Label(login_frame, text="EMAIL ADDRESS", font=("times new roman", 18, "bold"), bg="white",fg="gray")
        email.place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="gray")
        pass_.place(x=250,y=230)
        self.txt_pass_=Entry(login_frame,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_pass_.place(x=250,y=280,width=350,height=35)

        btn_reg=Button(login_frame,cursor="hand2",command=self.register_window,text="Register new Account?",font=("times new roman",14),bg="white",bd=0,fg="#800857")
        btn_reg.place(x=250,y=320)
        btn_forget = Button(login_frame, cursor="hand2", command=self.forget_password_window, text="Forget Password?",font=("times new roman",14),bg="white",bd=0,fg="red")
        btn_forget.place(x=450,y=320)

        btn_login = Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#800857",cursor="hand2")
        btn_login.place(x=250,y=360,width=180,height=40)

        #Clock========
        self.lbl=Label(self.root,text="\nWebCode Clock",font=("Book Antique",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)
        self.working()



    def reset(self):
        self.cmb_quection.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)

    def forget_password(self):
        if self.cmb_quection.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Neeraj@123", database="employee")

                cur = con.cursor()
                cur.execute("select * from students where email=%s and quection=%s and answer=%s",(self.txt_email.get(),self.cmb_quection.get(),self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:

                    messagebox.showerror("Error", "please Select the Correct Security Quection /Enter Answer  ",parent=self.root2)
                else:
                    cur.execute("update students set password=%s where email=%s",(self.txt_new_password.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","your password has been reset,please login with new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()



            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root)


    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error", "please enter the   email address to reset your password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="Neeraj@123",database="employee")

                cur=con.cursor()
                cur.execute("select * from students where email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row==None:

                    messagebox.showerror("Error", "please enter the  valid email address to reset your password",parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text="ForgetPassword", font=("time new roman", 20, "bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)

                    # ====Forgetpassword======
                    question = Label(self.root2, text="Security Quection", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)

                    self.cmb_quection = ttk.Combobox(self.root2, font=("times new roman", 13), state="readonly",justify=CENTER)
                    self.cmb_quection["values"] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
                    self.cmb_quection.place(x=50, y=130, width=250)
                    self.cmb_quection.current(0)

                    answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=50, y=180)
                    self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.txt_answer.place(x=50, y=210, width=250)

                    new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"),bg="white", fg="gray").place(x=50, y=260)
                    self.txt_new_password = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.txt_new_password.place(x=50, y=290, width=250)

                    btn_change_passwod = Button(self.root2, text="Reset Password",command=self.forget_password, bg="green", fg="white",font=("times new roman", 15, "bold")).place(x=90, y=340)


            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root)





    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="Neeraj@123",database="employee")

                cur=con.cursor()
                cur.execute("select * from students where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:

                    messagebox.showerror("Error", "Invalid USERNAME & PASSWORD", parent=self.root)
                else:
                    messagebox.showinfo("Success", f"Welcome:{self.txt_email.get()}", parent=self.root)
                    self.root.destroy()


                    os.system("python RMS.py")

                con.close()


            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root)


    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #====For Clock Image
        bg=Image.open("Images/clocks.png.png")
        bg=bg.resize((300,300),Image.LANCZOS)
        clock.paste(bg,(50,50))
         #====Hour Line Image=======
        origin=200,200
        draw.line((origin ,200+50*sin (radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #====Min Line Images=====
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="black", width=3)
        #=====Sec Line Images=====
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="yellow", width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("Images/clock_.png.png")
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        self.clock_image(hr,min_,sec_)
        self.image=ImageTk.PhotoImage(file="Images/clock_.png.png")
        self.lbl.config(image=self.image)
        self.lbl.after(200,self.working)


root=Tk()
obj=Login_window(root)
root.mainloop()
