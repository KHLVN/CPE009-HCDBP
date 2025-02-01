import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
import ttkbootstrap as ttk

register_window = tkinter.Tk()
register_window.title("Health Registration Form")
register_window.resizable(False, False)
register_window.minsize(width=500, height=300)

#Database

class Mainframe:

    def __init__(self, frame):

        frame = tkinter.Frame(register_window)
        frame.pack()

        self.user_info_frame = ttk.LabelFrame(frame, text="Resident Information")
        self.user_info_frame.grid(row= 0, column= 0, sticky="news", padx=10, pady=5)

        self.first_name_label = tkinter.Label(self.user_info_frame, text="First Name")
        self.first_name_label.grid(row=0, column=0)
        self.last_name_label = tkinter.Label(self.user_info_frame, text="Last Name")
        self.last_name_label.grid(row=0, column=1)

        self.first_name_entry = ttk.Entry(self.user_info_frame, bootstyle="dark")
        self.last_name_entry = ttk.Entry(self.user_info_frame, bootstyle="dark")
        self.first_name_entry.grid(row=1, column=0)
        self.last_name_entry.grid(row=1, column=1)

        self.gender_label = tkinter.Label(self.user_info_frame, text="Gender")
        self.gender_label.grid(row=0, column=2)

        self.gender_var = tkinter.StringVar(value="Undefined")
        self.gender_radio_button = ttk.Radiobutton(self.user_info_frame, text = "Male", value = "Male", variable=self.gender_var, bootstyle="dark").grid(row=1, column=2)
        self.gender_radio_button2 = ttk.Radiobutton(self.user_info_frame, text="Female", value = "Female", variable=self.gender_var, bootstyle="dark").grid(row=1, column=3)

        self.age_label = tkinter.Label(self.user_info_frame, text="Age")
        self.age_entry = ttk.Spinbox(self.user_info_frame, bootstyle="dark", from_=1, to=100, width=16)
        self.age_label.grid(row=2, column=0)
        self.age_entry.grid(row=3, column=0, sticky="we")

        self.contact_number_label = tkinter.Label(self.user_info_frame, text="Contact Number")
        self.contact_number_entry = ttk.Entry(self.user_info_frame, bootstyle="dark")
        self.contact_number_label.grid(row=2 , column= 1)
        self.contact_number_entry.grid(row=3, column= 1, sticky="news")

        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        #Address
        self.address_frame = ttk.LabelFrame(frame, text="Address")
        self.address_frame.grid(row=1, column=0, sticky="news", padx=10, pady=5)

        self.address_label = tkinter.Label(self.address_frame, text="Street, Building, House No.")
        self.address_entry = ttk.Entry(self.address_frame, width=46, bootstyle="dark")
        self.address_label.grid(row=0, column=0)
        self.address_entry.grid(row=1, column=0, pady=5)

        self.district_label = tkinter.Label(self.address_frame, text="Municipality / District")
        self.district_entry = ttk.Combobox(self.address_frame, values=["Barangay Uno", "Barangay Dos", "Barangay Tres", "Barangay Quatro"], width=30, bootstyle="dark", state="readonly")
        self.district_label.grid(row=0, column=1)
        self.district_entry.grid(row=1, column=1, pady=5)

        for widget in self.address_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        #Terms and Conditions
        self.tnc_frame = ttk.LabelFrame(frame, text="Terms and Conditions")
        self.tnc_frame.grid(row=2, column=0, sticky="news", padx=10, pady=5)

        self.accept_tnc_var = tkinter.StringVar(value="Disagree")
        self.tnc_checkbox = ttk.Checkbutton(self.tnc_frame, text="By checking this button, you agree to our User Terms and Conditions",
                                        variable=self.accept_tnc_var, bootstyle="dark", onvalue="Agree", offvalue="Disagree")
        self.tnc_checkbox.grid(row=0,column=0, padx=5, pady=5)

        #Register Button
        self.button = ttk.Button(frame, text="Register", bootstyle="dark", command=lambda: [self.register_data(), self.fill_up_data()])
        self.button.grid(row=3, column=0, sticky="news", padx=10, pady=5)

    def fill_up_data(self):
        agree = self.accept_tnc_var.get()
        firstname = self.first_name_entry.get()
        lastname = self.last_name_entry.get()
        age = self.age_entry.get()
        contact_number = self.contact_number_entry.get()
        address = self.address_entry.get()
        district = self.district_entry.get()
        gender = self.gender_var.get()

        if agree == "Agree" and firstname and lastname and age and address and district and gender!="Undefined":
            
            if contact_number.isdigit():
                import form2
                self.register_window.destroy()
            else:
                tkinter.messagebox.showwarning(title= "Error", message= "Invalid Contact Number. Please Try Again")
        else:
            tkinter.messagebox.showwarning(title= "Error", message= "Missing Information Required")

    def register_data(self):
        agree = self.accept_tnc_var.get()
        count = 0

        if agree == "Agree":
            firstname = self.first_name_entry.get()
            lastname = self.last_name_entry.get()
            age = self.age_entry.get()
            contact_number = self.contact_number_entry.get()
            address = self.address_entry.get()
            district = self.district_entry.get()
            gender = self.gender_var.get()

            if firstname and lastname and age and contact_number.isdigit() and address and district and gender!="Undefined":
                print("User Information Successfully Registered")
                #Database Table
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

            else:
                pass

        else:
            tkinter.messagebox.showwarning(title= "Error", message= "You have not agreed to our the Terms and Conditions.")

e = Mainframe(register_window)

register_window.mainloop()