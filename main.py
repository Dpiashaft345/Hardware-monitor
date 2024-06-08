from tkinter import *
import cpuinfo
import psutil

window =Tk()

window.geometry("800x500")
window.title("DP hardware monitor")
window.config(bg="#fffee8")

cpu_info = cpuinfo.get_cpu_info()


canvas=Canvas(window,width=600,height=7)
canvas.place(x=100,y=260)

def bytes_to_gb(byte):
    gb = 10737418
    giga = byte/gb
    giga = '{0:.1f}'.format(giga)
    return giga

def cpu_usage():
    cpu_use = psutil.cpu_percent(interval=0.5)
    cpu_use_label.config(text='{}%'.format(cpu_use))
    cpu_use_label.after(200,cpu_usage)

canvas.create_line(0,0,600,0,fill="black",width=12)

def ram_usage():

    ram_use = psutil.virtual_memory()
    ram_use = dict(ram_use._asdict())
    for ram in ram_use:
        if ram != 'percent':
            ram_use[ram]=bytes_to_gb(ram_use[ram])

    ram_use_label.config(text='{}'.format(ram_use))
    ram_use_label.after(200,ram_usage)




titlelabel = Label(window,text="HARDWARE MONITOR",font="arial 25 bold",fg="green",bg="#fffee8")
titlelabel.place(x=220,y=20)

cpu_title = Label(window,text="CPU",font="arial 26 italic bold",fg="red",bg="#fffee8")
cpu_title.place(x=350,y=100)

cpu_title_usage = Label(window,text="CPU usage:",font="arial 20 italic bold",fg="red",bg="#fffee8")
cpu_title_usage.place(x=270,y=200)

ram_title = Label(window,text="RAM",font="arial 26 italic bold",fg="red",bg="#fffee8")
ram_title.place(x=350,y=300)

ram_use_label = Label(window,font="arial 15 italic",fg="black",bg="#fffee8")
ram_use_label.place(x=60,y=360)

cpu_use_label = Label(window,font="arial 20 italic bold",fg="black",bg="#fffee8")
cpu_use_label.place(x=440,y=200)


cpu_tipe_label = Label(window,text=f"{cpu_info['brand_raw']}",font="arial 20 bold",fg="black",bg="#fffee8")
cpu_tipe_label.place(x=170,y=150)


ram_usage()
cpu_usage()
window.mainloop()
