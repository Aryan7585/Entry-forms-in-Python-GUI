# Python Code for Dance Academy Form
from tkinter import*

root = Tk()
root.geometry("655x333")

form = Label(root,text= "Dance Academy Form ",font=("comicssanms"))
form.grid(column=2)

n= Label(root,text= "\n")
n.grid(column=2)

name = Label(root,text = "Name :  ")                            # Lable of NAME
name.grid()

namevalue = StringVar()                                         # defining entry var 
name_entry = Entry(root, textvariable = namevalue)              # Entry Var
name_entry.grid(column = 1  , row = 2 )                         # Adding it in Grid

age = Label(root,text = "Age : ")                               # Label of Age 
age.grid()

age_value = StringVar()
age_Entry = Entry(root, textvariable = age_value  )
age_Entry.grid(column = 1 , row = 3  )

contact = Label(root,text = "Contact No. : ")                              
contact.grid()

contact_value = StringVar()
contact_Entry = Entry(root, textvariable = contact_value  )
contact_Entry.grid(column = 1 , row = 4  )

mail = Label(root,text = "E-Mail Adress  : ")                              
mail.grid()

mail_value = StringVar()
mail_Entry = Entry(root, textvariable = mail_value  )
mail_Entry.grid(column = 1 , row = 5  )


xp = Label(root,text = "Any Prior Experience  : ")                              
xp.grid()

xp_value = StringVar()
xp_Entry = Entry(root, textvariable = xp_value  )
xp_Entry.grid(column = 1 , row = 6  )

def Submit():
    print(f"{namevalue.get()}")
    print(f"{age_value.get()}")
    print(f"{contact_value.get()}")
    print(f"{mail_value.get()}")
    print(f"{xp_value.get()}")

    f = open("form_2.txt","a")  
    f.truncate(0)
    f.write(f"{namevalue.get()}")
    f.write('\n')
    f.write(f"{age_value.get()}")
    f.write('\n')
    f.write(f"{contact_value.get()}")
    f.write('\n')
    f.write(f"{mail_value.get()}")
    f.write('\n')
    f.write(f"{xp_value.get()}")
    f.write('\n')

submit_l1 = Label(root,text="\n")
submit_l1.grid( row = 8 )

submit_button = Button(root,text="Submit", command = Submit)
submit_button.grid( row = 8 )

root.mainloop()