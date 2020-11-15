import tkinter
from tkinter import *
from PIL import Image,ImageTk
import random

##root=Tk()
##root.geometry("1000x600")
##root.resizable(0, 0)
##root.title("FreeTeacher.org")
##root.iconbitmap("freeteacher.ico")
##logo=ImageTk.PhotoImage(Image.open("freeteacher.png"))

def main():
    root=Tk()
    root.geometry("1000x600")
    root.resizable(0, 0)
    root.title("FreeTeacher.org")
    root.iconbitmap("freeteacher.ico")
    logo=ImageTk.PhotoImage(Image.open("freeteacher.png"))
    bgcolour="navajo white"
    fgcolour="yellow green"
    
    start=Canvas(root,width=1000, height=600,bg=bgcolour)
    start.create_rectangle(222, 525, 762, 195,outline=fgcolour, fill="#ccd8a5")
    start.create_rectangle(0, 0, 1000, 105,outline="#fff4e0", fill="#fff4e0")
    start.pack()
    
    title=Label(root,text="FreeTeacher",font=("",45,"bold"),bg="#fff4e0",fg=fgcolour,width=15)
    dectitle=Label(root,text=".org",font=("",30,"bold"),bg="#fff4e0",fg=fgcolour)
    subhead=Label(root,text="·teachers helping students·",font=("",25,"italic"),bg=bgcolour,fg=fgcolour)

    line1=Label(root,text="-    Free teacher is a volunteering interface with the",bg="#ccd8a5",font=("",13))
    line2=Label(root,text="     aim of connecting students in need of educational assistance",bg="#ccd8a5",font=("",13))
    line3=Label(root,text="     or extra support with teachers willing to help.",bg="#ccd8a5",font=("",13))
    line4=Label(root,text="-    You will be able to connect with teachers",bg="#ccd8a5",font=("",13))
    line5=Label(root,text="     from all around the globe!",bg="#ccd8a5",font=("",13))
    line6=Label(root,text="-    Welcome to our teaching family!",bg="#ccd8a5",font=("",13))

    def signup():
        rrll("Register")
    
    def signin():
        rrll("Login")

    signupB=Button(root,text="Register",bd=0,width=27,font=("",12),bg="white", fg='#333333',command=signin)
    signinB=Button(root,text="Sign in",bd=0,width=27,font=("",12),bg="white", fg='#333333',command=signup)

    def OnHoverU(event):
        signupB.config(bg=fgcolour, fg="#dddddd")
    def OnLeaveU(event):
        signupB.config(bg="white", fg='#333333')
    def OnHoverI(event):
        signinB.config(bg=fgcolour, fg="#dddddd")
    def OnLeaveI(event):
        signinB.config(bg="white", fg='#333333')

    signupB.bind('<Enter>', OnHoverU)
    signupB.bind('<Leave>', OnLeaveU)
    signinB.bind('<Enter>', OnHoverI)
    signinB.bind('<Leave>', OnLeaveI)

    start.create_window(357,545,window=signupB)
    start.create_window(627,545,window=signinB)
    
    start.create_window(449,50,window=title)
    start.create_window(669,56,window=dectitle)
    start.create_window(495,152,window=subhead)

    start.create_window(492,235,window=line1)
    start.create_window(492,285,window=line2)
    start.create_window(492,335,window=line3)
    start.create_window(492,385,window=line4)
    start.create_window(492,435,window=line5)
    start.create_window(492,485,window=line6)
    
    start.create_image(60,55,image=logo)
    
    root.mainloop()
    
