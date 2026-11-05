import tkinter as tk
from tkinter import ttk, messagebox
import ipaddress
import os
import csv

# ==============================
# MAIN WINDOW
# ==============================

root = tk.Tk()
root.title("NetWatch")
root.geometry("1100x700")
root.configure(bg="#0f172a")

# ==============================
# DEVICE DATA
# ==============================

devices = [
    {
        "name": "Main Server",
        "ip": "192.168.1.10",
        "type": "Server",
        "status": "Online"
    },
    {
        "name": "Office Computer",
        "ip": "192.168.1.20",
        "type": "Computer",
        "status": "Online"
    },
    {
        "name": "Network Printer",
        "ip": "192.168.1.30",
        "type": "Printer",
        "status": "Offline"
    }
]

# saves the devices to CSV
def save_devices():
    with open("devices.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "ip", "type", "status"]
        )
        writer.writeheader()
        writer.writerows(devices)


# Load devices from CSV
def load_devices():
    if not os.path.exists("devices.csv"):
        return

    with open("devices.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        devices.clear()

        for row in reader:
            devices.append(row)


# ==============================
# HEADER
# ==============================

header = tk.Frame(root, bg="#0f172a")
header.pack(fill="x", pady=(20, 20))

title = tk.Label(
    header,
    text="NETWATCH",
    font=("Times New Roman", 24, "bold"),
    fg="white",
    bg="#0f172a"
)
title.pack()

subtitle = tk.Label(
    header,
    text="NETWORK SECURITY MONITORING TOOL",
    font=("Times New Roman", 12, "bold"),
    fg="#94a3b8",
    bg="#0f172a"
)
subtitle.pack()

# ==============================
# MAIN LAYOUT
# ==============================

main_frame = tk.Frame(root, bg="#0f172a")
main_frame.pack(fill="both", expand=True)

# ==============================
# SIDEBAR
# ==============================

sidebar = tk.Frame(
    main_frame,
    bg="#1e293b",
    width=220
)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

# ==============================
# MAIN CONTENT AREA
# ==============================

content = tk.Frame(
    main_frame,
    bg="#0f172a"
)
content.pack(side="right", fill="both", expand=True)

# ==============================
# CLEAR CONTENT AREA
# ==============================

def clear_main_area():
    for widget in content.winfo_children():
        widget.destroy()


# ==============================
# DASHBOARD PAGE
# ==============================

def show_dashboard():
    clear_main_area()

    heading = tk.Label(
        content,
        text="Dashboard",
        font=("Times New Roman", 22, "bold"),
        fg="white",
        bg="#0f172a"
    )
    heading.pack(anchor="w", padx=30, pady=30)

    welcome = tk.Label(
        content,
        text="Welcome to NetWatch Network Security Monitoring.",
        font=("Times New Roman", 12),
        fg="#94a3b8",
        bg="#0f172a"
    )
    welcome.pack(anchor="w", padx=30)

    device_count = tk.Label(
        content,
        text=f"Devices in Inventory: {len(devices)}",
        font=("Times New Roman", 14, "bold"),
        fg="white",
        bg="#0f172a"
    )
    device_count.pack(anchor="w", padx=30, pady=20)


# ==============================
# DEVICE INVENTORY PAGE
# ==============================

def show_inventory():
    clear_main_area()

    heading = tk.Label(
        content,
        text="Device Inventory",
        font=("Times New Roman", 22, "bold"),
        fg="white",
        bg="#0f172a"
    )
    heading.pack(anchor="w", padx=30, pady=(30, 15))

    # Device table

    columns = ("name", "ip", "type", "status")

    device_table = ttk.Treeview(
        content,
        columns=columns,
        show="headings"
    )

    device_table.heading("name", text="Device Name")
    device_table.heading("ip", text="IP Address")
    device_table.heading("type", text="Device Type")
    device_table.heading("status", text="Status")

    device_table.column("name", width=180)
    device_table.column("ip", width=150)
    device_table.column("type", width=150)
    device_table.column("status", width=120)

    device_table.pack(
        fill="x",
        padx=30,
        pady=10
    )

    # Load existing devices into the table

    for device in devices:
        device_table.insert(
            "",
            "end",
            values=(
                device["name"],
                device["ip"],
                device["type"],
                device["status"]
            )
        )

    # Add device section

    add_heading = tk.Label(
        content,
        text="Add New Device",
        font=("Times New Roman", 16, "bold"),
        fg="white",
        bg="#0f172a"
    )
    add_heading.pack(anchor="w", padx=30, pady=(25, 10))

    # Device name input

    name_label = tk.Label(
        content,
        text="Device Name",
        fg="white",
        bg="#0f172a"
    )
    name_label.pack(anchor="w", padx=30)

    name_entry = tk.Entry(
        content,
        width=35,
        font=("Times New Roman", 11)
    )
    name_entry.pack(anchor="w", padx=30, pady=(5, 10))

    # IP address input

    ip_label = tk.Label(
        content,
        text="IP Address",
        fg="white",
        bg="#0f172a"
    )
    ip_label.pack(anchor="w", padx=30)

    ip_entry = tk.Entry(
        content,
        width=35,
        font=("Times New Roman", 11)
    )
    ip_entry.pack(anchor="w", padx=30, pady=(5, 10))

    # Device type dropdown

    type_label = tk.Label(
        content,
        text="Device Type",
        fg="white",
        bg="#0f172a"
    )
    type_label.pack(anchor="w", padx=30)

    type_box = ttk.Combobox(
        content,
        values=["Server", "Computer", "Printer", "Router", "Other"],
        state="readonly",
        width=32
    )
    type_box.set("Server")
    type_box.pack(anchor="w", padx=30, pady=10)

    # Add device function

    def add_device():

        device_name = name_entry.get().strip()
        device_ip = ip_entry.get().strip()
        device_type = type_box.get()

        # Check for empty fields

        if not device_name or not device_ip or not device_type:
            messagebox.showerror(
                "Missing Information",
                "Please fill in all fields."
            )
            return

        # Validate IPv4 address

        try:
            ipaddress.IPv4Address(device_ip)

        except ipaddress.AddressValueError:
            messagebox.showerror(
                "Invalid IP Address",
                "Please enter a valid IPv4 address."
            )
            return

        # Check for duplicate IP addresses

        for device in devices:
            if device["ip"] == device_ip:
                messagebox.showerror(
                    "Duplicate IP",
                    "A device with this IP address already exists."
                )
                return

        # Create new device

        new_device = {
            "name": device_name,
            "ip": device_ip,
            "type": device_type,
            "status": "Online"
        }

        # Add device to Python list

        devices.append(new_device)

        # saves the device
        save_devices()

        # Add device to table

        device_table.insert(
            "",
            "end",
            values=(
                new_device["name"],
                new_device["ip"],
                new_device["type"],
                new_device["status"]
            )
        )

        # Clear input fields

        name_entry.delete(0, tk.END)
        ip_entry.delete(0, tk.END)
        type_box.set("Server")

        messagebox.showinfo(
            "Device Added",
            f"{device_name} was successfully added."
        )

    # Delete device

    def remove_device():

        # Get the selected row
        selected_item = device_table.selection()

        # Check if something is selected
        if not selected_item:
            messagebox.showwarning(
                "No Selection",
                "Please select a device to remove."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Deletion",
            "Are you sure you want to delete this device"
        )
        if not confirm:
            return

        # Get information from selected row
        device_data = device_table.item(selected_item[0])

        # Get IP address
        selected_ip = device_data["values"][1]

        # Remove device from Python list
        for device in devices:
            if device["ip"] == selected_ip:
                devices.remove(device)
                save_devices()
                break

        # Remove device from table
        device_table.delete(selected_item[0])

    def update_status():
        selected = device_table.selection()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please select device first."
            )
            return

        item = device_table.item(selected[0])
        values = item["values"]
        device_ip = values[1]

        #checks each device the checks if ip matches device
        for device in devices:
            if device["ip"] == device_ip:
                break
        else:
            messagebox.showerror(
                "Error",
                "Device not found."
            )
            return

        if device["status"] == "Online":
            device["status"] = "Offline"
        else:
            device["status"] = "Online"

        device_table.item(
            selected[0],
            values=(
                device["name"],
                device["ip"],
                device["type"],
                device["status"]
            )
        )
        save_devices()

    # ==============================
    # BUTTON FRAME
    # ==============================

    button_frame = tk.Frame(
        content,
        bg="#0f172a"
    )

    button_frame.pack(
        anchor="nw",
        padx=30,
        pady=10
    )

    # Add device button

    add_button = tk.Button(
        button_frame,
        text="Add Device",
        command=add_device,
        bg="#2563eb",
        fg="white",
        font=("Times New Roman", 12, "bold"),
        relief="flat",
        height=2,
        width=18
    )

    add_button.pack(side="left", padx=(0, 10))

    # Create Remove button

    remove_button = tk.Button(
        button_frame,
        text="Remove Device",
        command=remove_device,
        bg="#dc2626",
        fg="white",
        font=("Times New Roman", 12, "bold"),
        relief="flat",
        height=2,
        width=18
    )

    remove_button.pack(side="left")


