import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful Calculator")
        self.root.geometry("400x600")
        self.expression = ""
        
        self.input_text = tk.StringVar()
        
        self.input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.input_frame.pack(side=tk.TOP)
        
        self.input_field = tk.Entry(self.input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)
        
        self.buttons_frame = tk.Frame(self.root, width=400, height=450, bg="lightgrey")
        self.buttons_frame.pack()
        
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        colors = {
            'C': '#f00', '=': '#0f0',
            '0': '#ff0', '1': '#ff0', '2': '#ff0', '3': '#ff0', '4': '#ff0', '5': '#ff0', '6': '#ff0', '7': '#ff0', '8': '#ff0', '9': '#ff0',
            '+': '#00f', '-': '#00f', '*': '#00f', '/': '#00f'
        }
        
        for (text, row, col) in buttons:
            self.create_button(text, row, col, colors.get(text, "#fff"))

    def create_button(self, text, row, col, bg):
        button = tk.Button(self.buttons_frame, text=text, fg="black", width=10, height=3, bd=0, bg=bg, cursor="hand2",
                           command=lambda t=text: self.click_event(t))
        button.grid(row=row, column=col, padx=1, pady=1)

    def click_event(self, item):
        if item == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
                self.expression = ""
                self.input_text.set("")
        elif item == 'C':
            self.expression = ""
            self.input_text.set("")
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()