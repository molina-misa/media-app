import tkinter as tk
from cliente.vista import Frame_1, barrita_menu


def main():
    ventana = tk.Tk()
    ventana.title("Listado Películas")
    ventana.iconbitmap()
    ventana.resizable(False, False)

    barrita_menu(ventana)
    app = Frame_1(root=ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
