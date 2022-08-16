from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import messagebox
import random

# Main Screen
master = Tk()
master.title('David\'s Banking App')
master.geometry("400x500")
master.resizable(False, False)

# Vars
options_beneficiary = {"": ""}

# Image import
main_img = Image.open('Images/Pig_Pic.png')
main_img = ImageTk.PhotoImage(main_img)

# Background Image import
background_image = Image.open('Images/Digital-Transformation-in-Banking-Cover.jpg')
background_image = ImageTk.PhotoImage(background_image)

# Changing Directory to store Accounts in the Account directory
os.chdir(r"C:\Users\David\PycharmProjects\Banking_app_copy\Banking_app\Accounts")


# Creating Functions
def on_enter(e):
    e.widget['background'] = '#376AB4'


def on_leave(e):
    e.widget['background'] = '#659EDB'


def delete_temp_text(e):
    e.widget.delete(0, END)


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
        register_screen = Toplevel()
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
                                   bg='#659EDB', activebackground="#9EA3AB")
        register_button_1.pack(fill=BOTH, expand=True)

        back_button_register = Button(register_screen, text="<<", command=register_screen.destroy, font=("Calibri", 12),
                                      bg='#659EDB', activebackground="#9EA3AB")

        back_button_register.place(relx=0.03, rely=0.95, relwidth=0.05, relheight=0.05, anchor='n')

        # Binding Buttons
        register_button_1.bind('<Enter>', on_enter)
        register_button_1.bind('<Leave>', on_leave)

    else:
        messagebox.showerror("Terms & Conditions", "Sorry you need to agree to our Terms and Conditions to Register.")


def finish_reg():
    # Getting the variables
    username = temp_username.get()
    password = temp_password.get()
    name = temp_name.get()
    surname = temp_surname.get()
    age = temp_age.get()
    gender = temp_gender.get()
    all_accounts = os.listdir()
    Account_number = random.randrange(10000000, 99999999, 1)
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
            f.write(str(Account_number) + '\n')
            f.write('0')

        response = messagebox.showinfo('Success!', 'Successfully made Account!')
        register_screen.destroy()


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
                            bg='#659EDB', activebackground="#9EA3AB")
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
                                                 command=personal_details, activebackground="#9EA3AB")

                deposit_button = Button(dashboard_button_frame, text="Deposit", font=("Calibri", 12), bg='#659EDB',
                                        width=30, command=deposit, activebackground="#9EA3AB")

                withdraw_button = Button(dashboard_button_frame, text="Withdraw", font=("Calibri", 12), bg='#659EDB',
                                         width=30, command=withdraw, activebackground="#9EA3AB")

                pay_button = Button(dashboard_button_frame, text="Pay Beneficiary", font=("Calibri", 12), bg='#659EDB',
                                    width=30, command=pay, activebackground="#9EA3AB")

                back_button_dashboard = Button(account_dashboard, text="Logout", command=account_dashboard.destroy,
                                               font=("Calibri", 12),
                                               bg='#659EDB', activebackground="#9EA3AB")

                # Placing Buttons
                back_button_dashboard.place(relx=0.03, rely=0.95, relwidth=0.2, relheight=0.07, anchor='w')
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
    global options_beneficiary
    global beneficiary
    global pay_amount
    global create_beneficiary_button
    global pay_beneficiary_button
    global pay_screen

    # Vars
    beneficiary = StringVar()
    pay_amount = StringVar()

    # Screen
    pay_screen = Toplevel(master)
    pay_screen.title("Pay")
    pay_screen.geometry("350x200")
    pay_screen.resizable(False, False)
    pay_screen.transient(master)

    # Frame
    background_frame_pay = Frame(pay_screen, bg='black')
    pay_title_frame = Frame(pay_screen, bg='black', bd=2)
    label_pay_frame = Frame(pay_screen, bg='black', bd=2)
    entry_pay_frame = Frame(pay_screen, bg='black', bd=2)
    option_pay_frame = Frame(pay_screen, bg='black', bd=2)
    button_pay_frame = Frame(pay_screen, bg='black', bd=2)
    button_beneficiary_frame = Frame(pay_screen, bg='black', bd=2)

    # Placing Frames
    background_frame_pay.place(relheight=1, relwidth=1)
    pay_title_frame.place(relx=0.5, rely=0.05, relwidth=0.4, relheight=0.13, anchor='n')
    label_pay_frame.place(relx=0.05, rely=0.2, relwidth=0.5, relheight=0.62)
    option_pay_frame.place(relx=0.6, rely=0.2, relwidth=0.35, relheight=0.3)
    entry_pay_frame.place(relx=0.6, rely=0.52, relwidth=0.35, relheight=0.3)
    button_pay_frame.place(relx=0.05, rely=0.84, relheight=0.15, relwidth=0.25)
    button_beneficiary_frame.place(relx=0.6, rely=0.84, relheight=0.15, relwidth=0.35)

    # Labels
    Label(background_frame_pay, image=background_image).place(relwidth=1, relheight=1)
    Label(pay_title_frame, text="Payment", bg='#659EDB', font=('Calibri', 14)).place(relheight=1, relwidth=1)
    Label(label_pay_frame, text="Select Beneficiary", bg='#659EDB', font=('Calibri', 12)).pack(fill=BOTH, expand=True)
    Label(label_pay_frame, text="Enter Amount", bg='#659EDB', font=('Calibri', 12)).pack(fill=BOTH, expand=True)

    # Entry Screen
    Entry(entry_pay_frame, textvariable=pay_amount, bg='#659EDB').pack(fill=BOTH, expand=True)

    # Button
    pay_beneficiary_button = Button(button_pay_frame, text='Pay', bg='#659EDB', font=('Calibri', 12),
                                    command=finish_pay, activebackground="#9EA3AB")

    create_beneficiary_button1 = Button(button_beneficiary_frame, text='Create Beneficiary', bg='#659EDB',
                                        font=('Calibri', 10), command=create_beneficiary, activebackground="#9EA3AB")

    # Placing Buttons
    create_beneficiary_button1.pack(fill=BOTH, expand=True)
    pay_beneficiary_button.pack(fill=BOTH, expand=True)

    # Button Hovering
    create_beneficiary_button1.bind('<Enter>', on_enter)
    create_beneficiary_button1.bind('<Leave>', on_leave)

    pay_beneficiary_button.bind('<Enter>', on_enter)
    pay_beneficiary_button.bind('<Leave>', on_leave)

    # Option menu
    try:
        beneficiary.set(list(options_beneficiary)[0])
        beneficiary_option = OptionMenu(option_pay_frame, beneficiary, *options_beneficiary)
        beneficiary_option.config(bg='#659EDB', fg="BLACK", activebackground='#376AB4', activeforeground="BLACK")
        beneficiary_option['menu'].config(bg='#659EDB', fg="BLACK", activebackground="#9EA3AB",
                                          activeforeground="black")
        beneficiary_option.pack(fill=BOTH, expand=True)
    except TypeError:
        pass
    except IndexError:
        pass


