import tkinter as tk
from tkinter import messagebox
from cliente.vista import Frame, barrita_menu


def main():

    root = tk.Tk()
    root.title("Tu listado de Películas y Series")
    root.resizable(0, 0)
    barrita_menu(root)
    app = Frame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
