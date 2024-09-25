from tkinter import *
import mysql.connector
import sqlite3
import traceback
from tkinter import messagebox
from PIL import ImageTk,Image
from tkcalendar import Calendar, DateEntry
from tkinter import ttk #treeview 
import traceback #les erreurs de la base de données 
import datetime 
from tkinter import filedialog

class maingui:
    def __init__(self, root):

        self.root = root
        self.root.title("B.F.Z SARL")
        self.root.geometry('1200x800+200+10')
        self.root.resizable(0,0)


        self.img=ImageTk.PhotoImage(file="C:\\Users\\ORIGINAL SHOP\\Desktop\\RichesseMS\\RichesseMS\\a2.jpg")
        self.imgICON=ImageTk.PhotoImage(file="C:\\Users\\ORIGINAL SHOP\\Desktop\\RichesseMS\\RichesseMS\\d2.png")
        self.root.iconphoto(False,self.imgICON)
        self.bg_img=Label(self.root,image=self.img).place(x=0,y=0,relwidth=1,relheight=1)
        self.pageshow = Login_Page(self, self.root)
        self.pageshow = Login_Page(self, self.root)
    def changepage(self, page):
        self.page = page
        
        if self.page == 0:
            #del self.pageshow
            self.pageshow = Login_Page(self, self.root)

        if self.page == 1:
            #del self.pageshow
            self.pageshow = Sign_Page(self, self.root)
        if self.page == 2:
            #del self.pageshow
            self.pageshow = Home_Page(self, self.root)
        if self.page == 3:
            #del self.pageshow
            self.pageshow = Add_Page(self, self.root)
        if self.page == 4:
            #del self.pageshow
            self.pageshow = DU_Page(self, self.root)
        if self.page == 5:
            #del self.pageshow
            self.pageshow = SEARCH_Page(self, self.root)
        if self.page == 6:
            #del self.pageshow
            self.pageshow = VIEW_Page(self, self.root)
class Login_Page:
    def __init__(self, parent, window):
        
        self.parent = parent
        
        self.frame = Frame(window,width=580,height=800,bg='#9f9f9f')
        self.frame.place(x=0,y=0)
        
        self.username=Label(self.frame,text='اسم المستخدم',bg='#9f9f9f',fg='black',font=('Times New Roman',25))
        self.username.place(x=210,y=250)
        self.username_entry=Entry(self.frame,highlightthickness=0,relief=FLAT,bg='#9f9f9f',fg='black',font=('Times New Roman',20))
        self.username_entry.place(x=100,y=300)
        self.username_line=Canvas(self.frame,width=400,height=2.0,bg='black',highlightthickness=0)
        self.username_line.place(x=80,y=335)

        self.password = Label(self.frame, text='كلمة المرور', bg='#9f9f9f', fg='black', font=('Times New Roman', 25))
        self.password.place(x=210,y=375)
        self.password_entry=Entry(self.frame,highlightthickness=0,relief=FLAT,bg='#9f9f9f',fg='black',font=('Times New Roman',20))
        self.password_entry.place(x=100,y=415)
        self.password_line=Canvas(self.frame,width=400,height=2.0,bg='black',highlightthickness=0)
        self.password_line.place(x=80,y=450)

        self.loginbutton=Button(self.frame,bg="black",width=10,text='تسجيل الدخول',fg="white",command=self.sign_in)
        self.loginbutton.place(x=240,y=500)
        self.signUp=Label(self.frame,text="ليس لديك حساب :)",font=('Open Sans',9,'bold'),bg='#9f9f9f',fg="black")
        self.signUp.place(x=20,y=600)
        self.signUpButton=Button(self.frame,text="أنشئ واحدًا",font=('Open Sans',9,'bold underline'),bd=0,bg='#9f9f9f',fg='blue',cursor='hand2',activebackground='white',activeforeground='blue',command=self.clicked)
        self.signUpButton.place(x=170,y=600)
        self.jewlery=PhotoImage(file="C:\\Users\\ORIGINAL SHOP\\Desktop\\RichesseMS\\RichesseMS\\fingerprint-scan.png")
        self.jew=Label(self.frame,image=self.jewlery,bg="#9f9f9f")
        self.jew.place(x=240,y=120)    

       
       

    def clicked(self):
        self.frame.destroy()
        self.parent.changepage(1)
    def clickedHome(self):
        self.frame.destroy()
        self.parent.changepage(2)
    def clear(self):
       self.username_entry.delete(0,END)
       self.password_entry.delete(0,END)
    def sign_in(self):
    
         if self.username_entry.get()=='' or self.password_entry.get=='':
          messagebox.showerror('خطأ', 'يرجى ملء جميع الحقول')
      
         
         else :
           if (len(self.username_entry.get())<=2 or len(self.password_entry.get())<=2):
             messagebox.showerror('خطأ', 'يجب أن يحتوي اسم المستخدم أو كلمة المرور على 3 أحرف على الأقل')
           else:
              try:
                   database=mysql.connector.connect(
                   host="127.0.0.1",
                   database="richessedb",
                   user="root",
                   password="1234567890"
                    )
                  
                   cursor=database.cursor()
                   sql_research="SELECT * from users where nomUser=%s and passUser=%s"
                   val=(self.username_entry.get(),self.password_entry.get())
                   cursor.execute(sql_research,val)
                   resultat=cursor.fetchall()
                   if(len(resultat)>0):
                       self.parent.changepage(2)
                   else:
                     
                     
                      
                       messagebox.showerror('خطأ', 'لم يتم العثور على الحساب')
                       self.clear()
                       
              except:
                  messagebox.showerror('خطأ', 'فشل الاتصال بقاعدة البيانات')
                  traceback.print_exc()
    

class Sign_Page():
    def __init__(self, parent, window):

        self.parent = parent
        self.frame= Frame(window,width=580,height=800,bg='#9f9f9f')
        self.frame.place(x=0,y=0)
        
        self.username=Label(self.frame,text='اسم المستخدم',bg='#9f9f9f',fg='black',font=('Times New Roman',25))
        self.username.place(x=210,y=220)
        self.username_entry=Entry(self.frame,highlightthickness=0,relief=FLAT,bg='#9f9f9f',fg='black',font=('Times New Roman',20))
        self.username_entry.place(x=100,y=260)
        self.username_line=Canvas(self.frame,width=400,height=2.0,bg='black',highlightthickness=0)
        self.username_line.place(x=80,y=290)

        self.password=Label(self.frame,text='كلمة المرور',bg='#9f9f9f',fg='black',font=('Times New Roman',25))
        self.password.place(x=210,y=320)
        self.password_entry=Entry(self.frame,highlightthickness=0,relief=FLAT,bg='#9f9f9f',fg='black',font=('Times New Roman',20))
        self.password_entry.place(x=100,y=360)
        self.password_line=Canvas(self.frame,width=400,height=2.0,bg='black',highlightthickness=0)
        self.password_line.place(x=80,y=390)

        self.passwordConfirm=Label(self.frame,text='تأكيد كلمة المرور',bg='#9f9f9f',fg='black',font=('Times New Roman',25))
        self.passwordConfirm.place(x=150,y=430)
        self.passwordConfirm_entry=Entry(self.frame,highlightthickness=0,relief=FLAT,bg='#9f9f9f',fg='black',font=('Times New Roman',20))
        self.passwordConfirm_entry.place(x=100,y=470)
        self.passwordConfirm_line=Canvas(self.frame,width=400,height=2.0,bg='black',highlightthickness=0)
        self.passwordConfirm_line.place(x=80,y=500)

        self.SignUPButton=Button(self.frame,bg="black",width=10,text='تسجيل',fg="white",command=self.sign_up)
        self.SignUPButton.place(x=240,y=550)


        self.lock=PhotoImage(file="add-user2.png")
        self.lockpic=Label(self.frame,image=self.lock,bg="#9f9f9f")
        self.lockpic.place(x=240,y=125)

        self.signIN=Label(self.frame,text="لديك حساب بالفعل :)؟",font=('Open Sans',9,'bold'),bg='#9f9f9f',fg="black")
        self.signIN.place(x=20,y=600)
        self.signINButton=Button(self.frame,text="تسجيل الدخول",font=('Open Sans',9,'bold underline'),bd=0,bg='#9f9f9f',fg='blue',cursor='hand2',activebackground='white',activeforeground='blue',command=self.clickedLogin)
        self.signINButton.place(x=190,y=600)
    def clickedLogin(self):
        self.frame.destroy()
        self.parent.changepage(0)
  
    def sign_up(self):   
         self.tries=0
         if(self.username_entry.get()=='' or self.password_entry.get()=='' or self.passwordConfirm_entry==''):
             messagebox.showerror('خطأ', "يرجى ملء جميع الحقول")
         else:
           self.tries+=1
         if(self.password_entry.get()!= self.passwordConfirm_entry.get()):
            messagebox.showerror('خطأ', "كلمات المرور غير متطابقة")
         else:  
             self.tries+=1
         if (len(self.username_entry.get())<=2 or len(self.password_entry.get())<=2):
            messagebox.showerror('خطأ', 'يجب أن يحتوي اسم المستخدم أو كلمة المرور على 3 أحرف على الأقل')
         else:
             self.tries+=1

         if(self.tries==3):
            try:
                database=mysql.connector.connect(
                host="127.0.0.1",
                database="richessedb",
                user="root",
                password="1234567890"
                 )
               
                cursor=database.cursor()
                sql_research="SELECT * from users where nomUser=%s and passUser=%s"
                val=(self.username_entry.get(),self.password_entry.get())
                cursor.execute(sql_research,val)
                resultat=cursor.fetchall()
                if(len(resultat)>0):
                     messagebox.showerror('خطأ', 'الحساب موجود بالفعل')
                else: 
                 sql="Insert into users(nomUser,passUser) values (%s,%s)"
                 values=(self.username_entry.get(),self.password_entry.get())
                 cursor.execute(sql,values)
                 messagebox.showinfo('نجاح', "تم التسجيل بنجاح، يرجى تسجيل الدخول :)")
                 database.commit()
                 database.close()
                 self.clickedLogin()

            except: 
                messagebox.showerror('خطأ', 'فشل الاتصال بقاعدة البيانات')


