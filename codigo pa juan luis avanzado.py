import tkinter
from tkinter import *
from tkinter import filedialog
#Register:
#Teacher-Certificate, Full name, date of birth,Preferred Language(Radio button), Subject(check boxes), gmail. Submit button
#Student-Date of birth,Full name, gmail,Preferred language(Radio button), Subject(Check boxes). Submit button
def Chosen(chosenOption):
    if chosenOption=="Register":
        Register()
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
        photo = PhotoImage(file = "freeteacher.png")
        registerWindow.iconphoto(False, photo)
        
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
    registerWindow.iconphoto(False, photo)
    
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
        studentsMenu("Students","000001")
    loginButton=Button(questionFrame2,text="Login",font=("Georgia",11),width=15,height=1,command= LoginButton)

    teacher2=Radiobutton(radioFrame2,font=("Georgia",20),activebackground="lemon chiffon",text="Teacher",bg="lemon chiffon",variable=option1,value=0,command=lambda: teacherOrStudent2(questionFrame2,option2.get()))
    student2=Radiobutton(radioFrame2,font=("Georgia",20),activebackground="lemon chiffon",text="Student",bg="lemon chiffon",variable=option2,value=1,command=lambda: teacherOrStudent2(questionFrame2,option2.get()))
    teacher2.grid(row=1,column=0)
    spacer=Label(radioFrame2,text=" ",bg="lemon chiffon").grid(row=1,column=1)
    student2.grid(row=1,column=2,pady=10)

    nameLabel.grid(row=1,column=1,pady=3)
    idEntry.grid(row=2,column=1,pady=10)



    loginButton.grid(row=14,column=1)

Chosen("Register")
