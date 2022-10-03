import tkinter
from tkinter import *

root=tkinter.Tk()
root.geometry("800x550")
root.title("Bill Management")
root.resizable(False, False)

def resetButton():
    friedRice_entry.delete(0, END)
    chickenKatsu_entry.delete(0, END)
    frenchFries_entry.delete(0, END)
    indomie_entry.delete(0, END)
    spaghetti_entry.delete(0, END)
    tea_entry.delete(0, END)
    milk_entry.delete(0, END)
    coffee_entry.delete(0, END)
    water_entry.delete(0, END)
    totalBill.set("0")

def total():
    try: temp1 = int(friedRice.get())
    except: temp1 = 0

    try: temp2 = int(chickenKatsu.get())
    except: temp2 = 0

    try: temp3 = int(frenchFries.get())
    except: temp3 = 0

    try: temp4 = int(indomie.get())
    except: temp4 = 0

    try: temp5 = int(spaghetti.get())
    except: temp5 = 0

    try: temp6 = int(tea.get())
    except: temp6 = 0

    try: temp7 = int(milk.get())
    except: temp7 = 0

    try: temp8 = int(coffee.get())
    except: temp8 = 0

    try: temp9 = int(water.get())
    except: temp9 = 0

    #calc
    totalCalc = (temp1 * 20000) + (temp2 * 15000) + (temp3 * 5000) + (temp4 * 8000) + (temp5 * 22000)+(temp6 * 4000) + (temp7 * 8000) + (temp8 * 7000) + (temp9 * 3000)
    totalBill.set(str(totalCalc))

#title
Label(text="MyCafe", bg="black", fg="white", font=("Times New Roman", 25), width="300", height="2").pack()

#menu cafe
foodFrame = Frame(root, bg="red", highlightbackground="black", highlightthickness=1, width=250, height=200)
foodFrame.place(x=10, y=100)
Label(foodFrame, text="Food", bg="red", fg="white", font=("Times New Roman", 18, "bold")).place(x=85, y=0)
Label(foodFrame, text="Fried Rice.....20000", bg="red", fg="white", font=("Times New Roman", 12)).place(x=10, y=40)
Label(foodFrame, text="Chicken Katsu.....15000", bg="red", fg="white", font=("Times New Roman", 12)).place(x=10, y=70)
Label(foodFrame, text="French Fries.....5000", bg="red", fg="white", font=("Times New Roman", 12)).place(x=10, y=100)
Label(foodFrame, text="Indomie.....8000", bg="red", fg="white", font=("Times New Roman", 12)).place(x=10, y=130)
Label(foodFrame, text="Spaghetti.....22000", bg="red", fg="white", font=("Times New Roman", 12)).place(x=10, y=160)

drinkFrame = Frame(root, bg="red", highlightbackground="black", highlightthickness=1, width=250, height=170)
drinkFrame.place(x=10, y=320)
Label(drinkFrame, text="Drink", bg="red", fg="white", font=("Times New Roman", 18, "bold")).place(x=80, y=0)
Label(drinkFrame, text="Tea.....4000", bg="red", fg="white", font=("Times New Roman", 12)).place(x=10, y=40)
Label(drinkFrame, text="Milk.....8000", bg="red", fg="white", font=("Times New Roman", 12)).place(x=10, y=70)
Label(drinkFrame, text="Coffee.....7000", bg="red", fg="white", font=("Times New Roman", 12)).place(x=10, y=100)
Label(drinkFrame, text="Water.....3000", bg="red", fg="white", font=("Times New Roman", 12)).place(x=10, y=130)

#entry work
entryWorkFrame = Frame(root, bd=5, width=250, height=200, relief=RAISED)
entryWorkFrame.place(x=262, y=100)

friedRice = StringVar()
chickenKatsu = StringVar()
frenchFries = StringVar()
indomie = StringVar()
spaghetti = StringVar()
tea = StringVar()
milk = StringVar()
coffee = StringVar()
water = StringVar()

