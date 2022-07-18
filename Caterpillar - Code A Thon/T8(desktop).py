from tkinter import *
from tkinter import ttk
import time
import datetime
from tkinter import messagebox
import os
import csv
import ctypes
import threading
import time

def worker(title,close_until_seconds):
    time.sleep(close_until_seconds)
    wd=ctypes.windll.user32.FindWindowW(0,title)
    ctypes.windll.user32.SendMessageW(wd,0x00010,0,0)
    return
def AutoCloseMessageBoxW(text, title, close_until_seconds):
    t = threading.Thread(target=worker,args=(title,close_until_seconds))
    t.start()
    ctypes.windll.user32.MessageBoxW(0, text, title, 0)


def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200,tick)

mont={'01':'January',
      '02':'February',
      '03':'March',
      '04':'April',
      '05':'May',
      '06':'June',
      '07':'July',
      '08':'August',
      '09':'September',
      '10':'October',
      '11':'November',
      '12':'December'
      }

global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
day,month,year=date.split("-")    


app = Tk()
app.geometry("700x1000")
app.resizable(True,False)
app.title("Codeathon")
app.configure(background='#ECBC76')

frame1 = Frame(app, bg="#FFFFFF")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = Frame(app, bg="#FFFFFF")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

frame3 = Frame(app, bg="#FFFFFF")
frame3.place(relx=0.51, rely=0.09, relwidth=0.12, relheight=0.07)

frame4 = Frame(app, bg="#FFFFFF")
frame4.place(relx=0.38, rely=0.09, relwidth=0.12, relheight=0.07)

frame5 = Frame(app, bg="#FFF4E3")
frame5.place(relx=0.39, rely=0.10, relwidth=0.10, relheight=0.05)

frame6 = Frame(app, bg="#FFF4E3")
frame6.place(relx=0.52, rely=0.10, relwidth=0.10, relheight=0.05)

datef = Label(frame5, text = day+"-"+mont[month]+"-"+year, fg="#E48700",bg="#FFF4E3" ,width=55 ,height=1,font=('poppins', 22, ' bold '))
datef.pack(fill='both',expand=1)

clock = Label(frame6,fg="#E48700",bg="#FFF4E3" ,width=55 ,height=1,font=('poppins', 22, ' bold '))
clock.pack(fill='both',expand=1)
tick()

tv= ttk.Treeview(frame1, height=25, columns = ('bucket_weight','payload_weight','time'), x = 100, y = 100)
# tv.place(x = 100, y = 100)
tv.column('#0',width=130)
tv.column('bucket_weight',width=130)
tv.column('payload_weight',width=130)
tv.column('time',width=133)
tv.grid(row=2, column=0, padx=(80,0), pady=(150,0), columnspan=4)
tv.heading('#0',text ='COUNT')
tv.heading('bucket_weight',text='BUCKET')
tv.heading('payload_weight',text='PAYLOAD')
tv.heading('time',text ='TIME')
font1=('poppins', 16, ' bold ')


l1=Label(frame2, text='BUCKET WEIGHT', width=20, height=1, fg="#E48700", bg="#FFFFFF", font=('poppins', 16, ' bold '))
l1.place(x = 350, y = 100)
l2=Label(frame2,text='PAYLOAD LIMIT', width=20, height=1, fg="#E48700", bg="#FFFFFF", font=('poppins', 16, ' bold '))
l2.place(x = 45, y = 250)
l3=Label(frame2,text='STEP', width=20, height=1, fg="#E48700", bg="#FFFFFF", font=('poppins', 16, ' bold '))
l3.place(x = 45, y = 400)
l4=Label(frame2,text='DELAY: ms', width=20, height=1, fg="#E48700", bg="#FFFFFF", font=('poppins', 16, ' bold '))
l4.place(x = 360, y = 400)
l5=Label(frame2,text='PAYLOAD WEIGHT', width=20, height=1, fg="#E48700", bg="#FFFFFF", font=('poppins', 16, ' bold '))
l5.place(x = 350, y = 250)
l6=Label(frame2,text='PASS COUNT', width=20, height=1, fg="#E48700", bg="#FFFFFF", font=('poppins', 16, ' bold '))
l6.place(x = 205, y = 550)
l7=Label(frame2,text='BUCKET WEIGHT SET', width=20, height=1, fg="#E48700", bg="#FFFFFF", font=('poppins', 16, ' bold '))
l7.place(x = 45, y = 100)

