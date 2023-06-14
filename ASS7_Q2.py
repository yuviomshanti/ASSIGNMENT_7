import tkinter as tk
import calendar

def show_calendar():
    year = int(year_entry.get())
    cal_data = calendar.calendar(year)
    calendar_text.delete("1.0", tk.END)
    calendar_text.insert(tk.END, cal_data)

# Create the main window
window = tk.Tk()
window.title("Calendar Application")

# Create a label and entry field for the year
year_label = tk.Label(window, text="Enter the Year:")
year_label.pack()
year_entry = tk.Entry(window)
year_entry.pack()

# Create a button to show the calendar
show_button = tk.Button(window, text="Show Calendar", command=show_calendar)
show_button.pack()

# Create a text widget to display the calendar
calendar_text = tk.Text(window, height=15, width=30)
calendar_text.pack()

# Start the main loop
window.mainloop()

