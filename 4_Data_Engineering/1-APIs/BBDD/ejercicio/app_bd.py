from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

# Es la forma de definir los ENDPOINTS
@app.route('/', methods=['GET'])
def home():
    return "<h1>My first API</h1><p>Este sitio es una API de una base de datos de libros.</p>"

# Función para obtener todos los libros desde books.db
def get_all_books():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row  # Para obtener columnas con nombres
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    books = [dict(row) for row in rows]

    conn.close()
    return books

# 0.Ruta para obtener todos los libros
@app.route('/books', methods=['GET'])
def all_books():
    books = get_all_books()
    return jsonify(books) 

# 1.Ruta para obtener el conteo de libros por autor ordenados de forma descendente

# Función para contar libros por autor (orden descendente)
def count_books_by_author():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Consulta SQL para agrupar y contar
    cursor.execute("""
        SELECT author, COUNT(*) as book_count 
        FROM books 
        GROUP BY author 
        ORDER BY book_count DESC
    """)
    
    rows = cursor.fetchall()
    result = [dict(row) for row in rows]
    conn.close()
    return result

@app.route('/books_ordenados', methods=['GET'])
def books_ordenados():
    data = count_books_by_author()
    return jsonify(data)
    
# 2.Ruta para obtener los libros de un autor

# Función para obtener libros por autor
def get_books_by_author(author_name):
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Búsqueda insensible a mayúsculas y con trim
    cursor.execute("""
        SELECT * FROM books 
        WHERE LOWER(TRIM(author)) = LOWER(TRIM(?))
    """, (author_name,))
    
    rows = cursor.fetchall()
    books = [dict(row) for row in rows]
    conn.close()
    return books

@app.route('/books_autor/<string:author>', methods=['GET'])
def books_by_author(author):
    books = get_books_by_author(author)
    
    if not books:
        return jsonify({"message": f"No se encontraron libros del autor '{author}'"}), 404
    
    return jsonify(books)

# 3.Ruta para añadir un libro
@app.route('/books_add', methods=['POST'])
def add_book():
    # Conectar a la base de datos
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    
    # Obtener datos del JSON enviado
    nuevo_libro = request.get_json()
    
    # Insertar directamente (¡sin validaciones!)
    cursor.execute(
        "INSERT INTO books (title, author) VALUES (?, ?)",
        (nuevo_libro['title'], nuevo_libro['author'])
    )
    
    conn.commit()  # Guardar cambios
    conn.close()   # Cerrar conexión
    
    return jsonify({"mensaje": "Libro añadido!"}), 201

app.run() 