# Bucket Weight Set
bucket_weight_d=DoubleVar(value=0)
bucket_weight = Entry(frame2, width = 10, justify=CENTER, fg="#E48700", bg="#FFF4E3", textvariable=bucket_weight_d, font=font1) # added one Entry box
bucket_weight.place(x = 425, y = 50)

# Bucket Weight Set
sb3_d=DoubleVar(value=40)
sb3 = Spinbox(frame2, from_= 10, to = 50, increment=0.5, justify=CENTER, textvariable=sb3_d, width = 10, fg="#E48700", bg="#FFF4E3", font=font1)
sb3.place(x = 100, y = 50)

# Payload Weight
payload_weight_d=DoubleVar(value=0)
payload_weight = Entry(frame2, width = 10, justify=CENTER, fg="#E48700", bg="#FFF4E3", textvariable=payload_weight_d, font=font1) # added one Entry box
payload_weight.place(x = 425, y = 200)

# Payload Weight Limit
payload_limit_i=IntVar(value=400)
payload_limit = Entry(frame2, width = 10, justify=CENTER, fg="#E48700", bg="#FFF4E3", textvariable=payload_limit_i, font=font1) # added one Entry box
payload_limit.place(x = 100, y = 200)

# Step Count
sb1_d=DoubleVar(value=0.5)
sb1 = Spinbox(frame2, from_= 1, to = 10, increment=0.5, justify=CENTER, textvariable=sb1_d, width = 10, fg="#E48700", bg="#FFF4E3", font=font1)
sb1.place(x = 100, y = 350)

# Delay
sb2_i=IntVar(value=500)
sb2 = Spinbox(frame2, from_= 500, to = 5000, increment=500, justify=CENTER, textvariable=sb2_i, width = 10, fg="#E48700", bg="#FFF4E3", font=font1)
sb2.place(x = 425, y = 350)

# Pass Count
pass_count_i=IntVar(value=0)
pass_count = Entry(frame2, width = 10, justify=CENTER, fg="#E48700", bg="#FFF4E3", textvariable=pass_count_i, font=font1) # added one Entry box
pass_count.place(x = 275, y = 500)

def update_store():
    bucket_weight_d.set(0)
    AutoCloseMessageBoxW('Stored','Event',2)
   
def my_upd(*args):
    i=bucket_weight_d.get()+sb1_d.get()
    j=bucket_weight_d.get()+payload_weight_d.get()
    bucket_weight_val=bucket_weight_d.get()
    count=pass_count_i.get()
    payload=payload_weight_d.get()
    if(count<=20 and payload<payload_limit_i.get()): # check upper limit 
        if(bucket_weight_val<40):
            i="{:.2f}". format(i)
            j="{:.2f}". format(j) # formating upto 2 decimal place 
            bucket_weight_d.set(i)
            frame2.after(sb2_i.get(),my_upd)
        else:
            pass_count_i.set(count+1)
            j="{:.2f}". format(j)
            storeButton.invoke()
            payload_weight_d.set(j)
            frame2.after(sb2_i.get(),my_upd)
            col_names=['COUNT','','BUCKET','','PAYLOAD','','TIME']
            ts = time.time()
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            pyl=[str(count), '', str(bucket_weight_val), '', str(payload), '', str(timeStamp)]
            
            
            exists = os.path.isfile("Payload\Payload_" + str(date) + ".csv")
            if exists:
                with open("Payload\Payload_" + str(date) + ".csv", 'a+') as csvFile1:
                    writer = csv.writer(csvFile1)
                    writer.writerow(pyl)
                csvFile1.close()
            else:
                with open("Payload\Payload_" + str(date) + ".csv", 'a+') as csvFile1:
                    writer = csv.writer(csvFile1)
                    writer.writerow(col_names)
                    writer.writerow(pyl)
                csvFile1.close()
            with open("Payload\Payload_" + str(date) + ".csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                i=0
                for lines in reader1:
                    i = i + 1
                    if (i > 1):
                        if (i % 2 != 0):
                            iidd = str(lines[0]) + '   '
                            tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
            csvFile1.close()
    


    
my_upd() # start 
payload_limit_i.trace('w',my_upd)


storeButton = Button(frame2, text="STORE",fg="#FFFFFF", bg="#E48700", command=update_store, width=15, activebackground = "white", font=font1)
storeButton.place(x = 250, y = 600)

app.mainloop()