def finish_pay():
    pay_final = pay_amount.get()
    beneficiary_final = beneficiary.get()

    if beneficiary_final == "":
        messagebox.showerror("Error!", "Please select a beneficiary")
        return

    elif pay_final == "":
        messagebox.showerror("Error!", "Please fill in all fields!")
        return

    elif float(pay_final) <= 0:
        messagebox.showerror("Error!", "Negative Currency is not accepted")
        return

    else:
        beneficiary_username = options_beneficiary[beneficiary.get()]
        beneficiary_username = beneficiary_username.replace("\n", "")

        with open(beneficiary_username, "r") as f:
            file_data_beneficiary = f.readlines()

        with open(login_username, "r") as f:
            file_data_user = f.readlines()

        if float(pay_final) > float(file_data_user[6]):
            messagebox.showerror("Error!", "Insufficient Funds!")
            return
        else:
            file_data_user[6] = str(float(file_data_user[6]) - float(pay_final))
            file_data_beneficiary[6] = str(float(file_data_beneficiary[6]) + float(pay_final))

            with open(beneficiary_username, "w") as f:
                f.writelines(file_data_beneficiary)

            with open(login_username, "w") as f:
                f.writelines(file_data_user)

            messagebox.showinfo("Success!", "Beneficiary Payed!")


