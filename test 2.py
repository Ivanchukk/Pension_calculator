from tkinter import *

root =Tk()


fields = 'management_Fee', 'monthly_payment', 'age text', 'police_open_date', 'compensation', 'eccrisis_employee', 'eccrisis_employer', 'factor', 'current_balance'

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text = entry[1].get
        print(field, text)

def makeform(root, fields):
    entries  = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries

if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    root.bind('', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Show',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()


root.mainloop()