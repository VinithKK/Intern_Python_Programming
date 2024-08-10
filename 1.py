import tkinter as tk
from datetime import datetime

def update_time():
    # Get the current time and format it with AM/PM
    current_time = datetime.now().strftime("%I:%M:%S %p")
    # Update the label with the current time
    time_label.config(text=current_time)
    # Schedule the update_time function to be called again after 1000ms (1 second)
    root.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Define neon colors
bg_color = "#04D9FF"  # Neon blue background
fg_color = "#005249"  # Neon orange foreground

# Create a label to display the time
time_label = tk.Label(root, font=("Helvetica", 48), bg=bg_color, fg=fg_color)
time_label.pack(expand=True)

# Call the update_time function to initialize the time display
update_time()

# Run the Tkinter event loop
root.mainloop()
