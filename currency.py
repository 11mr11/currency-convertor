from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Currency convertor')
root.geometry('500x500')

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# Create two frames
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame= Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

# Add our tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="Convert")

# Disable 2nd Tab
my_notebook.tab(1, state='disabled')


##################
# Currencies
##################

def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("You did not fill all the entries")
    else:
        # disabled entry boxes
        home_entry.config(state='disabled')
        conversion_entry.config(state='disabled')
        rate_entry.config(state='disabled')
        # enabled tabe
        my_notebook.tab(1, state='normal')

        # Change tab fields
        amount_label.config(text=f'Amount of {home_entry.get()} To Convert To {conversion_entry.get()}')
        converted_label.config(text=f'Equals This MANY {conversion_entry.get()}')
        convert_button.config(text=f'Convert from {home_entry.get()}')
def unlock():
        # Enabled entry boxes
        home_entry.config(state='normal')
        conversion_entry.config(state='normal')
        rate_entry.config(state='normal')

        # Disabled tab
        my_notebook.tab(1, state='disabled')
    
home = LabelFrame(currency_frame,text= "Your Home Currency")
home.pack(pady=20)

# Home currency entry box
home_entry = Entry(home, font=("Helvetical", 24))
home_entry.pack(pady=10, padx=10)

# Conversion Currency Frame
conversion = LabelFrame(currency_frame, text="Conversion Currency")
conversion.pack(pady=20)

# Convert to label
conversion_label = Label(conversion, text="Currency to convert to... ")
conversion_label.pack(pady=10)


# Convert to entry
conversion_entry = Entry(conversion, font=("Helvetica", 24))
conversion_entry.pack(pady=10, padx=10)


# Rate to label
rate_label = Label(conversion, text="Currency conversion rate... ")
rate_label.pack(pady=10)


# Rate to entryf
rate_entry = Entry(conversion, font=("Helvetica", 24))
rate_entry.pack(pady=10, padx=10)

# Button frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

# Create buttons
lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command=unlock)
unlock_button.grid(row=0, column=1, padx=10)

####################
# Conversion Logic
####################

def convert():
    # Clear converted entry box
    converted_entry.delete(0, END)

    # CONVERT
    conversion = float(rate_entry.get()) * float(amount_entry.get())

    #convert tO two decimals
    conversion = round(conversion,2)

    # Add Commas
    conversion = '{:,}'.format(conversion)

    # update entry box
    converted_entry.insert(0, conversion)

    

def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)

amount_label = LabelFrame(conversion_frame, text='Amount To Convert')
amount_label.pack(pady=20)

# Entry Box For Ampuont
amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(pady=10, padx=10)

# Convert Button
convert_button = Button(amount_label, text='Convert', command=convert)
convert_button.pack(pady=20)

# Equals Frame
converted_label = LabelFrame(conversion_frame, text='Converted Currency')
converted_label.pack(pady=20)

# Converted entry
converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0, bg='systembuttonface')
converted_entry.pack(pady=10, padx=10)

# Clear Button
clear_button = Button(conversion_frame, text='Clear', command=clear)
clear_button.pack(pady=20)


# Fake Label Spacing
spacer = Label(conversion_frame, text='', width=68)
spacer.pack()



root.mainloop()