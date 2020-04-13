from tkinter import *
from tkinter import messagebox
from db import Database
import datetime
import numpy as np
import numpy_financial as npf
import pandas as pd
from pandas import Series, DataFrame
#from calculation_class import Calculator
#ccc = Calculator
db = Database('pensionDataBase.db')
#ttb = 3
def populate_list():
    data_list.delete(0,END)
    for row in db.fetch():
        data_list.insert(END,row)

def add_client():
    if management_fee.get() == '' or monthly_deposit.get() == '' or client_birth_age.get() == '' or police_creation_date.get() == '' or compensation_precentage.get() == '' or eccrisis_employee.get() == '' or eccrisis_employer.get() == '' or factor.get() == '' or current_balance.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.datev(client_birth_age.get())
    db.insert(management_fee.get(), monthly_deposit.get(), client_birth_age.get(), police_creation_date.get(),
              compensation_precentage.get(), eccrisis_employee.get(), eccrisis_employer.get(), factor.get(),
              current_balance.get())
    #data_list.delete(0,END)
    data_list.insert(END, (management_fee.get(), monthly_deposit.get(), client_birth_age.get(), police_creation_date.get(),
                           compensation_precentage.get(), eccrisis_employee.get(), eccrisis_employer.get(), factor.get(),
                           current_balance.get()))



    clear_text()
    populate_list()

def select_client(event):
    try:
        global selected_item
        index = data_list.curselection()[0]
        selected_item = data_list.get(index)

        management_fee_entry.delete(0, END)
        management_fee_entry.insert(END, selected_item[1])
        monthly_deposit_entry.delete(0, END)
        monthly_deposit_entry.insert(END, selected_item[2])
        client_birth_age_entry.delete(0, END)
        client_birth_age_entry.insert(END, selected_item[3])
        police_creation_date_entry.delete(0, END)
        police_creation_date_entry.insert(END, selected_item[4])
        compensation_precentage_entry.delete(0, END)
        compensation_precentage_entry.insert(END, selected_item[5])
        eccrisis_employee_entry.delete(0, END)
        eccrisis_employee_entry.insert(END, selected_item[6])
        eccrisis_employer_entry.delete(0, END)
        eccrisis_employer_entry.insert(END, selected_item[7])
        factor_entry.delete(0, END)
        factor_entry.insert(END, selected_item[8])
        current_balance_entry.delete(0, END)
        current_balance_entry.insert(END, selected_item[9])

    except IndexError:
        pass


def remove_client():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_client():
    db.update(selected_item[0], management_fee.get(), monthly_deposit.get(), client_birth_age.get(), police_creation_date.get(),
                           compensation_precentage.get(), eccrisis_employee.get(), eccrisis_employer.get(), factor.get(), current_balance.get())
    populate_list()


def clear_text():
    management_fee_entry.delete(0, END)
    monthly_deposit_entry.delete(0, END)
    client_birth_age_entry.delete(0, END)
    police_creation_date_entry.delete(0, END)
    compensation_precentage_entry.delete(0, END)
    eccrisis_employee_entry.delete(0, END)
    eccrisis_employer_entry.delete(0, END)
    factor_entry.delete(0, END)
    current_balance_entry.delete(0, END)


def search():
    get_entry= search_id.get()
    get_entry_data = db.search_c(get_entry)
    search_result_label = Label(app, text = get_id_data[0],font = 'David')
    search_result_label.grid(row =4, column = 3, sticky = E)
def calculate():
    get_entry = search_id.get()
    get_entry_data = db.search_c(get_entry)
    check_class1 = cc.test(get_entry_data)
    print(check_class1)