def rrll(data):
    def Chosen(chosenOption):
        if chosenOption=="Register":
            register()
        elif chosenOption=="Login":
            Login()
    def register():
        def teacherOrStudent2(window,value):
            global loginButton
            if value==0:
                pass
                
            elif value==1:
                pass
        def teacherOrStudent(window,value):
            global registerWindow
            if value.get()==0: #If teacher selected
                print("TEACHER")
                registerLabel=Label(registerWindow,text="Register!",bg="papaya whip",fg="#72FF27",font=("constantia",30),width=100,height=1)
                registerLabel.grid(row=0, column=0)
                registerWindow.grid_columnconfigure(0, weight=1)
                
                option=IntVar()
                questionFrame2=Frame(registerWindow,bg="lemon chiffon")
                questionFrame2.grid(row=2,column=0)
                
                radioFrame=Frame(registerWindow,pady=10,bg="lemon chiffon")
                radioFrame.grid(row=1,column=0)

                nameLabel=Label(questionFrame2,text="Full name",bg="lemon chiffon",font=("Georgia",14))
                name=Entry(questionFrame2,width=23)
                
                ageLabel=Label(questionFrame2,text="Age",bg="lemon chiffon",font=("Georgia",14))
                year=Entry(questionFrame2)
                
                emailLabel=Label(questionFrame2,text="Email",bg="lemon chiffon",font=("Georgia",14))
                email=Entry(questionFrame2,width=23)

                preferredLanguage=Label(questionFrame2,text="Preferred language",bg="lemon chiffon",font=("Georgia",14))
                language=IntVar()
                englishLanguage=Radiobutton(questionFrame2,font=("Georgia",12),activebackground="lemon chiffon",text="English",bg="lemon chiffon",variable=language,value=0)
                spanishLanguage=Radiobutton(questionFrame2,font=("Georgia",12),activebackground="lemon chiffon",text="Spanish",bg="lemon chiffon",variable=language,value=1)

                subjectsLabel=Label(questionFrame2,text="Subjects",bg="lemon chiffon",font=("Georgia",14))
                englishSubject=IntVar()
                english=Checkbutton(questionFrame2, text="English", variable=englishSubject,bg="lemon chiffon",font=("Georgia",9))
                mathSubject=IntVar()
                math=Checkbutton(questionFrame2, text="Math", variable=mathSubject,bg="lemon chiffon",font=("Georgia",9))
                physicsSubject=IntVar()
                physics=Checkbutton(questionFrame2, text="Physics", variable=physicsSubject,bg="lemon chiffon",font=("Georgia",9))
                biologySubject=IntVar()
                biology=Checkbutton(questionFrame2, text="Biology", variable=biologySubject,bg="lemon chiffon",font=("Georgia",9))
                chemistrySubject=IntVar()
                chemistry=Checkbutton(questionFrame2, text="Chemistry", variable=chemistrySubject,bg="lemon chiffon",font=("Georgia",9))
                computerScienceSubject=IntVar()
                computerScience=Checkbutton(questionFrame2, text="Computer Science", variable=computerScienceSubject,bg="lemon chiffon",font=("Georgia",9))

                uploadCertificate=Button(questionFrame2,text="Select Certificate",font=("Georgia",11),width=15,height=1,command=lambda: UploadAction(questionFrame))
                #Register button
                registerButton=Button(questionFrame2,text="Login",font=("Georgia",11),width=15,height=1,command= RegisterButton)
                
                teacher=Radiobutton(radioFrame,font=("Georgia",20),activebackground="lemon chiffon",text="Teacher",bg="lemon chiffon",variable=option,value=0,command=lambda: teacherOrStudent(questionFrame2,option.get()))
                student=Radiobutton(radioFrame,font=("Georgia",20),activebackground="lemon chiffon",text="Student",bg="lemon chiffon",variable=option,value=1,command=lambda: teacherOrStudent(questionFrame2,option.get()))
                teacher.grid(row=1,column=0)
                spacer=Label(radioFrame,text=" ",bg="lemon chiffon").grid(row=1,column=1)
                student.grid(row=1,column=2,pady=10)

                nameLabel.grid(row=1,column=1,pady=3)
                name.grid(row=2,column=1,pady=10)

                ageLabel.grid(row=3,column=1)
                year.grid(row=5,column=1,pady=10,padx=4)

                emailLabel.grid(row=6,column=1)
                email.grid(row=7,column=1,pady=3)

                preferredLanguage.grid(row=8,column=1,pady=5)
                englishLanguage.grid(row=9,column=1,sticky="w")
                spanishLanguage.grid(row=9,column=1,sticky="e")

                subjectsLabel.grid(row=10,column=1)
                english.grid(row=11,column=0)
                math.grid(row=11,column=1)
                physics.grid(row=11,column=2)
                biology.grid(row=12,column=0)
                chemistry.grid(row=12,column=1)
                computerScience.grid(row=12,column=2)


                registerButton.grid(row=14,column=1)

                questionFrame2.grid_forget()
                questionFrame.grid(row=2,column=0)  
            elif value.get()==1: #If student selected
                print("STUDENT")
                questionFrame.grid_forget()
                registerLabel=Label(registerWindow,text="Register!",bg="papaya whip",fg="#72FF27",font=("constantia",30),width=100,height=1)
                registerLabel.grid(row=0, column=0)
                registerWindow.grid_columnconfigure(0, weight=1)
                
                option=IntVar()
                questionFrame2=Frame(registerWindow,bg="lemon chiffon")
                questionFrame2.grid(row=2,column=0)
                
                radioFrame=Frame(registerWindow,pady=10,bg="lemon chiffon")
                radioFrame.grid(row=1,column=0)

                nameLabel=Label(questionFrame2,text="Full name",bg="lemon chiffon",font=("Georgia",14))
                name=Entry(questionFrame2,width=23)
                
                ageLabel=Label(questionFrame2,text="Age",bg="lemon chiffon",font=("Georgia",14))
                year=Entry(questionFrame2)
                
                emailLabel=Label(questionFrame2,text="Email",bg="lemon chiffon",font=("Georgia",14))
                email=Entry(questionFrame2,width=23)

                preferredLanguage=Label(questionFrame2,text="Preferred language",bg="lemon chiffon",font=("Georgia",14))
                language=IntVar()
                englishLanguage=Radiobutton(questionFrame2,font=("Georgia",12),activebackground="lemon chiffon",text="English",bg="lemon chiffon",variable=language,value=0)
                spanishLanguage=Radiobutton(questionFrame2,font=("Georgia",12),activebackground="lemon chiffon",text="Spanish",bg="lemon chiffon",variable=language,value=1)

                subjectsLabel=Label(questionFrame2,text="Subjects",bg="lemon chiffon",font=("Georgia",14))
                englishSubject=IntVar()
                english=Checkbutton(questionFrame2, text="English", variable=englishSubject,bg="lemon chiffon",font=("Georgia",9))
                mathSubject=IntVar()
                math=Checkbutton(questionFrame2, text="Math", variable=mathSubject,bg="lemon chiffon",font=("Georgia",9))
                physicsSubject=IntVar()
                physics=Checkbutton(questionFrame2, text="Physics", variable=physicsSubject,bg="lemon chiffon",font=("Georgia",9))
                biologySubject=IntVar()
                biology=Checkbutton(questionFrame2, text="Biology", variable=biologySubject,bg="lemon chiffon",font=("Georgia",9))
                chemistrySubject=IntVar()
                chemistry=Checkbutton(questionFrame2, text="Chemistry", variable=chemistrySubject,bg="lemon chiffon",font=("Georgia",9))
                computerScienceSubject=IntVar()
                computerScience=Checkbutton(questionFrame2, text="Computer Science", variable=computerScienceSubject,bg="lemon chiffon",font=("Georgia",9))

                uploadCertificate=Button(questionFrame2,text="Select Certificate",font=("Georgia",11),width=15,height=1,command=lambda: UploadAction(questionFrame))
                #Register button
                registerButton=Button(questionFrame2,text="Login",font=("Georgia",11),width=15,height=1,command= RegisterButton)
                
                teacher=Radiobutton(radioFrame,font=("Georgia",20),activebackground="lemon chiffon",text="Teacher",bg="lemon chiffon",variable=option,value=0,command=lambda: teacherOrStudent(questionFrame2,option.get()))
                student=Radiobutton(radioFrame,font=("Georgia",20),activebackground="lemon chiffon",text="Student",bg="lemon chiffon",variable=option,value=1,command=lambda: teacherOrStudent(questionFrame2,option.get()))
                teacher.grid(row=1,column=0)
                spacer=Label(radioFrame,text=" ",bg="lemon chiffon").grid(row=1,column=1)
                student.grid(row=1,column=2,pady=10)

                nameLabel.grid(row=1,column=1,pady=3)
                name.grid(row=2,column=1,pady=10)

                ageLabel.grid(row=3,column=1)
                year.grid(row=5,column=1,pady=10,padx=4)

                emailLabel.grid(row=6,column=1)
                email.grid(row=7,column=1,pady=3)

                preferredLanguage.grid(row=8,column=1,pady=5)
                englishLanguage.grid(row=9,column=1,sticky="w")
                spanishLanguage.grid(row=9,column=1,sticky="e")

                subjectsLabel.grid(row=10,column=1)
                english.grid(row=11,column=0)
                math.grid(row=11,column=1)
                physics.grid(row=11,column=2)
                biology.grid(row=12,column=0)
                chemistry.grid(row=12,column=1)
                computerScience.grid(row=12,column=2)


                registerButton.grid(row=14,column=1)

                

        def UploadAction(window):
            global previousFilename
            filename = filedialog.askopenfilename()
            previousFilename=filename
            x=0
            for i in range(len(filename)):
                if x<len(filename):
                    if filename[x]=='/':
                        filename=filename[x+1:]
                        x=-1
                x+=1
            Label(window,text=('Selected:', filename),font=("Georgia",11)).grid(row=13,column=2,padx=3)

        def RegisterButton():#Funcion al darle a registrar
            try:
                pass 
            except:
                Label(window,text="something went wrong, try again",font=("Georgia",10)).grid(row=15,column=1)
                
            
        def Register():
            global registerWindow
            global previousFilename
            global questionFrame
            previousFilename=""
            #Create 'Reistration window' for registration and save values in a file 
            registerWindow=(b)
            registerWindow.minsize(1000,700)
            registerWindow.maxsize(1000,700)
            registerWindow.title("Register")
            registerWindow.configure(bg="lemon chiffon")
            photo = PhotoImage(file = "freeteacher.ico")
            registerWindow.iconbitmap("freeteacher.ico")
            
            registerLabel=Label(registerWindow,text="Register!",bg="papaya whip",fg="#72FF27",font=("constantia",30),width=100,height=1)
            registerLabel.grid(row=0, column=0)
            registerWindow.grid_columnconfigure(0, weight=1)
            
            option=IntVar()
            questionFrame=Frame(registerWindow,bg="lemon chiffon")
            questionFrame.grid(row=2,column=0)
            
            radioFrame=Frame(registerWindow,pady=10,bg="lemon chiffon")
            radioFrame.grid(row=1,column=0)

            nameLabel=Label(questionFrame,text="Full name",bg="lemon chiffon",font=("Georgia",14))
            name=Entry(questionFrame,width=23)
            
            ageLabel=Label(questionFrame,text="Age",bg="lemon chiffon",font=("Georgia",14))
            year=Entry(questionFrame)
            
            emailLabel=Label(questionFrame,text="Email",bg="lemon chiffon",font=("Georgia",14))
            email=Entry(questionFrame,width=23)

            preferredLanguage=Label(questionFrame,text="Preferred language",bg="lemon chiffon",font=("Georgia",14))
            language=IntVar()
            englishLanguage=Radiobutton(questionFrame,font=("Georgia",12),activebackground="lemon chiffon",text="English",bg="lemon chiffon",variable=language,value=0)
            spanishLanguage=Radiobutton(questionFrame,font=("Georgia",12),activebackground="lemon chiffon",text="Spanish",bg="lemon chiffon",variable=language,value=1)

            subjectsLabel=Label(questionFrame,text="Subjects",bg="lemon chiffon",font=("Georgia",14))
            englishSubject=IntVar()
            english=Checkbutton(questionFrame, text="English", variable=englishSubject,bg="lemon chiffon",font=("Georgia",9))
            mathSubject=IntVar()
            math=Checkbutton(questionFrame, text="Math", variable=mathSubject,bg="lemon chiffon",font=("Georgia",9))
            physicsSubject=IntVar()
            physics=Checkbutton(questionFrame, text="Physics", variable=physicsSubject,bg="lemon chiffon",font=("Georgia",9))
            biologySubject=IntVar()
            biology=Checkbutton(questionFrame, text="Biology", variable=biologySubject,bg="lemon chiffon",font=("Georgia",9))
            chemistrySubject=IntVar()
            chemistry=Checkbutton(questionFrame, text="Chemistry", variable=chemistrySubject,bg="lemon chiffon",font=("Georgia",9))
            computerScienceSubject=IntVar()
            computerScience=Checkbutton(questionFrame, text="Computer Science", variable=computerScienceSubject,bg="lemon chiffon",font=("Georgia",9))

            uploadCertificate=Button(questionFrame,text="Select Certificate",font=("Georgia",11),width=15,height=1,command=lambda: UploadAction(questionFrame))
            #Register button
            registerButton=Button(questionFrame,text="Register",font=("Georgia",11),width=15,height=1,command= RegisterButton)
            
            teacher=Radiobutton(radioFrame,font=("Georgia",20),activebackground="lemon chiffon",text="Teacher",bg="lemon chiffon",variable=option,value=0,command=lambda: teacherOrStudent(questionFrame,option))
            student=Radiobutton(radioFrame,font=("Georgia",20),activebackground="lemon chiffon",text="Student",bg="lemon chiffon",variable=option,value=1,command=lambda: teacherOrStudent(questionFrame,option))
            teacher.grid(row=1,column=0)
            spacer=Label(radioFrame,text=" ",bg="lemon chiffon").grid(row=1,column=1)
            student.grid(row=1,column=2,pady=10)

            nameLabel.grid(row=1,column=1,pady=3)
            name.grid(row=2,column=1,pady=10)

            ageLabel.grid(row=3,column=1)
            year.grid(row=5,column=1,pady=10,padx=4)

            emailLabel.grid(row=6,column=1)
            email.grid(row=7,column=1,pady=3)

            preferredLanguage.grid(row=8,column=1,pady=5)
            englishLanguage.grid(row=9,column=1,sticky="w")
            spanishLanguage.grid(row=9,column=1,sticky="e")

            subjectsLabel.grid(row=10,column=1)
            english.grid(row=11,column=0)
            math.grid(row=11,column=1)
            physics.grid(row=11,column=2)
            biology.grid(row=12,column=0)
            chemistry.grid(row=12,column=1)
            computerScience.grid(row=12,column=2)

            uploadCertificate.grid(row=13,column=1,pady=7)

            registerButton.grid(row=14,column=1)
        Register()
        
    def Login():
        def teacherOrStudent(window,value):
            global registerWindow
            if value.get()==0: #If teacher selected
                print("TEACHER")
                registerLabel=Label(registerWindow,text="Register!",bg="papaya whip",fg="#72FF27",font=("constantia",30),width=100,height=1)
                registerLabel.grid(row=0, column=0)
                registerWindow.grid_columnconfigure(0, weight=1)
                
                option=IntVar()
                questionFrame2=Frame(registerWindow,bg="lemon chiffon")
                questionFrame2.grid(row=2,column=0)
                
                radioFrame=Frame(registerWindow,pady=10,bg="lemon chiffon")
                radioFrame.grid(row=1,column=0)

                nameLabel=Label(questionFrame2,text="Full name",bg="lemon chiffon",font=("Georgia",14))
                name=Entry(questionFrame2,width=23)
                
                ageLabel=Label(questionFrame2,text="Age",bg="lemon chiffon",font=("Georgia",14))
                year=Entry(questionFrame2)
                
                emailLabel=Label(questionFrame2,text="Email",bg="lemon chiffon",font=("Georgia",14))
                email=Entry(questionFrame2,width=23)

                preferredLanguage=Label(questionFrame2,text="Preferred language",bg="lemon chiffon",font=("Georgia",14))
                language=IntVar()
                englishLanguage=Radiobutton(questionFrame2,font=("Georgia",12),activebackground="lemon chiffon",text="English",bg="lemon chiffon",variable=language,value=0)
                spanishLanguage=Radiobutton(questionFrame2,font=("Georgia",12),activebackground="lemon chiffon",text="Spanish",bg="lemon chiffon",variable=language,value=1)

                subjectsLabel=Label(questionFrame2,text="Subjects",bg="lemon chiffon",font=("Georgia",14))
                englishSubject=IntVar()
                english=Checkbutton(questionFrame2, text="English", variable=englishSubject,bg="lemon chiffon",font=("Georgia",9))
                mathSubject=IntVar()
                math=Checkbutton(questionFrame2, text="Math", variable=mathSubject,bg="lemon chiffon",font=("Georgia",9))
                physicsSubject=IntVar()
                physics=Checkbutton(questionFrame2, text="Physics", variable=physicsSubject,bg="lemon chiffon",font=("Georgia",9))
                biologySubject=IntVar()
                biology=Checkbutton(questionFrame2, text="Biology", variable=biologySubject,bg="lemon chiffon",font=("Georgia",9))
                chemistrySubject=IntVar()
                chemistry=Checkbutton(questionFrame2, text="Chemistry", variable=chemistrySubject,bg="lemon chiffon",font=("Georgia",9))
                computerScienceSubject=IntVar()
                computerScience=Checkbutton(questionFrame2, text="Computer Science", variable=computerScienceSubject,bg="lemon chiffon",font=("Georgia",9))

                uploadCertificate=Button(questionFrame2,text="Select Certificate",font=("Georgia",11),width=15,height=1,command=lambda: UploadAction(questionFrame))
                #Register button
                registerButton=Button(questionFrame2,text="Login",font=("Georgia",11),width=15,height=1,command= RegisterButton)
                
                teacher=Radiobutton(radioFrame,font=("Georgia",20),activebackground="lemon chiffon",text="Teacher",bg="lemon chiffon",variable=option,value=0,command=lambda: teacherOrStudent(questionFrame2,option.get()))
                student=Radiobutton(radioFrame,font=("Georgia",20),activebackground="lemon chiffon",text="Student",bg="lemon chiffon",variable=option,value=1,command=lambda: teacherOrStudent(questionFrame2,option.get()))
                teacher.grid(row=1,column=0)
                spacer=Label(radioFrame,text=" ",bg="lemon chiffon").grid(row=1,column=1)
                student.grid(row=1,column=2,pady=10)

                nameLabel.grid(row=1,column=1,pady=3)
                name.grid(row=2,column=1,pady=10)

                ageLabel.grid(row=3,column=1)
                year.grid(row=5,column=1,pady=10,padx=4)

                emailLabel.grid(row=6,column=1)
                email.grid(row=7,column=1,pady=3)

                preferredLanguage.grid(row=8,column=1,pady=5)
                englishLanguage.grid(row=9,column=1,sticky="w")
                spanishLanguage.grid(row=9,column=1,sticky="e")

                subjectsLabel.grid(row=10,column=1)
                english.grid(row=11,column=0)
                math.grid(row=11,column=1)
                physics.grid(row=11,column=2)
                biology.grid(row=12,column=0)
                chemistry.grid(row=12,column=1)
                computerScience.grid(row=12,column=2)


                registerButton.grid(row=14,column=1)

                questionFrame2.grid_forget()
                questionFrame.grid(row=2,column=0)  
            elif value.get()==1: #If student selected
                print("STUDENT")
                questionFrame.grid_forget()
                registerLabel=Label(registerWindow,text="Register!",bg="papaya whip",fg="#72FF27",font=("constantia",30),width=100,height=1)
                registerLabel.grid(row=0, column=0)
                registerWindow.grid_columnconfigure(0, weight=1)
                
                option=IntVar()
                questionFrame2=Frame(registerWindow,bg="lemon chiffon")
                questionFrame2.grid(row=2,column=0)
                
                radioFrame=Frame(registerWindow,pady=10,bg="lemon chiffon")
                radioFrame.grid(row=1,column=0)

                nameLabel=Label(questionFrame2,text="Full name",bg="lemon chiffon",font=("Georgia",14))
                name=Entry(questionFrame2,width=23)
                
                ageLabel=Label(questionFrame2,text="Age",bg="lemon chiffon",font=("Georgia",14))
                year=Entry(questionFrame2)
                
                emailLabel=Label(questionFrame2,text="Email",bg="lemon chiffon",font=("Georgia",14))
                email=Entry(questionFrame2,width=23)

                preferredLanguage=Label(questionFrame2,text="Preferred language",bg="lemon chiffon",font=("Georgia",14))
                language=IntVar()
                englishLanguage=Radiobutton(questionFrame2,font=("Georgia",12),activebackground="lemon chiffon",text="English",bg="lemon chiffon",variable=language,value=0)
                spanishLanguage=Radiobutton(questionFrame2,font=("Georgia",12),activebackground="lemon chiffon",text="Spanish",bg="lemon chiffon",variable=language,value=1)

                subjectsLabel=Label(questionFrame2,text="Subjects",bg="lemon chiffon",font=("Georgia",14))
                englishSubject=IntVar()
                english=Checkbutton(questionFrame2, text="English", variable=englishSubject,bg="lemon chiffon",font=("Georgia",9))
                mathSubject=IntVar()
                math=Checkbutton(questionFrame2, text="Math", variable=mathSubject,bg="lemon chiffon",font=("Georgia",9))
                physicsSubject=IntVar()
                physics=Checkbutton(questionFrame2, text="Physics", variable=physicsSubject,bg="lemon chiffon",font=("Georgia",9))
                biologySubject=IntVar()
                biology=Checkbutton(questionFrame2, text="Biology", variable=biologySubject,bg="lemon chiffon",font=("Georgia",9))
                chemistrySubject=IntVar()
                chemistry=Checkbutton(questionFrame2, text="Chemistry", variable=chemistrySubject,bg="lemon chiffon",font=("Georgia",9))
                computerScienceSubject=IntVar()
                computerScience=Checkbutton(questionFrame2, text="Computer Science", variable=computerScienceSubject,bg="lemon chiffon",font=("Georgia",9))

                uploadCertificate=Button(questionFrame2,text="Select Certificate",font=("Georgia",11),width=15,height=1,command=lambda: UploadAction(questionFrame))
                #Register button
                registerButton=Button(questionFrame2,text="Login",font=("Georgia",11),width=15,height=1,command= RegisterButton)
                
                teacher=Radiobutton(radioFrame,font=("Georgia",20),activebackground="lemon chiffon",text="Teacher",bg="lemon chiffon",variable=option,value=0,command=lambda: teacherOrStudent(questionFrame2,option.get()))
                student=Radiobutton(radioFrame,font=("Georgia",20),activebackground="lemon chiffon",text="Student",bg="lemon chiffon",variable=option,value=1,command=lambda: teacherOrStudent(questionFrame2,option.get()))
                teacher.grid(row=1,column=0)
                spacer=Label(radioFrame,text=" ",bg="lemon chiffon").grid(row=1,column=1)
                student.grid(row=1,column=2,pady=10)

                nameLabel.grid(row=1,column=1,pady=3)
                name.grid(row=2,column=1,pady=10)

                ageLabel.grid(row=3,column=1)
                year.grid(row=5,column=1,pady=10,padx=4)

                emailLabel.grid(row=6,column=1)
                email.grid(row=7,column=1,pady=3)

                preferredLanguage.grid(row=8,column=1,pady=5)
                englishLanguage.grid(row=9,column=1,sticky="w")
                spanishLanguage.grid(row=9,column=1,sticky="e")

                subjectsLabel.grid(row=10,column=1)
                english.grid(row=11,column=0)
                math.grid(row=11,column=1)
                physics.grid(row=11,column=2)
                biology.grid(row=12,column=0)
                chemistry.grid(row=12,column=1)
                computerScience.grid(row=12,column=2)


                registerButton.grid(row=14,column=1)

        def teacherOrStudent2(window,value):
            global loginButton
            if value==0:
                pass
                
            elif value==1:
                pass

        def UploadAction(window):
            global previousFilename
            filename = filedialog.askopenfilename()
            previousFilename=filename
            x=0
            for i in range(len(filename)):
                if x<len(filename):
                    if filename[x]=='/':
                        filename=filename[x+1:]
                        x=-1
                x+=1
            Label(window,text=('Selected:', filename),font=("Georgia",11)).grid(row=13,column=2,padx=3)

        def RegisterButton():#Funcion al darle a registrar
            try:
                pass 
            except:
                Label(window,text="something went wrong, try again",font=("Georgia",10)).grid(row=15,column=1)


        global loginButton
        global questionFrame2
        #Create login window and read csv file from registration to check maybe encrypt
        registerWindow=Tk()
        registerWindow.minsize(1000,700)
        registerWindow.maxsize(1000,700)
        registerWindow.title("Login")
        registerWindow.configure(bg="lemon chiffon")
        photo = PhotoImage(file = "freeteacher.png")
        registerWindow.iconbitmap("freeteacher.ico")
        
        registerLabel=Label(registerWindow,text="Login!",bg="papaya whip",fg="#72FF27",font=("constantia",30),width=100,height=1)
        registerLabel.grid(row=0, column=0)
        registerWindow.grid_columnconfigure(0, weight=1)
        
        option2=IntVar()
        questionFrame2=Frame(registerWindow,bg="lemon chiffon")
        questionFrame2.grid(row=2,column=0)
        
        radioFrame2=Frame(registerWindow,pady=10,bg="lemon chiffon")
        radioFrame2.grid(row=1,column=0)

        nameLabel=Label(questionFrame2,text="Enter your ID",bg="lemon chiffon",font=("Georgia",14))
        idEntry=Entry(questionFrame2,width=23)
        
        ageLabel=Label(questionFrame2,text="Age",bg="lemon chiffon",font=("Georgia",14))
        year=Entry(questionFrame2)
        
        emailLabel=Label(questionFrame2,text="Email",bg="lemon chiffon",font=("Georgia",14))
        email=Entry(questionFrame2,width=23)

        preferredLanguage=Label(questionFrame2,text="Preferred language",bg="lemon chiffon",font=("Georgia",14))
        language=IntVar()
        englishLanguage=Radiobutton(questionFrame2,font=("Georgia",12),activebackground="lemon chiffon",text="English",bg="lemon chiffon",variable=language,value=0)
        spanishLanguage=Radiobutton(questionFrame2,font=("Georgia",12),activebackground="lemon chiffon",text="Spanish",bg="lemon chiffon",variable=language,value=1)

        subjectsLabel=Label(questionFrame2,text="Subjects",bg="lemon chiffon",font=("Georgia",14))
        englishSubject=IntVar()
        english=Checkbutton(questionFrame2, text="English", variable=englishSubject,bg="lemon chiffon",font=("Georgia",9))
        mathSubject=IntVar()
        math=Checkbutton(questionFrame2, text="Math", variable=mathSubject,bg="lemon chiffon",font=("Georgia",9))
        physicsSubject=IntVar()
        physics=Checkbutton(questionFrame2, text="Physics", variable=physicsSubject,bg="lemon chiffon",font=("Georgia",9))
        biologySubject=IntVar()
        biology=Checkbutton(questionFrame2, text="Biology", variable=biologySubject,bg="lemon chiffon",font=("Georgia",9))
        chemistrySubject=IntVar()
        chemistry=Checkbutton(questionFrame2, text="Chemistry", variable=chemistrySubject,bg="lemon chiffon",font=("Georgia",9))
        computerScienceSubject=IntVar()
        computerScience=Checkbutton(questionFrame2, text="Computer Science", variable=computerScienceSubject,bg="lemon chiffon",font=("Georgia",9))

        uploadCertificate=Button(questionFrame2,text="Select Certificate",font=("Georgia",11),width=15,height=1,command=lambda: UploadAction(questionFrame))
        #Register button
            


        option1=BooleanVar()
        option2=BooleanVar()

        def LoginButton():
            students=option1.get()
            teachers=option2.get()
            studentMenu("Students","000001")
        loginButton=Button(questionFrame2,text="Login",font=("Georgia",11),width=15,height=1,command= LoginButton)

        teacher2=Radiobutton(radioFrame2,font=("Georgia",20),activebackground="lemon chiffon",text="Teacher",bg="lemon chiffon",variable=option1,value=0,command=lambda: teacherOrStudent2(questionFrame2,option2.get()))
        student2=Radiobutton(radioFrame2,font=("Georgia",20),activebackground="lemon chiffon",text="Student",bg="lemon chiffon",variable=option2,value=1,command=lambda: teacherOrStudent2(questionFrame2,option2.get()))
        teacher2.grid(row=1,column=0)
        spacer=Label(radioFrame2,text=" ",bg="lemon chiffon").grid(row=1,column=1)
        student2.grid(row=1,column=2,pady=10)

        nameLabel.grid(row=1,column=1,pady=3)
        idEntry.grid(row=2,column=1,pady=10)



        loginButton.grid(row=14,column=1)

    Chosen(data)



