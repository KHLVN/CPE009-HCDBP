import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
import ttkbootstrap as ttk

def disable_event():
    tkinter.messagebox.showwarning(title= "Error", message= "Please Fill-up the form.")

fillup_window = Toplevel()
fillup_window.title("Health History Check-up")
fillup_window.protocol("WM_DELETE_WINDOW", disable_event)
fillup_window.minsize(width=350, height=400)
fillup_window.resizable(False, False)

class Mainframe1:
    def __init__(self, frame):
        
        frame2 = tkinter.Frame(fillup_window)
        frame2.pack()

        self.health_history_frame = ttk.LabelFrame(frame2, text="Have you experienced any of these?")
        self.health_history_frame.grid(row= 0, column= 0, sticky="news", padx=10, pady=5)

        #R1
        self.health_q1 = ttk.Label(self.health_history_frame, text="Back/spinal pain?")
        self.health_q1.grid(row=0, column=0, sticky="w")
        self.health_q1_var = StringVar(value="null")
        self.health_q1_radiobutton1 = ttk.Radiobutton(self.health_history_frame, text = "Yes", value = "Yes", variable= self.health_q1_var, bootstyle="dark").grid(row=0, column=2, sticky="news")
        self.health_q1_radiobutton2 = ttk.Radiobutton(self.health_history_frame, text = "No", value = "No", variable= self.health_q1_var, bootstyle="dark").grid(row=0, column=3, sticky="news")

        #R2
        self.health_q2 = ttk.Label(self.health_history_frame, text="Headaches or Migraines?")
        self.health_q2.grid(row=1, column=0, sticky="w")
        self.health_q2_var = StringVar(value="null")
        self.health_q2_radiobutton1 = ttk.Radiobutton(self.health_history_frame, text = "Yes", value = "Yes", variable= self.health_q2_var, bootstyle="dark").grid(row=1, column=2, sticky="news")
        self.health_q2_radiobutton2 = ttk.Radiobutton(self.health_history_frame, text = "No", value = "No", variable= self.health_q2_var, bootstyle="dark").grid(row=1, column=3, sticky="news")

        #R3
        self.health_q3 = ttk.Label(self.health_history_frame, text="Surgery?")
        self.health_q3.grid(row=2, column=0, sticky="w")
        self.health_q3_var = StringVar(value="null")
        self.health_q3_radiobutton1 = ttk.Radiobutton(self.health_history_frame, text = "Yes", value = "Yes", variable= self.health_q3_var, bootstyle="dark").grid(row=2, column=2, sticky="news")
        self.health_q3_radiobutton2 = ttk.Radiobutton(self.health_history_frame, text = "No", value = "No", variable= self.health_q3_var, bootstyle="dark").grid(row=2, column=3, sticky="news")

        #R4
        self.health_q4 = ttk.Label(self.health_history_frame, text="Currently prescribed medication?")
        self.health_q4.grid(row=3, column=0, sticky="w")
        self.health_q4_var = StringVar(value="null")
        self.health_q4_radiobutton1 = ttk.Radiobutton(self.health_history_frame, text = "Yes", value = "Yes", variable= self.health_q4_var, bootstyle="dark").grid(row=3, column=2, sticky="news")
        self.health_q4_radiobutton2 = ttk.Radiobutton(self.health_history_frame, text = "No", value = "No", variable= self.health_q4_var, bootstyle="dark").grid(row=3, column=3, sticky="news")

        #R5
        self.health_q5 = ttk.Label(self.health_history_frame, text="finished a course of medication?")
        self.health_q5.grid(row=4, column=0, sticky="w")
        self.health_q5_var = StringVar(value="null")
        self.health_q5_radiobutton1 = ttk.Radiobutton(self.health_history_frame, text = "Yes", value = "Yes", variable= self.health_q5_var, bootstyle="dark").grid(row=4, column=2, sticky="news")
        self.health_q5_radiobutton2 = ttk.Radiobutton(self.health_history_frame, text = "No", value = "No", variable= self.health_q5_var, bootstyle="dark").grid(row=4, column=3, sticky="news")

        #R6
        self.health_q6 = ttk.Label(self.health_history_frame, text="Infected by SARS-COV 2?")
        self.health_q6.grid(row=5, column=0, sticky="w")
        self.health_q6_var = StringVar(value="null")
        self.health_q6_radiobutton1 = ttk.Radiobutton(self.health_history_frame, text = "Yes", value = "Yes", variable= self.health_q6_var, bootstyle="dark").grid(row=5, column=2, sticky="news")
        self.health_q6_radiobutton2 = ttk.Radiobutton(self.health_history_frame, text = "No", value = "No", variable= self.health_q6_var, bootstyle="dark").grid(row=5, column=3, sticky="news")

        #R7
        self.health_q7 = ttk.Label(self.health_history_frame, text="Diabetes?")
        self.health_q7.grid(row=6, column=0, sticky="w")
        self.health_q7_var = StringVar(value="null")
        self.health_q7_radiobutton1 = ttk.Radiobutton(self.health_history_frame, text = "Yes", value = "Yes", variable= self.health_q7_var, bootstyle="dark").grid(row=6, column=2, sticky="news")
        self.health_q7_radiobutton2 = ttk.Radiobutton(self.health_history_frame, text = "No", value = "No", variable= self.health_q7_var, bootstyle="dark").grid(row=6, column=3, sticky="news")

        #R8
        self.health_q8 = ttk.Label(self.health_history_frame, text="Respiratory problems?")
        self.health_q8.grid(row=7, column=0, sticky="w")
        self.health_q8_var = StringVar(value="null")
        self.health_q8_radiobutton1 = ttk.Radiobutton(self.health_history_frame, text = "Yes", value = "Yes", variable= self.health_q8_var, bootstyle="dark").grid(row=7, column=2, sticky="news")
        self.health_q8_radiobutton2 = ttk.Radiobutton(self.health_history_frame, text = "No", value = "No", variable= self.health_q8_var, bootstyle="dark").grid(row=7, column=3, sticky="news")

        #R9 w/ Entry and Frame
        self.q9entry_frame = ttk.LabelFrame(frame2, text="Follow-up question, type N/A if Not Applicable")
        self.q9entry_frame.grid(row=1, column=0, sticky="news", padx=10, pady=5)

        self.health_q9 = ttk.Label(self.q9entry_frame, text="Any other health-concerning reasons?")
        self.health_q9.grid(row=8, column=0, sticky="ws", padx=10, pady=5)
        self.health_q9_entry = ttk.Entry(self.q9entry_frame, bootstyle="dark", width=50)
        self.health_q9_entry.grid(row=9, column=0, padx=10, pady=10)

        #Button
        self.button = ttk.Button(frame2, text="Submit", bootstyle="dark", command=lambda: [self.get_data(), self.submit_data()])
        self.button.grid(row=2, column=0, sticky="news", padx=10, pady=5)

        for widget in self.health_history_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    def submit_data(self):
        healthq1 = self.health_q1_var.get()
        healthq2 = self.health_q2_var.get()
        healthq3 = self.health_q3_var.get()
        healthq4 = self.health_q4_var.get()
        healthq5 = self.health_q5_var.get()
        healthq6 = self.health_q6_var.get()
        healthq7 = self.health_q7_var.get()
        healthq8 = self.health_q8_var.get()
        #Entry
        healthq9entry = self.health_q9_entry.get()
        
        if healthq1 != 2 and healthq2 != 2 and healthq3 != 2 and healthq4 != 2 and healthq5 != 2 and healthq6 != 2 and healthq7 != 2 and healthq8 != 2 and healthq9entry != "":
            tkinter.messagebox.showinfo(title= "Form Submitted", message= "You have successfully registered your information")
            fillup_window.destroy()
            exit()
        else:
            tkinter.messagebox.showwarning(title= "Error", message= "Missing Information Required")

    def get_data(self):
        healthq1 = self.health_q1_var.get()
        healthq2 = self.health_q2_var.get()
        healthq3 = self.health_q3_var.get()
        healthq4 = self.health_q4_var.get()
        healthq5 = self.health_q5_var.get()
        healthq6 = self.health_q6_var.get()
        healthq7 = self.health_q7_var.get()
        healthq8 = self.health_q8_var.get()
        healthq9entry = self.health_q9_entry.get()
        
        if healthq1 and healthq2 and healthq3 and healthq4 and healthq5 and healthq6 and healthq7 and healthq8 and healthq9entry:
            print("Health Info Successfully Saved")
            conn = sqlite3.connect('userDatabase.db')
            healthtable_create_query = '''CREATE TABLE IF NOT EXISTS Resident_Data
                (healthq1 TEXT, healthq2 TEXT, healthq3 TEXT, healthq4 TEXT, healthq5 TEXT, healthq6 TEXT, healthq7 TEXT, healthq8 TEXT, healthq9entry TEXT)
            '''
            conn.execute(healthtable_create_query)

            healthdata_input_query = '''INSERT INTO Health_Data (healthq1, healthq2, healthq3, healthq4, healthq5, healthq6, healthq7, healthq8, healthq9entry) VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            healthdata_input_tuple = (healthq1, healthq2, healthq3, healthq4, healthq5, healthq6, healthq7, healthq8, healthq9entry)
            cursor = conn.cursor()
            cursor.execute(healthdata_input_query, healthdata_input_tuple)
            conn.commit()
            conn.close()

        else:
            pass

e = Mainframe1(fillup_window)

fillup_window.mainloop()