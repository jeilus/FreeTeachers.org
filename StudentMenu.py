import tkinter
import random
from tkinter import *
from PIL import Image,ImageTk

profile=["Students","000001"]

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

    def OnHoverR(event):
        refreshB.config(bg=fgcolour, fg="#dddddd")
    def OnLeaveR(event):
        refreshB.config(bg="white", fg='#333333')

        decbutArr(teacherBs)

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
            

    refreshB=Button(root,text="Refresh List",bd=0,width=27,font=("",12),bg="white", fg='#333333',command=refreshT)
    refreshB.bind('<Enter>', OnHoverR)
    refreshB.bind('<Leave>', OnLeaveR)

    menu.create_window(850,260,window=refreshB)
    
    menu.create_image(60,55,image=logo)

    title=Label(root,text="Welcome {0}!".format(name),font=("",40,"bold"),bg="#fff4e0",fg=fgcolour)

    menu.create_window(500,50,window=title)

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

    def logout():
        pass

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

studentMenu(profile[0],profile[1])
    
