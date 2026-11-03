
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()

# Sets window title
root.title("Netwatch")

# Sets window dimensions
root.geometry("1100x700")

# Sets background as dark blue
root.configure(bg="#0f172a")


# Displays "Netwatch" in the center of the window
title = tk.Label(
    root,
    text="NETWATCH",
    font=("Times New Roman", 24, "bold"),
    bg="#0f172a",
    fg="white"
)

# Displays the subtitle
subheading = tk.Label(
    root,
    text="NETWORK SECURITY MONITORING TOOL",
    font=("Times New Roman", 12, "bold"),
    bg="#0f172a",
    fg="#94a3b8"
)

# Spacing for both titles
title.pack(pady=(20, 2))
subheading.pack(pady=(0, 20))


# Creates the sidebar frame
sidebar = tk.Frame(root, width=220, bg="#1e293b")
sidebar.pack(side="left", fill="y")

# Prevents the sidebar from shrinking
sidebar.pack_propagate(False)


# Creates the main content area
main_area = tk.Frame(root, bg="#0f172a")
main_area.pack(side="right", fill="both", expand=True)


# Stores network device information
devices = [
    {
        "name": "Main Server",
        "ip": "192.168.1.10",
        "type": "Server",
        "status": "Online"
    },
    {
        "name": "Office Computer",
        "ip": "192.168.1.15",
        "type": "Workstation",
        "status": "Online"
    },
    {
        "name": "Network Printer",
        "ip": "192.168.1.20",
        "type": "Printer",
        "status": "Offline"
    }
]


# Function to clear the main area
def clear_main_area():
    for widget in main_area.winfo_children():
        widget.destroy()


# Displays the Dashboard page
def show_dashboard():

    clear_main_area()

    heading = tk.Label(
        main_area,
        text="Dashboard",
        font=("Times New Roman", 24, "bold"),
        bg="#0f172a",
        fg="white"
    )
    heading.pack(pady=20)

    subtitle = tk.Label(
        main_area,
        text="Welcome to NetWatch",
        font=("Arial", 12),
        bg="#0f172a",
        fg="#94a3b8"
    )
    subtitle.pack()


# Displays the Device Inventory page
def show_inventory():

    clear_main_area()

    # Display page heading
    heading = tk.Label(
        main_area,
        text="Device Inventory",
        font=("Times New Roman", 24, "bold"),
        bg="#0f172a",
        fg="white"
    )
    heading.pack(pady=20)

    # Display subtitle
    subtitle = tk.Label(
        main_area,
        text="Manage and monitor network devices",
        font=("Arial", 12),
        bg="#0f172a",
        fg="#94a3b8"
    )
    subtitle.pack()

    # Create device table
    device_table = ttk.Treeview(
        main_area,
        columns=("name", "ip", "type", "status"),
        show="headings"
    )

    # Set column headings
    device_table.heading("name", text="Device Name")
    device_table.heading("ip", text="IP Address")
    device_table.heading("type", text="Device Type")
    device_table.heading("status", text="Status")

    # Set column widths
    device_table.column("name", width=200)
    device_table.column("ip", width=150)
    device_table.column("type", width=150)
    device_table.column("status", width=120)

    # Display table
    device_table.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # Insert all devices into table
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


# Displays the Port Analyzer page
def show_port_analyzer():

    clear_main_area()

    heading = tk.Label(
        main_area,
        text="Port Analyzer",
        font=("Times New Roman", 24, "bold"),
        bg="#0f172a",
        fg="white"
    )
    heading.pack(pady=20)

    subtitle = tk.Label(
        main_area,
        text="Analyze network ports and traffic",
        font=("Arial", 12),
        bg="#0f172a",
        fg="#94a3b8"
    )
    subtitle.pack()


# Displays the Security Alerts page
def show_security_alerts():

    clear_main_area()

    heading = tk.Label(
        main_area,
        text="Security Alerts",
        font=("Times New Roman", 24, "bold"),
        bg="#0f172a",
        fg="white"
    )
    heading.pack(pady=20)

    subtitle = tk.Label(
        main_area,
        text="Monitor and respond to security threats",
        font=("Arial", 12),
        bg="#0f172a",
        fg="#94a3b8"
    )
    subtitle.pack()


# Displays the Traffic Analysis page
def show_traffic_analysis():

    clear_main_area()

    heading = tk.Label(
        main_area,
        text="Traffic Analysis",
        font=("Times New Roman", 24, "bold"),
        bg="#0f172a",
        fg="white"
    )
    heading.pack(pady=20)

    subtitle = tk.Label(
        main_area,
        text="Analyze network traffic patterns",
        font=("Arial", 12),
        bg="#0f172a",
        fg="#94a3b8"
    )
    subtitle.pack()


# Creates the Dashboard button
dashboard_button = tk.Button(
    sidebar,
    text="Dashboard",
    font=("Times New Roman", 12),
    bg="#334155",
    fg="white",
    relief="flat",
    command=show_dashboard
)
dashboard_button.pack(fill="x", padx=10, pady=5)


# Creates the Device Inventory button
device_inventory_button = tk.Button(
    sidebar,
    text="Device Inventory",
    font=("Times New Roman", 12),
    bg="#334155",
    fg="white",
    relief="flat",
    command=show_inventory
)
device_inventory_button.pack(fill="x", padx=10, pady=5)


# Creates the Port Analyzer button
port_analyzer_button = tk.Button(
    sidebar,
    text="Port Analyzer",
    font=("Times New Roman", 12),
    bg="#334155",
    fg="white",
    relief="flat",
    command=show_port_analyzer
)
port_analyzer_button.pack(fill="x", padx=10, pady=5)


# Creates the Traffic Analysis button
traffic_analysis_button = tk.Button(
    sidebar,
    text="Traffic Analysis",
    font=("Times New Roman", 12),
    bg="#334155",
    fg="white",
    relief="flat",
    command=show_traffic_analysis
)
traffic_analysis_button.pack(fill="x", padx=10, pady=5)


# Creates the Security Alerts button
security_alert_button = tk.Button(
    sidebar,
    text="Security Alerts",
    font=("Times New Roman", 12),
    bg="#334155",
    fg="white",
    relief="flat",
    command=show_security_alerts
)
security_alert_button.pack(fill="x", padx=10, pady=5)


# Opens the dashboard when the program starts
show_dashboard()

# Keeps the application running
root.mainloop()
