import threading
from tkinter import *
from tkinter import filedialog, messagebox
from scanner import start_scanner
from organizer import initial_scan

# ---------- THEME ----------
BG_COLOR = "#1e1e1e"
PANEL_COLOR = "#2b2b2b"
TEXT_COLOR = "white"
SUBTEXT_COLOR = "#cfcfcf"
BTN_START = "#2ecc71"
BTN_BROWSE = "#555555"

# ---------- MAIN WINDOW ----------
root = Tk()
root.title("AI Based Directory Management System")
root.geometry("700x520")
root.configure(bg=BG_COLOR)

# ---------- VARIABLES ----------
status_text = StringVar(value="Ready")
folder_text = StringVar(value="Not Selected")
ai_status_text = StringVar(value="OFF")
count_text = StringVar(value="0")
last_action_text = StringVar(value="None")

file_count = 0

# ---------- FUNCTIONS ----------
# In gui.py, update this function
def add_log(msg):
    global file_count
    file_count += 1
    count_text.set(str(file_count))
    last_action_text.set(msg)

    # 🔹 ADD encoding="utf-8" HERE
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def choose_folder():
    path = filedialog.askdirectory()
    if path:
        folder_text.set(path)

def start_ai():
    path = folder_text.get()
    if path == "Not Selected":
        messagebox.showerror("Error", "Please select a folder first")
        return

    ai_status_text.set("ON")
    status_text.set("Initial scan running...")

    # 🔹 NEW: Categorize existing files
    initial_scan(path, add_log)

    status_text.set("AI Monitoring Running")

    t = threading.Thread(
        target=start_scanner,
        args=(path, add_log),
        daemon=True
    )
    t.start()

# ---------- TITLE ----------
Label(
    root,
    text="AI Based Directory Management System",
    font=("Arial", 18, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
).pack(pady=10)

# ---------- DASHBOARD ----------
dashboard = Frame(root, bg=BG_COLOR)
dashboard.pack(pady=10)

def create_card(title, variable):
    card = Frame(dashboard, bg=PANEL_COLOR, width=340, height=60)
    card.pack(pady=6)
    card.pack_propagate(False)

    Label(
        card, text=title,
        bg=PANEL_COLOR, fg=SUBTEXT_COLOR,
        font=("Arial", 10)
    ).pack(anchor="w", padx=10, pady=(5, 0))

    Label(
        card, textvariable=variable,
        bg=PANEL_COLOR, fg=TEXT_COLOR,
        font=("Arial", 12, "bold"),
        wraplength=320, justify=LEFT
    ).pack(anchor="w", padx=10)

create_card("📂 Selected Folder", folder_text)
create_card("🧠 AI Status", ai_status_text)
create_card("📊 Files Organized", count_text)
create_card("🕒 Last Action", last_action_text)

# ---------- CONTROLS ----------
controls = Frame(root, bg=BG_COLOR)
controls.pack(pady=15)

Button(
    controls, text="Browse Folder",
    command=choose_folder,
    bg=BTN_BROWSE, fg=TEXT_COLOR,
    width=18
).pack(side=LEFT, padx=10)

Button(
    controls, text="Start Monitoring",
    command=start_ai,
    bg=BTN_START, fg="black",
    width=18
).pack(side=LEFT, padx=10)

# ---------- STATUS BAR ----------
status_bar = Label(
    root, textvariable=status_text,
    bg=PANEL_COLOR, fg=TEXT_COLOR,
    anchor=W, padx=10
)
status_bar.pack(side=BOTTOM, fill=X)

# ---------- RUN GUI ----------
if __name__ == "__main__":
    root.mainloop()
