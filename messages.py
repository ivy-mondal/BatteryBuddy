import customtkinter as ctk


def nagging_mode(battery_level):
    root = ctk.CTk()
    dialog = ctk.CTkToplevel(root)
    dialog.title("BatteryBuddy Meows...")
    dialog.attributes('-topmost', True)

    ctk.set_appearance_mode("light")

    window_width = 500
    window_height = 300
    screen_width = dialog.winfo_screenwidth()
    screen_height = dialog.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    dialog.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    frame = ctk.CTkFrame(dialog,
                         fg_color="#FFE6F3",
                         corner_radius=20)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    progress = ctk.CTkProgressBar(
        frame,
        width=250,
        height=15,
        corner_radius=10,
        border_width=2,
        bg_color="#FFE6F3",
        border_color="#FF69B4"
    )
    progress.set(battery_level / 100)
    progress.pack(pady=15)

    if battery_level <= 35:
        message = "Excuse meh!!! I'm telling AWIFEO that yo being a bad boi -_-"
        color = "#FF1493"
    elif battery_level <= 70:
        message = "Yo know what to do neow UwU"
        color = "#FF69B4"
    elif battery_level <= 90:
        message = "I guess yo are behaving.....aighty 5 points for yo"
        color = "#FFB6C1"
    else:
        message = "Awwww look at yo being such goof boi! *proud cat noises*"
        color = "#851c36"

    title_label = ctk.CTkLabel(
        frame,
        text="✧ Meow Message ✧",
        font=ctk.CTkFont(size=18, weight="bold"),
        text_color=color,
        bg_color="#FFE6F3"
    )
    title_label.pack(pady=(0, 10))

    message_label = ctk.CTkLabel(
        frame,
        text=message,
        font=ctk.CTkFont(size=16),
        text_color=color,
        wraplength=300,
        bg_color="#FFE6F3"
    )
    message_label.pack(pady=15)

    def force_close():
        try:
            # Cancel ALL scheduled events
            root.after_cancel('all')
            for widget in dialog.winfo_children():
                if hasattr(widget, 'after_cancel'):
                    widget.after_cancel('all')
            dialog.after_cancel('all')
        except:
            pass
        finally:
            dialog.destroy()
            root.quit()
            root.destroy()

    def close_dialog():
        force_close()

    ok_button = ctk.CTkButton(
        frame,
        text="✧ *paws at screen* ✧",
        command=close_dialog,
        width=200,
        height=35,
        fg_color=color,
        hover_color="#FF69B4",
        corner_radius=15,
        font=ctk.CTkFont(size=14, weight="bold")
    )
    ok_button.pack(pady=15)

    progress.configure(progress_color=color)

    decorative_label1 = ctk.CTkLabel(
        frame,
        text="♡ ♡ ♡",
        font=ctk.CTkFont(size=20),
        text_color="#FF69B4",
        bg_color="#FFE6F3"
    )
    decorative_label1.pack(side="bottom", pady=5)

    dialog.after(8000, force_close)

    dialog.protocol("WM_DELETE_WINDOW", force_close)

    root.withdraw()

    try:
        root.mainloop()
    except:
        force_close()


if __name__ == "__main__":
    nagging_mode(100)
