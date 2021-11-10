from tkinter import *
import math,random,os
from tkinter import messagebox
class BillApp:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x720+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times mew roman",30, "bold"),pady=2).pack(fill=X)

       #  --------------------- variables ------------

       #  -------------- Cosmetics ------------
        self.soap = IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()

        #  -------------- Cosmetics ------------
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.suger=IntVar()
        self.tea=IntVar()

        #  -------------- Cold drink ------------
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #  -------------- Total Product Price and Tax Variable ------------
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        # -------------- Customer -------------
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.c_bill_no=StringVar()
        x=random.randint(1000,9999)
        self.c_bill_no.set(str(x))
        self.c_search_bill=StringVar()

        # ----------------------  customer Detail Frame ------------------------
        F1 = LabelFrame(self.root,text="Customer Details",font=("time new roman",15,"bold"),fg="gold",bg=bg_color,bd=10)
        F1.place(x=0,y=70,relwidth=1)

        cname_lb1 = Label(F1,text="Customer Name",bg=bg_color, font=("time new roman",15,"bold"),fg="white").grid(row=0,column=0,padx=20,pady=5)
        cname_txt= Entry(F1,width=15,textvariable=self.c_name, font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphone_lb1 = Label(F1,text="Phone no.",bg=bg_color, font=("time new roman",15,"bold"),fg="white").grid(row=0,column=2,padx=20,pady=5)
        cphone_txt= Entry(F1,width=15,textvariable=self.c_phone, font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        c_bill_no_lb1 = Label(F1,text="Bill no.",bg=bg_color, font=("time new roman",15,"bold"),fg="white").grid(row=0,column=4,padx=20,pady=5)
        c_bill_no_txt= Entry(F1,width=15,textvariable=self.c_bill_no, font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bill_btn = Button(F1,text="Search",command=self.find_bill, width=15,font="arial 15",bd=7).grid(row=0,column=6,padx=10,pady=5)


        # ----------------------  cosmatics Frame ------------------------
        F2 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=0,y=170,height=380)

        bath_lb1 = Label(F2,text="Bath Soap",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt= Entry(F2,width=10,textvariable=self.soap, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lb1 = Label(F2,text="Face cream",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt= Entry(F2,width=10,textvariable=self.face_cream, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w_lb1 = Label(F2,text="Face Wash",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt= Entry(F2,width=10,textvariable=self.face_wash, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_s_lb1 = Label(F2,text="Hair Spray",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt= Entry(F2,width=10,textvariable=self.spray, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_g_lb1 = Label(F2,text="Hair Gell",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt= Entry(F2,width=10,textvariable=self.gell, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lb1 = Label(F2,text="Body Loshan",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt= Entry(F2,width=10,textvariable=self.loshan, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



        # ----------------------  Grocery Frame ------------------------
        F3 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=170,height=380)

        g1_lb1 = Label(F3,text="Rice",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt= Entry(F3,width=10,textvariable=self.rice, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lb1 = Label(F3,text="Food Oil",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt= Entry(F3,width=10,textvariable=self.food_oil, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lb1 = Label(F3,text="Daal",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt= Entry(F3,width=10,textvariable=self.daal, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lb1 = Label(F3,text="Wheat",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt= Entry(F3,width=10,textvariable=self.wheat, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lb1 = Label(F3,text="Sugar",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt= Entry(F3,width=10,textvariable=self.suger, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lb1 = Label(F3,text="Tea",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt= Entry(F3,width=10,textvariable=self.tea, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        # ----------------------  Cool Drink Frame ------------------------
        F4 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Cool Drink",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=628,y=170,height=380)

        c1_lb1 = Label(F4,text="Maza",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt= Entry(F4,width=10,textvariable=self.maza, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lb1 = Label(F4,text="Cock",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt= Entry(F4,width=10,textvariable=self.cock, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lb1 = Label(F4,text="Frooti",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt= Entry(F4,width=10,textvariable=self.frooti, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lb1 = Label(F4,text="Thumbs Up",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt= Entry(F4,width=10,textvariable=self.thumbsup, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lb1 = Label(F4,text="Limca",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt= Entry(F4,width=10,textvariable=self.limca, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lb1 = Label(F4,text="Sprite",bg=bg_color, font=("time new roman",16,"bold"),fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt= Entry(F4,width=10,textvariable=self.sprite, font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        # ----------------------  Bill Area Frame ------------------------
        F5 = Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=955,y=170,width=385,height=380)
        bill_title = Label(F5,text="Bill Area", font=("arial 15 bold"),bd=7,relief=GROOVE).pack(fill=X)
        scrol_y =Scrollbar(F5,orient=VERTICAL)
        self.textarea = Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        # ---------------- Button Fram --------------
        F6 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=550,relwidth=1,height=170)

        
        m1_lb1 = Label(F6,text="Total Cosmetic Price",bg=bg_color, font=("time new roman",14,"bold"),fg="white").grid(row=0,padx=10,pady=1,column=0,sticky="w")
        m1_txt= Entry(F6,width=15,textvariable=self.cosmetic_price, font=("time new roman",14,"bold"),bd=7,relief=SUNKEN).grid(row=0,padx=0,pady=1,column=1)
        
        m2_lb1 = Label(F6,text="Total Grocery Price",bg=bg_color, font=("time new roman",14,"bold"),fg="white").grid(row=1,padx=10,pady=1,column=0,sticky="w")
        m2_txt= Entry(F6,width=15,textvariable=self.grocery_price, font=("time new roman",14,"bold"),bd=7,relief=SUNKEN).grid(row=1,padx=0,pady=1,column=1)
        
        m3_lb1 = Label(F6,text="Total Cold Drink Price",bg=bg_color, font=("time new roman",14,"bold"),fg="white").grid(row=2,padx=10,pady=1,column=0,sticky="w")
        m3_txt= Entry(F6,width=15,textvariable=self.cold_drink_price, font=("time new roman",14,"bold"),bd=7,relief=SUNKEN).grid(row=2,padx=0,pady=1,column=1)
        
        c1_lb1 = Label(F6,text="Cosmetic Tax",bg=bg_color, font=("time new roman",14,"bold"),fg="white").grid(row=0,padx=10,pady=1,column=2,sticky="w")
        c1_txt= Entry(F6,width=15,textvariable=self.cosmetic_tax, font=("time new roman",14,"bold"),bd=7,relief=SUNKEN).grid(row=0,padx=0,pady=1,column=3)

        c2_lb1 = Label(F6,text="Grocery Tax",bg=bg_color, font=("time new roman",14,"bold"),fg="white").grid(row=1,padx=10,pady=1,column=2,sticky="w")
        c2_txt= Entry(F6,width=15,textvariable=self.grocery_tax, font=("time new roman",14,"bold"),bd=7,relief=SUNKEN).grid(row=1,padx=0,pady=1,column=3)

        c3_lb1 = Label(F6,text="Cold Drink Tax",bg=bg_color, font=("time new roman",14,"bold"),fg="white").grid(row=2,padx=10,pady=1,column=2,sticky="w")
        c3_txt= Entry(F6,width=15,textvariable=self.cold_drink_tax, font=("time new roman",14,"bold"),bd=7,relief=SUNKEN).grid(row=2,padx=0,pady=1,column=3)

        btn_f = Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=770,y=10,width=560,height=105)
        
        total_btn = Button(btn_f,command=self.total,text="Total",width=10,font="arial 14",bd=2,bg="cadetblue",fg="white",pady=15).grid(row=0,column=0,padx=5,pady=5)
        gbill_btn = Button(btn_f,command=self.bill_area,text="Generate Bill",width=10,font="arial 14",bd=2,bg="cadetblue",fg="white",pady=15).grid(row=0,column=1,padx=5,pady=5)
        clear_btn = Button(btn_f,text="Clear",command=self.clear_data, width=10,font="arial 14",bd=2,bg="cadetblue",fg="white",pady=15).grid(row=0,column=2,padx=5,pady=5)
        exit_btn = Button(btn_f,text="Exit",command=self.Exit_app,width=10,font="arial 14",bd=2,bg="cadetblue",fg="white",pady=15).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gell.get()*140
        self.c_bl_p=self.loshan.get()*180

        self.total_cosmetic_price=float(
            self.c_s_p+
            self.c_fc_p+
            self.c_fw_p+
            self.c_hs_p+
            self.c_hg_p+
            self.c_bl_p
        )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price*0.18),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.rice.get()*80
        self.g_fo_p=self.food_oil.get()*280
        self.g_d_p=self.daal.get()*80
        self.g_w_p=self.wheat.get()*40
        self.g_s_p=self.suger.get()*40
        self.g_t_p=self.tea.get()*300

        self.total_grocery_price=float(
            self.g_r_p+
            self.g_fo_p+
            self.g_d_p+
            self.g_w_p+
            self.g_s_p+
            self.g_t_p
        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.18),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.d_m_p=self.maza.get()*80
        self.d_c_p=self.cock.get()*80
        self.d_f_p=self.frooti.get()*60
        self.d_t_p=self.thumbsup.get()*50
        self.d_l_p=self.limca.get()*40
        self.d_s_p=self.sprite.get()*60

        self.total_drink_price=float(
            self.d_m_p+
            self.d_c_p+
            self.d_f_p+
            self.d_t_p+
            self.d_l_p+
            self.d_s_p
        )
        self.cold_drink_price.set("Rs. "+str(self.total_drink_price))
        self.d_tax = round((self.total_drink_price*0.18),2)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))

        self.Total_bill = round(float(self.total_cosmetic_price+
            self.total_grocery_price+
            self.total_drink_price+
            self.c_tax+
            self.g_tax+
            self.d_tax
        ),2)


    def welcome_bill(self):
        self.textarea.delete("1.0", END)
        self.textarea.insert(END,"\tWelcome to Shop Reatil\n")
        self.textarea.insert(END,f"\n Bill Number : {self.c_bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
        self.textarea.insert(END,"\n===========================================")
        self.textarea.insert(END,"\n Products\t\tQTY\t\tPrice")

        self.textarea.insert(END,"\n===========================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        
        elif self.cosmetic_price.get()== "Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product purchased")

        else:
            self.welcome_bill()
            # -------------- cosmetics-----------
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
                
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
                
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
                
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
                
            if self.gell.get()!=0:
                self.textarea.insert(END,f"\n Hair Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
                
            if self.loshan.get()!=0:
                self.textarea.insert(END,f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")
                
            # -------------- grocety-----------
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
                
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
                
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
                
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
                
            if self.suger.get()!=0:
                self.textarea.insert(END,f"\n Suger\t\t{self.suger.get()}\t\t{self.g_s_p}")
                
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")
                
            # -------------- Cold Drink-----------
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
                
            if self.cock.get()!=0:
                self.textarea.insert(END,f"\n Cock\t\t{self.cock.get()}\t\t{self.d_c_p}")
                
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
                
            if self.thumbsup.get()!=0:
                self.textarea.insert(END,f"\n Thumbsup\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")
                
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
                
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
            
            self.textarea.insert(END,"\n-------------------------------------------")
            
            if self.cosmetic_tax.get() !="Rs. 0.0":
                self.textarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            
            if self.grocery_tax.get() != "Rs. 0.0":
                self.textarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            
            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.textarea.insert(END,f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")

            self.textarea.insert(END,"\n-------------------------------------------")
            self.textarea.insert(END,f"\n Total Bill\t\t\tRs. {self.Total_bill}")
            self.textarea.insert(END,"\n-------------------------------------------")
            self.save_bill()


    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            self.bill_data = self.textarea.get("1.0",END)
            f1 = open("bills/"+str(self.c_bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no. : {self.c_bill_no.get()} saved Successfully")
        else:
            return
    
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            # print(i)
            if i.split('.')[0] == self.c_bill_no.get():
                f1 = open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def clear_data(self):
        
       #  -------------- Cosmetics ------------
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.loshan.set(0)

        #  -------------- Cosmetics ------------
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.suger.set(0)
        self.tea.set(0)

        #  -------------- Cold drink ------------
        self.maza.set(0)
        self.cock.set(0)
        self.frooti.set(0)
        self.thumbsup.set(0)
        self.limca.set(0)
        self.sprite.set(0)

        #  -------------- Total Product Price and Tax Variable ------------
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_drink_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")

        # -------------- Customer -------------
        self.c_name.set("")
        self.c_phone.set("")
        self.c_bill_no.set("")
        x=random.randint(1000,9999)
        self.c_bill_no.set(str(x))

        self.c_search_bill.set("")
        self.welcome_bill()

    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")

        if op >0:
            self.root.destroy()

 

root = Tk()
obj = BillApp(root)
root.mainloop()