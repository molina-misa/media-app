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
        CREATE TABLE IF NOT EXISTS Plataforma(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(50),
        PRIMARY KEY (ID AUTOINCREMENT)
        );
    """
    sql3 = """
        CREATE TABLE IF NOT EXISTS Peliculas(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(150),
        Duracion VARCHAR(4),
        Plataforma VARCHAR(100),
        Puntuacion VARCHAR(5),
        Genero INTEGER,
        PRIMARY KEY (ID AUTOINCREMENT),
        FOREIGN KEY (Genero) REFERENCES Genero(ID),
        FOREIGN KEY (Plataforma) REFERENCES Plataforma(ID)
        );
"""
    sql4 = """
    CREATE TABLE IF NOT EXISTS Series(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(150),
        Duracion VARCHAR(4),
        Plataforma VARCHAR(100),
        Puntuacion VARCHAR(5),
        Genero INTEGER,
        PRIMARY KEY (ID AUTOINCREMENT),
        FOREIGN KEY (Genero) REFERENCES Genero(ID),
        FOREIGN KEY (Plataforma) REFERENCES Plataforma(ID)
        );
    """

    try:
        conn.cursor.execute(sql1)
        conn.cursor.execute(sql2)
        conn.cursor.execute(sql3)
        conn.cursor.execute(sql4)
        conn.cerrar_con()
    except:
        pass


### Metodos para el manejo de la tabla Peliculas


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
        INSERT INTO Peliculas(Nombre,Duracion,Plataforma,Puntuacion, Genero)
        VALUES('{pelicula.nombre}','{pelicula.duracion}',{pelicula.plataforma},'{pelicula.puntuacion}',{pelicula.genero});
"""
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


def get_movies():
    conn = Conneccion()
    movies = []

    conn.cursor.execute(
        """
        SELECT p.ID, p.nombre, p.duracion, pl.Nombre AS plataforma, p.puntuacion, g.Nombre AS genero 
        FROM peliculas AS p 
        INNER JOIN genero AS g ON p.genero = g.ID 
        INNER JOIN plataforma AS pl ON p.plataforma = pl.ID;

        """
    )
    movies = conn.cursor.fetchall()
    conn.cerrar_con()
    return movies


def editar_peli(pelicula, id):
    conn = Conneccion()

    sql = f"""
        UPDATE Peliculas
        SET Nombre = '{pelicula.nombre}', Duracion = '{pelicula.duracion}', Plataforma = {pelicula.plataforma}, Puntuacion = '{pelicula.puntuacion}', Genero = {pelicula.genero}
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


### Metodos para el manejo de la tabla Series


class Series:
    def __init__(self, nombre, duracion, plataforma, puntuacion, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.plataforma = plataforma
        self.puntuacion = puntuacion
        self.genero = genero

    def __str__(self):
        return f"Series[{self.nombre},{self.duracion},{self.plataforma},{self.puntuacion},{self.genero}]"


def guardar_serie(serie):
    conn = Conneccion()

    sql = f"""
        INSERT INTO Series(Nombre,Duracion,Plataforma, Puntuacion, Genero)
        VALUES('{serie.nombre}','{serie.duracion}',{serie.plataforma},'{serie.puntuacion}',{serie.genero});
"""
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


def get_series():
    conn = Conneccion()
    series = []

    conn.cursor.execute(
        """
        SELECT s.ID, s.nombre, s.duracion, pl.Nombre AS plataforma, s.puntuacion, g.Nombre AS genero 
        FROM series AS s
        INNER JOIN genero AS g ON s.genero = g.ID 
        INNER JOIN plataforma AS pl ON s.plataforma = pl.ID;
        """
    )
    series = conn.cursor.fetchall()
    conn.cerrar_con()
    return series


def editar_serie(serie, id):
    conn = Conneccion()

    sql = f"""
        UPDATE Series
        SET Nombre = '{serie.nombre}', Duracion = '{serie.duracion}', Plataforma = {serie.plataforma}, Puntuacion = '{serie.puntuacion}', Genero = {serie.genero}
        WHERE ID = {id}
        ;
"""
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


def borrar_serie(id):
    conn = Conneccion()

    sql = f"""
        DELETE FROM Series
        WHERE ID = {id}
        ;
"""
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


### Metodos para mostrar la tabla generos y plataformas


def listar_generos():
    conn = Conneccion()
    listar_genero = []

    sql = f"""
        SELECT * FROM Genero ORDER BY ID;
"""
    try:
        conn.cursor.execute(sql)
        listar_genero = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_genero
    except:
        pass


def listar_plataformas():
    conn = Conneccion()
    listar_plataforma = []

    sql = f"""
        SELECT * FROM Plataforma ORDER BY ID;
    """
    try:
        conn.cursor.execute(sql)
        listar_plataforma = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_plataforma
    except:
        pass
