# Imports ---------------------------------------------------
import tkinter
from tkinter import ttk
from tkinter import messagebox
import openpyxl
import os 



# Functions ---------------------------------------------------
def enter_data():
    accepted = conditions_var.get()
    
    # if terms are accepted
    if accepted == "Accepted":
        # take name data
        fname = fname_entry.get()
        lname = lname_entry.get()   

        # if name is string
        if fname and lname:       
            ntitle = name_title_combo.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            courses = numcourses_spinbox.get()
            semesters = numsemesters_spinbox.get()
            r_status = reg_status.get()


            print("First Name: ", fname, "Last Name: ", lname)
            print("Title: ", ntitle, "Age: ", age, "Nationality: ", nationality)
            print("Registration Status: ", r_status, "# of Courses: ", courses, "# of Semesters: ", semesters)
            print("--------------------------------------------------------")

            # create filepath variable
            # 'D:\Directory\Current Folder\excel-sheet.xlsx
            filepath = r'C:\Users\tahne\OneDrive\Desktop\coding projects\Tkinter Data Entry Form\data.xlsx'

            # if no excel datasheet
            if not os.path.exists(filepath):
                # workbook initialized
                workbook = openpyxl.Workbook()
                # workbook sheet initialized
                sheet = workbook.active
                # create sheet heading 
                headings = ["First Name", 
                           "Last Name", 
                           "Title", 
                           "Age", 
                           "Nationality", 
                           "# Courses", 
                           "# Semesters", 
                           "Registration Status"]
                # save sheet headings
                sheet.append(headings)
                # save workbook
                workbook.save(filepath)
            
            # open data excel workbook
            workbook = openpyxl.load_workbook(filepath)
            # open sheet
            sheet = workbook.active
            # save entered data
            sheet.append([fname, 
                          lname, 
                          ntitle, 
                          age, 
                          nationality, 
                          courses, 
                          semesters, 
                          r_status])
            # save new entry
            workbook.save(filepath)

        else:
            print("Error: First and last name not inputted.")
            print("--------------------------------------------------------")
            messagebox.showwarning("Error","Error. Please enter your first and last name.")


    else:
        print("Error: Terms & Conditions not accepted by user.")
        print("--------------------------------------------------------")
        messagebox.showerror("Error","Error. Please accept the terms & conditions to enter data.")


# Window Initialized ----------------------------------------
window = tkinter.Tk()
window.title("Data Entry Form")
window.geometry("490x430")

# Window Elements
frame = tkinter.Frame(window)
frame.pack()

# 1st Frame [row 0, column 0] 
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

# 1st Frame Elements 
name_title_label = tkinter.Label(user_info_frame, 
                                 text="Title")
name_title_label = name_title_label.grid(row=0, column=0)
name_title_combo = ttk.Combobox(user_info_frame, 
                                values=["", "Mr", "Ms", "Mrs","Dr"])
name_title_combo.grid(row=1, column=0)

fname_label = tkinter.Label(user_info_frame, 
                            text="First Name")
fname_label.grid(row=0, column=1)
fname_entry = tkinter.Entry(user_info_frame)
fname_entry.grid(row=1,column=1)

lname_label = tkinter.Label(user_info_frame, 
                            text="Last Name")
lname_label.grid(row=0, column=2)
lname_entry = tkinter.Entry(user_info_frame)
lname_entry.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, 
                          text="Age")
age_label.grid(row=2, column=0)
age_spinbox = tkinter.Spinbox(user_info_frame, 
                              from_=19, 
                              to=95)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, 
                                  text="Nationality (Continental)")
nationality_label.grid(row=2, column=1)
nationality_combobox = ttk.Combobox(user_info_frame, 
                                    values=['Canadian', 'American', 'European', 'Asian', 'South Asian', 'Other', 'Prefer Not To Say'])
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=7, pady=5)



# 2nd Frame -------------------------------------------------
courses_frame = tkinter.LabelFrame(frame, text="Course Registration")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# 2nd Frame Elements
registered_label = tkinter.Label(courses_frame, 
                                 text="Registration Status")
registered_label.grid(row=0, column=0)
reg_status = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, 
                                       text="Currently Registered",
                                       variable=reg_status,
                                       onvalue="Registered",
                                       offvalue="Not Registered")
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, 
                                 text="# of Completed Courses")
numcourses_label.grid(row=0,column=1)
numcourses_spinbox = ttk.Spinbox(courses_frame, 
                                 from_=0, 
                                 to='infinity')
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, 
                                   text="# of Semesters")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox = ttk.Spinbox(courses_frame, 
                                   from_=0,
                                   to=50)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=7, pady=5)


# 3rd Frame ------------------------------------------------------
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)
conditions_var = tkinter.StringVar(value="Not Accepted")
conditions_checkbox = tkinter.Checkbutton(terms_frame, 
                                          text="I accept the terms and conditions",
                                          variable=conditions_var,
                                          onvalue="Accepted",
                                          offvalue="Not Accepted")
conditions_checkbox.grid(row=0, column=0)


# 4th Frame ------------------------------------------------------
entry_btn = tkinter.Button(frame, text="Enter Data", command=enter_data)
entry_btn.grid(row=3, column=0, sticky="news", padx=20, pady=10)

exit_btn = tkinter.Button(frame, text="Cancel", command=window.destroy)
exit_btn.grid(row=4, column=0, sticky="news", padx=20, pady=10)


# Main ------------------------------------------------------
window.mainloop()