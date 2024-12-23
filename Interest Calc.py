from tkinter import *
import tkinter as tk

def cal_interest():
    principle = float(ent_principle.get())
    rate = float(ent_rate.get())
    time = float(ent_time.get())
    
    interest = (principle * rate * time) / 100
    total_amount = principle + interest
    
    l_result.config(text = f"Interest:  {interest: .2f}\nTotal: {total_amount: .2f}")
    

root = tk.Tk()
root.title("Interest Calculator")

l_principle = tk.Label(root, text = "Enter Principle: ")
l_principle.grid(row = 0, column = 0, padx = 10, pady = 5)

ent_principle = tk.Entry(root)
ent_principle.grid(row = 0, column = 1, padx = 10, pady = 5)

l_rate = tk.Label(root, text = "Enter Rate of Interest (%): ")
l_rate.grid(row = 1, column = 0, padx = 10, pady = 5)

ent_rate = tk.Entry(root)
ent_rate.grid(row = 1, column = 1, padx = 10, pady = 5)

l_time = tk.Label(root, text = "Enter Time (Years): ")
l_time.grid(row = 2, column = 0, padx = 10, pady = 5)

ent_time = tk.Entry(root)
ent_time.grid(row = 2, column = 1, padx = 10, pady = 5)

btn_cal = tk.Button(root, text = "Calculate", command = cal_interest)
btn_cal.grid(row = 3, column = 0, columnspan = 2, pady = 10)

l_result = tk.Label(root, text = "Interest: \nTotal: ", justify = LEFT)
l_result.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 5)

root.mainloop()