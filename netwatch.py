
import tkinter as tk

# Create the main window
root = tk.Tk()
#Sets window title
root.title("Netwatch")
#sets window dimensions
root.geometry("1100x700")
#sets backround as dark blue
root.configure(bg="#0f172a")

#Displays "Netwatch" in the center of the window with a large font size
title = tk.Label(
    root,
    text="NETWATCH",
    font=("Times New Roman", 24, "bold"),
    bg="#0f172a",
    fg="white"
)
#Displays "NETWORK SECURITY MONITORING TOOL" in the center of the window with a smaller font size
subheading = tk.Label(
    root,
    text="NETWORK SECURITY MONITORING TOOL",
    font=("Times New Roman", 12, "bold"),
    bg="#0f172a",
    fg="#94a3b8"
)
#Spacing for both titles
title.pack(pady=(20, 2))
subheading.pack(pady=(0, 20))

#Creates a sidebar frame on the left side of the window with a width of 220 pixels and a dark blue background color
sidebar = tk.Frame(root, width=220, bg="#1e293b")
sidebar.pack(side="left", fill="y")

#Creates a main area frame on the right side of the window with a dark blue background color
main_area = tk.Frame(root, bg="#0f172a")
main_area.pack(side="right", fill="both", expand=True)

#Creates a button in the sidebar with the text "Dashboard", a font size of 12, a dark blue background color, white text color, and a flat relief style
dashboard_button = tk.Button(
    sidebar,
    text="Dashboard",
    font=("Times New Roman", 12),
    bg="#334155",
    fg="white",
    relief="flat",
)
dashboard_button.pack(fill="x", padx=10, pady=5)

device_inventory_button = tk.Button(
    sidebar,
    text="Device Inventory",
    font=("Times New Roman", 12),
    bg="#334155",
    fg="white",
    relief="flat",
)
device_inventory_button.pack(fill="x", padx=10, pady=5)

port_analyzer_button = tk.Button(
    sidebar,
    text="Port Analyzer",
    font=("Times New Roman", 12),
    bg="#334155",
    fg="white",
    relief="flat",
)
port_analyzer_button.pack(fill="x", padx=10, pady=5)

traffic_analysis_button = tk.Button(
    sidebar,
    text="Traffic Analysis",
    font=("Times New Roman", 12),
    bg="#334155",
    fg="white",
    relief="flat",
)
traffic_analysis_button.pack(fill="x", padx=10, pady=5)

security_alert_button = tk.Button(
    sidebar,
    text="Security Alerts",
    font=("Times New Roman", 12),
    bg="#334155",
    fg="white",
    relief="flat",
)
security_alert_button.pack(fill="x", padx=10, pady=5)

root.mainloop()
