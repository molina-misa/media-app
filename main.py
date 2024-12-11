import tkinter as tk
from tkinter import messagebox
from cliente.vista import Frame, barrita_menu


def main():

    root = tk.Tk()
    app = Frame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
