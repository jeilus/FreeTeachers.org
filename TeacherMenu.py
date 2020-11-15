import tkinter as tk 
from tkinter import * 
from datetime import date

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
       #     file2.write("\n")o
       
      #  file2.close()

    TeachersMenu(0)
teacherMenu()
