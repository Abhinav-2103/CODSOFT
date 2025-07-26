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
root.resizable(False, False)

tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Address").grid(row=3, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=4, column=1, pady=5)

tk.Label(root, text="Search").grid(row=5, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=5, column=1)
tk.Button(root, text="Search", command=search_contact).grid(row=5, column=2)

contact_list = tk.Listbox(root, width=50)
contact_list.grid(row=6, column=0, columnspan=3, pady=10)

root.mainloop()
