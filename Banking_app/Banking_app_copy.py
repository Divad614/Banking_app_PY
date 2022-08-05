from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import messagebox

# Main Screen
master = Tk()
master.title('David\'s Banking App')
master.geometry("400x500")
master.resizable(False, False)

# Image import
main_img = Image.open('Images/Pig_Pic.png')
main_img = ImageTk.PhotoImage(main_img)

background_image = Image.open('Images/Digital-Transformation-in-Banking-Cover.jpg')
background_image = ImageTk.PhotoImage(background_image)


# Creating Functions
def on_enter(e):
    e.widget['background'] = '#376AB4'


def on_leave(e):
    e.widget['background'] = '#659EDB'


def temp_text_password(e):
    password_entry.delete(0, END)


def temp_text_username(e):
    username_entry.delete(0, END)


def register():
    # Vars
    global register_screen
    global temp_username
    global temp_password
    global temp_name
    global temp_surname
    global temp_age
    global temp_gender
    global notif

    temp_username = StringVar()
    temp_password = StringVar()
    temp_name = StringVar()
    temp_surname = StringVar()
    temp_age = StringVar()

    # Register Screen
    response = messagebox.askquestion("Terms & Conditions", "Click Yes or No to agree to our Terms and Conditions")
    if response == "yes":
        register_screen = Toplevel(master)
        register_screen.title("Register")
        register_screen.transient(master)
        register_screen.geometry("450x400")

        # Frame
        background_frame_register = Frame(register_screen, bg='black')
        Register_title_frame = Frame(register_screen, bg='black', bd=2)
        register_label_frame = Frame(register_screen, bg='black', bd=2)
        register_entry_frame = Frame(register_screen, bg='black', bd=2)
        register_button_frame = Frame(register_screen, bg='black', bd=2)

        # Placing Frames
        background_frame_register.place(relheight=1, relwidth=1)
        Register_title_frame.place(relx=0.5, rely=0.05, relheight=0.1, relwidth=0.8, anchor='n')
        register_label_frame.place(relx=0.1, rely=0.2, relheight=0.6, relwidth=0.3)
        register_entry_frame.place(relx=0.45, rely=0.2, relheight=0.6, relwidth=0.5)
        register_button_frame.place(relx=0.1, rely=0.82, relheight=0.1, relwidth=0.3)

        # Labels
        Label(background_frame_register, image=background_image).place(relwidth=1, relheight=1)
        Label(Register_title_frame, text="Please enter your details below to register:", font=("Calibri", 13),
              bg='#659EDB').place(relwidth=1, relheight=1)
        Label(register_label_frame, text="Username:", font=("Calibri", 12), bg='#659EDB').pack(fill=BOTH, expand=True)
        Label(register_label_frame, text="Password:", font=("Calibri", 12), bg='#659EDB').pack(fill=BOTH, expand=True)
        Label(register_label_frame, text="Name:", font=("Calibri", 12), bg='#659EDB').pack(fill=BOTH, expand=True)
        Label(register_label_frame, text="Surname:", font=("Calibri", 12), bg='#659EDB').pack(fill=BOTH, expand=True)
        Label(register_label_frame, text="Age:", font=("Calibri", 12), bg='#659EDB').pack(fill=BOTH, expand=True)
        Label(register_label_frame, text="Gender:", font=("Calibri", 12), bg='#659EDB').pack(fill=BOTH, expand=True)
        notif = Label(register_label_frame, font=("Calibri", 12))

        # Entries
        Entry(register_entry_frame, textvariable=temp_username, bg='#659EDB').pack(fill=BOTH, expand=True)
        Entry(register_entry_frame, textvariable=temp_password, show='*', bg='#659EDB').pack(fill=BOTH, expand=True)
        Entry(register_entry_frame, textvariable=temp_name, bg='#659EDB').pack(fill=BOTH, expand=True)
        Entry(register_entry_frame, textvariable=temp_surname, bg='#659EDB').pack(fill=BOTH, expand=True)
        Entry(register_entry_frame, textvariable=temp_age, bg='#659EDB').pack(fill=BOTH, expand=True)

        # Gender drop down menu
        options = ["Male", "Female", "Other"]
        temp_gender = StringVar()
        temp_gender.set(options[0])
        gender_option = OptionMenu(register_entry_frame, temp_gender, *options)
        gender_option.config(bg='#659EDB', fg="BLACK", activebackground='#376AB4', activeforeground="BLACK")
        gender_option['menu'].config(bg='#659EDB', fg="BLACK", activebackground="#9EA3AB", activeforeground="black")
        gender_option.pack(fill=BOTH)

        # Buttons
        register_button_1 = Button(register_button_frame, text="Register", command=finish_reg, font=("Calibri", 12),
                                   bg='#659EDB')
        register_button_1.pack(fill=BOTH, expand=True)

        # Binding Buttons
        register_button_1.bind('<Enter>', on_enter)
        register_button_1.bind('<Leave>', on_leave)

    else:
        master.destroy()