# ==============================
# PORT ANALYZER PAGE
# ==============================

def show_port_analyzer():
    clear_main_area()

    heading = tk.Label(
        content,
        text="Port Analyzer",
        font=("Times New Roman", 22, "bold"),
        fg="white",
        bg="#0f172a"
    )
    heading.pack(anchor="w", padx=30, pady=30)

    description = tk.Label(
        content,
        text="Analyze ports and identify their commonly associated services.",
        font=("Times New Roman", 12),
        fg="#94a3b8",
        bg="#0f172a"
    )
    description.pack(anchor="w", padx=30)


# ==============================
# TRAFFIC ANALYSIS PAGE
# ==============================

def show_traffic_analysis():
    clear_main_area()

    heading = tk.Label(
        content,
        text="Traffic Analysis",
        font=("Times New Roman", 22, "bold"),
        fg="white",
        bg="#0f172a"
    )
    heading.pack(anchor="w", padx=30, pady=30)

    description = tk.Label(
        content,
        text="Analyze network traffic records and identify patterns.",
        font=("Times New Roman", 12),
        fg="#94a3b8",
        bg="#0f172a"
    )
    description.pack(anchor="w", padx=30)


# ==============================
# SECURITY ALERTS PAGE
# ==============================

def show_security_alerts():
    clear_main_area()

    heading = tk.Label(
        content,
        text="Security Alerts",
        font=("Times New Roman", 22, "bold"),
        fg="white",
        bg="#0f172a"
    )
    heading.pack(anchor="w", padx=30, pady=30)

    description = tk.Label(
        content,
        text="Security alerts and suspicious activity will appear here.",
        font=("Times New Roman", 12),
        fg="#94a3b8",
        bg="#0f172a"
    )
    description.pack(anchor="w", padx=30)


# ==============================
# SIDEBAR BUTTONS
# ==============================

button_style = {
    "font": ("Arial", 11),
    "fg": "white",
    "bg": "#1e293b",
    "activebackground": "#334155",
    "activeforeground": "white",
    "relief": "flat",
    "anchor": "w",
    "padx": 20,
    "pady": 15
}

dashboard_button = tk.Button(
    sidebar,
    text="Dashboard",
    command=show_dashboard,
    **button_style
)
dashboard_button.pack(fill="x")

inventory_button = tk.Button(
    sidebar,
    text="Device Inventory",
    command=show_inventory,
    **button_style
)
inventory_button.pack(fill="x")

port_button = tk.Button(
    sidebar,
    text="Port Analyzer",
    command=show_port_analyzer,
    **button_style
)
port_button.pack(fill="x")

traffic_button = tk.Button(
    sidebar,
    text="Traffic Analysis",
    command=show_traffic_analysis,
    **button_style
)
traffic_button.pack(fill="x")

alerts_button = tk.Button(
    sidebar,
    text="Security Alerts",
    command=show_security_alerts,
    **button_style
)
alerts_button.pack(fill="x")


# ==============================
# START PROGRAM
# ==============================

load_devices()

show_dashboard()

root.mainloop()

