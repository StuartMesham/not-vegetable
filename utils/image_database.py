import sqlite3

DB_PATH = 'data/images.db'

TYPE_FRUIT = 0
TYPE_VEGETABLE = 1
TYPE_OTHER = 2

conn = None
cursor = None


def connect(reset=False):
    global conn, cursor
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('PRAGMA foreign_keys = ON')
    
    if reset:
        cursor.execute('DROP TABLE IF EXISTS images_categories_link')
        cursor.execute('DROP TABLE IF EXISTS images')
        cursor.execute('DROP TABLE IF EXISTS categories')

    cursor.execute('CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY, url TEXT UNIQUE NOT NULL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS categories (id TEXT PRIMARY KEY NOT NULL, name TEXT, type INTEGER NOT NULL)')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images_categories_link (
        image_id INTEGER NOT NULL, category_id TEXT NOT NULL,
        PRIMARY KEY (image_id, category_id),
        FOREIGN KEY (image_id) REFERENCES images(id) ON DELETE CASCADE,
        FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
        )
    ''')
    conn.commit()


def add_category(id, name, type):
    global conn, cursor
    if not conn:
        raise Exception('image database not connected')
    
    cursor.execute('INSERT OR IGNORE INTO categories (id, name, type) VALUES (?, ?, ?)', (id, name, type))


def add_url(url, category_id=None):
    global conn, cursor
    if not conn:
        raise Exception('image database not connected')
    
    cursor.execute('SELECT id FROM images WHERE url = ?', (url,))
    row = cursor.fetchone()
    if row:
        image_id = row[0]
    else:
        cursor.execute('INSERT INTO images (url) VALUES (?)', (url,))
        image_id = cursor.lastrowid
    
    if category_id:
        add_image_category_link(image_id, category_id)
    
    return image_id


def add_image_category_link(image_id, category_id):
    global conn, cursor
    if not conn:
        raise Exception('image database not connected')
    
    cursor.execute('INSERT OR IGNORE INTO images_categories_link (image_id, category_id) VALUES (?, ?)', (image_id, category_id))


def query_urls(sql):
    rows = conn.execute(sql).fetchall()
    return [row[0] for row in rows]


def commit():
    global conn
    if not conn:
        raise Exception('image database not connected')
    
    conn.commit()


def close():
    global conn
    if not conn:
        raise Exception('image database not connected')
    
    conn.close()
