import sqlite3
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import datetime
from tkinter import messagebox


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS pensionDataBase (id INTEGER PRIMARY KEY, management_fee text, monthly_deposit text, "
            "birth_date text, police_creation_date text, compensation text, crisis_employee text, "
            "eccrisis_employer text, factor text, current_balance text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM pensionDataBase")
        rows = self.cur.fetchall()
        return rows
    def search_c(self,id):

        self.cur.execute("SELECT * FROM pensionDataBase WHERE id=?",(id,))
        g = self.cur.fetchall()
        return g

    def show_table(self, management_fee, monthly_deposit, birth_date, police_creation_date, compensation, crisis_employee,
               eccrisis_employer, factor, current_balance):
        ser1 = Series([management_fee, monthly_deposit, birth_date, police_creation_date, compensation, crisis_employee,
               eccrisis_employer, factor, current_balance], index=['דמי ניהול','הפקדה חודשים','תאריך לידה','תאריך פתיחת פוליסה','הפרשות פיצויים','הפרשות עובד','הפרשות מעסיק','מקדם','יתרה נוכחית'])
        return ser1
    def insert (self, management_fee, monthly_deposit, birth_date, police_creation_date, compensation, crisis_employee, eccrisis_employer, factor, current_balance):
        self.cur.execute("INSERT INTO pensionDataBase VALUES (NULL, ?,?,?,?,?,?,?,?,?)",
                         (management_fee, monthly_deposit, birth_date, police_creation_date, compensation, crisis_employee, eccrisis_employer, factor, current_balance))

        self.conn.commit()

    def datev(self,date):
        try:
            datetime.datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            #raise ValueError("Incorrect data format, should be DD/MM/YYY")
            response = messagebox.showinfo("תאריך שגוי", "יש להכניס תאריך בפורמט הבא: 30/05/2020")
            Label(app, text=response).pack()

    def remove(self, id):
        self.cur.execute("DELETE FROM pensionDataBase WHERE id=?", (id,))
        self.conn.commit()

    def update(self,id, management_fee, monthly_deposit, birth_date, police_creation_date, compensation, crisis_employee, eccrisis_employer, factor, current_balance):
        self.cur.execute("UPDATE pensionDataBase SET management_fee = ?, monthly_deposit= ?, birth_date= ?, police_creation_date= ?, compensation= ?, crisis_employee= ?, eccrisis_employer= ?, factor= ?, current_balance= ? WHERE id = ?",
                         (management_fee, monthly_deposit, birth_date, police_creation_date, compensation, crisis_employee, eccrisis_employer, factor, current_balance, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#db = Database('pensionDataBase.db')
#db.insert("0.9", "1000", "10/10/2000", "10/10/2015", "8.3", "6","6","240","200000")