class Home_Page():
    def __init__(self, parent,window):
        self.window=window
        self.parent = parent
        self.frame=Frame(self.window,width=1200,height=800)
        self.info_frame=Frame(self.window,width=1200,height=100,bg='#9f9f9f')
        self.info_frame.place(x=0,y=0)
        self.backg_image=ImageTk.PhotoImage(Image.open('C:\\Users\\ORIGINAL SHOP\\Desktop\\RichesseMS\\RichesseMS\\bg2.jpg'))
      
        self.buttons_frame=Label(self.window,width=1200,height=800,image=self.backg_image)
        self.buttons_frame.place(x=0,y=100)
        self.title=Label(self.info_frame,text="B.F.Z SARL ",bg='#9f9f9f',fg='black',font=('Times New Roman',25))
        self.title.place(x=590,y=30)

        self.add_button=Button(self.buttons_frame,text=" إضافة العجلات",fg='white',width=20,height=3,bg='black',command=self.clickedADD,font="Times 12 bold",borderwidth=8)
        self.add_button.place(x=370,y=90)
        self.delete_button=Button(self.buttons_frame,text=" حذف & تحديث",fg='white',width=20,height=3,bg='black',command=self.clickedDU,font="Times 12 bold",borderwidth=8)
        self.delete_button.place(x=670,y=90)
        update_button=Button(self.buttons_frame,text="فاتورة",fg='white',width=20,height=3,bg='black',command=self.clickedDU,font="Times 12 bold",borderwidth=8)
        update_button.place(x=370,y=240)
        self.view_button=Button(self.buttons_frame,text=" إضافة المزود",fg='white',width=20,height=3,bg='black',command=self.clickedVIEW,font="Times 12 bold",borderwidth=8)
        self.view_button.place(x=670,y=390)
        self.search_button=Button(self.buttons_frame,text="خروج",fg='white',width=20,height=3,bg='black',command=self.exit,font="Times 12 bold",borderwidth=8)
        self.search_button.place(x=670,y=240)
    
    def clickedADD(self):
        self.frame.destroy()
        self.parent.changepage(3)
    def clickedDU(self):
        self.frame.destroy()
        self.parent.changepage(4)
    def clickedSEARCH(self):
        self.frame.destroy()
        self.parent.changepage(5)
    def clickedVIEW(self):
        self.frame.destroy()
        self.parent.changepage(6)
    def exit(self):
       exit= messagebox.askyesno("معلومات","هل أنت متأكد أنك تريد الخروج؟")
       if exit>0:
          self.parent.root.destroy()
          return
       

class Add_Page():       
 def __init__(self, parent, window):
      self.parent = parent
      self.window=window
      self.frame=Frame(self.window,width=1200,height=800)
      self.info_frame=Frame(self.window,width=1200,height=100,bg='#9f9f9f')
      self.info_frame.place(x=0,y=0)
      self.add_image=ImageTk.PhotoImage(Image.open('C:\\Users\\ORIGINAL SHOP\\Desktop\\RichesseMS\\RichesseMS\\ADDIM.png'))
      self.im_label=Label(self.info_frame,image=self.add_image,bg='#9f9f9f')
      self.im_label.place(x=980,y=15)
      self.buttons_frame=Label(self.window,width=1200,height=800)
      self.buttons_frame.place(x=0,y=100)
      self.title=Label(self.info_frame,text="B.F.Z SARL",bg='#9f9f9f',fg='black',font=('Times New Roman',25))
      self.title.place(x=390,y=30)
      self.products_frame=Frame(window,width=1200,height=800)
      self.products_frame.place(x=0,y=100)
           #products frame 
#name
      self.product_name=Label(self.products_frame,text="رقم  : ")
      self.product_name.place(x=10,y=40)
      self.product_name_entry=Entry(self.products_frame)
      self.product_name_entry.place(x=150,y=40)

#desc
      self.product_desc=Label(self.products_frame,text="نوع  : ")
      self.product_desc.place(x=10,y=80)
      self.product_desc_entry=Entry(self.products_frame)
      self.product_desc_entry.place(x=150,y=80)
#price
      self.product_price=Label(self.products_frame,text="السعر  : ")
      self.product_price.place(x=10,y=120)
      self.product_price_entry=Entry(self.products_frame)
      self.product_price_entry.place(x=150,y=120)
#quantity
      self.product_qty=Label(self.products_frame,text="الكمية  : ")
      self.product_qty.place(x=10,y=160)
      self.product_qty_entry=Entry(self.products_frame)
      self.product_qty_entry.place(x=150,y=160)
#Seuil alerte idk
      self.product_alertThreshold=Label(self.products_frame,text="حد التنبيه : ")
      self.product_alertThreshold.place(x=10,y=200)
      self.product_alertThreshold_entry=Entry(self.products_frame)
      self.product_alertThreshold_entry.place(x=150,y=200)

#dates 

#Entree
      self.product_lastEntryDate=Label(self.products_frame,text="تاريخ آخر إدخال : ")
      self.product_lastEntryDate.place(x=440,y=40)
      self.product_lastEntryDate_DP=DateEntry(self.products_frame, width= 16, background= "brown", foreground= "white",bd=2)
      self.product_lastEntryDate_DP.place(x=580,y=40)

#Sortie
      self.product_lastRemovalDate=Label(self.products_frame,text="تاريخ آخر إخراج : ")
      self.product_lastRemovalDate.place(x=440,y=80)
      self.product_lastRemovalDate_DP=DateEntry(self.products_frame, width= 16, background= "brown", foreground= "white",bd=2)
      self.product_lastRemovalDate_DP.place(x=580,y=80)
      
      fournisseurs = self.get_fournisseurs()
      self.fournisseurs_dict = fournisseurs  # Store the dictionary

      self.buyer_name = Label(self.products_frame, text="اسم مزود : ")
      self.buyer_name.place(x=440, y=120)
      self.buyer_name_var = StringVar()
      self.buyer_name_entry = ttk.Combobox(self.products_frame, textvariable=self.buyer_name_var, values=list(fournisseurs.keys()))
      self.buyer_name_entry.place(x=580, y=120)
      self.product_qty_added = Label(self.products_frame, text="الكمية المضافة : ")
      self.product_qty_added.place(x=440, y=160)
      self.product_qty_added_entry = Entry(self.products_frame)
      self.product_qty_added_entry.place(x=580, y=160)


#Image :) 

     


#Listview 
      self.cols=('المرجع','رقم','الوصف','السعر','الكمية','حد التنبيه','تاريخ الإدخال','تاريخ الإخراج','اسم مزود')
      self.listview=ttk.Treeview(self.products_frame,columns=self.cols,show='headings')


      for col in self.cols:
          self.listview.heading(col,text=col)
          self.listview.column(col,width=140,stretch=False)
          self.listview.place(x=60,y=230)
          self.listview.column("الوصف",width=200)
          self.listview.column('السعر',width=70)
          self.listview.column('الكمية',width=70)
        
          self.listview.column('المرجع',width=50)
      self.listview.bind("<ButtonRelease-1>",self.getPic)
