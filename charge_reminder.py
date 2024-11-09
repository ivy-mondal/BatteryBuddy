import customtkinter as ctk
from messages import nagging_mode


def charge_reminder():
    battery_result = None

    def on_submit():
        try:
            battery_level = int(battery_entry.get())
            if 0 <= battery_level <= 100:
                window.destroy()
                nagging_mode(battery_level)
                nonlocal battery_result  # Use nonlocal to modify outer variable
                battery_result = battery_level  # Store the result

            else:
                show_error("Trying to lie now QwQ")
        except ValueError:
            show_error("Numbers only, please!")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    window = ctk.CTk()
    window.title("Battery Buddy 🤗")
    window.configure(fg_color="#db5171")

    window.lift()
    window.attributes('-topmost', True)

    window_width = 500
    window_height = 300
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    frame = ctk.CTkFrame(window,
                         fg_color="#d96c86",
                         corner_radius=15,  # Rounded corners
                         border_width=2,  # Border width
                         border_color="#12136e"  # Border color
                         )

    frame.pack(pady=20, padx=20, fill="both", expand=True)

    title_label = ctk.CTkLabel(
        frame,
        text="Battery Check!",
        font=ctk.CTkFont(family="Times new roman", size=24, weight="bold"),
        text_color="#54152f"
    )
    title_label.pack(pady=10)

    message_label = ctk.CTkLabel(
        frame,
        text="Mr Fluffball!🙂 \nTime for a quick phone battery check UwU \nTell me, tell me, here:",
        font=ctk.CTkFont(family="Times new roman", size=15, weight="bold"),
        text_color="#14306b"
    )
    message_label.pack(pady=10)

    battery_entry = ctk.CTkEntry(
        frame,
        placeholder_text="Enter 0-100",
        width=200,
        font=ctk.CTkFont(family="Helvetica", size=12),
        fg_color="#f7e4e9",  # Entry background
        text_color="#851c36",  # Text color
        placeholder_text_color="#808080",  # Placeholder color
        border_color="#4A4A4A"
    )
    battery_entry.pack(pady=10)
    battery_entry.focus()

    def show_error(message):
        error_label.configure(text=message)
        error_label.pack(pady=10)
        window.after(3000, lambda: error_label.pack_forget())

    submit_button = ctk.CTkButton(
        frame,
        text="Submit",
        command=on_submit,
        width=200,
        height=40,
        font=ctk.CTkFont(family="Helvetica", size=14, weight="bold"),
        fg_color="#800610",  # Button color
        hover_color="#FF7000",  # Hover color
        corner_radius=10
    )
    submit_button.pack(pady=10)

    error_label = ctk.CTkLabel(
        frame,
        text="",
        font=ctk.CTkFont(family="Helvetica", size=14, weight="bold"),
        text_color="red"
    )

    def on_closing():
        show_error("You must enter your battery percentage!")

    window.protocol("WM_DELETE_WINDOW", on_closing)

    window.mainloop()

    return battery_result


if __name__ == "__main__":
    charge_reminder()