def show_tablee():
    try:
        global retierement_age_entry
        global client_id
        get_entry = search_id.get()
        get_entry_data = db.search_c(get_entry)
        client_id = get_entry_data[0]
        cal = Tk()
        frame_cal = Frame(cal)
        row_number = 0
        row_number2 = 0
        z = ('id', 'דמי ניהול', 'הפקדה חודשים', 'תאריך לידה', 'תאריך פתיחת פוליסה', 'הפרשות פיצויים', 'הפרשות עובד',
             'הפרשות מעסיק', 'מקדם', 'יתרה נוכחית')
        for i in z:
            m = Label(frame_cal, text=i)
            m.grid(row=0, column=row_number)
            row_number += 1
        for i in client_id:
            r = Label(frame_cal, text=i)
            r.grid(row=1, column=row_number2)
            row_number2 += 1

    except IndexError:
        wrong_input_return = "תעודת זהות {} לא נמצאה, מספר הכנס תעוזת זהות תקין".format(get_entry)
        response = messagebox.showinfo("מספר תעודת זהות שגוי",wrong_input_return)
        Label(app, text=response).pack()




    def calculate_future_value():
        get_retierement_age= float(retierement_age_entry.get())
        client_birth_date = client_id[3]

        #calculate client years to retirement
        date_now = datetime.datetime.now()
        date_now_year = date_now.year
        client_birth_date_dateFormat = datetime.datetime.strptime(client_birth_date, '%d/%m/%Y')
        client_birth_date_dateFormat_year = client_birth_date_dateFormat.year
        client_age = date_now_year - client_birth_date_dateFormat_year
        yeat_to_retirement = get_retierement_age - client_age

        #calculate actual yearly rate
        rate = (5 - float(client_id[1]))/100

        #calculate Future Value
        z = npf.fv(rate, yeat_to_retirement,-float(client_id[2]),-float(client_id[9]))
        z_num = f"{int(z):,d}"
        # Result Label
        print(u"\u20AA")
        result_label = Label(cal, text= u"\u20AA" + " " + z_num, font='David')
        result_label.grid(row=3, column=2, sticky=E, pady=20)

    #frame grid
    frame_cal.grid(row=0,column=0,columnspan = 10)
    #Entry and Label
    retierement_age = IntVar()
    retierement_age_label = Label(cal,text = "גיל פרישה",font = 'David')
    retierement_age_label.grid(row = 2, column = 2, sticky = E,pady = 20)
    retierement_age_entry = Entry(cal, textvariable = retierement_age)
    retierement_age_entry.grid(row=2,column = 1,pady = 20)

    #buttons
    cal_future_pension_btn = Button(cal, text = 'חשב', command = calculate_future_value)
    cal_future_pension_btn.grid(row = 2, column = 0,pady = 20)
    cal.mainloop()





app =Tk()

#Client personal details
frame_personal_details = Frame(app)
frame_personal_details.grid(row=0, column=0,columnspan=1,
                            padx = 30,pady=20)

client_Fname_label = Label(frame_personal_details,text ="שם פרטי")
client_Fname_label.grid(row=0, column=1)
client_Fname = StringVar()
client_Fname_entry = Entry(frame_personal_details, textvariable = client_Fname)
client_Fname_entry.grid(row=0, column = 0)

client_Lname_label = Label(frame_personal_details,text ="שם משפחה")
client_Lname_label.grid(row=1, column=1)
client_Lname = StringVar()
client_Lname_entry = Entry(frame_personal_details, textvariable = client_Lname)
client_Lname_entry.grid(row=1, column = 0)

client_ID_label = Label(frame_personal_details,text ="תעודת זהות")
client_ID_label.grid(row=2, column=1)
client_ID = IntVar()
client_ID_entry = Entry(frame_personal_details, textvariable = client_ID)
client_ID_entry.grid(row=2, column = 0)