#label
friedRice_label = Label(entryWorkFrame, text="Fried Rice", fg="black", font=("Times New Roman", 12, "bold"), width=15)
chickenKatsu_label = Label(entryWorkFrame, text="Chicken Katsu", fg="black", font=("Times New Roman", 12, "bold"), width=15)
frenchFries_label = Label(entryWorkFrame, text="French Fries", fg="black", font=("Times New Roman", 12, "bold"), width=15)
indomie_label = Label(entryWorkFrame, text="Indomie", fg="black", font=("Times New Roman", 12, "bold"), width=15)
spaghetti_label = Label(entryWorkFrame, text="Spaghetti", fg="black", font=("Times New Roman", 12, "bold"), width=15)
tea_label = Label(entryWorkFrame, text="Tea", fg="black", font=("Times New Roman", 12, "bold"), width=15)
milk_label = Label(entryWorkFrame, text="Milk", fg="black", font=("Times New Roman", 12, "bold"), width=15)
coffee_label = Label(entryWorkFrame, text="Coffee", fg="black", font=("Times New Roman", 12, "bold"), width=15)
water_label = Label(entryWorkFrame, text="Water", fg="black", font=("Times New Roman", 12, "bold"), width=15)

friedRice_label.grid(row=1, column=0)
chickenKatsu_label.grid(row=2, column=0)
frenchFries_label.grid(row=3, column=0)
indomie_label.grid(row=4, column=0)
spaghetti_label.grid(row=5, column=0)
tea_label.grid(row=6, column=0)
milk_label.grid(row=7, column=0)
coffee_label.grid(row=8, column=0)
water_label.grid(row=9, column=0)

#entry
friedRice_entry = Entry(entryWorkFrame, textvariable=friedRice, fg="black", font=("Times New Roman", 12, "bold"), width=10, bd=6, bg="lightgrey")
chickenKatsu_entry = Entry(entryWorkFrame, textvariable=chickenKatsu, fg="black", font=("Times New Roman", 12, "bold"), width=10, bd=6, bg="lightgrey")
frenchFries_entry = Entry(entryWorkFrame, textvariable=frenchFries, fg="black", font=("Times New Roman", 12, "bold"), width=10, bd=6, bg="lightgrey")
indomie_entry = Entry(entryWorkFrame, textvariable=indomie, fg="black", font=("Times New Roman", 12, "bold"), width=10, bd=6, bg="lightgrey")
spaghetti_entry = Entry(entryWorkFrame, textvariable=spaghetti, fg="black", font=("Times New Roman", 12, "bold"), width=10, bd=6, bg="lightgrey")
tea_entry = Entry(entryWorkFrame, textvariable=tea, fg="black", font=("Times New Roman", 12, "bold"), width=10, bd=6, bg="lightgrey")
milk_entry = Entry(entryWorkFrame, textvariable=milk, fg="black", font=("Times New Roman", 12, "bold"), width=10, bd=6, bg="lightgrey")
coffee_entry = Entry(entryWorkFrame, textvariable=coffee, fg="black", font=("Times New Roman", 12, "bold"), width=10, bd=6, bg="lightgrey")
water_entry = Entry(entryWorkFrame, textvariable=water, fg="black", font=("Times New Roman", 12, "bold"), width=10, bd=6, bg="lightgrey")

friedRice_entry.grid(row=1, column=1)
chickenKatsu_entry.grid(row=2, column=1)
frenchFries_entry.grid(row=3, column=1)
indomie_entry.grid(row=4, column=1)
spaghetti_entry.grid(row=5, column=1)
tea_entry.grid(row=6, column=1)
milk_entry.grid(row=7, column=1)
coffee_entry.grid(row=8, column=1)
water_entry.grid(row=9, column=1)

#button
reset_button = Button(entryWorkFrame, text="Reset", fg= "black", font=("Times New Roman", 12, "bold"), width=12, bd=6, bg="lightblue", command=resetButton)
reset_button.grid(row=10, column=0)

total_button = Button(entryWorkFrame, text="Total", fg= "black", font=("Times New Roman", 12, "bold"), width=12, bd=6, bg="lightblue", command=total)
total_button.grid(row=10, column=1)

#bill
billFrame =  Frame(root, bg="lightblue", highlightbackground="black", highlightthickness=1, width=250, height=200)
billFrame.place(x=542, y=100)

Label(billFrame, text="Bill", bg="lightblue", fg="black", font=("Times New Roman", 18, "bold")).place(x=100, y=0)

Label(billFrame, text="Total Price", bg="lightblue", fg="black", font=("Times New Roman", 15, "bold")).place(x=70, y=50)

#total calc
totalBill = StringVar()
totalBill.set("0")

Label(billFrame, textvariable=totalBill, fg="black", font=("Times New Roman", 15, "bold"), width=15, bd=6, bg="lightgrey", highlightbackground="black",highlightthickness=2).place(x=25, y=80)

root.mainloop()