def create_beneficiary():
    global beneficiary_account_number
    global beneficiary_name
    global create_beneficiary_button
    global create_beneficiary_screen

    # Vars
    beneficiary_name = StringVar()
    beneficiary_account_number = StringVar()

    # Create screen
    create_beneficiary_screen = Toplevel(master)
    create_beneficiary_screen.title("Create Beneficiary")
    create_beneficiary_screen.geometry("350x200")
    create_beneficiary_screen.resizable(False, False)
    create_beneficiary_screen.transient(master)

    # Creating Frames
    background_frame_beneficiary = Frame(create_beneficiary_screen, bg='black')
    beneficiary_title_frame = Frame(create_beneficiary_screen, bg='black', bd=2)
    label_beneficiary_frame = Frame(create_beneficiary_screen, bg='black', bd=2)
    entry_beneficiary_frame = Frame(create_beneficiary_screen, bg='black', bd=2)
    button_beneficiary_frame = Frame(create_beneficiary_screen, bg='black', bd=2)

    # Placing Frames
    background_frame_beneficiary.place(relheight=1, relwidth=1)
    beneficiary_title_frame.place(relx=0.5, rely=0.05, relwidth=0.4, relheight=0.13, anchor='n')
    label_beneficiary_frame.place(relx=0.02, rely=0.2, relwidth=0.5, relheight=0.6)
    entry_beneficiary_frame.place(relx=0.55, rely=0.2, relwidth=0.38, relheight=0.6)
    button_beneficiary_frame.place(relx=0.02, rely=0.8, relwidth=0.4, relheight=0.23)

    # Label
    Label(background_frame_beneficiary, image=background_image).place(relwidth=1, relheight=1)
    Label(beneficiary_title_frame, text="Create Beneficiary", bg='#659EDB', font=('Calibri', 12)).place(relheight=1,
                                                                                                        relwidth=1)
    Label(label_beneficiary_frame, text="Enter Beneficiary Full Name:", bg='#659EDB', font=('Calibri', 10)).pack(
        fill=BOTH, expand=True)
    Label(label_beneficiary_frame, text="Enter Account Number:", bg='#659EDB', font=('Calibri', 10)).pack(fill=BOTH,
                                                                                                          expand=True)
    # Button
    create_beneficiary_button2 = Button(button_beneficiary_frame, text='Add Beneficiary',
                                        command=finish_create_beneficiary, font=('Calibri', 12), bg='#659EDB', activebackground="#9EA3AB")

    # Placing Button
    create_beneficiary_button2.pack(fill=BOTH, expand=True)

    # Button Hovering
    create_beneficiary_button2.bind('<Enter>', on_enter)
    create_beneficiary_button2.bind('<Leave>', on_leave)

    # Entries
    beneficiary_name_entry = Entry(entry_beneficiary_frame, textvariable=beneficiary_name, width=25, bg='#659EDB')
    account_number_entry = Entry(entry_beneficiary_frame, textvariable=beneficiary_account_number, width=25,
                                 bg='#659EDB')

    # Placing Entries
    beneficiary_name_entry.pack(fill=BOTH, expand=True)
    account_number_entry.pack(fill=BOTH, expand=True)

    # Insert into entries
    beneficiary_name_entry.insert(END, "Enter Name:", )
    account_number_entry.insert(END, "Enter Account number:")

    # Deletes existing text
    beneficiary_name_entry.bind("<FocusIn>", delete_temp_text)
    account_number_entry.bind("<FocusIn>", delete_temp_text)


