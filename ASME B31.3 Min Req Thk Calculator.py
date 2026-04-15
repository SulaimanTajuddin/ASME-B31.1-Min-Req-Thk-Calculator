import tkinter as tk
from tkinter import messagebox

def calculate_thickness():
    try:
        # Read input values
        P = float(entry_pressure.get())      # MPa
        D = float(entry_diameter.get())      # mm
        S = float(entry_stress.get())        # MPa
        E = float(entry_efficiency.get())
        W = float(entry_weld_factor.get())
        Y = float(entry_y.get())
        c = float(entry_ca.get())            # mm

        # ASME B31.3 thickness equation
        t = (P * D) / (2 * (S * E * W + P * Y)) + c

        label_result.config(
            text=f"Minimum Required Thickness:\n{t:.3f} mm",
            fg="green"
        )

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid numeric values."
        )


# ---------------- GUI SETUP ---------------- #

root = tk.Tk()
root.title("ASME B31.3 Minimum Thickness Calculator")
root.geometry("480x420")
root.resizable(False, False)

title = tk.Label(
    root,
    text="ASME B31.3 Pipe Thickness Calculator",
    font=("Arial", 14, "bold")
)
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

# Helper function for labels and entries
def create_row(text, row):
    tk.Label(frame, text=text, anchor="w", width=28).grid(row=row, column=0, pady=3)
    entry = tk.Entry(frame, width=15)
    entry.grid(row=row, column=1)
    return entry

entry_pressure = create_row("Design Pressure P (MPa)", 0)
entry_diameter = create_row("Outside Diameter D (mm)", 1)
entry_stress = create_row("Allowable Stress S (MPa)", 2)
entry_efficiency = create_row("Weld Joint Efficiency E", 3)
entry_weld_factor = create_row("Weld Strength Factor W", 4)
entry_y = create_row("Parameter Y", 5)
entry_ca = create_row("Corrosion Allowance c (mm)", 6)

btn_calculate = tk.Button(
    root,
    text="Calculate Thickness",
    command=calculate_thickness,
    width=25,
    bg="#1f7aff",
    fg="white"
)
btn_calculate.pack(pady=15)

label_result = tk.Label(
    root,
    text="Minimum Required Thickness:\n—",
    font=("Arial", 11, "bold"),
    fg="blue"
)
label_result.pack(pady=10)

footer = tk.Label(
    root,
    text="Based on ASME B31.3 – Design Pressure Formula\nFor engineering use only",
    font=("Arial", 9),
    fg="gray"
)
footer.pack(side="bottom", pady=10)

root.mainloop()