def studentMenu(acctype,idnumn):
    def getName(acc,idnumn):
        file=open(acc+".txt","r+")
        students=file.readlines()
        name=""
        for x in range(len(students)):
            students[x]=students[x][:len(students[x])-1]
            students[x]=students[x].split(",")
        for x in range(len(students)):
            for y in range(len(students[x])):
                if students[x][y]==idnumn:
                    name=students[x][0]
        file.close()
        return name

    def findTeacher(datar):
        file=open("Teachers.txt","r+")
        teachers=file.readlines()
        teacherspos=[]
        names=[]
        global idnums
        idnums=[]
        for x in range(len(teachers)):
            teachers[x]=teachers[x].strip("\n")
            teachers[x]=teachers[x].split(",")
        for x in range(6):
            num=random.randint(0,len(teachers)-1)
            while num in teacherspos:
                num=random.randint(0,len(teachers)-1)
            teacherspos.append(num)
            names.append(teachers[num][0])
            idnums.append(teachers[num][3])
        file.close()
        if datar=="names":
            return names
        
    def findTeacherS(varArr):
        subjectSSS=["Maths","Science","English","Geography","History","Spanish"]
        subjectL=[]
        for x in range(len(varArr)):
            if varArr[x]==True:
                subjectL.append(subjectSSS[x])
        file=open("Teachers.txt","r+")
        teachers=file.readlines()
        teacherspos=[]
        names=[]
        global idnums
        global subjects
        idnums=[]
        subjects=[]
        for x in range(len(teachers)):
            teachers[x]=teachers[x].strip("\n")
            teachers[x]=teachers[x].split(",")
        for x in range(6):
            num=random.randint(0,len(teachers)-1)
            while (num in teacherspos) or (teachers[num][2] not in subjectL):
                print()
                print(idnums,subjects,names)
                num=random.randint(0,len(teachers)-1)
            teacherspos.append(num)
            names.append(teachers[num][0])
            idnums.append(teachers[num][3])
            subjects.append(teachers[num][2])
        print(idnums,subjects,names)
        file.close()
        return names

    def decbutArr(teacherBs):
        
        def OnHoverT1(event):
            teacherBs[0].config(bg="#a6e09d", fg="white")
        def OnLeaveT1(event):
            teacherBs[0].config(bg="white", fg='#333333')
        teacherBs[0].bind('<Enter>', OnHoverT1)
        teacherBs[0].bind('<Leave>', OnLeaveT1)
            
        def OnHoverT2(event):
            teacherBs[1].config(bg="#a6e09d", fg="white")
        def OnLeaveT2(event):
            teacherBs[1].config(bg="white", fg='#333333')
        teacherBs[1].bind('<Enter>', OnHoverT2)
        teacherBs[1].bind('<Leave>', OnLeaveT2)
            
        def OnHoverT3(event):
            teacherBs[2].config(bg="#a6e09d", fg="white")
        def OnLeaveT3(event):
            teacherBs[2].config(bg="white", fg='#333333')
        teacherBs[2].bind('<Enter>', OnHoverT3)
        teacherBs[2].bind('<Leave>', OnLeaveT3)
            
        def OnHoverT4(event):
            teacherBs[3].config(bg="#a6e09d", fg="white")
        def OnLeaveT4(event):
            teacherBs[3].config(bg="white", fg='#333333')
        teacherBs[3].bind('<Enter>', OnHoverT4)
        teacherBs[3].bind('<Leave>', OnLeaveT4)
                
        def OnHoverT5(event):
            teacherBs[4].config(bg="#a6e09d", fg="white")
        def OnLeaveT5(event):
            teacherBs[4].config(bg="white", fg='#333333')
        teacherBs[4].bind('<Enter>', OnHoverT5)
        teacherBs[4].bind('<Leave>', OnLeaveT5)
            
        def OnHoverT6(event):
            teacherBs[5].config(bg="#a6e09d", fg="white")
        def OnLeaveT6(event):
            teacherBs[5].config(bg="white", fg='#333333')
        teacherBs[5].bind('<Enter>', OnHoverT6)
        teacherBs[5].bind('<Leave>', OnLeaveT6)
        

    def teacher1():
        idnum=idnums[0]
        print(idnum)
    def teacher2():
        idnum=idnums[1]
        print(idnum)
    def teacher3():
        idnum=idnums[2]
        print(idnum)
    def teacher4():
        idnum=idnums[3]
        print(idnum)
    def teacher5():
        idnum=idnums[4]
        print(idnum)
    def teacher6():
        idnum=idnums[5]
        print(idnum)
    
    name=getName(acctype,idnumn)
    root=Tk()
    root.geometry("1000x600")
    root.resizable(0, 0)
    root.title("FreeTeacher.org")
    root.iconbitmap("freeteacher.ico")
    logo=ImageTk.PhotoImage(Image.open("freeteacher.png"))

    bgcolour="navajo white"
    fgcolour="yellow green"
    
    menu=Canvas(root,width=1000, height=600,bg=bgcolour)
    menu.create_rectangle(0, 0, 1000, 105,outline="#fff4e0", fill="#fff4e0")
    menu.create_rectangle(720, 580, 980, 280,outline=fgcolour, fill="#ccd8a5")
    menu.pack()

    mathV=BooleanVar()
    scienceV=BooleanVar()
    englishV=BooleanVar()
    geographyV=BooleanVar()
    historyV=BooleanVar()
    spanishV=BooleanVar()
    
    mathC=Checkbutton(root, text="",bg=bgcolour,bd=0, variable=mathV)
    scienceC=Checkbutton(root, text="",bg=bgcolour,bd=0, variable=scienceV)
    englishC=Checkbutton(root, text="",bg=bgcolour,bd=0, variable=englishV)
    geographyC=Checkbutton(root, text="",bg=bgcolour,bd=0, variable=geographyV)
    historyC=Checkbutton(root, text="",bg=bgcolour,bd=0, variable=historyV)
    spanishC=Checkbutton(root, text="",bg=bgcolour,bd=0, variable=spanishV)

    mathL=Label(root, text="Maths",bg=bgcolour,fg=fgcolour,font=("",12))
    scienceL=Label(root, text="Science",bg=bgcolour,fg=fgcolour,font=("",12))
    englishL=Label(root, text="English",bg=bgcolour,fg=fgcolour,font=("",12))
    geographyL=Label(root, text="Geography",bg=bgcolour,fg=fgcolour,font=("",12))
    historyL=Label(root, text="History",bg=bgcolour,fg=fgcolour,font=("",12))
    spanishL=Label(root, text="Spanish",bg=bgcolour,fg=fgcolour,font=("",12))

    varL=[mathL,scienceL,englishL,geographyL,historyL,spanishL]

    varA=[mathC,scienceC,englishC,geographyC,historyC,spanishC]
    for x in range(3):
        menu.create_window(830,135+(40*x),window=varA[x])
        menu.create_window(770,135+(40*x),window=varL[x])
    for x in range(3):
        menu.create_window(960,135+(40*x),window=varA[x+3])
        menu.create_window(900,135+(40*x),window=varL[x+3])

    def refreshT():
        varA=[mathV,scienceV,englishV,geographyV,historyV,spanishV]
        varB=[False,False,False,False,False,False]

        for x in range(len(varA)):
            varB[x]=varA[x].get()

        if True not in varB:
            teachers=findTeacher("names")
            teachr1=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher1)
            teachr2=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher2)
            teachr3=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher3)
            teachr4=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher4)
            teachr5=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher5)
            teachr6=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher6)
            teacherBs=[teachr1,teachr2,teachr3,teachr4,teachr5,teachr6]
            for t in range(6):
                teachn=Label(root,text=teachers[t],bg="#ccd8a5",font=("",13,"bold"),width=10)
                menu.create_window(785,315+(45*t),window=teachn)
                menu.create_window(915,315+(45*t),window=teacherBs[t])
        else:
            teachers=findTeacherS(varB)
            teachr1=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher1)
            teachr2=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher2)
            teachr3=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher3)
            teachr4=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher4)
            teachr5=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher5)
            teachr6=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher6)
            teacherBs=[teachr1,teachr2,teachr3,teachr4,teachr5,teachr6]
            for t in range(6):
                teachn=Label(root,text=teachers[t],bg="#ccd8a5",font=("",13,"bold"),width=10)
                menu.create_window(785,315+(45*t),window=teachn)
                menu.create_window(915,315+(45*t),window=teacherBs[t])
                
    teachers=findTeacher("names")
    teachr1=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher1)
    teachr2=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher2)
    teachr3=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher3)
    teachr4=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher4)
    teachr5=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher5)
    teachr6=Button(root,text="Request Lesson",bd=0,width=14,font=("",10),bg="white", fg='#333333',command=teacher6)
    teacherBs=[teachr1,teachr2,teachr3,teachr4,teachr5,teachr6]
    
    for t in range(6):
        teachn=Label(root,text=teachers[t],bg="#ccd8a5",font=("",13,"bold"))
        menu.create_window(785,315+(45*t),window=teachn)
        menu.create_window(915,315+(45*t),window=teacherBs[t])
                
    def OnHoverR(event):
        refreshB.config(bg=fgcolour, fg="#dddddd")
    def OnLeaveR(event):
        refreshB.config(bg="white", fg='#333333')

        decbutArr(teacherBs)
            

    refreshB=Button(root,text="Refresh List",bd=0,width=27,font=("",12),bg="white", fg='#333333',command=refreshT)
    refreshB.bind('<Enter>', OnHoverR)
    refreshB.bind('<Leave>', OnLeaveR)

    menu.create_window(850,260,window=refreshB)
    
    menu.create_image(60,55,image=logo)

    title=Label(root,text="Welcome {0}!".format(name),font=("",40,"bold"),bg="#fff4e0",fg=fgcolour)

    menu.create_window(500,50,window=title)

    def logout():
        root.destroy()
        main()

    def OnHoverL(event):
        logoutB.config(bg=fgcolour, fg="#dddddd")
    def OnLeaveL(event):
        logoutB.config(bg="white", fg='#333333')

    logoutB=Button(root,text="Log Out",bd=0,width=20,font=("",12),bg="white", fg='#333333',command=logout)
    logoutB.bind('<Enter>', OnHoverL)
    logoutB.bind('<Leave>', OnLeaveL)
    menu.create_window(115,573,window=logoutB)

    decbutArr(teacherBs)
    
    root.mainloop()