def finish_create_beneficiary():
    global options_beneficiary
    global username_beneficiary
    all_accounts = os.listdir()
    name = str(beneficiary_name.get())
    account_number = str(beneficiary_account_number.get())
    exist = False

    # Opening File
    if name == "" or account_number == "":
        messagebox.showerror("Error!", "All fields required *")
        return

    elif name == "Enter Name:" or account_number == "Enter Account Number:":
        messagebox.showerror("Error!", "Click the entry screen!")
        return

    else:
        for name_check in all_accounts:
            with open(login_username, "r") as f:
                file_data = f.read()
                user_details = file_data.split('\n')
                user_account_num = user_details[5]

            with open(name_check, "r") as f:
                file_data = f.readlines()
            if file_data[2] == name + '\n' and file_data[5] == account_number + '\n':

                username_beneficiary = file_data[0]
                # Checking if Empty Key pair exists
                if "" in options_beneficiary.keys():
                    del options_beneficiary[""]

                if user_account_num == account_number:
                    messagebox.showerror("Error!", "Can't save yourself as a Beneficiary")
                    return

                # Checking if beneficiary is already saved
                elif name in options_beneficiary.keys():
                    messagebox.showerror("Error!", "Beneficiary already saved")
                    return

                options_beneficiary.update({name: username_beneficiary})
                messagebox.showinfo("Success", "Saved Account number")
                pay_screen.destroy()
                create_beneficiary_screen.destroy()
                exist = True
                break
            else:
                continue

    if not exist:
        messagebox.showerror("Error!", "No Account exists!")


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
    details_balance = user_details[6]

    # Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title("Deposit")
    deposit_screen.geometry("300x200")
    deposit_screen.resizable(False, False)
    deposit_screen.transient(master)

    # Frames
    background_frame_deposit = Frame(deposit_screen)
    title_frame_deposit = Frame(deposit_screen, bg='black', bd=2)
    entry_frame_deposit = Frame(deposit_screen, bg='black', bd=2)
    subtitle_frame_deposit = Frame(deposit_screen, bg='black', bd=2)
    button_frame_deposit = Frame(deposit_screen, bg='black', bd=2)

    # Placing Frames
    background_frame_deposit.place(relheight=1, relwidth=1)
    title_frame_deposit.place(relx=0.5, rely=0.05, relwidth=0.4, relheight=0.15, anchor='n')
    subtitle_frame_deposit.place(relx=0.5, rely=0.22, relwidth=0.8, relheight=0.1, anchor='n')
    entry_frame_deposit.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.3)
    button_frame_deposit.place(relx=0.05, rely=0.75, relwidth=0.3, relheight=0.15)

    # Labels
    Label(background_frame_deposit, image=background_image).place(relwidth=1, relheight=1)
    Label(title_frame_deposit, text="Deposit", font=("Calibri", 12), bg='#659EDB').pack(fill=BOTH, expand=True)
    current_balance_label = Label(subtitle_frame_deposit, text="Current Balance: R" + details_balance,
                                  font=("Calibri", 12), bg='#659EDB')
    current_balance_label.pack(fill=BOTH, expand=True)
    Label(entry_frame_deposit, text="Amount : ", font=("Calibri", 12), bg='#659EDB').pack(fill=BOTH, expand=True,
                                                                                          side=LEFT)

    # Entry
    Entry(entry_frame_deposit, textvariable=amount, bg='#659EDB').pack(fill=BOTH, expand=True)

    # Button
    deposit_button = Button(button_frame_deposit, text="Finish", font=("Calibri", 12), bg='#659EDB',
                            command=finish_deposit, activebackground="#9EA3AB")
    deposit_button.pack(fill=BOTH, expand=True)

    # Binding Buttons
    deposit_button.bind('<Enter>', on_enter)
    deposit_button.bind('<Leave>', on_leave)


