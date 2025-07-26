import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact added!")
    else:
        messagebox.showwarning("Input Error", "Name and phone are required.")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for c in contacts:
        contact_list.insert(tk.END, f"{c['name']} - {c['phone']}")

def search_contact():
    search_text = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for c in contacts:
        if search_text in c['name'].lower() or search_text in c['phone']:
            contact_list.insert(tk.END, f"{c['name']} - {c['phone']}")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        update_contact_list()
        messagebox.showinfo("Deleted", "Contact deleted.")
    else:
        messagebox.showwarning("Selection Error", "Select a contact to delete.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Book")
root.geometry("550x400")
root.configure(bg="beige")
root.resizable(False, False)

label_fg = "darkgreen"
btn_add_color = "#4CAF50"
btn_delete_color = "#F44336"
btn_clear_color = "#9E9E9E"
btn_search_color = "#2196F3"

tk.Label(root, text="Contact Book", bg="beige", fg="black", font=("futura", 18, "bold")).pack(pady=10)

tk.Label(root, text="Name", bg="beige", fg=label_fg, font=("ubuntu", 11)).place(x=30, y=60)
name_entry = tk.Entry(root, font=("ubuntu", 10))
name_entry.place(x=150, y=60)

tk.Label(root, text="Phone", bg="beige", fg=label_fg, font=("ubuntu", 11)).place(x=30, y=90)
phone_entry = tk.Entry(root, font=("ubuntu", 10))
phone_entry.place(x=150, y=90)

tk.Label(root, text="Email", bg="beige", fg=label_fg, font=("ubuntu", 11)).place(x=30, y=120)
email_entry = tk.Entry(root, font=("ubuntu", 10))
email_entry.place(x=150, y=120)

tk.Label(root, text="Address", bg="beige", fg=label_fg, font=("ubuntu", 11)).place(x=30, y=150)
address_entry = tk.Entry(root, font=("ubuntu", 10))
address_entry.place(x=150, y=150)

tk.Button(root, text="Add Contact", command=add_contact, bg=btn_add_color, fg="white", font=("ubuntu", 10)).place(x=50, y=190)
tk.Button(root, text="Delete Contact", command=delete_contact, bg=btn_delete_color, fg="white", font=("ubuntu", 10)).place(x=160, y=190)
tk.Button(root, text="Clear Fields", command=clear_entries, bg=btn_clear_color, fg="white", font=("ubuntu", 10)).place(x=280, y=190)

tk.Label(root, text="Search", bg="beige", fg=label_fg, font=("ubuntu", 11)).place(x=30, y=230)
search_entry = tk.Entry(root, font=("ubuntu", 10))
search_entry.place(x=150, y=230)
tk.Button(root, text="Search", command=search_contact, bg=btn_search_color, fg="white", font=("ubuntu", 10)).place(x=330, y=226)

contact_list = tk.Listbox(root, width=60, height=8, bg="white", fg="black", font=("ubuntu", 10))
contact_list.place(x=30, y=270)

root.mainloop()
