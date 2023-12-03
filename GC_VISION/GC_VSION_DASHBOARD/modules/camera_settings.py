import tkinter as tk

def show_settings(cap):
    settings_window = tk.Toplevel()
    settings_window.title("Camera Settings")

    # Example: Add widgets for camera settings
    label_dimension = tk.Label(settings_window, text="Video Dimension:")
    label_dimension.pack()

    entry_width = tk.Entry(settings_window)
    entry_width.insert(0, str(cap.get(3)))  # Width
    entry_width.pack()

    entry_height = tk.Entry(settings_window)
    entry_height.insert(0, str(cap.get(4)))  # Height
    entry_height.pack()

    apply_button = tk.Button(settings_window, text="Apply", command=lambda: apply_settings(cap, entry_width, entry_height))
    apply_button.pack()

def apply_settings(cap, entry_width, entry_height):
    new_width = int(entry_width.get())
    new_height = int(entry_height.get())

    cap.set(3, new_width)
    cap.set(4, new_height)

    print(f"Applied new video dimension: {new_width} x {new_height}")
