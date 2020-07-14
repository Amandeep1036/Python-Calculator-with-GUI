from tkinter import*


def btn_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btn_clear_display():
    global operator
    operator = ""
    text_Input.set("")


def btn_equals_input():
    global operator
    sum_up = str(eval(operator))
    text_Input.set(sum_up)
    operator = ""


cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=40, insertwidth=6,
                   bg="grey", justify='right').grid(columnspan=4)

btn7 = Button(cal, padx=16, pady=16,  bd=15, fg='black', font=('arial', 20, 'bold'), text="7",
              command=lambda: btn_click(7), bg="grey").grid(row=1, column=0)

btn8 = Button(cal, padx=16, pady=16,  bd=15, fg='black', font=('arial', 20, 'bold'), text="8",
              command=lambda: btn_click(8), bg="grey").grid(row=1, column=1)

btn9 = Button(cal, padx=16, pady=16,  bd=15, fg='black', font=('arial', 20, 'bold'), text="9",
              command=lambda: btn_click(9), bg="grey").grid(row=1, column=2)

Add_btn = Button(cal, padx=16, pady=16,  bd=13, fg='black', font=('arial', 20, 'bold'), text="+",
                 command=lambda: btn_click("+"), bg="grey").grid(row=1, column=3)

btn4 = Button(cal, padx=16, pady=16,  bd=15, fg='black', font=('arial', 20, 'bold'), text="4",
              command=lambda: btn_click(4), bg="grey").grid(row=2, column=0)

btn5 = Button(cal, padx=16, pady=16,  bd=15, fg='black', font=('arial', 20, 'bold'), text="5",
              command=lambda: btn_click(5), bg="grey").grid(row=2, column=1)

btn6 = Button(cal, padx=16, pady=16,  bd=15, fg='black', font=('arial', 20, 'bold'), text="6",
              command=lambda: btn_click(6), bg="grey").grid(row=2, column=2)

Sub_btn = Button(cal, padx=16, pady=16,  bd=15, fg='black', font=('arial', 20, 'bold'), text="-",
                 command=lambda: btn_click("-"), bg="grey").grid(row=2, column=3)

btn3 = Button(cal, padx=16, pady=16,  bd=15, fg='black', font=('arial', 20, 'bold'), text="3",
              command=lambda: btn_click(3), bg="grey").grid(row=3, column=0)

btn2 = Button(cal, padx=16, pady=16,  bd=15, fg='black', font=('arial', 20, 'bold'), text="2",
              command=lambda: btn_click(2), bg="grey").grid(row=3, column=1)

btn1 = Button(cal, padx=16, pady=16,  bd=15, fg='black', font=('arial', 20, 'bold'), text="1",
              command=lambda: btn_click(1), bg="grey").grid(row=3, column=2)

Multiply_btn = Button(cal, padx=16, pady=16,  bd=15, fg='black', font=('arial', 20, 'bold'), text="*",
                      command=lambda: btn_click("*"), bg="grey").grid(row=3, column=3)

btn0 = Button(cal, padx=16, pady=16, bd=15, fg='black', font=('arial', 20, 'bold'), text="0",
              command=lambda: btn_click(0), bg="grey").grid(row=4, column=0)

Clear_btn = Button(cal, padx=16, pady=16, bd=15, fg='black', font=('arial', 20, 'bold'), text="C",
                   bg="grey", command=btn_clear_display).grid(row=4, column=1)

Equals_btn = Button(cal, padx=16, pady=16, bd=15, fg='black', font=('arial', 20, 'bold'), text="=",
                    bg="grey", command=btn_equals_input).grid(row=4, column=2)

Division_btn = Button(cal, padx=16, pady=16, bd=15, fg='black', font=('arial', 20, 'bold'), text="/",
                      command=lambda: btn_click("/"), bg="grey").grid(row=4, column=3)
cal.mainloop()