#buttons
      self.add_button = Button(self.products_frame, text="إضافة", bg='white', width=12, fg='black', height=2, command=self.addData, font="Times 10 bold", borderwidth=8)
      self.add_button.place(x=120, y=610)
      self.view_button = Button(self.products_frame, text="عرض المنتجات", bg='white', width=12, height=2, fg='black', command=self.displayData, font="Times 10 bold", borderwidth=8)
      self.view_button.place(x=280, y=610)
      self.reset_button = Button(self.products_frame, text="إعادة تعيين", bg='white', width=12, height=2, fg='black', command=self.reset, font="Times 10 bold", borderwidth=8)
      self.reset_button.place(x=430, y=610)
      self.update_button = Button(self.products_frame, text="تحديث", bg='white', width=12, height=2, fg='black', command=self.updateData, font="Times 10 bold", borderwidth=8)
      self.update_button.place(x=580, y=610)
      self.delete_button = Button(self.products_frame, text="حذف", bg='white', width=15, height=2, fg='black', command=self.deleteData, font="Times 10 bold", borderwidth=8)
      self.delete_button.place(x=730, y=610)
      self.search_button=Button(self.products_frame,text="بحث",bg='white',width=15,height=2,fg='black',command= self.searchData,font="Times 10 bold",borderwidth=8)
      self.search_button.place(x=880,y=610)
      self.back_button = Button(self.products_frame, text="عودة", bg='white', width=12, height=2, fg='black', command=self.clickedHOME, font="Times 10 bold", borderwidth=8)
      self.back_button.place(x=1030, y=610)
      
 def get_fournisseurs(self):
    """Fetch fournisseur names and IDs from the database and return them as a dictionary."""
    fournisseurs = {}
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host="127.0.0.1",
            database="richessedb",
            user="root",
            password="1234567890"
        )
        cursor = conn.cursor()

        # Fetch fournisseur IDs and names
        cursor.execute("SELECT idFournisseur, nomFournisseur FROM fournisseur")
        rows = cursor.fetchall()
        fournisseurs = {row[1]: row[0] for row in rows}  # Map name to ID
        
    except Exception as e:
        messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
        print(f"Error: {e}")
        traceback.print_exc()

    finally:
        # Ensure database connection is closed
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return fournisseurs

 
 def clickedHOME(self):
        self.frame.destroy()
        self.parent.changepage(2)
 def addData(self):
    # Vérifiez les valeurs des widgets Entry
    if (self.product_name_entry.get() == "" or 
        self.product_desc_entry.get() == "" or 
        self.product_price_entry.get() == "" or 
        self.product_qty_entry.get() == "" or 
        self.product_alertThreshold_entry.get() == "" or
        self.buyer_name_var.get() == ""):  # Add check for fournisseur
        messagebox.showerror("خطأ", "يجب ملء جميع الحقول")
    else:
        # Vérifiez la longueur des champs de texte
        if len(self.product_name_entry.get()) < 3 or len(self.product_desc_entry.get()) < 3:
            messagebox.showerror("خطأ", "يجب أن يكون اسم المنتج أو الوصف على الأقل 3 أحرف")
        else:
            # Vérifiez les dates
            if (self.product_lastEntryDate_DP.get_date() > datetime.datetime.now().date() or
                self.product_lastRemovalDate_DP.get_date() >= datetime.datetime.now().date()):
                messagebox.showerror("خطأ", "تاريخ غير صحيح")
            else:
                try:
                    # Connexion à la base de données
                    database = mysql.connector.connect(
                        host="127.0.0.1",
                        database="richessedb",
                        user="root",
                        password="1234567890"
                    )
                    cursor = database.cursor()

                    # Vérification si le produit existe déjà
                    sql_research = "SELECT * FROM produits WHERE UPPER(nomProduit) = UPPER(%s)"
                    val = self.product_name_entry.get()
                    cursor.execute(sql_research, (val,))
                    res = cursor.fetchall()

                    if len(res) > 0:
                        messagebox.showerror("خطأ", "المنتج موجود بالفعل")
                    else:

                        # Obtenir l'ID du fournisseur
                        fournisseur_name = self.buyer_name_var.get()
                        fournisseur_id = self.fournisseurs_dict.get(fournisseur_name, None)

                        if fournisseur_id is None:
                            messagebox.showerror("خطأ", "فورنيشور غير موجود")
                            return

                        # Insertion des données dans la base de données
                        sql = """INSERT INTO produits (nomProduit, descProduit, prixUnitaire, quantiteProduit, seuilAlerteProduit, date_entree, date_sortie,  idFournisseur) 
                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                        values = (
                            self.product_name_entry.get(),
                            self.product_desc_entry.get(),
                            self.product_price_entry.get(),
                            self.product_qty_entry.get(),
                            self.product_alertThreshold_entry.get(),
                            self.product_lastEntryDate_DP.get_date(),
                            self.product_lastRemovalDate_DP.get_date(),
                        
                            fournisseur_id  # Ajouter l'ID du fournisseur
                        )
                        cursor.execute(sql, values)
                        database.commit()
                        database.close()
                        messagebox.showinfo("نجاح", "تم إضافة المنتج بنجاح")
                        self.listview.delete(*self.listview.get_children())
                        self.displayData()
                except:
                    messagebox.showerror("خطأ", "الاتصال بقاعدة البيانات لم يكن ناجحاً")
                    traceback.print_exc()

 def updateData(self):
    # Vérification des champs vides
    if (self.product_name_entry.get() == "" or 
        self.product_desc_entry.get() == "" or 
        self.product_price_entry.get() == "" or 
        self.product_qty_entry.get() == "" or 
        self.product_alertThreshold_entry.get() == "" or 
        self.buyer_name_var.get() == ""):
        messagebox.showerror("خطأ", "يجب إدخال جميع الحقول")
        return

    if len(self.product_name_entry.get()) < 3 or len(self.product_desc_entry.get()) < 3:
        messagebox.showerror("خطأ", "يجب أن يكون اسم المنتج أو الوصف على الأقل 3 أحرف")
        return

    today = datetime.datetime.now().date()
    if (self.product_lastEntryDate_DP.get_date() > today or 
        self.product_lastRemovalDate_DP.get_date() >= today):
        messagebox.showerror("خطأ", "التاريخ غير صحيح")
        return

    try:
        # Connexion à la base de données
        database = mysql.connector.connect(
            host="127.0.0.1",
            database="richessedb",
            user="root",
            password="1234567890"
        )
        cursor = database.cursor()

        # Sélectionner la ligne à mettre à jour
        selected = self.listview.selection()
        if not selected:
            raise ValueError("الرجاء تحديد صف للتحديث.")

        item = self.listview.item(selected)
        row_id = item['values'][0]
        

        # Récupérer la quantité actuelle depuis la base de données
        cursor.execute("SELECT quantiteProduit FROM produits WHERE numSerie = %s", (row_id,))
        result = cursor.fetchone()
        if result:
            current_qty = result[0]
        else:
            raise ValueError("Produit non trouvé dans la base de données.")

        # Vérifier la quantité ajoutée
        added_qty = int(self.product_qty_added_entry.get()) if self.product_qty_added_entry.get() else 0

        # Calculer la nouvelle quantité
        if added_qty > 0:
            new_qty = current_qty + added_qty
        else:
            new_qty = current_qty  # Pas de changement si aucune quantité n'est ajoutée

        # Mettre à jour les données dans la base de données
        sql = """UPDATE produits SET nomProduit=%s, descProduit=%s, prixUnitaire=%s, quantiteProduit=%s, 
                 seuilAlerteProduit=%s, date_entree=%s, date_sortie=%s, idFournisseur=%s 
                 WHERE numSerie=%s"""
        cursor.execute(sql, (
            self.product_name_entry.get(),
            self.product_desc_entry.get(),
            self.product_price_entry.get(),
            new_qty,
            self.product_alertThreshold_entry.get(),
            self.product_lastEntryDate_DP.get_date(),
            self.product_lastRemovalDate_DP.get_date(),
      
            self.fournisseurs_dict.get(self.buyer_name_var.get(), None),
            row_id
        ))
        database.commit()

        # Mettre à jour la vue
        self.listview.item(selected, values=(
            row_id,
            self.product_name_entry.get(),
            self.product_desc_entry.get(),
            self.product_price_entry.get(),
            new_qty,
            self.product_alertThreshold_entry.get(),
            self.product_lastEntryDate_DP.get_date().strftime('%Y-%m-%d'),
            self.product_lastRemovalDate_DP.get_date().strftime('%Y-%m-%d'),
         
            self.buyer_name_var.get()
        ))

        messagebox.showinfo("معلومات", "تم تحديث البيانات")

    except Exception as e:
        messagebox.showerror("خطأ", f"فشل في تحديث البيانات: {e}")
        traceback.print_exc()

    finally:
        # Assurez-vous que la connexion est toujours fermée
        if 'database' in locals() and database.is_connected():
            cursor.close()
            database.close()


 def deleteData(self):
    try:
        # Connect to the database using a context manager for automatic resource management
        with mysql.connector.connect(
            host="127.0.0.1",
            database="richessedb",
            user="root",
            password="1234567890"
        ) as database:
            with database.cursor() as cursor:
                
                # Get the selected item from the listview
                selected_item = self.listview.selection()
                if not selected_item:
                    raise ValueError("الرجاء تحديد صف للحذف.")
                
                # Iterate over the selected items
                for item in selected_item:
                    item_values = self.listview.item(item, 'values')
                    product_name = item_values[1]  # Adjust the index based on your column order

                    # SQL query to delete the selected item from the database
                    sql = "DELETE FROM produits WHERE nomProduit = %s"
                    cursor.execute(sql, (product_name,))
                    database.commit()  # Commit the transaction

                    # Remove the item from the listview
                    self.listview.delete(item)
        
        # Notify the user of success
        messagebox.showinfo("نجاح", "تم حذف البيانات بنجاح")
        
        # Refresh the listview to reflect changes
        self.displayData()

    except mysql.connector.Error as err:
        # Handle specific MySQL errors
        messagebox.showerror("خطأ", f"فشل في حذف البيانات: {err}")
        traceback.print_exc()
    except Exception as e:
        # Handle other exceptions
        messagebox.showerror("خطأ", f"فشل في حذف البيانات: {e}")
        traceback.print_exc()
 def searchData(self):
    self.listview.delete(*self.listview.get_children())
    
    # Vérifier si au moins un champ de recherche est rempli
    if not any([
        self.product_name_entry.get(),
        self.product_desc_entry.get(),
        self.product_price_entry.get(),
        self.product_qty_entry.get(),
        self.product_alertThreshold_entry.get(),
        self.product_lastEntryDate_DP.get_date() != datetime.datetime.now().date(),
        self.product_lastRemovalDate_DP.get_date() != datetime.datetime.now().date(),
        self.buyer_name_entry.get()
    ]):
        messagebox.showerror('خطأ', 'يرجى إدخال قيمة واحدة على الأقل للبحث عنها')
        return
    
    try:
        database = mysql.connector.connect(
            host="127.0.0.1",
            database="richessedb",
            user="root",
            password="1234567890"
        )
        cursor = database.cursor()

        sql = "SELECT * FROM produits WHERE 1=1"
        params = []

        if self.product_name_entry.get():
            sql += " AND UPPER(nomProduit) LIKE UPPER(%s)"
            params.append('%' + self.product_name_entry.get() + '%')

        if self.product_desc_entry.get():
            sql += " AND UPPER(descProduit) LIKE UPPER(%s)"
            params.append('%' + self.product_desc_entry.get() + '%')

        if self.product_price_entry.get():
            sql += " AND prixUnitaire = %s"
            params.append(self.product_price_entry.get())

        if self.product_qty_entry.get():
            sql += " AND quantiteProduit = %s"
            params.append(self.product_qty_entry.get())

        if self.product_alertThreshold_entry.get():
            sql += " AND seuilAlerteProduit = %s"
            params.append(self.product_alertThreshold_entry.get())

        if self.product_lastEntryDate_DP.get_date() != datetime.datetime.now().date():
            sql += " AND date_entree = %s"
            params.append(self.product_lastEntryDate_DP.get_date().strftime('%Y-%m-%d'))

        if self.product_lastRemovalDate_DP.get_date() != datetime.datetime.now().date():
            sql += " AND date_sortie = %s"
            params.append(self.product_lastRemovalDate_DP.get_date().strftime('%Y-%m-%d'))
        
        if self.buyer_name_entry.get():
            sql += " AND nomAcheteur = %s"
            params.append(self.buyer_name_entry.get())

        cursor.execute(sql, params)
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                self.listview.insert('', END, values=row)
        else:
            messagebox.showinfo('معلومات', 'لا توجد نتائج مطابقة.')

        cursor.close()
        database.close()

    except mysql.connector.Error as e:
        messagebox.showerror('خطأ في الاتصال', str(e))
        traceback.print_exc()
 

 def reset(self):
    self.product_name_entry.delete(0,END)
    self.product_desc_entry.delete(0,END)
    self.product_price_entry.delete(0,END)
    self.product_qty_entry.delete(0,END)
    self.product_alertThreshold_entry.delete(0,END)
    self.product_lastEntryDate_DP.set_date(datetime.datetime.now().date())
    self.product_lastRemovalDate_DP.set_date(datetime.datetime.now().date())
    self.buyer_name_entry.delete(0,END)

 def displayData(self):
     try:

        database=mysql.connector.connect(
                host="127.0.0.1",
                database="richessedb",
                user="root",
                password="1234567890"
                 )
               
        cursor=database.cursor()
        sql = """
        SELECT
            p.numSerie,
            p.nomProduit,
            p.descProduit,
            p.prixUnitaire,
            p.quantiteProduit,
            p.seuilAlerteProduit,
            p.date_entree,
            p.date_sortie,
           
            f.nomFournisseur
        FROM produits p

        JOIN fournisseur f ON p.idFournisseur = f.idFournisseur
        """
        cursor.execute(sql)
        result=cursor.fetchall()
        #clear existing items of tree view
        for i in self.listview.get_children():
            self.listview.delete(i)
        if len(result)>0:
           for row in result:
              
              self.listview.insert('', END, values=row)
              self.listview.yview_moveto(0)
              database.commit()
        database.close()
     except:
        messagebox.showerror("خطأ", "لم يكن الاتصال بقاعدة البيانات ناجحاً")
        traceback.print_exc() 


 def getPic(self, event):
    try:
        # Réinitialiser le formulaire
        self.reset()
        
        # Obtenir l'ID de la ligne sélectionnée
        item_id = self.listview.selection()[0]
        
        # Récupérer les valeurs de la ligne sélectionnée
        values = self.listview.item(item_id)['values']
        
        # Remplir les champs du formulaire avec les valeurs
        self.product_name_entry.delete(0, END)
        self.product_name_entry.insert(0, values[1])
        
        self.product_desc_entry.delete(0, END)
        self.product_desc_entry.insert(0, values[2])
        
        self.product_price_entry.delete(0, END)
        self.product_price_entry.insert(0, values[3])
        
        self.product_qty_entry.delete(0, END)
        self.product_qty_entry.insert(0, values[4])
        
        self.product_alertThreshold_entry.delete(0, END)
        self.product_alertThreshold_entry.insert(0, values[5])
        
        # Convertir les dates en objets datetime.date
        last_entry_date = values[6]
        last_removal_date = values[7]
        
        if isinstance(last_entry_date, str):
            last_entry_date = datetime.datetime.strptime(last_entry_date, '%Y-%m-%d').date()
        if isinstance(last_removal_date, str):
            last_removal_date = datetime.datetime.strptime(last_removal_date, '%Y-%m-%d').date()
        
        # Afficher les dates dans les champs DateEntry
        self.product_lastEntryDate_DP.set_date(last_entry_date)
        self.product_lastRemovalDate_DP.set_date(last_removal_date)
        
        # Afficher l'image
       
        
        # Afficher le nom du fournisseur dans le champ approprié
        supplier_name = values[8]  # Assurez-vous que l'index 9 est correct pour le nom du fournisseur
        self.buyer_name_entry.delete(0, END)
        self.buyer_name_entry.insert(0, supplier_name)
    
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la récupération des informations : {e}")
        traceback.print_exc()


class DU_Page():
   def __init__(self, parent, window):
        self.parent = parent
        self.window = window
        self.frame = Frame(self.window, width=1200, height=800)
        self.info_frame = Frame(self.window, width=1200, height=100, bg='#9f9f9f')
        self.info_frame.place(x=0, y=0)
        self.buttons_frame = Label(self.window, width=1200, height=800)
        self.buttons_frame.place(x=0, y=100)

      # Images
      
      # Title
        self.title = Label(self.info_frame, text="B.F.Z SARL", bg='#9f9f9f', fg='black', font=('Times New Roman', 25))
        self.title.place(x=390, y=30)

      # Product details
        self.products_frame = Frame(window, width=1200, height=800)
        self.products_frame.place(x=0, y=100)
      
        self.field_frame = Frame(self.products_frame, width=650, height=200,  relief="ridge")
        self.field_frame.place(x=10, y=10)
        

        self.product_name = Label(self.products_frame, text="رقم : ")
        self.product_name.place(x=10, y=40)
        self.product_name_entry = Entry(self.products_frame)
        self.product_name_entry.place(x=50, y=40)

        self.product_desc = Label(self.products_frame, text="نوع  : ")
        self.product_desc.place(x=180, y=40)
        self.product_desc_entry = Entry(self.products_frame)
        self.product_desc_entry.place(x=220, y=40)

        self.product_qty_sold = Label(self.products_frame, text="الكمية المباعة : ")
        self.product_qty_sold.place(x=480, y=40)
        self.product_qty_sold_entry = Entry(self.products_frame)
        self.product_qty_sold_entry.place(x=570, y=40)
        self.buyer_name = Label(self.products_frame, text="اسم المشتري : ")
        self.buyer_name.place(x=700, y=40)
        self.buyer_name_entry = Entry(self.products_frame)
        self.buyer_name_entry.place(x=790, y=40)
        # Ajout d'une entrée pour le mode de paiement
        self.payment_mode_var = StringVar()
        self.payment_mode_var.set("Oui")  # Option par défaut
        self.payment_mode_label = Label(self.products_frame, text="طريقة الدفع : ")
        self.payment_mode_label.place(x=920, y=40)

# Combobox pour sélectionner "Oui" ou "Non"
        self.payment_mode_menu = OptionMenu(self.products_frame, self.payment_mode_var, "Oui", "Non")
        self.payment_mode_menu.place(x=1000, y=30)

      
      
      # ListView initialization
        self.listview = ttk.Treeview(self.products_frame, columns=('المرجع', 'الاسم', 'النوع', 'السعر', 'الكمية', 'عتبة التنبيه', 'تاريخ الدخول', 'تاريخ الإزالة'), show='headings')
        self.listview.place(x=60, y=80)
        for col in self.listview['columns']:
         self.listview.heading(col, text=col)
         self.listview.column(col, width=180, stretch=False)
         self.listview.column("النوع", width=200)
         self.listview.column('السعر', width=70)
         self.listview.column('الكمية', width=70)
         self.listview.column('المرجع', width=50)
         self.listview.bind("<ButtonRelease-1>", self.getInfo)

      # Buttons
         self.delete_button = Button(self.products_frame, text="بحث", bg='white', width=15, height=2, fg='black',command=self.search_client,  font="Times 10 bold", borderwidth=8)
         self.delete_button.place(x=250, y=600)
         self.delete_button = Button(self.products_frame, text="مسح", bg='white', width=15, height=2, fg='black',command=self.delete_order,font="Times 10 bold", borderwidth=8)
         self.delete_button.place(x=80, y=600)
# Bouton pour mettre à jour la commande
         self.update_button = Button(self.products_frame, text="تحديث", bg='white', width=15, height=2, fg='black', command=self.update_order, font="Times 10 bold", borderwidth=8)
         self.update_button.place(x=400, y=600)
         self.update_button['state'] = 'disabled'  # Désactiver le bouton jusqu'à ce qu'une commande soit sélectionnée

         self.reset_button = Button(self.products_frame, text="إعادة تعيين", bg='white', width=15, height=2, fg='black', command=self.reset, font="Times 10 bold", borderwidth=8)
         self.reset_button.place(x=550, y=600)
         
         self.back_button = Button(self.products_frame, text="عودة", bg='white', width=15, height=2, fg='black', command=self.clickedHOME, font="Times 10 bold", borderwidth=8)
         self.back_button.place(x=700, y=600)

         self.search_button=Button(self.products_frame,text="بحث",bg='white',width=15,height=2,fg='black',command= self.searchData,font="Times 10 bold",borderwidth=8)
         self.search_button.place(x=350,y=20)
         # Bouton pour enregistrer la commande
         self.save_order_button = Button(self.products_frame, text="حفظ الطلب", bg='white', width=15, height=2, fg='black', 
                                command=self.saveOrder, font="Times 10 bold", borderwidth=8)
         self.save_order_button.place(x=1070, y=20)  # Vous pouvez ajuster les coordonnées (x, y) en fonction de votre mise en page
         self.date_label = Label(self.products_frame, text="تاريخ_الطلب : ")
         self.date_label.place(x=50, y=510)
         self.date_entry = Entry(self.products_frame)
         self.date_entry.place(x=150, y=510)
         self.client_name_label = Label(self.products_frame, text="اسم العميل : ")
         self.client_name_label.place(x=60, y=540)
         self.client_name_entry = Entry(self.products_frame)
         self.client_name_entry.place(x=150, y=540)

         self.qty_requested_label = Label(self.products_frame, text="الرقم المطلوب : ")
         self.qty_requested_label.place(x=280, y=540)
         self.qty_requested_entry = Entry(self.products_frame)
         self.qty_requested_entry.place(x=370, y=540)

         self.product_number_label = Label(self.products_frame, text="رقم : ")
         self.product_number_label.place(x=500, y=540)
         self.product_number_entry = Entry(self.products_frame)
         self.product_number_entry.place(x=590, y=540)

         self.payment_mode_label = Label(self.products_frame, text="طريقة الدفع : ")
         self.payment_mode_label.place(x=710, y=540)
         self.payment_mode_entry = Entry(self.products_frame)
         self.payment_mode_entry.place(x=790, y=540)

         self.description_label = Label(self.products_frame, text="الوصف : ")
         self.description_label.place(x=900, y=540)
         self.description_entry = Entry(self.products_frame)
         self.description_entry.place(x=970, y=540)
# Déplacement du cadre des commandes plus haut
         self.orders_frame = Frame(window, width=1200, height=300)
         self.orders_frame.place(x=0, y=300)  # Augmenter cette valeur pour déplacer vers le haut (par exemple 500)

         self.orders_listview = ttk.Treeview(self.orders_frame, columns=('معرف_الطلب', 'اسم_العميل','الرقم المطلوب', 'رقم','الوصف', 'المبلغ_الإجمالي', 'طريقة_الدفع', 'تاريخ_الطلب'), show='headings')
         self.orders_listview.place(x=60, y=50)  # Ajustez la position interne si nécessaire
        for col in self.orders_listview['columns']:
          self.orders_listview.heading(col, text=col)
          self.orders_listview.column(col, width=140, stretch=False)
        self.loadOrders()

        self.orders_listview.bind('<<TreeviewSelect>>', self.on_order_select)
   
   def search_client(self):
    # Récupérer le texte saisi dans le champ d'entrée pour le nom du client et la date de commande
    client_name = self.client_name_entry.get().strip()
    order_date = self.date_entry.get().strip()

    # Vérifier si au moins un critère est fourni
    if not client_name and not order_date:
        messagebox.showinfo("Recherche", "Veuillez entrer un nom de client ou une date de commande.")
        return

    conn = None
    try:
        # Connexion à la base de données
        conn = mysql.connector.connect(
            host="127.0.0.1",
            database="richessedb",
            user="root",
            password="1234567890"
        )
        cursor = conn.cursor()

        # Construire la requête en fonction des critères disponibles
        query = """
        SELECT c.id_commande, c.nom_client, c.nbr_demandé, p.nomProduit, p.descProduit, 
               c.montant_total, c.mode_paiement, c.date_commande 
        FROM commande c
        JOIN produits p ON c.numSerie = p.numSerie
        WHERE 1=1
        """
        
        # Paramètres pour la requête SQL
        params = []
        
        # Ajouter des filtres selon les critères fournis
        if client_name:
            query += " AND c.nom_client LIKE %s"
            params.append('%' + client_name + '%')
        
        if order_date:
            query += " AND c.date_commande = %s"
            params.append(order_date)

        # Exécuter la requête SQL
        cursor.execute(query, params)
        
        # Effacer les anciennes données de la Treeview
        self.orders_listview.delete(*self.orders_listview.get_children())

        # Récupérer les résultats
        results = cursor.fetchall()

        if results:
            for row in results:
                # Insérer les résultats dans la liste
                self.orders_listview.insert("", "end", values=row)
        else:
            messagebox.showinfo("Résultats de la recherche", "Aucun client trouvé.")

    except mysql.connector.Error as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

    finally:
        if conn:
            conn.close()

       
   def loadOrders(self):
    """Fetches orders from the database and populates the Treeview."""
    try:
        # Connexion à la base de données
        database = mysql.connector.connect(
            host="127.0.0.1",
            database="richessedb",
            user="root",
            password="1234567890"
        )
        cursor = database.cursor()

        # Requête pour récupérer les informations des commandes
        query = """
            SELECT c.id_commande, c.nom_client,c.nbr_demandé, p.nomProduit, p.descProduit, c.montant_total, c.mode_paiement, c.date_commande 
            FROM commande c
            JOIN produits p ON c.numSerie = p.numSerie
            """
        cursor.execute(query)
        rows = cursor.fetchall()
        

        # Suppression des anciennes données dans le Treeview
        self.orders_listview.delete(*self.orders_listview.get_children())

        # Insérer les données récupérées dans le Treeview
        for row in rows:
            self.orders_listview.insert('', 'end', values=row)

        cursor.close()
        database.close()

    except mysql.connector.Error as e:
        messagebox.showerror('خطأ', f"فشل في استرجاع الطلبات: {str(e)}")
        traceback.print_exc()

   def fetch_product_names(self):
        """Fetch product names from the database and return them as a list."""
        try:
            database = mysql.connector.connect(
                host="127.0.0.1",
                database="richessedb",
                user="root",
                password="1234567890"
            )
            cursor = database.cursor()
            cursor.execute("SELECT nomProduit FROM produits")
            rows = cursor.fetchall()
            product_names = [row[0] for row in rows]  # Get the first column (product names)
            database.close()
            return product_names
        except:
            messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
            traceback.print_exc()
            return []
   def saveOrder(self):
    try:
        # Connexion à la base de données
        database = mysql.connector.connect(
            host="127.0.0.1",
            database="richessedb",
            user="root",
            password="1234567890"
        )
        cursor = database.cursor()

        # Vérifier que le champ 'nom_client' n'est pas vide
        buyer_name = self.buyer_name_entry.get()
        if not buyer_name:
            raise ValueError("الرجاء إدخال اسم المشتري.")

        # Sélectionner la ligne du produit pour récupérer l'ID du produit (numSerie)
        selected = self.listview.selection()
        if not selected:
            raise ValueError("الرجاء تحديد صف المنتج لربطه بالطلب.")

        item = self.listview.item(selected)
        numSerie = item['values'][0]  # Récupérer l'identifiant du produit (numéro de série)

        # Récupérer le montant total (prix unitaire * quantité vendue)
        cursor.execute("SELECT prixUnitaire FROM produits WHERE numSerie = %s", (numSerie,))
        result = cursor.fetchone()
        if not result:
            raise ValueError("Produit non trouvé dans la base de données.")
        prix_unitaire = result[0]

        # Récupérer la quantité vendue
        sold_qty = int(self.product_qty_sold_entry.get()) if self.product_qty_sold_entry.get() else 0
        if sold_qty <= 0:
            raise ValueError("الرجاء إدخال كمية صالحة للطلب.")

        # Calculer le montant total
        montant_total = prix_unitaire * sold_qty

        # Récupérer le mode de paiement (par exemple depuis une entrée ou un bouton radio)
        mode_paiement = self.payment_mode_var.get()  # Assurez-vous que ce champ existe
        if not mode_paiement:
            raise ValueError("الرجاء إدخال طريقة الدفع.")

        # Insérer les informations de la commande dans la table 'commande'
        sql_order = ("INSERT INTO commande (nom_client, numSerie, nbr_demandé, montant_total, mode_paiement, date_commande) "
                     "VALUES (%s, %s, %s, %s, %s, NOW())")
        cursor.execute(sql_order, (buyer_name, numSerie ,sold_qty, montant_total, mode_paiement))

        # Confirmer la transaction
        database.commit()
        self.loadOrders()

        messagebox.showinfo("معلومات", "تم حفظ الطلب بنجاح")

    except Exception as e:
        messagebox.showerror("خطأ", f"فشل في حفظ الطلب: {e}")
        traceback.print_exc()

    finally:
        # Assurez-vous que la connexion est toujours fermée
        if 'database' in locals() and database.is_connected():
            cursor.close()
            database.close()

   def searchData(self):
    self.listview.delete(*self.listview.get_children())
    
    # Vérifier si au moins un champ de recherche est rempli
    if not any([
        self.product_name_entry.get(),
        self.product_desc_entry.get(),
        
        self.buyer_name_entry.get()
    ]):
        messagebox.showerror('خطأ', 'يرجى إدخال قيمة واحدة على الأقل للبحث عنها')
        return
    
    try:
        database = mysql.connector.connect(
            host="127.0.0.1",
            database="richessedb",
            user="root",
            password="1234567890"
        )
        cursor = database.cursor()

        sql = "SELECT * FROM produits WHERE 1=1"
        params = []

        if self.product_name_entry.get():
            sql += " AND UPPER(nomProduit) LIKE UPPER(%s)"
            params.append('%' + self.product_name_entry.get() + '%')

        if self.product_desc_entry.get():
            sql += " AND UPPER(descProduit) LIKE UPPER(%s)"
            params.append('%' + self.product_desc_entry.get() + '%')

        
        if self.buyer_name_entry.get():
            sql += " AND nomAcheteur = %s"
            params.append(self.buyer_name_entry.get())

        cursor.execute(sql, params)
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                self.listview.insert('', END, values=row)
        else:
            messagebox.showinfo('معلومات', 'لا توجد نتائج مطابقة.')

        cursor.close()
        database.close()

    except mysql.connector.Error as e:
        messagebox.showerror('خطأ في الاتصال', str(e))
        traceback.print_exc()

   def reset(self):
    self.product_name_entry.delete(0, 'end')
    self.product_desc_entry.delete(0, 'end')
    self.client_name_entry.delete(0, 'end')
    self.qty_requested_entry.delete(0, 'end')
    self.product_number_entry.delete(0, 'end')
    self.payment_mode_entry.delete(0, 'end')
    self.description_entry.delete(0, 'end')
    
    # Optionally, you can reset the labels if needed, but usually, labels remain constant
    self.client_name_label.config(text="اسم العميل : ")
    self.qty_requested_label.config(text="الرقم المطلوب : ")
    self.product_number_label.config(text="رقم : ")
    self.payment_mode_label.config(text="طريقة الدفع : ")
    self.description_label.config(text="الوصف : ")
     

   def clickedHOME(self):
        self.frame.destroy()
        self.parent.changepage(2)
        
   

   def getInfo(self,event):
    self.reset()
    item_id=self.listview.selection()
    values=self.listview.item(item_id)['values']
    self.product_name_entry.insert(0,values[1])
    self.product_desc_entry.insert(0,values[2])
    pic=values[8]
    self.displayPhoto(pic)
    
   def deleteData(self):
    try:
        # Connect to the database
        database = mysql.connector.connect(
            host="127.0.0.1",
            database="richessedb",
            user="root",
            password="1234567890"
        )
        cursor = database.cursor()

        # Get the selected item from the listview
        selected_item = self.listview.selection()
        if not selected_item:
            raise ValueError("الرجاء تحديد صف للحذف.")

        # Fetch the selected item's values
        for item in selected_item:
            item_values = self.listview.item(item, 'values')
            product_name = item_values[1]  # Adjust the index based on your column order

            # SQL query to delete the selected item from the database
            sql = "DELETE FROM produits WHERE nomProduit = %s"
            cursor.execute(sql, (product_name,))
            database.commit()

            # Remove the item from the listview
            self.listview.delete(item)

        database.close()
        messagebox.showinfo("نجاح", "تم حذف البيانات بنجاح")
        
        # Refresh the listview to reflect changes
        self.displayData()

    except Exception as e:
        messagebox.showerror("خطأ", f"فشل في حذف البيانات: {e}")
        traceback.print_exc()
   def on_order_select(self, event):
    # Récupérer la commande sélectionnée
    selected = self.orders_listview.selection()
    if not selected:
        return  # Rien n'est sélectionné

    item = self.orders_listview.item(selected)
    order_id = item['values'][0]  # ID de la commande

    try:
        # Connexion à la base de données
        conn = mysql.connector.connect(
            host="127.0.0.1",
            database="richessedb",
            user="root",
            password="1234567890"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les données de la commande
        query = """
        SELECT 
            c.nom_client, 
            c.nbr_demandé, 
            p.nomProduit, 
            p.descProduit, 
            c.mode_paiement,
            c.date_commande
        FROM 
            commande c
        JOIN 
            produits p 
        ON 
            c.numSerie = p.numSerie
        WHERE 
            c.id_commande = %s;
        """
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()

        if result:
            # Charger les données dans les champs d'entrée
            self.client_name_entry.delete(0, END)
            self.client_name_entry.insert(0, str(result[0]))

            self.qty_requested_entry.delete(0, END)
            self.qty_requested_entry.insert(0, str(result[1]))

            self.product_number_entry.delete(0, END)
            self.product_number_entry.insert(0, str(result[2]))

            self.description_entry.delete(0, END)
            self.description_entry.insert(0, str(result[3]))

            self.payment_mode_entry.delete(0, END)
            self.payment_mode_entry.insert(0, str(result[4]))

    except mysql.connector.Error as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue lors de la récupération des données : {e}")

    finally:
        if conn:
            conn.close()

    # Activer le bouton de mise à jour une fois les données chargées
    self.update_button['state'] = 'normal'





   def update_order(self):
    try:
        # Connexion à la base de données
        database = mysql.connector.connect(
            host="127.0.0.1",
            database="richessedb",
            user="root",
            password="1234567890"
        )
        cursor = database.cursor()

        # Récupérer les informations sur le produit basé sur le nomProduit
        product_name = self.product_number_entry.get()
        cursor.execute("""
            SELECT numSerie, prixUnitaire
            FROM produits
            WHERE nomProduit = %s
        """, (product_name,))
        product_result = cursor.fetchone()

        if not product_result:
            raise ValueError("Le produit n'existe pas dans la base de données.")
        
        numSerie, prix_unitaire = product_result

        # Calculer le montant total
        try:
            sold_qty = int(self.qty_requested_entry.get()) if self.qty_requested_entry.get() else 0
            montant_total = prix_unitaire * sold_qty
        except ValueError:
            montant_total = 0  # Si la quantité n'est pas valide, ne pas calculer le montant total

        # Sélectionner la ligne à mettre à jour
        selected = self.orders_listview.selection()
        if not selected:
            raise ValueError("Veuillez sélectionner une commande à mettre à jour.")

        item = self.orders_listview.item(selected)
        order_id = item['values'][0]

        # Préparer la mise à jour en fonction des champs modifiés
        update_fields = []
        update_values = []

        # Récupérer les valeurs actuelles pour conserver celles non modifiées
        current_nom_client = item['values'][1]  # Nom client à l'index 1
        current_numSerie = item['values'][2]  # numSerie à l'index 2
        current_qty_demande = item['values'][3]  # Quantité demandée à l'index 3
        current_description = item['values'][4]  # Description à l'index 4
        current_date_commande = item['values'][7]  # Date commande à l'index 5
        current_mode_paiement = item['values'][6]  # Mode paiement à l'index 6
        current_montant_total = item['values'][5]  # Montant total à l'index 7

        if self.client_name_entry.get():
            update_fields.append("nom_client=%s")
            update_values.append(self.client_name_entry.get())
        else:
            update_values.append(current_nom_client)

        if self.qty_requested_entry.get():
            update_fields.append("nbr_demandé=%s")
            update_values.append(self.qty_requested_entry.get())
        else:
            update_values.append(current_qty_demande)
        
        if self.product_number_entry.get():
            update_fields.append("numSerie=%s")
            update_values.append(numSerie)
        else:
            update_values.append(current_numSerie)
        
        if self.payment_mode_entry.get():
            update_fields.append("mode_paiement=%s")
            update_values.append(self.payment_mode_entry.get())
        else:
            update_values.append(current_mode_paiement)

        if montant_total is not None:
            update_fields.append("montant_total=%s")
            update_values.append(montant_total)
        else:
            update_values.append(current_montant_total)
        
        

        if not update_fields:
            raise ValueError("Aucun champ à mettre à jour.")

        # Ajouter l'ID de la commande à la fin des valeurs
        update_values.append(order_id)

        # Créer la chaîne de requête SQL dynamique
        update_query = "UPDATE commande SET " + ", ".join(update_fields) + " WHERE id_commande=%s"
        
        cursor.execute(update_query, tuple(update_values))
        database.commit()

        # Mettre à jour la vue avec les nouvelles valeurs (y compris la date et le montant total)
        updated_values = (
            order_id,
            self.client_name_entry.get() if self.client_name_entry.get() else current_nom_client,
            self.qty_requested_entry.get() if self.qty_requested_entry.get() else current_qty_demande,
            self.product_number_entry.get() if self.product_number_entry.get() else current_numSerie,
            self.description_entry.get() if self.description_entry.get() else current_description,
            montant_total if montant_total is not None else current_montant_total,
      # S'assurer que la date commande est correctement réinclus
            self.payment_mode_entry.get() if self.payment_mode_entry.get() else current_mode_paiement,
            current_date_commande, 
        )
        
        print("Updated values:", updated_values)  # Debug: afficher les valeurs mises à jour
        
        self.orders_listview.item(selected, values=updated_values)

        messagebox.showinfo("Information", "Les données ont été mises à jour avec succès.")

    except Exception as e:
        messagebox.showerror("Erreur", f"Échec de la mise à jour des données : {e}")
        traceback.print_exc()

    finally:
        # Assurez-vous que la connexion est toujours fermée
        if 'database' in locals() and database.is_connected():
            cursor.close()
            database.close()

    # Réactiver le bouton de mise à jour si nécessaire
    self.update_button['state'] = 'normal'

   def delete_order(self):
    try:
        # Connexion à la base de données
        database = mysql.connector.connect(
            host="127.0.0.1",
            database="richessedb",
            user="root",
            password="1234567890"
        )
        cursor = database.cursor()

        # Sélectionner la ligne à supprimer
        selected = self.orders_listview.selection()
        if not selected:
            raise ValueError("Veuillez sélectionner une commande à supprimer.")

        item = self.orders_listview.item(selected)
        order_id = item['values'][0]  # ID de la commande à l'index 0

        # Exécuter la requête de suppression
        delete_query = "DELETE FROM commande WHERE id_commande=%s"
        cursor.execute(delete_query, (order_id,))
        database.commit()

        # Supprimer l'élément de la vue
        self.orders_listview.delete(selected)

        messagebox.showinfo("Information", "La commande a été supprimée avec succès.")

    except Exception as e:
        messagebox.showerror("Erreur", f"Échec de la suppression de la commande : {e}")
        traceback.print_exc()

    finally:
        # Assurez-vous que la connexion est toujours fermée
        if 'database' in locals() and database.is_connected():
            cursor.close()
            database.close()



       






class SEARCH_Page():
    def __init__(self, parent, window):
      self.parent = parent
      self.window=window
      self.frame=Frame(self.window,width=1200,height=800)
      self.info_frame=Frame(self.window,width=1200,height=100,bg='#9f9f9f')
      self.info_frame.place(x=0,y=0)
      self.buttons_frame=Label(self.window,width=1200,height=800)
      self.buttons_frame.place(x=0,y=100)
      self.Search_image=ImageTk.PhotoImage(Image.open('C:\\Users\\ORIGINAL SHOP\\Desktop\\RichesseMS\\RichesseMS\\SEARIM.png'))
      self.im_label=Label(self.info_frame,image=self.Search_image,bg='#9f9f9f')
      self.im_label.place(x=980,y=15)
      self.title=Label(self.info_frame,text="B.F.Z SARL ",bg='#9f9f9f',fg='black',font=('Times New Roman',25))
      self.title.place(x=580,y=30)
      
      self.products_frame=Frame(window,width=1200,height=800)
      self.products_frame.place(x=0,y=100)
      self.field_frame=Frame(self.products_frame,width= 650,height= 200,bg="#9f9f9f",borderwidth=2,relief="ridge")
      self.field_frame.place(x=10,y=10)

      self.help=Label(self.field_frame, text="البحث عن طريق :", bg="#9f9f9f")
      self.help.place(x=10,y=10)
      self.orL=Label( self.field_frame,text="أو",bg="#9f9f9f")
      self.orL.place(x=250,y=70)
      self.orL2=Label( self.field_frame,text="أو",bg="#9f9f9f")
      self.orL2.place(x=250,y=150)
#name
      self.product_names = self.fetch_product_names()

        # Use a dropdown (OptionMenu) instead of Entry for product names
      self.product_name = Label(self.field_frame, text="الاسم : ", bg="#9f9f9f")
      self.product_name.place(x=70, y=40)
      self.selected_product_name = StringVar(self.field_frame)
      if self.product_names:  # Set the first product name as the default
            self.selected_product_name.set(self.product_names[0])
      self.product_name_dropdown = OptionMenu(self.field_frame, self.selected_product_name, *self.product_names)
      self.product_name_dropdown.place(x=50, y=70)

#price
      self.product_price=Label( self.field_frame,text="السعر : ",bg="#9f9f9f")
      self.product_price.place(x=370,y=40)
      self.product_price_entry=Entry( self.field_frame)
      self.product_price_entry.place(x=350,y=70)
#quantity
      self.product_qty=Label( self.field_frame,text="الكمية : ",bg="#9f9f9f")
      self.product_qty.place(x=70,y=120)
      self.product_qty_entry=Entry( self.field_frame)
      self.product_qty_entry.place(x=50,y=150)

#Entree
      self.product_lastEntryDate=Label( self.field_frame,text="تاريخ آخر دخول : ",bg="#9f9f9f")
      self.product_lastEntryDate.place(x=370,y=120)
      self.product_lastEntryDate_DP=DateEntry( self.field_frame, width= 16, background= "brown", foreground= "white",bd=2)
      self.product_lastEntryDate_DP.place(x=350,y=150)
 
#Image :) 

      self.product_image=Label(self.products_frame,text="الصورة :")
      self.product_image.place(x=900,y=60)
      self.prop=ImageTk.PhotoImage(Image.open('C:\\Users\\ORIGINAL SHOP\\Desktop\\RichesseMS\\RichesseMS\\box2.png'))

      self.products_image=Frame(self.products_frame,bg="#9f9f9f",width=100,height=100,borderwidth=1, relief="solid", highlightthickness=1, highlightbackground="black")
      self.products_image.place(x=1000,y=40)
      self.products_image_DISPLAY=Label(self.products_image,image=self.prop,width=75,height=75,bg="#9f9f9f")
      self.products_image_DISPLAY.place(x=10,y=10)

 #Listview 
      self.cols = ('المرجع', 'الاسم', 'الوصف', 'السعر', 'الكمية', 'عتبة التنبيه', 'تاريخ الدخول', 'تاريخ الإزالة', 'الصورة')
      self.listview=ttk.Treeview(self.products_frame,columns=self.cols,show='headings')


      for col in self.cols:
          self.listview.heading(col,text=col)
          self.listview.column(col,width=130,stretch=False)
          self.listview.place(x=60,y=300)
          self.listview.column("الوصف",width=200)
          self.listview.column('السعر',width=70)
          self.listview.column('الكمية',width=70)
          self.listview.column('الصورة',width=100)
          self.listview.column('المرجع',width=50)
      self.listview.bind("<ButtonRelease-1>",self.getPic)




#search button
      self.search_button=Button(self.products_frame,text="بحث",bg='white',width=12,height=1,fg='black',command= self.searchData,font="Times 10 bold",borderwidth=8)
      self.search_button.place(x=540,y=70)
      self.reset_button=Button( self.products_frame,text="إعادة تعيين",bg='white',width=12,height=1,fg='black',command= self.reset,font="Times 10 bold",borderwidth=8)
      self.reset_button.place(x=540,y=150)
      
      self.back_button=Button(self.products_frame,text="رجوع",bg='white',width=15,height=2,fg='black',command=self.clickedHOME,font="Times 10 bold",borderwidth=8)
      self.back_button.place(x=390,y=600)
    def fetch_product_names(self):
        """Fetch product names from the database and return them as a list."""
        try:
            database = mysql.connector.connect(
                host="127.0.0.1",
                database="richessedb",
                user="root",
                password="1234567890"
            )
            cursor = database.cursor()
            cursor.execute("SELECT nomProduit FROM produits")
            rows = cursor.fetchall()
            product_names = [row[0] for row in rows]  # Get the first column (product names)
            database.close()
            return product_names
        except:
            messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
            traceback.print_exc()
            return []
    def reset(self):
      self.product_name_entry.delete(0,END)
      self.product_price_entry.delete(0,END)
      self.product_qty_entry.delete(0,END)
      self.product_lastEntryDate_DP.set_date(datetime.datetime.now().date())
   
    def searchData(self):
     self.listview.delete(*self.listview.get_children())
     if (self.selected_product_name.get() != "" and self.product_price_entry.get() != "" and self.product_qty_entry.get() != "" and self.product_lastEntryDate_DP.get_date()== datetime.datetime.now().date()):
        messagebox.showerror('خطأ', 'يرجى اختيار حقل واحد للبحث عنه')
     else:
         try:
            self.database = mysql.connector.connect(
                host="127.0.0.1",
                database="richessedb",
                user="root",
                password="1234567890"
            )

            cursor = self.database.cursor()
            if self.selected_product_name.get() != "" and self.product_price_entry.get() == "" and self.product_qty_entry.get() == "" and self.product_lastEntryDate_DP.get_date() == datetime.date.today():
                sql = "SELECT * FROM produits WHERE UPPER(nomProduit) like UPPER(%s)"
                cursor.execute(sql, (self.selected_product_name.get() + '%',))
                
            elif self.selected_product_name.get() == "" and self.product_price_entry.get() != "" and self.product_qty_entry.get() == "" and self.product_lastEntryDate_DP.get_date() == datetime.date.today():
                sql = "SELECT * FROM produits WHERE prixUnitaire=%s"
                cursor.execute(sql, (self.product_price_entry.get(),))
            elif self.selected_product_name.get() == "" and self.product_price_entry.get() == "" and self.product_qty_entry.get() != "" and self.product_lastEntryDate_DP.get_date() == datetime.date.today():
                sql = "SELECT * FROM produits WHERE quantiteProduit=%s"
                cursor.execute(sql, (self.product_qty_entry.get(),))
            elif self.selected_product_name.get() == "" and self.product_price_entry.get() == "" and self.product_qty_entry.get() == "" and self.product_lastEntryDate_DP.get_date() <= datetime.datetime.now().date():
                selected_date = self.product_lastEntryDate_DP.get_date().strftime('%Y-%m-%d')  # Format YYYY-MM-DD
                sql = "SELECT * FROM produits WHERE date_entree = %s"
                cursor.execute(sql, (selected_date,)) 
            else:
                   messagebox.showerror('خطأ', 'يرجى اختيار حقل واحد فقط للبحث عنه')
                   return

            rows = cursor.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.listview.insert("", END, values=row)
                self.reset()
                self.listview.yview_moveto(0)
                self.database.commit()
            
            else:
                 messagebox.showerror("خطأ", "لم يتم العثور على المنتج")
            self.database.close()
         except :
            messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
            traceback.print_exc()



    def getPic(self,event): 
      self.reset()
      item_id =self.listview.selection()[0]
      self.values=self.listview.item(item_id)['values']
    
      pic=self.values[8]
      self.displayPhoto(pic)
    
    def displayPhoto(self,pic):
     try:

              
       if(pic !='None' and pic is not None):
    
            img = Image.open(pic)
            img.thumbnail((self.products_image_DISPLAY.winfo_width(), self.products_image_DISPLAY.winfo_height()))
            img = ImageTk.PhotoImage(img)
            self.products_image_DISPLAY.config(image=img)
            self.products_image_DISPLAY.image = img  # to prevent garbage collection
       else:
            
            self.products_image_DISPLAY.config(image=self.prop)
              
     except:
       messagebox.showerror("خطأ", "حدث خطأ أثناء عرض الصورة")
       traceback.print_exc()

    def clickedHOME(self):
        self.frame.destroy()
        self.parent.changepage(2)


class VIEW_Page:
    def __init__(self, parent, window):
        self.parent = parent
        self.window = window
        self.frame = Frame(self.window, width=1200, height=800)
        self.frame.pack(fill=BOTH, expand=True)

        try:
            # Title
            self.title = Label(self.frame, text="إدارة الموردين", font=("Arial", 24))
            self.title.pack(pady=20)

            # Frame for supplier info
            self.fournisseur_frame = Frame(self.frame)
            self.fournisseur_frame.pack(pady=10)

            # Supplier name
            self.nom_label = Label(self.fournisseur_frame, text="اسم المورد:")
            self.nom_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)
            self.nom_entry = Entry(self.fournisseur_frame)
            self.nom_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

            # Supplier address
            self.adresse_label = Label(self.fournisseur_frame, text="العنوان:")
            self.adresse_label.grid(row=1, column=0, padx=10, pady=10, sticky=E)
            self.adresse_entry = Entry(self.fournisseur_frame)
            self.adresse_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

            # Supplier phone
            self.tel_label = Label(self.fournisseur_frame, text="الهاتف:")
            self.tel_label.grid(row=2, column=0, padx=10, pady=10, sticky=E)
            self.tel_entry = Entry(self.fournisseur_frame)
            self.tel_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

            # Buttons
            self.add_button = Button(self.fournisseur_frame, text="إضافة", command=self.add_fournisseur)
            self.add_button.grid(row=3, column=0, padx=10, pady=10)

            self.update_button = Button(self.fournisseur_frame, text="تعديل", command=self.update_fournisseur)
            self.update_button.grid(row=3, column=1, padx=10, pady=10)

            self.delete_button = Button(self.fournisseur_frame, text="حذف", command=self.delete_fournisseur)
            self.delete_button.grid(row=3, column=2, padx=10, pady=10)

            # Table of suppliers
            self.cols = ('ID', 'الاسم', 'العنوان', 'الهاتف')
            self.fournisseur_list = ttk.Treeview(self.frame, columns=self.cols, show='headings')
            for col in self.cols:
                self.fournisseur_list.heading(col, text=col)
                self.fournisseur_list.column(col, width=150, anchor='center')  # Adjust column width as necessary

            self.fournisseur_list.pack(pady=20, fill=BOTH, expand=True)

            # Bind selection
            self.fournisseur_list.bind('<ButtonRelease-1>', self.select_fournisseur)

            # Display data
            self.display_fournisseurs()
            self.back_button = Button(self.frame, text="عودة", bg='white', width=15, height=2, fg='black', 
                                      command=self.clickedHOME, font="Times 10 bold", borderwidth=8)
            self.back_button.place(x=930, y=200)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))

    def db_connect(self):
        """Connect to the database."""
        return mysql.connector.connect(host="localhost", user="root", password="1234567890", database="richessedb")
    def clickedHOME(self):
        self.frame.destroy()
        self.parent.changepage(2) 
    def add_fournisseur(self):
        nom = self.nom_entry.get()
        adresse = self.adresse_entry.get()
        tel = self.tel_entry.get()

        if nom and adresse and tel:
            try:
                db = self.db_connect()
                cursor = db.cursor()
                cursor.execute("INSERT INTO fournisseur (nomFournisseur, adresseFournisseur, telephoneFournisseur) VALUES (%s, %s, %s)", (nom, adresse, tel))
                db.commit()
                cursor.close()
                db.close()
                messagebox.showinfo("نجاح", "تمت إضافة المورد بنجاح")
                self.clear_fields()
                self.display_fournisseurs()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", str(err))
        else:
            messagebox.showwarning("تحذير", "يرجى ملء جميع الحقول")

    def update_fournisseur(self):
        selected_item = self.fournisseur_list.selection()
        if selected_item:
            id = self.fournisseur_list.item(selected_item)['values'][0]
            nom = self.nom_entry.get()
            adresse = self.adresse_entry.get()
            tel = self.tel_entry.get()

            if nom and adresse and tel:
                try:
                    db = self.db_connect()
                    cursor = db.cursor()
                    cursor.execute("UPDATE fournisseur SET nomFournisseur=%s, adresseFournisseur=%s, telephoneFournisseur=%s WHERE idFournisseur=%s", 
                                   (nom, adresse, tel, id))
                    db.commit()
                    cursor.close()
                    db.close()
                    messagebox.showinfo("نجاح", "تم تعديل المورد بنجاح")
                    self.clear_fields()
                    self.display_fournisseurs()
                except mysql.connector.Error as err:
                    messagebox.showerror("Database Error", str(err))
            else:
                messagebox.showwarning("تحذير", "يرجى ملء جميع الحقول")
        else:
            messagebox.showwarning("تحذير", "يرجى تحديد المورد")

    def delete_fournisseur(self):
        selected_item = self.fournisseur_list.selection()
        if selected_item:
            try:
                id = self.fournisseur_list.item(selected_item)['values'][0]
                db = self.db_connect()
                cursor = db.cursor()
                cursor.execute("DELETE FROM fournisseur WHERE idFournisseur=%s", (id,))
                db.commit()
                cursor.close()
                db.close()
                messagebox.showinfo("نجاح", "تم حذف المورد بنجاح")
                self.clear_fields()
                self.display_fournisseurs()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", str(err))
        else:
            messagebox.showwarning("تحذير", "يرجى تحديد المورد")

    def display_fournisseurs(self):
        try:
            db = self.db_connect()
            cursor = db.cursor()
            cursor.execute("SELECT idFournisseur, nomFournisseur, adresseFournisseur, telephoneFournisseur FROM fournisseur")
            rows = cursor.fetchall()
            self.fournisseur_list.delete(*self.fournisseur_list.get_children())
            for row in rows:
                self.fournisseur_list.insert('', 'end', values=row)
            cursor.close()
            db.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))

    def select_fournisseur(self, event):
        selected_item = self.fournisseur_list.selection()
        if selected_item:
            values = self.fournisseur_list.item(selected_item)['values']
            self.nom_entry.delete(0, END)
            self.nom_entry.insert(0, values[1])
            self.adresse_entry.delete(0, END)
            self.adresse_entry.insert(0, values[2])
            self.tel_entry.delete(0, END)
            self.tel_entry.insert(0, values[3])

    def clear_fields(self):
        """Clear all input fields."""
        self.nom_entry.delete(0, END)
        self.adresse_entry.delete(0, END)
        self.tel_entry.delete(0, END)



    
def main():
    root = Tk()
    maingui(root)
    root.mainloop()
    
if __name__ =='__main__':
    main()