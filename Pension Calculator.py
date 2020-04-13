from tkinter import *
import sqlite3

root =Tk()
root.title('Pension Calculator')
#root.iconbitmap('/c')

# creat Submit Function to detabase
# creat detabase or connect to
conn = sqlite3.connect('pension.db')
# creat corsor
c = conn.cursor()
'''
c.execute("""CREATE TABLE pension (
    management_Fee text,
    monthly_payment text,
    age text,
    police_open_date text,
    compensation text,
    eccrisis_employee text,
    eccrisis_employer text,
    factor text,
    current_balance text
    )""")
'''


def police_details():
    global my_police
    police_details = Toplevel()
    police_details.title('פרטי הפנסיה שלך')
    #police_details.iconbitmap('C:/Users/Happy People/Downloads/icon.ico')

    def save_details():
        # creat detabase or connect to
        conn = sqlite3.connect('pension.db')
        # creat corsor
        c = conn.cursor()

        c.execute("INSERT INTO pension VALUES(:management_Fee, :monthly_payment, :age, :police_open_date, :compensation, :eccrisis_employee, :eccrisis_employer, :factor, :current_balance )",
                  {
                      'management_Fee':management_Fee_entry.get(),
                      'monthly_payment': monthly_payment_entry.get(),
                      'age': age_entry.get(),
                      'police_open_date': police_open_date_entry.get(),
                      'compensation': compensation_entry.get(),
                      'eccrisis_employee': eccrisis_employee_entry.get(),
                      'eccrisis_employer': eccrisis_employer_entry.get(),
                      'factor': factor_entry.get(),
                      'current_balance': current_balance_entry.get()

                  })

        a = [management_Fee_entry, monthly_payment_entry, age_entry, police_open_date_entry,compensation_entry, eccrisis_employee_entry, eccrisis_employer_entry, factor_entry, current_balance_entry]
        for i in a:
            i.delete(0,END)
        conn.commit()
        # close Connection
        conn.close()



    def show_data():

        # creat detabase or connect to
        conn = sqlite3.connect('pension.db')
        # creat corsor
        c = conn.cursor()

        c.execute("SELECT *, oid FROM pension")

        records = c.fetchall()
        print_records = ""
        #for record in records:
            #print_records += str(record[0]) + " " + str(record[1]) + " " + " " + "\t" + str(record[6]) + "\n"

        show_data_label = Label(police_details, text=records)
        show_data_label.grid(row=14, column=0, columnspan=2)



        # commit Changes
        conn.commit()
        # close Connection
        conn.close()

    def delete():
        # creat detabase or connect to
        conn = sqlite3.connect('pension.db')
        # creat corsor
        c = conn.cursor()

        # delete record
        c.execute("DELETE from pension WHERE oid=" + select_id_entry.get())

        # commit Changes
        conn.commit()
        # close Connection
        conn.close()

    def delete_all_data():
        # creat detabase or connect to
        conn = sqlite3.connect('pension.db')
        # creat corsor
        c = conn.cursor()

        # delete record
        c.execute("DELETE from pension")

        # commit Changes
        conn.commit()
        # close Connection
        conn.close()

    show_data_btn = Button(police_details, text="הראה נתונים", command=show_data)
    show_data_btn.grid(row=11, column=1, pady=10, padx=10, ipadx=30)
    save_btn = Button(police_details, text = "שמור", command = save_details)
    save_btn.grid(row = 11, column = 0, ipadx = 70)
    delete_btn = Button(police_details, text = "מחק נתון לפי מפתח", command = delete)
    delete_btn.grid(row = 13, column = 1, columnspan = 2)
    delete_btn = Button(police_details, text="מחק כל נתונים", command=delete_all_data)
    delete_btn.grid(row=13, column=0, columnspan=2)


    records_name = [("management_Fee","דמי ניהול"), ("monthly_payment","משכורת חודשית"), ("age" ,"גיל נוכחי"), ("police_open_date","תאריך פתיחת פוליסה")
        ,("compensation","פיצויים"), ("eccrisis_employee","הפרשות עובד"), ("eccrisis_employer","הפרות מעביד"), ("factor","מקדם"),  ("current_balance", "יתרה נוכחית")]
    n = 2
    for record, record_name in records_name:
        record = Label(police_details, text = record_name)
        record.grid(row = n, column = 1, padx = 10, sticky = E)
        n+=1

    '''
    management_Fee = Label(police_details, text="דמי ניהול")
    management_Fee.grid(row = 2, column = 1, sticky = E)
    monthly_payment = Label(police_details, text="משכורת חודשית")
    monthly_payment.grid(row=3, column=1, sticky = E)
    age = Label(police_details, text="גיל נוכחי")
    age.grid(row=4, column=1, sticky = E)
    police_open_date = Label(police_details, text="תאריך פתיחת פוליסה")
    police_open_date.grid(row=5, column=1, sticky = E)
    compensation = Label(police_details, text="פיצויים")
    compensation.grid(row=6, column=1, sticky = E)
    eccrisis_employee = Label(police_details, text="הפרשות עובד")
    eccrisis_employee.grid(row=7, column=1, sticky = E)
    eccrisis_employer = Label(police_details, text="הפרות מעביד")
    eccrisis_employer.grid(row=8, column=1, sticky = E)
    factor = Label(police_details, text="מקדם")
    factor.grid(row=9, column=1, sticky = E)
    current_balance = Label(police_details, text="יתרה נוכחית")
    current_balance.grid(row=10, column=1, sticky=E)
    '''
    select_id = Label(police_details, text="בחר מס' מפתח")
    select_id.grid(row=12, column=1, sticky=E)
    #create entery boxes
    management_Fee_entry = Entry(police_details, width = 30)
    management_Fee_entry.grid(row =2 , column = 0,padx = 10, pady = 5)
    monthly_payment_entry = Entry(police_details, width = 30)
    monthly_payment_entry.grid(row =3 , column = 0, pady = 5)
    age_entry = Entry(police_details, width = 30)
    age_entry.grid(row =4 , column = 0, pady = 5)
    police_open_date_entry = Entry(police_details, width = 30)
    police_open_date_entry.grid(row =5 , column = 0, pady = 5)
    compensation_entry = Entry(police_details, width = 30)
    compensation_entry.grid(row =6 , column = 0, pady = 5)
    eccrisis_employee_entry = Entry(police_details, width = 30)
    eccrisis_employee_entry.grid(row =7 , column = 0, pady = 5)
    eccrisis_employer_entry = Entry(police_details, width=30)
    eccrisis_employer_entry.grid(row=8, column=0, pady = 5)
    factor_entry = Entry(police_details, width=30)
    factor_entry.grid(row=9, column=0, pady = 5)
    current_balance_entry = Entry(police_details, width=30)
    current_balance_entry.grid(row=10, column=0)
    select_id_entry = Entry(police_details, width=30)
    select_id_entry.grid(row=12, column=0)


#my_label = Label(police_details, image=my_image).pack()
    #bt2 = Button(top, text="close window", command=police_details.destroy).pack()


myPension = Button(root, text = 'חישוב פנסיה עתידית', command = police_details)
myPension.pack()




# commit Changes
conn.commit()
# close Connection
conn.close()


root.mainloop()