import sqlite3
import tkinter
import ttkbootstrap
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login form")
window.resizable(False, False)
window.geometry('440x300')
window.configure()

def login():

    password = "admin"
    if password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        window.state(newstate='iconic')
        
        def clear_data():
            for item in resident_treeview.get_children():
                resident_treeview.delete(item)

        def query_data():
            conn = sqlite3.connect("userDatabase.db")
            c = conn.cursor()
            c.execute("SELECT * FROM Resident_Data")
            records = c.fetchall()

            global count
            count = 0
            for row in records:
                if count % 2 == 0:
                    resident_treeview.insert("", index='end', iid=count, values=row, tags=('evenrow',))
                else:
                    resident_treeview.insert("", index='end', iid=count, values=row, tags=('oddrow',))
                count += 1

            print(("Table Query Successfull"))
            conn.commit()
            conn.close()

        #CRUD
        def add_data():

            firstname = fn_entry.get()
            lastname = ln_entry.get()
            age = age_entry.get()
            gender = gender_entry.get()
            contact_number = contact_entry.get()
            address = address_entry.get()
            district = district_entry.get()

            print("User Information Successfully Registered")

            conn = sqlite3.connect('userDatabase.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Resident_Data
                (firstname TEXT, lastname TEXT, age INT, gender TEXT, contact_number INT, address TEXT, district TEXT)
            '''
            conn.execute(table_create_query)
            #Input Data
            data_input_query = '''INSERT INTO Resident_Data (firstname, lastname, age, gender, contact_number, address, district) VALUES
            (?, ?, ?, ?, ?, ?, ?)'''
            data_input_tuple = (firstname, lastname, age, gender, contact_number, address, district)
            cursor = conn.cursor()
            cursor.execute(data_input_query, data_input_tuple)
            conn.commit()
            conn.close()
            
            import form2

        def remove_data():
            x = resident_treeview.selection()[0]
            resident_treeview.delete(x)

        def update_record():
            conn = sqlite3.connect("userDatabase.db")
            c = conn.cursor()

            firstname = str(fn_entry.get())
            lastname = str(ln_entry.get())
            gender = str(gender_entry.get())
            age = int(age_entry.get())
            contact = int(contact_entry.get())
            address = str(address_entry.get())
            district = str(district_entry.get())

            value = [firstname, firstname, lastname, gender, age, contact, address, district]
            selected = resident_treeview.focus()
            resident_treeview.item(selected, text="", values=value)

            fn_entry.delete(0, tkinter.END)
            ln_entry.delete(0, tkinter.END)
            gender_entry.delete(0, tkinter.END)
            age_entry.delete(0, tkinter.END)
            contact_entry.delete(0, tkinter.END)
            address_entry.delete(0, tkinter.END)
            district_entry.delete(0, tkinter.END)

            data_update_query = '''UPDATE Resident_Data SET firstname= "Jamal", lastname= "Blames", gender= "Male", age= "23", contact_number= "23123124", address= "h", district= "Barangay Uno" WHERE firstname = "Hello";'''

            c.execute(data_update_query, value)
            conn.commit()
            conn.close()

        def save_data():
            conn = sqlite3.connect("userDatabase.db")
            save_prompt = messagebox.askyesno(title="Database", message="Save all data changes?")
            if save_prompt:
                messagebox.showinfo(title="Save Database", message="Database saved successfully.")
                print("Data saved successfully")
                conn.commit()
                conn.close()
            else:
                conn.close()

        def exit_prog():
            exit_prompt = messagebox.askyesno(title="Exit Program", message="Do you want to exit the Program?")
            if exit_prompt:
                main_window.destroy()
            
        def health_history():
            health_window = tkinter.Toplevel()
            health_window.title("Health History Treeview")
            health_window.resizable(False, False)

            health_frame = ttk.Frame(health_window)
            health_frame.pack()

            columns = ("Back Pain", "Headaches", "Surgery", "Currently Prescribed Med", "Course of Medication", "COVID", "Diabetes", "Respiratory Problems", "Others")

            name_treeview = ttk.Treeview(health_frame, columns=("First Name", "Last Name"), show="headings", bootstyle="dark", height=20)
            name_treeview.column("First Name", width=50, anchor=tkinter.CENTER)
            name_treeview.column("Last Name", width=50, anchor=tkinter.CENTER)
            name_treeview.heading("First Name", text="Name")
            name_treeview.heading("Last Name", text="Surname")
            name_treeview.grid(row=0, column=0, pady=5)

            health_treeview = ttk.Treeview(health_frame, columns=columns, show="headings", bootstyle="dark", height=20)
            health_treeview.column("Back Pain", width=70, anchor=tkinter.CENTER)
            health_treeview.column("Headaches", width=80, anchor=tkinter.CENTER)
            health_treeview.column("Surgery", width=60, anchor=tkinter.CENTER)
            health_treeview.column("Currently Prescribed Med", width=150, anchor=tkinter.CENTER)
            health_treeview.column("Course of Medication", width=130, anchor=tkinter.CENTER)
            health_treeview.column("COVID", width=60, anchor=tkinter.CENTER)
            health_treeview.column("Diabetes", width=70, anchor=tkinter.CENTER)
            health_treeview.column("Respiratory Problems", width=120, anchor=tkinter.CENTER)
            health_treeview.column("Others", width=70, anchor=tkinter.CENTER)

            health_treeview.heading("Back Pain", text="Back Pain")
            health_treeview.heading("Headaches", text="Headaches")
            health_treeview.heading("Surgery", text="Surgery")
            health_treeview.heading("Currently Prescribed Med", text="Currently Prescribed Med")
            health_treeview.heading("Course of Medication", text="Course of Medication")
            health_treeview.heading("COVID", text="COVID")
            health_treeview.heading("Diabetes", text="Diabetes")
            health_treeview.heading("Respiratory Problems", text="Respiratory Problems")
            health_treeview.heading("Others", text="Others")
            health_treeview.grid(row=0, column=1, padx=0, pady=5)

            tree_scroll = ttk.Scrollbar(health_frame, bootstyle="round-dark")
            tree_scroll.grid(row=0, column=2, sticky="news")
            tree_scroll.config(command=lambda: (health_treeview.yview, name_treeview.yview))

            health_treeview.tag_configure('oddrow', background="white")
            health_treeview.tag_configure('evenrow', background="lightgray")

            name_treeview.tag_configure('oddrow', background="white")
            name_treeview.tag_configure('evenrow', background="lightgray")
            
            def query_health_data():
                conn = sqlite3.connect("userDatabase.db")
                c = conn.cursor()
                c2 = conn.cursor()
                health_alter_query = '''CREATE TABLE IF NOT EXISTS Resident_Data
                                        (healthq1 TEXT, healthq2 TEXT, healthq3 TEXT, healthq4 TEXT, healthq5 TEXT, healthq6 TEXT, healthq7 TEXT, healthq8 TEXT, healthq9entry TEXT, firstname TEXT)'''
                conn.execute(health_alter_query)


                c.execute('''SELECT * FROM Health_Data''')
                c2.execute('''SELECT firstname, lastname FROM Resident_Data''')
                records = c.fetchall()
                records2 = c2.fetchall()

                global count
                count = 0
                for row in records:
                    if count % 2 == 0:
                        health_treeview.insert("", index='end', iid=count, values=row, tags=('evenrow',))
                    else:
                        health_treeview.insert("", index='end', iid=count, values=row, tags=('oddrow',)) 
                    count += 1
                
                for row in records2:
                    if count % 2 == 0:
                        name_treeview.insert("", index="end", iid=count, values=row, tags=('evenrow',))
                    else:
                        name_treeview.insert("", index="end", iid=count, values=row, tags=('oddrow',))
                    count += 1

                print(("Table Query Successfull"))
                conn.commit()
                conn.close()
            
            query_health_data()

        #Frame 1
        main_window = tkinter.Toplevel()
        main_window.title("Database Application")
        main_window.resizable(False, False)

        main_frame = ttk.Frame(main_window)
        main_frame.pack()

        data_label = ttk.Label(main_frame, text="RESIDENT RECORDS", bootstyle="dark", font={'Calibri', 50, 'bold'})
        data_label.grid(row=0, column=0, pady=5, sticky="ns")

        #Treeview

        columns=("First Name", "Last Name", "Age", "Gender", "Contact Number", "Address", "District")
        resident_treeview = ttk.Treeview(main_frame, columns=columns, show="headings", bootstyle="dark", height=20)

        #Treeview Columns
        resident_treeview.column("First Name", width=100)
        resident_treeview.column("Last Name", width=100)
        resident_treeview.column("Age", width=50)
        resident_treeview.column("Gender", width=100)
        resident_treeview.column("Contact Number", width=130)
        resident_treeview.column("Address", width=200)
        resident_treeview.column("District", width=100)

        resident_treeview.heading("First Name", text="First Name")
        resident_treeview.heading("Last Name", text="Last Name")
        resident_treeview.heading("Age", text="Age")
        resident_treeview.heading("Gender", text="Gender")
        resident_treeview.heading("Contact Number", text="Contact Number")
        resident_treeview.heading("Address", text="Address")
        resident_treeview.heading("District", text="District")
        resident_treeview.grid(row=1, column=0, sticky="news", padx=10, pady=10)

        resident_treeview.tag_configure('oddrow', background="white")
        resident_treeview.tag_configure('evenrow', background="lightgray")

        scrollbar = ttk.Scrollbar(main_frame, orient=tkinter.VERTICAL, command=resident_treeview.yview, bootstyle="round-dark")
        resident_treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky="ns")

        #Entry Frame
        entry_frame = ttk.LabelFrame(main_frame, text="Update Records", bootstyle="dark")
        entry_frame.grid(row=2, column=0, sticky="news", padx=10, pady=5)
            
        fn_label = ttk.Label(entry_frame, text="First Name")
        fn_label.grid(row=0, column=0)
        fn_entry = ttk.Entry(entry_frame)
        fn_entry.grid(row=1, column=0)

        ln_label = ttk.Label(entry_frame, text="Last Name")
        ln_label.grid(row=0, column=1)
        ln_entry = ttk.Entry(entry_frame)
        ln_entry.grid(row=1, column=1)

        gender_label = ttk.Label(entry_frame, text="Gender")
        gender_label.grid(row=0, column=2)
        gender_entry = ttk.Combobox(entry_frame, values=["", "Male", "Female"], state="readonly")
        gender_entry.grid(row=1, column=2)

        age_label = ttk.Label(entry_frame, text="Age")
        age_entry = ttk.Spinbox(entry_frame, from_=1, to=100, width=5)
        age_label.grid(row=0, column=3)
        age_entry.grid(row=1, column=3)

        contact_label = ttk.Label(entry_frame, text="Contact Number")
        contact_entry = ttk.Entry(entry_frame)
        contact_label.grid(row=0, column=4)
        contact_entry.grid(row=1, column=4)

        address_label = ttk.Label(entry_frame, text="Address")
        address_entry = ttk.Entry(entry_frame, width=45)
        address_label.grid(row=0, column=5)
        address_entry.grid(row=1, column=5)

        district_label = ttk.Label(entry_frame, text="District")
        district_entry = ttk.Combobox(entry_frame, values=["", "Barangay Uno", "Barangay Dos", "Barangay Tres", "Barangay Quatro"], state="readonly")
        district_label.grid(row=0, column=6)
        district_entry.grid(row=1, column=6)

        for widget in entry_frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

        for widget in entry_frame.winfo_children():
            widget.configure(bootstyle="dark")

        #Buttons Frame
        button_frame = ttk.LabelFrame(main_frame, text="Commands", bootstyle="dark")
        button_frame.grid(row=3, column=0, sticky="news", padx=10, pady=10)

        add_button = ttk.Button(button_frame, text="Add Data", bootstyle="dark", command=lambda: add_data(), width=20)
        add_button.grid(row=0, column=0, sticky="news")

        delete_button = ttk.Button(button_frame, text="Delete Row", bootstyle="dark", command=lambda: remove_data(), width=20)
        delete_button.grid(row=0, column=1, sticky="news")

        update_button = ttk.Button(button_frame, text="Update Row", bootstyle="dark", command=lambda: update_record(), width=20)
        update_button.grid(row=0, column=2, sticky="news")

        save_button = ttk.Button(button_frame, text="Save Database", bootstyle="dark", command=lambda: save_data(), width=20)
        save_button.grid(row=0, column=3, sticky="news")

        health_button = ttk.Button(button_frame, text="Health History", bootstyle="dark", command= lambda: health_history(), width=20)
        health_button.grid(row=0, column=4, sticky="news")

        exit_button = ttk.Button(button_frame, text="Exit Database", bootstyle="dark", command=lambda: exit_prog(), width=20)
        exit_button.grid(row=0, column=8, sticky="news")

        for widget in button_frame.winfo_children():
            widget.grid_configure(padx=5, pady=10)

        query_data()

        main_window.mainloop()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tkinter.Frame()

login_label = ttk.Label(frame, text="Database Login", font={40})
login_label.grid(row=0, column=1, pady=40)

password_label = ttk.Label(frame, text="Enter Access Key")
password_label.grid(row=1, column=1, padx= 5, pady=5)

password_entry = ttk.Entry(frame, show="*", width=40, bootstyle="dark")
password_entry.grid(row=2, column=1, sticky="news", pady=5)

login_button = ttk.Button(frame, text="Login", command=login, width=40, bootstyle="dark")
login_button.grid(row=3, column=1, sticky="news", pady=5)

frame.pack()

window.mainloop()