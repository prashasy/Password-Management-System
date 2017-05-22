import tkinter as tk
from tkinter import messagebox
import os
from random import randint
class app:
	def Return(wn):
		messagebox.showinfo("Logged Out","You have logged out")
		wn.destroy()
		app.Main()

	def Return_to_Main(wn):
		wn.destroy()
		app.Main()

	def generatePas():
		string=""
		arr=[0,1,12,3,4,5,6,7,8,9,'!','@','#','$','%','^','&','*','-','+',':',',','.','<','>','?','/','\\','{','}','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
		for i in range(0,8): 
			string+=str(arr[randint(0,43)])
		messagebox.showinfo("Random Password",string)
		print(string)


	def passGen(master):
		global string
		master.destroy()
		string="Aß∫ "
		wn=tk.Tk()
		wn.geometry("800x800")
		wn.configure(background="grey")
		xy = tk.PhotoImage (file = "tumblr.gif")
		l=tk.Label(wn,image=xy)
		l.image=xy
		l.place(x=0,y=0,relwidth=1,relheight=1)
		l_title=tk.Message(wn,text="Password Generator",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_title.config(font=("Courier",24))
		l_title.pack(side="top")
		l_foot=tk.Message(wn,text="J U I T",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_foot.config(font=("Courier",24))
		l_foot.pack(side="bottom")	


		b=tk.Button(wn,text="Generate a random password",command=lambda:app.generatePas())	
		b.place(x=250,y=450)
		back=tk.Button(wn,text="Go Back",command=lambda:app.Return_to_Main(wn))
		back.pack(side="bottom")

		wn.bind("<Return>",lambda x: app.generatePas())
		
	def do_signup(master,name,pas):
		fdet=open(name+".txt",'w')
		fdet.write(name+"\n")
		fdet.write(pas)
		fdet.close()
		messagebox.showinfo("Congratulations!!","You have Successfully SignedUp!!")
		master.destroy()
		


	def passMngr_signup():
		print("1")
		wn=tk.Tk()
		wn.geometry("800x500")
		wn.configure(background="grey")
		l_title=tk.Message(wn,text="SignUp for the Password Management System",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_title.config(font=("Courier",24))
		l_title.pack(side="top")
		l_foot=tk.Message(wn,text="J U I T",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_foot.config(font=("Courier",24))
		l_foot.pack(side="bottom")
		l1=tk.Label(wn,text="Enter Name:",relief="raised")
		l1.pack(side="top")
		e1=tk.Entry(wn)
		e1.pack(side="top")
		l2=tk.Label(wn,text="Enter password:",relief="raised")
		l2.pack(side="top")
		e2=tk.Entry(wn,show="*")
		e2.pack(side="top")
		b=tk.Button(wn,text="Submit",relief="raised",command=lambda:app.do_signup(wn,e1.get().strip(),e2.get().strip()))
		b.pack(side="top")
		wn.bind("<Return>",lambda x:app.do_signup(wn,e1.get().strip(),e2.get().strip()))

	def do_newPass(wn,user,name,pas):
		wn.destroy()
		f=open(user+"-records.txt",'a+')
		f.write(name+"\n")
		f.write(pas+"\n\n")
		f.close()
		messagebox.showinfo("Cogratulations!!","New Record Added Successfully!!")

	def newPass(user):
		wn=tk.Tk()
		wn.geometry("800x500")
		wn.configure(background="grey")
		l_title=tk.Message(wn,text="SignUp for the Password Management System",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_title.config(font=("Courier",24))
		l_title.pack(side="top")
		l_foot=tk.Message(wn,text="J U I T",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_foot.config(font=("Courier",24))
		l_foot.pack(side="bottom")
		l1=tk.Label(wn,text="Enter Name of Website:",relief="raised")
		l1.pack(side="top")
		e1=tk.Entry(wn)
		e1.pack(side="top")
		l2=tk.Label(wn,text="Enter password:",relief="raised")
		l2.pack(side="top")
		e2=tk.Entry(wn,show="*")
		e2.pack(side="top")
		b=tk.Button(wn,text="Submit",relief="raised",command=lambda:app.do_newPass(wn,user,e1.get().strip(),e2.get().strip()))
		b.pack(side="top")
		wn.bind("<Return>",lambda x:app.do_newPass(wn,user,e1.get().strip(),e2.get().strip()))

	def showRecords(user):
		wn=tk.Tk()
		wn.geometry("800x500")
		wn.configure(background="grey")
		l_title=tk.Message(wn,text="Your Saved Passwords:",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_title.config(font=("Courier",24))
		l_title.pack(side="top")
		l_foot=tk.Message(wn,text="J U I T",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_foot.config(font=("Courier",24))
		l_foot.pack(side="bottom")
		frec=open(user+"-records.txt",'r')
		c = tk.Canvas(wn,width=200)
		c.pack(side = 'left',expand=1)
		for line in frec:
			l = tk.Label(c,text=line,bg='orange',fg="white",width=300)
			l.pack(side='top',expand=1,fill='x')

		frec.close()
		quit=tk.Button(text="Quit",command=lambda:wn.destroy())



	def login_home(root,user):
		root.destroy()
		wn=tk.Tk()
		wn.geometry("800x500")
		wn.configure(background="grey")
		l_title=tk.Message(wn,text="",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_title.config(font=("Courier",24))
		l_title.pack(side="top")
		l_foot=tk.Message(wn,text="J U I T",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_foot.config(font=("Courier",24))
		l_foot.pack(side="bottom")

		b1=tk.Button(text="Save New Password",command=lambda:app.newPass(user))
		b1.pack(side="top")

		b2=tk.Button(text="Show Saved Passwords",command=lambda:app.showRecords(user))
		b2.pack(side="top")

		img=tk.PhotoImage(file="logout.gif")
		img1=img.subsample(2,2)
		b3=tk.Button(image=img1,relief="raised",command=lambda:app.Return(wn))
		b3.image=img1
		b3.pack(side="bottom")


	def check_login(name,pas):
		try:
			f=open(name+".txt")
		except FileNotFoundError:
			messagebox.showinfo("Error","Invalid Login Credentials")
			return 0
		f.close()
		return 1

	def do_login(root,master,name,pas):
		master.destroy()
		if app.check_login(name,pas)==1 :
			app.login_home(root,name)

	def passMngr_login(root):
		wn=tk.Tk()
		wn.geometry("800x500")
		wn.configure(background="grey")
		l_title=tk.Message(wn,text="SignUp for the Password Management System",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_title.config(font=("Courier",24))
		l_title.pack(side="top")
		l_foot=tk.Message(wn,text="J U I T",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_foot.config(font=("Courier",24))
		l_foot.pack(side="bottom")
		l1=tk.Label(wn,text="Enter Name:",relief="raised")
		l1.pack(side="top")
		e1=tk.Entry(wn)
		e1.pack(side="top")
		l2=tk.Label(wn,text="Enter password:",relief="raised")
		l2.pack(side="top")
		e2=tk.Entry(wn,show="*")
		e2.pack(side="top")
		b=tk.Button(wn,text="Log in",relief="raised",command=lambda:app.do_login(root,wn,e1.get().strip(),e2.get().strip()))
		b.pack(side="top")
		wn.bind('<Return>',lambda x:app.do_login(root,wn,e1.get().strip(),e2.get().strip()))


	def passMngr(master):
		master.destroy()
		wn=tk.Tk()
		wn.geometry("800x400")
		wn.configure(background="grey")
		l_title=tk.Message(text="Welcome to the Password Management System",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_title.config(font=("Courier",24))
		l_title.pack(side="top")
		l_foot=tk.Message(text="J U I T",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_foot.config(font=("Courier",24))
		l_foot.pack(side="bottom")
		b1=tk.Button(text="SignUp",command=lambda:app.passMngr_signup())
		b1.place(x=200,y=150)
		b2=tk.Button(text="Login",command=lambda:app.passMngr_login(wn))
		b2.place(x=600,y=150)
		b3=tk.Button(text="Return",command=lambda:app.Return_to_Main(wn))
		b3.place(x=400,y=300)




	def Main():
		rootwn=tk.Tk()
		rootwn.geometry("1000x500")
		rootwn.title("Password System")
		rootwn.configure(background="grey")
		bg_image = tk.PhotoImage(file ="bg1.gif")
		xy = tk.Label (rootwn,image = bg_image)
		xy.place(x=0,y=0,relwidth=1,relheight=1)

		l_title=tk.Message(text="Welcome to\n\nPassword Management System",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_title.config(font=("Courier",24))
		l_title.pack(side="top")

		b1=tk.Button(text="A guide to strong passwords",command=lambda:os.system("open "+"report.pdf"))
		b1.place(x=450,y=150)	

		b2=tk.Button(text="Password Generator",command=lambda:app.passGen(rootwn))
		b2.place(x=230,y=340)


		b3=tk.Button(text="Password Manager",command=lambda:app.passMngr(rootwn))
		b3.place(x=475,y=340)	


		l_foot=tk.Message(text="J U I T",relief="raised",width=2000,padx=520,pady=10,fg="white",bg="black",justify="center",anchor="center")
		l_foot.config(font=("Courier",24))
		l_foot.pack(side="bottom")
		rootwn.mainloop()



app.Main()
