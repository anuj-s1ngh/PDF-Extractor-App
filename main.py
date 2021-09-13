from os import read, startfile
import tkinter as tk
from tkinter.filedialog import askopenfile
from PyPDF2 import PdfFileReader
from PIL import Image, ImageTk
import os
from pathlib import Path


# creating root window
root = tk.Tk()


# creating canvas object on top of root window
upper_canvas = tk.Canvas(
    root,
    width=600,
    height=300
)
upper_canvas.grid(
    columnspan=3,
    rowspan=3
)


# setting logo
logo_img = Image.open("logo.png")
logo_img_tk = ImageTk.PhotoImage(logo_img)
logo_label = tk.Label(
    root,
    image=logo_img_tk
)
logo_label.image = logo_img_tk
logo_label.grid(
    row=0,
    column=1
)


# instructions
instructions_label = tk.Label(
    root,
    text="Select a PDF file on your computer to extract all of it's text.",
    font="Raleway"
)
instructions_label.grid(
    row=1,
    column=0,
    columnspan=3
)


# Browse Button
def open_pdf_file():
    browse_text_var.set("Loading...")
    init_dir = os.path.join(Path.home(), "Documents")
    pdf_file = askopenfile(
        parent=root,
        mode="rb",
        title="Choose a PDF file",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")],
        initialdir=init_dir
    )
    if pdf_file:
        pdf = PdfFileReader(pdf_file)
        page = pdf.getPage(0)
        page_text = page.extractText()

        # frame for text box and scroll bar
        frame = tk.Frame(
            root
        )
        frame.grid(
            row=3,
            column=0,
            columnspan=3
        )

        #scroll bar
        scroll_y = tk.Scrollbar(
            frame,
            orient="vertical"
        )
        scroll_y.grid(
            row=3,
            column=2,
            columnspan=1,
            sticky="ns"
        )

        # text box
        text_box = tk.Text(
            frame,
            height=10,
            width=50,
            padx=15,
            pady=15,
            font=("Comic Sans MS", 11, "normal", "italic"),     # Font Options : (family:str, size:int in px, weight:str, slant:str("italic", "roman"), underline:int(0, 1), overstrike:int(0, 1))
            yscrollcommand=scroll_y.set
        )
        text_box.insert(1.0, page_text)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(
            row=3,
            column=0,
            columnspan=2
        )

        scroll_y.config(command=text_box.yview)

        browse_text_var.set("Browse Another PDF File")


browse_text_var = tk.StringVar()
browse_text_var.set("Browse A PDF File")

browse_btn = tk.Button(
    root,
    textvariable=browse_text_var,
    font="Raleway",
    bg="#20bebe",
    fg="#ffffff",
    height=2,
    width=30,
    command=open_pdf_file
)
browse_btn.grid(
    row=2,
    column=1
)


# creating another canvas
lower_canvas = tk.Canvas(
    root,
    width=600,
    height=250
)
lower_canvas.grid(
    columnspan=3,
    pady=20
)


root.mainloop()
