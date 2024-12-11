from .conecciondb import Conneccion


def crear_tabla():
    conn = Conneccion()

    sql1 = """
        CREATE TABLE IF NOT EXISTS Genero(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(50),
        PRIMARY KEY (ID AUTOINCREMENT)
        );
        """
    sql2 = """
        CREATE TABLE IF NOT EXISTS Peliculas(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(150),
        Duracion VARCHAR(4),
        Plataforma VARCHAR(100),
        Puntuacion VARCHAR(5),
        Genero INTEGER,
        PRIMARY KEY (ID AUTOINCREMENT),
        FOREIGN KEY (Genero) REFERENCES Genero(ID)
        );
"""
    try:
        conn.cursor.execute(sql1)
        conn.cursor.execute(sql2)
        conn.cerrar_con()
    except:
        pass


class Peliculas:

    def __init__(self, nombre, duracion, plataforma, puntuacion, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.plataforma = plataforma
        self.puntuacion = puntuacion
        self.genero = genero

    def __str__(self):
        return f"Pelicula[{self.nombre},{self.duracion},{self.plataforma},{self.puntuacion},{self.genero}]"


def guardar_peli(pelicula):
    conn = Conneccion()

    sql = f"""
        INSERT INTO Peliculas(Nombre,Duracion,Plataforma, Puntuacion, Genero)
        VALUES('{pelicula.nombre}','{pelicula.duracion}','{pelicula.plataforma}','{pelicula.puntuacion}',{pelicula.genero});
"""
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


def listar_peli():
    conn = Conneccion()
    listar_peliculas = []

    sql = f"""
        SELECT * FROM Peliculas as p
        INNER JOIN Genero as g
        ON p.Genero = g.ID;
"""
    try:
        conn.cursor.execute(sql)
        listar_peliculas = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_peliculas
    except:
        pass


def listar_generos():
    conn = Conneccion()
    listar_genero = []

    sql = f"""
        SELECT * FROM Genero;
"""
    try:
        conn.cursor.execute(sql)
        listar_genero = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_genero
    except:
        pass


def editar_peli(pelicula, id):
    conn = Conneccion()

    sql = f"""
        UPDATE Peliculas
        SET Nombre = '{pelicula.nombre}', Duracion = '{pelicula.duracion}', Plataforma = '{pelicula.plataforma}', Puntuacion = '{pelicula.puntuacion}', Genero = {pelicula.genero}
        WHERE ID = {id}
        ;
"""
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


def borrar_peli(id):
    conn = Conneccion()

    sql = f"""
        DELETE FROM Peliculas
        WHERE ID = {id}
        ;
"""
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass
