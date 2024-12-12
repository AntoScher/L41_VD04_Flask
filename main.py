import os
from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Генерация криптографически безопасного случайного ключа

@app.route('/')
def index():
    dishes = [
        {
            'name': 'Борщ',
            'rating': 9,
            'recipe_link': 'https://m.povar.ru/recipes/borsh_klassicheskii_s_govyadinoi-54428.html',
            'image': 'https://img.freepik.com/premium-photo/borscht-soup-borscht-with-meat-wooden-white-background_560930-1776.jpg?w=740',
            'author': 'Иван Иванович',
            'author_city': 'Москва',
            'author_photo': 'https://civilisable.com/wp-content/uploads/2024/02/Traditional-Russian-Clothing-for-Men-25.2.2024.jpg'
        },
        {
            'name': 'Драники',
            'rating': 8,
            'recipe_link': 'https://m.povar.ru/recipes/draniki_kartofelnye_klassicheskie-43098.html',
            'image': 'https://c7.alamy.com/comp/2AWB3K7/traditional-ukrainian-potato-pancakes-deruny-served-on-stone-background-with-copy-space-2AWB3K7.jpg',
            'author': 'Анна Петровна',
            'author_city': 'Минск',
            'author_photo': 'https://i.pinimg.com/736x/26/f5/81/26f58177ef9ff343993723c110854cb0.jpg'
        },
        {
            'name': 'Вареники',
            'rating': 9,
            'recipe_link': 'https://m.povar.ru/recipes/vareniki_s_tvorogom_klassicheskie-90658.html',
            'image': 'https://img.freepik.com/premium-photo/classic-ukrainian-pierogi-varenyky-with-cherries_960396-627186.jpg?w=740',
            'author': 'Олег Сергеевич',
            'author_city': 'Киев',
            'author_photo': 'https://m.media-amazon.com/images/I/51Sp7nmeWeL.jpg'
        },
        {
            'name': 'Бигос',
            'rating': 8,
            'recipe_link': 'https://m.povar.ru/recipes/bigos_polskii-47302.html',
            'image': 'https://eatingeuropean.com/wp-content/uploads/2017/10/Bigos-Polish-Hunter-Stew-1.jpg',
            'author': 'Мария Ивановна',
            'author_city': 'Варшава',
            'author_photo': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT5Ml31KHSVbyaJxqAiZ642-8lOCYuLE3DVLPNgsfpPjn0_SHS1p0jM9yZLl9Do'
        },
        {
            'name': 'Фалафель',
            'rating': 10,
            'recipe_link': 'https://m.povar.ru/recipes/falafel-5014.html',
            'image': 'https://tastythriftytimely.com/wp-content/uploads/2023/06/Falafel-Pita-1-1367x2048.jpg',
            'author': 'Давид Абрамович',
            'author_city': 'Тель-Авив',
            'author_photo': 'https://img.freepik.com/free-photo/portrait-young-orthodox-jewish-man-with-bet-slip_155003-26405.jpg?t=st=1733507252~exp=1733510852~hmac=46e08eb1a5add293e50cae2a9deacaf18d7e1ed2a55733fc08741c94fe5b7f12&w=2000'
        }
    ]
    return render_template('index_receipt.html', dishes=dishes)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    try:
        conn = sqlite3.connect('blog_subscribers.db')
        cursor = conn.cursor()
        
        # Создаем таблицу, если она не существует
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                subscribed_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Вставляем email, игнорируя дубликаты
        cursor.execute('INSERT OR IGNORE INTO subscribers (email) VALUES (?)', (email,))
        conn.commit()
        
        flash('Вы успешно подписались на рассылку!', 'success')
    except sqlite3.Error as e:
        flash(f'Ошибка подписки: {e}', 'error')
    finally:
        conn.close()
    
    return redirect('/blog')

@app.route('/submit_review', methods=['POST'])
def submit_review():
    name = request.form.get('name')
    review = request.form.get('review')
    rating = request.form.get('rating')
    
    conn = None
    try:
        conn = sqlite3.connect('blog_reviews.db')
        cursor = conn.cursor()
        
        # Создаем таблицу, если она не существует
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                review TEXT NOT NULL,
                rating INTEGER NOT NULL,
                submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Вставляем отзыв
        cursor.execute('''
            INSERT INTO reviews (name, review, rating) 
            VALUES (?, ?, ?)
        ''', (name, review, rating))
        conn.commit()
        
        flash('Ваш отзыв успешно отправлен!', 'success')
    except sqlite3.Error as e:
        flash(f'Ошибка отправки отзыва: {e}', 'error')
    finally:
        if conn:
            conn.close()
    
    return redirect('/blog')

if __name__ == '__main__':
    app.run(debug=True)