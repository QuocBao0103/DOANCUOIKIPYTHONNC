import tkinter as tk
from tkinter import messagebox

def calculate(operator):
    try:
        # Lấy dữ liệu từ các ô nhập
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        # Xử lý các phép toán
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("Không thể chia cho 0.")
            result = num1 / num2
        else:
            raise ValueError("Phép toán không hợp lệ.")

        # In kết quả
        label_result.config(text=f"Kết quả: {result}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")
    except ZeroDivisionError as e:
        messagebox.showerror("Lỗi", str(e))

def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Kết quả: ")

# Tạo cửa sổ chính
app = tk.Tk()
app.title("Máy tính đơn giản")
app.geometry("300x300")

# Tiêu đề
label_title = tk.Label(app, text="Máy tính đơn giản", font=("Arial", 16))
label_title.pack(pady=10)

# Nhập số thứ nhất
label_num1 = tk.Label(app, text="Số thứ nhất:")
label_num1.pack()
entry_num1 = tk.Entry(app, width=20, font=("Arial", 14), justify="center")
entry_num1.pack(pady=5)

# Nhập số thứ hai
label_num2 = tk.Label(app, text="Số thứ hai:")
label_num2.pack()
entry_num2 = tk.Entry(app, width=20, font=("Arial", 14), justify="center")
entry_num2.pack(pady=5)

# Các nút phép toán
frame_buttons = tk.Frame(app)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Cộng (+)", command=lambda: calculate("+"), width=8, bg="lightblue")
btn_add.grid(row=0, column=0, padx=5)

btn_subtract = tk.Button(frame_buttons, text="Trừ (-)", command=lambda: calculate("-"), width=8, bg="lightblue")
btn_subtract.grid(row=0, column=1, padx=5)

btn_multiply = tk.Button(frame_buttons, text="Nhân (*)", command=lambda: calculate("*"), width=8, bg="lightblue")
btn_multiply.grid(row=1, column=0, padx=5)

btn_divide = tk.Button(frame_buttons, text="Chia (/)", command=lambda: calculate("/"), width=8, bg="lightblue")
btn_divide.grid(row=1, column=1, padx=5)

# Nút xóa
btn_clear = tk.Button(app, text="Xóa", command=clear, width=10, bg="lightcoral")
btn_clear.pack(pady=10)

# Hiển thị kết quả
label_result = tk.Label(app, text="Kết quả: ", font=("Arial", 14))
label_result.pack(pady=10)

# Chạy ứng dụng
app.mainloop()