#managment fee
management_fee = DoubleVar()
management_fee_label = Label(app, text = 'דמי ניהול', font = 'David', pady = 20)
management_fee_label.grid(row = 2, column = 1, sticky = E)
management_fee_entry = Entry(app, textvariable = management_fee)
management_fee_entry.grid(row=2, column=0)
#monthly deposit
monthly_deposit = IntVar()
monthly_deposit_label = Label(app, text = 'הפקדה חודשית', font = 'David')
monthly_deposit_label.grid(row = 3, column = 1, sticky = E)
monthly_deposit_entry = Entry(app , textvariable = monthly_deposit)
monthly_deposit_entry.grid(row=3, column=0)
#Client birth age
client_birth_age= StringVar()
client_birth_age_label = Label(app, text = 'תאריך לידה', font = 'David')
client_birth_age_label.grid(row =4, column = 1, sticky = E)
client_birth_age_entry = Entry(app , textvariable = client_birth_age)
client_birth_age_entry.grid(row=4, column=0)
client_birth_age_entry.insert(0, 'D/M/YYYY')
#Police creation date
police_creation_date = StringVar()
police_creation_date_label = Label(app, text = 'תאריך פתיחת פוליסה', font = 'David')
police_creation_date_label.grid(row =5, column = 1, sticky = E)
police_creation_date_entry = Entry(app , textvariable = police_creation_date)
police_creation_date_entry.grid(row=5, column=0)
police_creation_date_entry.insert(0, 'D/M/YYYY')
#Compensation precentage
compensation_precentage = IntVar()
compensation_precentage_label = Label(app, text = 'הפרשות פיצויים', font = 'David')
compensation_precentage_label.grid(row =6, column = 1, sticky = E)
compensation_precentage_entry = Entry(app , textvariable = compensation_precentage)
compensation_precentage_entry.grid(row=6, column=0)
#Eccrisis employee
eccrisis_employee = IntVar()
eccrisis_employee_label = Label(app, text = 'הפרשות עובד', font = 'David')
eccrisis_employee_label.grid(row =7, column = 1, sticky = E)
eccrisis_employee_entry = Entry(app , textvariable = eccrisis_employee)
eccrisis_employee_entry.grid(row=7, column=0)
#Eccrisis employer
eccrisis_employer = IntVar()
eccrisis_employer_label = Label(app, text = 'הפרשות מעביד', font = 'David')
eccrisis_employer_label.grid(row =8, column = 1, sticky = E)
eccrisis_employer_entry = Entry(app , textvariable = eccrisis_employer)
eccrisis_employer_entry.grid(row=8, column=0)
#Factor
factor = IntVar()
factor_label = Label(app, text = 'מקדם', font = 'David')
factor_label.grid(row =9, column = 1, sticky = E)
factor_entry = Entry(app , textvariable = factor)
factor_entry.grid(row=9, column=0)
#current balance
'''בעתיד יש לפצל את היתרה להפרשות מעסיק/עובד והפרשות פיצויים'''
current_balance = IntVar()
current_balance_label = Label(app, text = 'יתרה נוכחית', font = 'David')
current_balance_label.grid(row =10, column = 1, sticky = E)
current_balance_entry = Entry(app , textvariable = current_balance)
current_balance_entry.grid(row=10, column=0)
#search ID
search_id = IntVar()
search_id_label = Label(app, text = "חפש לקוח לפי תעודת זהות", font = 'David')
search_id_label.grid(row = 2, column = 4, sticky = E)
search_id_entry = Entry(app, textvariable = search_id)
search_id_entry.grid(row = 2, column = 3)
#


# Buttons
add_btn = Button(app, text='הוסף לקוח', width=12, command=add_client)
add_btn.grid(row=11, column=0, pady=20)

remove_btn = Button(app, text='הסר לקוח', width=12, command=remove_client)
remove_btn.grid(row=11, column=1)

update_btn = Button(app, text='עדכן פרטי לקוח', width=12, command=update_client)
update_btn.grid(row=12, column=0)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=12, column=1)

search_btn = Button(app, text='חפש', width=8, command=search)
search_btn.grid(row=3, column=3)

show_table_btn = Button(app, text='הראה טבלה', width=8, command=show_tablee)
show_table_btn.grid(row=3, column=4)

# Data List (Listbox)
data_list = Listbox(app, height=8, width=50, border=0)
data_list.grid(row=13, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=13, column=3)
# Set scroll to listbox
data_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=data_list.yview)
# Bind select
data_list.bind('<<ListboxSelect>>', select_client)


app.title('נתוני לקוח')
app.geometry('700x500')

# Populate data
populate_list()


app.mainloop()