def teacherMenu():
    def TeachersMenu(screen):
        if screen==1:
            timetableTeacher.destroy()
        if screen==2:
            searchScreen.destroy()
        if screen==3:
            attendance.destroy()
        if screen==4:
            grads.destroy()
        if screen==5:
            notScreen.destroy()
        global menuTeacher 
        menuTeacher=Tk()
        menuTeacher.resizable(0, 0)
        menuTeacher.title("MENU")
        menuTeacher.geometry("1000x600")
        field=Canvas(menuTeacher,width=1000,height=600,bg="yellow green")
        field.create_rectangle(0, 0, 1000, 105,outline="#fff4e0", fill="#fff4e0")
        field.pack()
        titleLable=Label(menuTeacher, text="TEACHER-MENU",bg="#fff4e0",fg="yellow green", font=("Bold",22),width=25, height=2)
        field.create_window(500,50,window=titleLable)

        TimetableButtonT=Button(menuTeacher,text="TIMETABLE",command=lambda: Timetable(0),width=30,height=2,fg="orange")
        field.create_window(838,180,window=TimetableButtonT)
        TimetableButtonS=Button(menuTeacher,text="SEARCH FOR STUDENT",width=30,height=2,fg="orange",command=lambda: searchStudents(0,0))
        field.create_window(233,180,window=TimetableButtonS)
        TimetableButtonN=Button(menuTeacher,text="NOTIFICATIONS",command=lambda: notifications(0),width=30,height=2,fg="orange")
        field.create_window(536,180,window=TimetableButtonN)
        field.pack()


    def searchStudents(screen,displayScreen):
        if screen==0:
            menuTeacher.destroy()
        if displayScreen==0: 
            global searchScreen
            searchScreen=Tk()
            searchScreen.title("SEARCH SCREEN")
            searchScreen.resizable(0, 0)
            searchScreen.geometry("1000x600")
            displayScreen=searchScreen
        field=Canvas(displayScreen,width=1000,height=600,bg="yellow green")
        field.create_rectangle(0, 0, 1000, 105,outline="#fff4e0", fill="#fff4e0")
        field.pack()
        titleLabel=Label(displayScreen,text="SEARCH FOR STUDENT",bg="yellow green",fg="snow",font=("Arial",15),width=20,height=2)
        field.create_window(500,50,window=titleLabel)
        back=Button(displayScreen,text="MENU",font=20,fg="dark blue",width=20,command=lambda:(TeachersMenu(2)))
        field.create_window(250,180,window=back)
        global searchLabel
        searchLabel=Label(displayScreen,text="Select the student: ",bg="navajo white")
        field.create_window(500,180,window=searchLabel)
        students=[]
        names=[]
        file=open("Students.txt","r")
        for item in file.readlines():
            students.append(item.strip())
        student=StringVar(searchScreen)
        for i in range(len(students)):
            if "Name: " in students[i]:
                names.append(students[i])
        OPTION_TUPPLE=names
        student.set("Possible names")
        global entryStudent
        entryStudent=OptionMenu(displayScreen,student,OPTION_TUPPLE)
        field.create_window(500,220,window=entryStudent)
        global search
        search=Button(displayScreen,text="SEARCH",command=lambda:(printStudentInfo(0,student.get(),searchScreen)))
        field.create_window(700,220,window=search)
        

    def printStudentInfo(screen,name2,displayScreen):
        students=[]
        info=[]
        if screen==0: 
            searchLabel.grid_forget()
            entryStudent.grid_forget()
            search.grid_forget()
        file=open("Students.txt","r")
        for item in file.readlines():
            students.append(item.strip())
        file.close()
        for i in range(len(students)):
            if name2 in students[i]:
                info.append(students[i-1:i+3])
        for p in info[0]:
            info.append(p)
        info.pop(0)
        name=name2[6:len(name2)]
        file2=open(name+".txt","r")
        for item2 in (file2.readlines()):
            info.append(item2.strip())

        info.pop(4)
        
        space=Label(displayScreen,text=("   ")).grid()
        for item3 in info:
            label=Label(displayScreen,text=item3,bg="navajo white",width=20).grid(column=0)
        
        space=Label(displayScreen,text=("   ")).grid()
        global changeAttend
        changeAttend=Button(displayScreen,text="CHANGE ATTENDANCE",command=lambda: changeAttd(name,displayScreen) ,width=20,height=2)
        changeAttend.grid()
        space=Label(displayScreen,text=("   ")).grid()
        global changeGrad
        changeGrad=Button(displayScreen,text="CHANGE GRADES",command=lambda:changeGrads(name,displayScreen) ,width=20,height=2)
        changeGrad.grid()
        space=Label(displayScreen,text=("   ")).grid()
      

    def changeAttd(name,displayScreen):
        global attendance
        name2="Name: "+name
        displayScreen.destroy()
        attendance=Tk()
        attendance.title("LOOK AT ATTENDANCE")
        root.resizable(0, 0)
        attendance.geometry("1000x600")
        titleLabel=Label(attendance,text="SEARCH FOR STUDENT",bg="yellow green",fg="snow",font=("Arial",15),width=20,height=2).grid()
        back=Button(attendance,text="MENU",font=20,fg="dark blue",width=20,command=lambda:(TeachersMenu(3))).grid(column=0)
        printStudentInfo(20,name2,attendance)
        
        file=open(name+" Attendance.txt","r")
        attend1=[]
        attend=[]
        fileRead=file.readlines()
        for item in (fileRead):
            attend1.append(item.strip())
        for x in attend1:
            date=x[:len(x)-2]
            if x[len(x)-1]=="1":
                attend.append(date)
                attend.append(" Present")
            elif x[len(x)-1]=="0":
                attend.append(date)
                attend.append(" Absent ")


       
        space=Label(attendance,text=" "*30).grid(column=5)
        header=["DATE" , "ATTENDANCE"] 
        i=6
        for x in header:
            headerLabel=Label(attendance,text=(x),fg="snow", bg="LightBlue2",font=("Helvetica",15),width=12 , height =1).grid(row=3,column=i,sticky="nsew")
            i=i+1
        i=6
        c=4
        a=0
        for l in attend:
            if a==2:
                c=c+1
                i=6
                a=0
           
            textLabel1=Label(attendance,text=(l),bg="navajo white",font=("Helvetica",12), height =1).grid(row=c,column=i,sticky="nsew")
            i=i+1
            a=a+1
        Label(attendance,text="",height=2).grid()
        textLabel2=Label(attendance,text="Today: ",bg="LightBlue2").grid(column=9,row=3)
        att=StringVar()
        att.set("Choose attendance")
        OPTION_TUPPLE=("Present","Absent")
        textLabel3=OptionMenu(attendance,att,*OPTION_TUPPLE).grid(column=9,row=4)
        textLabel4=Button(attendance, text="SAVE",command=lambda:changeAttdData(name,att.get())).grid(column=9,row=5)
        
    def changeAttdData(name,att):
        print(att)
        file=open(name+" Attendance.txt","r")
        attend1=[]
        attend=[]
        fileRead=file.readlines()
        for item in (fileRead):
            attend1.append(item.strip())
        attend1.pop(len(attend1)-1)

        for item2 in attend1:
            attend.append(item2[len(item2)-1])
        print(attend)

        today=str(date.today())+" "
        if att =="Present":
            att1="1"
        elif att=="Absent":
            att1="0"
        file1=open(name+" Attendance.txt","a")
        file1.write("\n")
        file1.write(today)
        file1.write(att1)
        file1.close()

        
        summ=int(att1)
        for k in attend:
            summ=summ+int(k)
        perc=round(((summ/(len(attend)+1))*100),1)
        file3=open(name+".txt","r")
        info=[]
        newAttend="Attendance: "+str(perc)+"%"

        for item3 in file3.readlines():
            info.append(item3.strip())
        for b in range(len(info)):
            if "Attendance:" in info[b]:
                info[b]=(newAttend)

        file4=open(name+".txt","a")
        file4.truncate(0)
        for item4 in info:
            file4.write(item4)
            file4.write("\n")
        file.close()
        file4.close()
        label=Label(searchScreen,text="SAVED!").grid(column=9,row=6)

    def changeGrads(name,displayScreen):
        global grads
        name2="Name: "+name
        displayScreen.destroy()
        grads=Tk()
        grads.title("LOOK AT GRADES")
        grads.resizable(0, 0)
        grads.geometry("1000x600")
        titleLabel=Label(grads,text="SEARCH FOR STUDENT",bg="yellow green",fg="snow",font=("Arial",15),width=20,height=2).grid()
        back=Button(grads,text="MENU",font=20,fg="dark blue",width=20,command=lambda:(TeachersMenu(4))).grid(column=0)
        printStudentInfo(20,name2,grads)

        
        file=open(name+" Grades.txt","r")
        grades1=[]
        grades=[]
        fileRead=file.readlines()
        for item in (fileRead):
            grades1.append(item.strip())
       
        space=Label(grads,text=" "*30).grid(column=5)
        header=["UNIT" , "GRADE"] 
        i=6
        for x in header:
            Label(grads,text=(x),fg="snow", bg="LightBlue2",font=("Helvetica",15),width=12 , height =1).grid(row=3,column=i,sticky="nsew")
            i=i+1

        c=4
        a=0
        for l in grades1:
            unit=l[:len(l)-4]
            grade=l[len(l)-3::]
            if a ==2:
                c=c+1
                a=0 
            Label(grads,text=(unit),bg="navajo white",font=("Helvetica",12), height =1).grid(row=c,column=6,sticky="nsew")
            Label(grads,text=(grade),bg="navajo white",font=("Helvetica",12),height=1).grid(row=c,column=7,sticky="nswe")
            a=a+2

        Label(grads,text="",height=2).grid()
        Label(grads,text="Add grade: ",bg="LightBlue2").grid(column=9,row=3)
        unit=StringVar()
        unitEntry=Entry(grads,textvariable=unit).grid(column=9,row=4)
        grad=DoubleVar()
        gradEntry=Entry(grads,textvariable=grad).grid(column=9,row=5)
        Button(grads, text="SAVE",command=lambda:changeGradsData(name,unit.get(),grad.get())).grid(column=9,row=6)
        
    def changeGradsData(name,unit1,grade): 
        file2=open(name+" Grades.txt","r")
        grades1=[]
        grades=[]
        for item2 in file2.readlines():
            grades1.append(item2.strip())
        
        for item3 in grades1:
            grades.append(item3[len(item3)-3::])
        print(grades)
        file2.close()
        unit=unit1+": "
        file1=open(name+" Grades.txt","a")
        file1.write("\n")
        file1.write(unit)
        file1.write(str(grade))
        file1.close()
        summ2=grade
        for a in grades:
            summ2=summ2+float(a)
        perc2=round((((summ2/10)/(len(grades)+1))*100),1)
        file2.close()
        print(perc2)
        file3=open(name+".txt","r")
        info=[]
        newGrades="Grades (average):"+str(perc2)+"%"
        for item3 in file3.readlines():
            info.append(item3.strip())
        for b in range(len(info)):
           
            if "Grades (average):" in info[b]:
                info[b]=(newGrades)
        file3.close()

        file4=open(name+".txt","a")
        file4.truncate(0)
        for item4 in info:
            file4.write(item4)
            file4.write("\n")
        
        file4.close()


        
    def Timetable(screen):
        global timetableTeacher
        if screen==0:
            menuTeacher.destroy()
        timetableTeacher=Tk()
        timetableTeacher.resizable(0, 0)
        timetableTeacher.geometry("1000x600")
        timetableTeacher.title("TIMETABLE")
        main_frame=Frame(timetableTeacher)
        main_frame.pack(fill=BOTH,expand=1)

        canvas=Canvas(main_frame)
        canvas.pack(fill=BOTH,expand=1)
        
        scrollbar=Scrollbar(main_frame,orient=VERTICAL,command=canvas.yview)
        scrollbar.pack(side=RIGHT,fill=Y)

        
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        global second_frame
        second_frame=Frame(canvas,bg="navajo white")
        canvas.create_window((0,0),window=second_frame,anchor="nw")


        TimetableInfo()
        
    def TimetableInfo(): 
        columns=[]
        rows=[]
        num=0
        titleLabel=Label(second_frame, text=("MY STUDENTS: "),font=40,bg="yellow green",fg="snow",width=20,height=2).grid(column=0)
        back=Button(second_frame,text="MENU",font=20,fg="dark blue",width=20,command=lambda:(TeachersMenu(1))).grid(column=0)

        space=Label(second_frame,text=("   "),fg="navajo white",bg="navajo white").grid()
        file=open("Students.txt","r")
        students=[]
        
        for item in file.readlines():
            students.append(item.strip())
        students.append(" ")
        
        for p in range(len(students)) :
            if "STUDENT" in students[p]:
                num=num+1
        for b in range(3): 
            for x in range((int(num/3)+1)*5):
                rows.append(x+2)

        for t in range(0,4):
            for f in range((int(num/3)+1)*5):
                columns.append(t)

        name=[i for i in range(len(students))]
        for l in range(len(students)) :
            if "STUDENT" in students[l]:
                new=Label(second_frame, text=students[l], width=30,height=2,bg="LightBlue2").grid(column=columns[l],row=rows[l])
            else:   
                Label(second_frame,text=students[l],bg="navajo white",font=(90),widt=30,height=1).grid(column=columns[l],row=rows[l])
        file.close()
        
    def notifications(screen):
        if screen==0 :    
            menuTeacher.destroy()
        
        global notScreen
        notScreen=Tk()
        notScreen.title("NOTIFICATIONS")
        notScreen.resizable(0, 0)
        notScreen.geometry("1000x600")
        title=Label(notScreen,text="NOTIFICATIONS",bg="yellow green",fg="snow",width=20,height=2).grid(column=0)
        back=Button(notScreen,text="MENU",font=20,fg="dark blue",width=20,command=lambda:(TeachersMenu(5))).grid(column=0)
        notifications1()
        
    def notifications1():
        
        notif=[]
        students=[]
        edit=[]

        file=open("Notifications.txt","r")
        for item in file.readlines():
            if item.strip() != ' ':
                if item.strip() != '': 
                    notif.append(item.strip())
        if notif==[]:
            Label(notScreen,text="No new notfications",bg="LightBlue2",font=("Helvetica",30)).grid(column=10,row=50, pady=200, padx=150, sticky="wens")
        else:
            file.close()
            file2=open("Students.txt","r")
            for item2 in file2.readlines():
                students.append(item2.strip())

            for y in notif:
                if "STUDENT" in y:
                    edit.append(y)
            num2=1 
            for i in range(len(edit)):
                edit[i]="STUDENT "+str(num2)+":"
                num2=num2+1
            for item3 in range(len(notif)):
                if "STUDENT" in notif[item3]:
                    notif[item3]=edit[int(item3/5)]


            acceptL=Label(notScreen,text="Accept student: ",bg="LightBlue2").grid(column=0,row=3)
            OPTION_TUPPLE1=edit
            accept=StringVar()
            accept.set("Search for student")
            acceptM=OptionMenu(notScreen,accept,*OPTION_TUPPLE1).grid(column=0,row=4)
            acceptB=Button(notScreen,text="SAVE ",command=lambda:(AcceptData(accept.get(),notif))).grid(column=0,row=5)
            declineL=Label(notScreen,text="Decline student: ",bg="LightBlue2").grid(column=0,row=6)
            decline=StringVar()
            decline.set("Search for student")
            declineM=OptionMenu(notScreen,decline,*OPTION_TUPPLE1).grid(column=0,row=7)
            decelineB=Button(notScreen,text="SAVE ",command=lambda:(declineData(decline.get(),notif))).grid(column=0,row=8)
            
            notif.append(" ")
            notif.append(" ")
            row=5
            column=5
            a=0
            b=0
            for l in range(len(notif)):
                
                if "STUDENT" in notif[l]:
                    b=b+1
                    if b==4:
                        space=Label(notScreen,text=" ").grid(column=column+1,row=5)
                        column=column+3
                        b=0
                        row=5
                    space=Label(notScreen,text=" ").grid(column=column,row=row)
                    row=row+1
                    label1=Label(notScreen,text=notif[l],bg="LightBlue2").grid(column=column,row=row,sticky="nsew")
                    row=row+1
                    a=0
                elif "STUDENT" not in notif[l]:
                    if l != (len(notif)-1):
                        label=Label(notScreen,text=notif[l],bg="navajo white").grid(column=column,row=row,sticky="nsew")
                        row=row+1
                        a=a+1
                
           
    #def AcceptData(accept,notif):
        #save=[]
        #for items in range(len(notif)):
           # if notif[items]==accept:
               # save=(notif[items:items+4])
               # del notif[items:items+4]
               # break
            
       # file=open("Students.txt","a")
       # file.write("\n")
        #file.write("\n")
        #for item in save: 
            #file.write(item)
            #file.write("\n")
        #file.close()
        
        #file2=open("Notifications.txt","w")
        #file2.truncate(0)
        #for p in notif: 
           # file2.write(p)
            #file2.write("\n")
       # file2.close()
        
        
    #def declineData(decline,notif):
       # for items in range(len(notif)):
           # if notif[items]==decline:
               # del notif[items:items+4]
               # break
        #for item in notif:
           # if "STUDENT" in item:
               # item="STUDENT: "
        #print(notif)
       # file2=open("Notifications.txt","w")
        #file2.truncate(0)
        #for p in notif: 
        #    file2.write(p)
       #     file2.write("\n")
      #  file2.close()

    TeachersMenu(0)
main()