def finish_reg():
    # Getting the variables
    username = temp_username.get()
    password = temp_password.get()
    name = temp_name.get()
    surname = temp_surname.get()
    age = temp_age.get()
    gender = temp_gender.get()
    all_accounts = os.listdir()
    running = True

    if username == "" or password == "" or name == "" or surname == "" or age == "" or gender == "":
        messagebox.showerror("Error!", "All fields not filled in *")
        return

        # Checking if account exists
    for name_check in all_accounts:
        if username == name_check:
            messagebox.showerror("Error!", "Account Already exists")
            running = False
            break
        else:
            continue
    if running == True:
        with open(username, "w") as f:
            f.write(username + '\n')
            f.write(password + '\n')
            f.write(name + " " + surname + '\n')
            f.write(age + '\n')
            f.write(gender + '\n')
            f.write('0')

        response = messagebox.showinfo('Success!', 'Successfully made Account!')


def login():
    # Variables
    global temp_login_username
    global temp_login_password
    global login_screen
    global login_notif

    temp_login_username = StringVar()
    temp_login_password = StringVar()

    # Login screen
    login_screen = Toplevel(master)
    login_screen.title("Login")
    login_screen.geometry("350x200")
    login_screen.resizable(False, False)
    login_screen.transient(master)

    # Frame
    background_frame_login = Frame(login_screen, bg='black')
    Login_title_frame = Frame(login_screen, bg='black', bd=2)
    username_frame = Frame(login_screen, bg='black', bd=2)
    password_frame = Frame(login_screen, bg='black', bd=2)
    entry_frame = Frame(login_screen, bg='black', bd=2)
    Login_button_frame = Frame(login_screen, bg='black', bd=2)

    # Place Frame
    Login_title_frame.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=0.2, anchor='n')
    background_frame_login.place(relheight=1, relwidth=1)
    username_frame.place(relx=0.02, rely=0.32, relwidth=0.4, relheight=0.25)
    password_frame.place(relx=0.02, rely=0.57, relwidth=0.4, relheight=0.25)
    entry_frame.place(relx=0.45, rely=0.32, relwidth=0.5, relheight=0.5)
    Login_button_frame.place(relx=0.02, rely=0.82, relheight=0.15, relwidth=0.4)

    # Labels
    Label(background_frame_login, image=background_image).place(relwidth=1, relheight=1)
    Label(Login_title_frame, text="Login to your account:", font=('Calibri', 12), bg='#659EDB').place(relheight=1,
                                                                                                      relwidth=1)
    Label(username_frame, text="Username:", font=('Calibri', 12), bg='#659EDB').place(relheight=1, relwidth=1)
    Label(password_frame, text="Password:", font=('Calibri', 12), bg='#659EDB').place(relheight=1, relwidth=1)

    # Entry
    Entry(entry_frame, textvariable=temp_login_username, bg='#659EDB').place(relheight=0.5, relwidth=1)
    Entry(entry_frame, textvariable=temp_login_password, show='*', bg='#659EDB').place(relheight=0.5, relwidth=1,
                                                                                       rely=0.5)

    # Button
    login_button_1 = Button(Login_button_frame, text='Login', command=login_session, width=15, font=('Calibri', 12),
                            bg='#659EDB')
    login_button_1.place(relwidth=1, relheight=1)

    # Binding Buttons
    login_button_1.bind('<Enter>', on_enter)
    login_button_1.bind('<Leave>', on_leave)


