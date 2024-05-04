import pyqrcode
import tkinter as tk
from tkinter import Label,Entry,StringVar,Button


#To create Window	
win=tk.Tk()
win.title("QR Generator")
win.geometry('750x350')

def genqr():
    if (name_input.get()!="") & (email_input.get()!="") & (dob_input.get()!="") &(mbn_input.get()!="") &(eme2_input.get()!="" ) & (address_input.get()!=""):
        if ((instafb_input.get()!="")):
            whole_str= 'Name : '+ name_input.get()+'\n'+'Email : ' + email_input.get()+'\n'+'Date of Birth : '+dob_input.get()+'\n'+'Mobile Number : '+mbn_input.get()+'\n'+'LinkedIn : '+eme2_input.get()+'\n'+'Instagram/Facebook : '+instafb_input.get()+'\n'+'Address : '+address_input.get()+'\n'
        else:
            whole_str= 'Name : '+ name_input.get()+'\n'+'Email : ' + email_input.get()+'\n'+'Date of Birth : '+dob_input.get()+'\n'+'Mobile Number : '+mbn_input.get()+'\n'+'LinkedIn : '+eme2_input.get()+'\n'+'Address : '+address_input.get()+'\n'  
        uu=pyqrcode.create(whole_str)
        uu.png('{}.png'.format(name_input.get()),scale=7)
        Label(win,text="",fg='blue',width=30).grid(row=8,column=1)
    else:
        Label(win,text="Please Enter All Details",fg='blue',width=30).grid(row=8,column=1)


name_input=StringVar()
email_input=StringVar()
dob_input=StringVar()
mbn_input=StringVar()
eme2_input=StringVar()
instafb_input=StringVar()
address_input=StringVar()


#Name 
name_lbl=Label(win,text=" Name ",fg='#143347',width=25).grid(row=0,column=0)
name_display=Entry(win,font=('monospace',20,'bold'),textvariable=name_input,bd=3,width=35,insertwidth=2,bg="#C2E3DB",justify='left').grid(row=0,column=1)

#Email
email_lbl=Label(win,text="Email ",fg='#143347',width=25).grid(row=1,column=0)
email_display=Entry(win,font=('monospace',20,'bold'),textvariable=email_input,bd=3,insertwidth=2,width=35,bg="#C2E3DB",justify='left').grid(row=1,column=1)

#Date of Birth
dob_lbl=Label(win,text="Date Of Birth ",fg='#143347',width=25).grid(row=2,column=0)
dob_display=Entry(win,font=('monospace',20,'bold'),textvariable=dob_input,bd=3,insertwidth=2,width=35,bg="#C2E3DB",justify='left').grid(row=2,column=1)

#mobile number
mbn_lbl=Label(win,text="Mobile Number ",fg='#143347',width=25).grid(row=3,column=0)
mbn_display=Entry(win,font=('monospace',20,'bold'),textvariable=mbn_input,bd=3,insertwidth=2,width=35,bg="#C2E3DB",justify='left').grid(row=3,column=1)

#LInkedin
eme2_lbl=Label(win,text="LinkedIn ",fg='#143347',width=25).grid(row=4,column=0)
eme2_display=Entry(win,font=('monospace',20,'bold'),textvariable=eme2_input,bd=3,insertwidth=2,width=35,bg="#C2E3DB",justify='left').grid(row=4,column=1)

#Insta/FB Number 
instafb_lbl=Label(win,text="Instagram/Facebook ",fg='#143347',width=25).grid(row=5,column=0)
instafb_display=Entry(win,font=('monospace',20,'bold'),textvariable=instafb_input,bd=3,insertwidth=2,width=35,bg="#C2E3DB",justify='left').grid(row=5,column=1)

#Address 
address_lbl=Label(win,text="Address ",fg='#143347',width=25).grid(row=6,column=0)
address_display=Entry(win,font=('monospace',20,'bold'),textvariable=address_input,bd=3,insertwidth=2,width=35,bg="#C2E3DB",justify='left').grid(row=6,column=1)

#Button to Generate 
generate_btn=Button(win,padx=4,pady=4,bd=3,fg='black',bg='green',font=('arial',10,'bold'),text='Generate QR Code',command=lambda:genqr()).grid(row=8,column=0)


win.mainloop()