def finish_deposit():
    if amount.get() == "":
        messagebox.showerror("Error!", "Amount is Required!")
        return
    if float(amount.get()) <= 0:
        messagebox.showerror("Error!", "Negative Currency is not accepted")
        return

    # Opening File
    file = open(login_username, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[6]
    updated_balance = float(current_balance) + float(amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : R " + str(updated_balance), fg="green")
    messagebox.showinfo("Success!", "Balance Updated")


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
    details_balance = user_details[6]

    # Deposit Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("Deposit")
    withdraw_screen.geometry("300x200")
    withdraw_screen.resizable(False, False)
    withdraw_screen.transient(master)

    # Frames
    background_frame_withdraw = Frame(withdraw_screen)
    title_frame_withdraw = Frame(withdraw_screen, bg='black', bd=2)
    entry_frame_withdraw = Frame(withdraw_screen, bg='black', bd=2)
    subtitle_frame_withdraw = Frame(withdraw_screen, bg='black', bd=2)
    button_frame_withdraw = Frame(withdraw_screen, bg='black', bd=2)

    # Placing Frames
    background_frame_withdraw.place(relheight=1, relwidth=1)
    title_frame_withdraw.place(relx=0.5, rely=0.05, relwidth=0.4, relheight=0.15, anchor='n')
    subtitle_frame_withdraw.place(relx=0.5, rely=0.22, relwidth=0.8, relheight=0.1, anchor='n')
    entry_frame_withdraw.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.3)
    button_frame_withdraw.place(relx=0.05, rely=0.75, relwidth=0.3, relheight=0.15)

    # Labels
    Label(background_frame_withdraw, image=background_image).place(relwidth=1, relheight=1)
    Label(title_frame_withdraw, text="Withdraw", font=("Calibri", 12), bg='#659EDB').pack(fill=BOTH, expand=True)
    current_balance_label = Label(subtitle_frame_withdraw, text="Current Balance: R" + details_balance,
                                  font=("Calibri", 12), bg='#659EDB')
    current_balance_label.pack(fill=BOTH, expand=True)
    Label(entry_frame_withdraw, text="Amount : ", font=("Calibri", 12), bg='#659EDB').pack(fill=BOTH, expand=True,
                                                                                           side=LEFT)

    # Entry
    Entry(entry_frame_withdraw, bg='#659EDB', textvariable=withdraw_amount).pack(fill=BOTH, expand=True)

    # Button
    withdraw_button = Button(button_frame_withdraw, text="Finish", font=("Calibri", 12), activebackground="#9EA3AB", bg='#659EDB',
                             command=finish_withdraw)
    withdraw_button.pack(fill=BOTH, expand=True)

    # Binding Buttons
    withdraw_button.bind('<Enter>', on_enter)
    withdraw_button.bind('<Leave>', on_leave)


def finish_withdraw():
    # Opening File
    file = open(login_username, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[6]

    if withdraw_amount.get() == "":
        messagebox.showerror("Error!", 'Amount is Required!')
        return

    if float(withdraw_amount.get()) <= 0:
        messagebox.showerror("Error!", "Negative Currency is not accepted")
        return

    if float(withdraw_amount.get()) > float(current_balance):
        messagebox.showerror("Error!", 'Insufficient Funds!')
        return

    # Updating File
    updated_balance = float(current_balance) - float(withdraw_amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : R " + str(updated_balance), fg="green")
    messagebox.showinfo("Success", "Balance Updated")


def personal_details():
    global personal_details_screen
    global login_username
    global details_account_number
    # Vars
    file = open(login_username, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_username = user_details[0]
    details_full_name = user_details[2]
    details_age = user_details[3]
    details_gender = user_details[4]
    details_account_number = user_details[5]
    details_balance = user_details[6]

    # Personal Details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title("Personal Details")
    personal_details_screen.geometry("250x350")
    personal_details_screen.resizable(False, False)

    # Establishing Frame
    personal_details_background = Frame(personal_details_screen)
    personal_details_title = Frame(personal_details_screen, bg='black', bd=2)
    personal_details_contents = Frame(personal_details_screen, bg='black', bd=2)
    personal_details_button = Frame(personal_details_screen, bg='black', bd=2)

    # Placing Frames
    personal_details_background.place(relheight=1, relwidth=1)
    personal_details_title.place(relx=0.5, rely=0.05, relwidth=0.6, relheight=0.1, anchor='n')
    personal_details_contents.place(relx=0.5, rely=0.16, relwidth=0.8, relheight=0.7, anchor='n')
    personal_details_button.place(relx=0.5, rely=0.88, relheight=0.1, relwidth=0.4, anchor='n')

    # Labels
    Label(personal_details_background, image=background_image).place(relwidth=1, relheight=1)

    Label(personal_details_title, text="Personal Details", font=("Calibri", 14), bg='#659EDB').pack(fill=BOTH,
                                                                                                    expand=True)

    Label(personal_details_contents, text="Account Number : " + details_account_number, font=("Calibri", 12),
          bg='#659EDB').pack(
        fill=BOTH, expand=True)

    Label(personal_details_contents, text="Username : " + login_username, font=("Calibri", 12), bg='#659EDB').pack(
        fill=BOTH, expand=True)

    Label(personal_details_contents, text="Name : " + details_full_name, font=("Calibri", 12), bg='#659EDB').pack(
        fill=BOTH, expand=True)

    Label(personal_details_contents, text="Age : " + details_age, font=("Calibri", 12), bg='#659EDB').pack(fill=BOTH,
                                                                                                           expand=True)

    Label(personal_details_contents, text="Gender : " + details_gender, font=("Calibri", 12), bg='#659EDB').pack(
        fill=BOTH, expand=True)

    Label(personal_details_contents, text="Balance : R" + details_balance, font=("Calibri", 12), bg='#659EDB').pack(
        fill=BOTH, expand=True)

    # Establishing Button
    edit_details_button = Button(personal_details_button, text="Edit Profile", font=("Calibri", 12),
                                 command=edit_details, bg='#659EDB'
                                 , activebackground="#9EA3AB")

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
    edit_details_screen.geometry("350x200")
    edit_details_screen.transient(master)

    # Frame
    background_frame_edit_details = Frame(edit_details_screen)
    title_frame_edit_details = Frame(edit_details_screen, bg='black', bd=2)
    entry_frame_edit_details = Frame(edit_details_screen, bg='black', bd=2)
    label_frame_edit_details = Frame(edit_details_screen, bg='black', bd=2)
    button_frame_edit_details = Frame(edit_details_screen, bg='black', bd=2)

    # Placing Frames
    background_frame_edit_details.place(relheight=1, relwidth=1)
    title_frame_edit_details.place(relx=0.5, rely=0.05, relwidth=0.6, relheight=0.15, anchor='n')
    label_frame_edit_details.place(relx=0.02, rely=0.22, relheight=0.55, relwidth=0.45)
    entry_frame_edit_details.place(relx=0.5, rely=0.22, relheight=0.55, relwidth=0.48)
    button_frame_edit_details.place(relx=0.02, rely=0.8, relheight=0.2, relwidth=0.2)

    # Label
    Label(background_frame_edit_details, image=background_image).place(relwidth=1, relheight=1)
    Label(title_frame_edit_details, text="Personal Details:", font=("Calibri", 14), bg='#659EDB').pack(fill=BOTH,
                                                                                                       expand=True)
    Label(label_frame_edit_details, text="Username : " + details_username, font=("Calibri", 12), bg='#659EDB').pack(
        fill=BOTH, expand=True)
    Label(label_frame_edit_details, text="Password : " + "*******", font=("Calibri", 12), bg='#659EDB').pack(fill=BOTH,
                                                                                                             expand=True)
    # notif = Label(edit_details_screen, font=("Calibri", 12))
    # notif.grid(row=3, column=1, sticky=N, pady=10)

    # Entries
    username_entry = Entry(entry_frame_edit_details, textvariable=new_username, width=25, bg='#659EDB')
    password_entry = Entry(entry_frame_edit_details, textvariable=new_password, width=25, bg='#659EDB')

    # Placing Entries
    username_entry.pack(fill=BOTH, expand=True)
    password_entry.pack(fill=BOTH, expand=True)

    # Insert into entries
    username_entry.insert(END, "Enter new Name here:", )
    password_entry.insert(END, "Enter new Password here:")

    # Deletes existing text
    username_entry.bind("<FocusIn>", delete_temp_text)
    password_entry.bind("<FocusIn>", delete_temp_text)

    # Button
    Button(button_frame_edit_details, text='Save', command=finish_edit_details, activebackground="#9EA3AB",
           bg='#659EDB').pack(fill=BOTH, expand=True)


def finish_edit_details():
    global login_username
    # Vars
    all_accounts = os.listdir()

    Taken = False

    # Opening File
    if new_username.get() == "" or new_password.get() == "":
        messagebox.showerror("Error!", "All fields required *")
        return

    elif new_username.get() == "Enter new Name here:" or new_password.get() == "Enter new Password here:":
        messagebox.showerror("Error!", "Error please click the entry screen!")
        return

    else:
        for name_check in all_accounts:

            if new_username.get() == name_check:
                # print(name_check)
                messagebox.showerror("Error!", "Username already taken")
                Taken = True
                break
            else:
                continue

    if not Taken:
        with open(str(login_username), "r") as f:
            file_data = f.readlines()

        file_data[0] = str(new_username.get()) + '\n'
        file_data[1] = str(new_password.get()) + '\n'

        with open(str(new_username.get()), 'w') as f:
            f.writelines(file_data)
            os.remove(login_username)
            login_username = new_username.get()

        messagebox.showinfo("Success!", "Account details append successfully!")
        personal_details_screen.destroy()
        edit_details_screen.destroy()


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
                         command=register, activebackground="#9EA3AB")
register_button.place(relheight=1, relwidth=1)
login_button = Button(login_frame, text="Login", font=('Calibri', 12), width=20, bg='#659EDB', command=login
                      , activebackground="#9EA3AB")
login_button.place(relheight=1, relwidth=1)

# Binding Buttons
login_button.bind('<Enter>', on_enter)
login_button.bind('<Leave>', on_leave)
register_button.bind('<Enter>', on_enter)
register_button.bind('<Leave>', on_leave)

# Running Mainloop
master.mainloop()
