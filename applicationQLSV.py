import tkinter as tk
from tkinter import ttk, messagebox

# Danh sách sinh viên
students = []

# Hàm thêm sinh viên
def add_student():
    id = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    class_name = entry_class.get()

    if not id or not name or not age or not class_name:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return
    
    try:
        age = int(age)
        student = {"id": id, "name": name, "age": age, "class": class_name}
        students.append(student)
        update_student_list()
        clear_entries()
        messagebox.showinfo("Thành công", "Thêm sinh viên thành công!")
    except ValueError:
        messagebox.showerror("Lỗi", "Tuổi phải là một số nguyên!")

# Hàm hiển thị danh sách sinh viên
def update_student_list():
    for row in tree.get_children():
        tree.delete(row)
    for student in students:
        tree.insert("", "end", values=(student["id"], student["name"], student["age"], student["class"]))

# Hàm xóa sinh viên
def delete_student():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Lỗi", "Vui lòng chọn một sinh viên để xóa!")
        return
    
    for item in selected_item:
        values = tree.item(item, "values")
        for student in students:
            if student["id"] == values[0]:
                students.remove(student)
        tree.delete(item)
    messagebox.showinfo("Thành công", "Xóa sinh viên thành công!")

# Hàm tìm kiếm sinh viên
def search_student():
    search_id = entry_search.get()
    if not search_id:
        messagebox.showerror("Lỗi", "Vui lòng nhập mã sinh viên để tìm kiếm!")
        return
    
    for student in students:
        if student["id"] == search_id:
            tree.delete(*tree.get_children())
            tree.insert("", "end", values=(student["id"], student["name"], student["age"], student["class"]))
            return
    
    messagebox.showinfo("Kết quả", "Không tìm thấy sinh viên có mã đã nhập!")

# Hàm xóa dữ liệu trong ô nhập
def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_class.delete(0, tk.END)

# Giao diện ứng dụng
app = tk.Tk()
app.title("Quản lý sinh viên")
app.geometry("700x500")

# Tiêu đề
title_label = tk.Label(app, text="Quản lý sinh viên", font=("Arial", 18))
title_label.pack(pady=10)

# Khu vực nhập thông tin sinh viên
frame_input = tk.Frame(app)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Mã sinh viên:").grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(frame_input)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Tên:").grid(row=1, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_input)
entry_name.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Tuổi:").grid(row=2, column=0, padx=5, pady=5)
entry_age = tk.Entry(frame_input)
entry_age.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Lớp:").grid(row=3, column=0, padx=5, pady=5)
entry_class = tk.Entry(frame_input)
entry_class.grid(row=3, column=1, padx=5, pady=5)

# Nút thêm sinh viên
btn_add = tk.Button(frame_input, text="Thêm sinh viên", command=add_student, bg="lightblue")
btn_add.grid(row=4, column=0, columnspan=2, pady=10)

# Bảng hiển thị danh sách sinh viên
tree = ttk.Treeview(app, columns=("ID", "Name", "Age", "Class"), show="headings", height=10)
tree.pack(pady=20)
tree.heading("ID", text="Mã sinh viên")
tree.heading("Name", text="Tên")
tree.heading("Age", text="Tuổi")
tree.heading("Class", text="Lớp")

# Nút xóa và tìm kiếm sinh viên
frame_actions = tk.Frame(app)
frame_actions.pack(pady=10)

entry_search = tk.Entry(frame_actions)
entry_search.grid(row=0, column=0, padx=5)
btn_search = tk.Button(frame_actions, text="Tìm kiếm", command=search_student, bg="lightgreen")
btn_search.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_actions, text="Xóa sinh viên", command=delete_student, bg="lightcoral")
btn_delete.grid(row=0, column=2, padx=5)

# Chạy ứng dụng
app.mainloop()