def login_session():
    global login_username
    all_accounts = os.listdir()
    login_username = temp_login_username.get()
    login_password = temp_login_password.get()

    for username in all_accounts:
        if username == login_username:
            file = open(username, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            full_name = file_data[2]

            # Account dashboard
            if login_password == password:
                login_screen.destroy()

                # Creating Dashboard screen
                account_dashboard = Toplevel(master)
                account_dashboard.title("Dashboard")
                account_dashboard.geometry("300x350")

                # Frame
                background_frame_dashboard = Frame(account_dashboard, bg='black')
                dashboard_heading_frame = Frame(account_dashboard, bg='black', bd=2)
                dashboard_button_frame = Frame(account_dashboard, bg='black', bd=5)
                dashboard_subheading_frame = Frame(account_dashboard, bg='black', bd=2)

                # Placing Frames
                background_frame_dashboard.place(relheight=1, relwidth=1)
                dashboard_heading_frame.place(relx=0.5, rely=0.05, relwidth=0.6, relheight=0.1, anchor='n')
                dashboard_subheading_frame.place(relx=0.5, rely=0.16, relheight=0.1, relwidth=0.7, anchor='n')
                dashboard_button_frame.place(relx=0.5, rely=0.3, relwidth=0.8, relheight=0.6, anchor='n')

                # Labels

                Label(background_frame_dashboard, image=background_image).place(relwidth=1, relheight=1)
                Label(dashboard_heading_frame, text="ACCOUNT DASHBOARD", font=("Calibri", 12), bg='#659EDB').pack(
                    fill=BOTH, expand=True)
                Label(dashboard_subheading_frame, text="Welcome " + full_name, font=("Calibri", 12), bg='#659EDB').pack(
                    fill=BOTH, expand=True)

                # Establishing Buttons
                personal_details_button = Button(dashboard_button_frame, text="Personal Details", font=("Calibri", 12),
                                                 bg='#659EDB', width=30,
                                                 command=personal_details)
                deposit_button = Button(dashboard_button_frame, text="Deposit", font=("Calibri", 12), bg='#659EDB',
                                        width=30, command=deposit)
                withdraw_button = Button(dashboard_button_frame, text="Withdraw", font=("Calibri", 12), bg='#659EDB',
                                         width=30, command=withdraw)
                pay_button = Button(dashboard_button_frame, text="Pay Beneficiary", font=("Calibri", 12), bg='#659EDB',
                                    width=30, command=pay)

                # Placing Buttons
                personal_details_button.pack(fill=BOTH, expand=True)
                deposit_button.pack(fill=BOTH, expand=True)
                withdraw_button.pack(fill=BOTH, expand=True)
                pay_button.pack(fill=BOTH, expand=True)

                # Binding Buttons
                personal_details_button.bind('<Enter>', on_enter)
                personal_details_button.bind('<Leave>', on_leave)

                deposit_button.bind('<Enter>', on_enter)
                deposit_button.bind('<Leave>', on_leave)

                withdraw_button.bind('<Enter>', on_enter)
                withdraw_button.bind('<Leave>', on_leave)

                pay_button.bind('<Enter>', on_enter)
                pay_button.bind('<Leave>', on_leave)

                return
            else:
                messagebox.showerror("Error!", "Password Incorrect")
                return
    messagebox.showerror("Error!", "No Account Found!")


def pay():
    pass


def deposit():
    # Vars
    global amount
    global deposit_notif
    global current_balance_label

    amount = StringVar()

    # opening file
    file = open(login_username, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[5]

    # Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title("Deposit")
    # Labels
    Label(deposit_screen, text="Deposit", font=("Calibri", 12)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(deposit_screen, text="Current Balance: R" + details_balance, font=("Calibri", 12))
    current_balance_label.grid(row=1, sticky=N, pady=10)
    Label(deposit_screen, text="Amount : ", font=("Calibri", 12)).grid(row=2, sticky=W)
    deposit_notif = Label(deposit_screen, font=("Calibri", 12))
    deposit_notif.grid(row=4, sticky=N, pady=5)

    # Entry
    Entry(deposit_screen, textvariable=amount).grid(row=2, column=1)

    # Button
    Button(deposit_screen, text="Finish", font=("Calibri", 12), command=finish_deposit).grid(row=3, sticky=W, pady=5)


def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(fg="red", text='Amount is Required')
        return
    if float(amount.get()) <= 0:
        deposit_notif.config(text="Negative Currency is not accepted", fg='red')
        return
    file = open(login_username, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[5]
    updated_balance = float(current_balance) + float(amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : R " + str(updated_balance), fg="green")
    deposit_notif.config(text='Balance Updated', fg='green')


def withdraw():
    # Vars
    global details_balance
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()

    # opening file
    file = open(login_username, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[5]

    # Withdraw Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("Withdraw")

    # Labels
    Label(withdraw_screen, text="Withdraw", font=("Calibri", 12)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(withdraw_screen, text="Current Balance: R" + details_balance, font=("Calibri", 12))
    current_balance_label.grid(row=1, sticky=N, pady=10)
    Label(withdraw_screen, text="Amount : ", font=("Calibri", 12)).grid(row=2, sticky=W)
    withdraw_notif = Label(withdraw_screen, font=("Calibri", 12))
    withdraw_notif.grid(row=4, sticky=N, pady=5)

    # Entry
    Entry(withdraw_screen, textvariable=withdraw_amount).grid(row=2, column=1)

    # Button
    Button(withdraw_screen, text="Finish", font=("Calibri", 12), command=finish_withdraw).grid(row=3, sticky=W, pady=5)


def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(fg="red", text='Amount is Required')
        return
    if float(withdraw_amount.get()) <= 0:
        withdraw_notif.config(text="Negative Currency is not accepted", fg='red')
        return
    file = open(login_username, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[5]

    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(text='Insufficient Funds!', fg='red')
        return

    updated_balance = float(current_balance) - float(withdraw_amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : R " + str(updated_balance), fg="green")
    withdraw_notif.config(text='Balance Updated', fg='green')


def personal_details():
    global personal_details_screen
    global login_username
    # Vars
    file = open(login_username, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_username = user_details[0]
    details_full_name = user_details[2]
    details_age = user_details[3]
    details_gender = user_details[4]
    details_balance = user_details[5]

    # Personal Details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title("Personal Details")
    personal_details_screen.geometry("250x350")

    # Establishing Frame
    personal_details_title = Frame(personal_details_screen, bg='black', bd=5)
    personal_details_contents = Frame(personal_details_screen, bg='black', bd=2)
    personal_details_background = Frame(personal_details_screen)
    personal_details_button = Frame(personal_details_screen, bg='black', bd=2)

    # Placing Frames
    personal_details_background.place(relheight=1, relwidth=1)
    personal_details_title.place(relx=0.5, rely=0.05, relwidth=0.6, relheight=0.1, anchor='n')
    personal_details_contents.place(relx=0.5, rely=0.16, relwidth=0.7, relheight=0.7, anchor='n')
    personal_details_button.place(relx=0.1, rely=0.8, relheight=0.1, relwidth=0.1)



    # Labels
    Label(personal_details_background, image=background_image).place(relwidth=1, relheight=1)

    Label(personal_details_title, text="Personal Details", font=("Calibri", 14)).pack(fill=BOTH, expand=True)

    Label(personal_details_contents, text="Username : " + login_username, font=("Calibri", 12)).pack(fill=BOTH, expand=True)

    Label(personal_details_contents, text="Name : " + details_full_name, font=("Calibri", 12)).pack(fill=BOTH, expand=True)

    Label(personal_details_contents, text="Age : " + details_age, font=("Calibri", 12)).pack(fill=BOTH, expand=True)

    Label(personal_details_contents, text="Gender : " + details_gender, font=("Calibri", 12)).pack(fill=BOTH, expand=True)

    Label(personal_details_contents, text="Balance : R" + details_balance, font=("Calibri", 12)).pack(fill=BOTH, expand=True)

    # Establishing Button
    edit_details_button = Button(personal_details_button, text="Edit Profile", font=("Calibri", 12), command=edit_details)

    # Placing Button
    edit_details_button.pack(fill=BOTH, expand=True)

    # Flashing buttons
    edit_details_button.bind('<Enter>', on_enter)
    edit_details_button.bind('<Leave>', on_leave)


def edit_details():
    # global Vars
    global new_username
    global new_password
    global username_entry
    global password_entry
    global notif
    global details_username
    global details_password
    global edit_details_screen

    # Vars
    new_username = StringVar()
    new_password = StringVar()

    # Retrieving Info from File
    with open(login_username, 'r') as f:
        file_data = f.read()
        user_details = file_data.split('\n')
        details_username = user_details[0]
        details_password = user_details[1]

    # Personal details Edit Screen
    edit_details_screen = Toplevel(master)
    edit_details_screen.title("Edit Details")

    # Label
    Label(edit_details_screen, text="Personal Details:", font=("Calibri", 14)).grid(row=0, sticky=N, pady=10)
    Label(edit_details_screen, text="Username : " + details_username, font=("Calibri", 12)).grid(row=1, sticky=W,
                                                                                                 pady=10)
    Label(edit_details_screen, text="Password : " + "*******", font=("Calibri", 12)).grid(row=2, sticky=W, pady=10)
    notif = Label(edit_details_screen, font=("Calibri", 12))
    notif.grid(row=3, column=1, sticky=N, pady=10)

    # Entries
    username_entry = Entry(edit_details_screen, textvariable=new_username, width=25)
    password_entry = Entry(edit_details_screen, textvariable=new_password, width=25)

    # Placing Entries
    username_entry.grid(row=1, column=1, columnspan=2)
    password_entry.grid(row=2, column=1, columnspan=2)

    # Insert into entries
    username_entry.insert(END, "Enter new Name here:", )
    password_entry.insert(END, "Enter new Password here:")

    # Deletes existing text
    username_entry.bind("<FocusIn>", temp_text_username)
    password_entry.bind("<FocusIn>", temp_text_password)

    # Button
    Button(edit_details_screen, text='Save', command=finish_edit_details).grid(row=3, column=0, pady=10, padx=5)


def finish_edit_details():
    global login_username
    # Vars
    all_accounts = os.listdir()
    Taken = True

    # Opening File
    if new_username.get() == "" or new_password.get() == "":
        notif.config(fg="red", text="All fields required * ")
        return
    elif new_username.get() == "Enter new Name here:" or new_password.get() == "Enter new Password here:":
        notif.config(fg="red", text="Error please click the entry screen")
        return

    # elif new_username.get() == login_username:
    #     with open(str(login_username), "r") as f:
    #         file_data = f.readlines()
    #
    #     file_data[0] = str(new_username.get()) + '\n'
    #     file_data[1] = str(new_password.get()) + '\n'
    #
    #     with open(str(login_username), "w") as f:
    #         f.writelines(file_data)
    #
    #     notif.config(fg="green", text="Account details appended succesfully!")
    #     return

    else:
        for name_check in all_accounts:
            print(all_accounts)
            print(new_username.get())
            if new_username.get() == name_check:
                # print(name_check)
                notif.config(fg="red", text="Username already taken")
                Taken = False
                break
            else:
                continue

    if Taken == True:
        with open(str(login_username), "r") as f:
            file_data = f.readlines()

        file_data[0] = str(new_username.get()) + '\n'
        file_data[1] = str(new_password.get()) + '\n'

        with open(str(new_username.get()), 'w') as f:
            f.writelines(file_data)
            os.remove(login_username)
            login_username = new_username.get()

        personal_details_screen.destroy()
        notif.config(fg="green", text="Account details appended succesfully!")


"""
Creating Main Screen
"""
# Frame
background_frame = Frame(master)
title_frame = Frame(master, bg='black', bd=2)
subtitle_frame = Frame(master, bg='black', bd=3)
register_frame = Frame(master, bg='black', bd=5)
login_frame = Frame(master, bg='black', bd=5)
pig_pic_frame = Frame(master, bg='black', bd=2)

# Placing Frames
background_frame.place(relheight=1, relwidth=1)
title_frame.place(relx=0.5, rely=0.05, relwidth=0.6, relheight=0.06, anchor='n')
subtitle_frame.place(relx=0.5, rely=0.12, relwidth=0.6, relheight=0.06, anchor='n')
register_frame.place(relx=0.5, rely=0.7, relwidth=0.5, relheight=0.1, anchor='n')
login_frame.place(relx=0.5, rely=0.81, relwidth=0.5, relheight=0.1, anchor='n')
pig_pic_frame.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.4, anchor='n')

# Transparent Background


# Labels
Label(title_frame, text="Lothian Trust Banking Beta", font=('Calibri', 14, 'bold'), bg='#659EDB').place(relwidth=1,
                                                                                                        relheight=1)
Label(subtitle_frame, text="Banking has never felt easier!", bg='#659EDB', font=('Calibri', 12, 'bold')).place(
    relwidth=1, relheight=1)
Label(pig_pic_frame, image=main_img, bg='#062C63').place(relwidth=1, relheight=1)
Label(background_frame, image=background_image).place(relwidth=1, relheight=1)

# Buttons
register_button = Button(register_frame, text="Register", font=('Calibri', 12), width=20, bg='#659EDB',
                         command=register)
register_button.place(relheight=1, relwidth=1)
login_button = Button(login_frame, text="Login", font=('Calibri', 12), width=20, bg='#659EDB', command=login)
login_button.place(relheight=1, relwidth=1)

# Binding Buttons
login_button.bind('<Enter>', on_enter)
login_button.bind('<Leave>', on_leave)
login_button.bind('')
register_button.bind('<Enter>', on_enter)
register_button.bind('<Leave>', on_leave)

# Running Mainloop
master.mainloop()
