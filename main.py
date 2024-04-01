import sqlite3
import os
try:
    os.remove('cinema.db')
except OSError:
    pass
# Создаем подключение к базе данных (файл будет создан)
con = sqlite3.connect('cinema.db')
cursor = con.cursor()

print("________________________________________________БАЗА ДАННЫХ____________________________________________________")
# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
phone TEXT NOT NULL,
email TEXT,
password TEXT NOT NULL
)
''')

# Заполняем таблицу Users
with con:
    sql = 'INSERT INTO Users (username, phone, password) values(?, ?, ?)'
# указываем данные для запроса
data = [
    ('admin', '89998887766', '123'),
    ('client', '89625876385', '25052001'),
    ('combo', '89625943451', 'GodOfEverything2024'),
    ('lapOchka123', '89625943451', 'lapOchka123')
]

with con:
    con.executemany(sql, data)

# Вывод таблицы
cursor.execute('''
    SELECT id,username, phone, password
    FROM Users''')
print(cursor.fetchall())


# Создаем таблицу Roles
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roles (
id INTEGER PRIMARY KEY,
userRole TEXT NOT NULL
)
''')

# Заполняем таблицу Roles
with con:
    con.executemany('INSERT INTO Roles (userRole) values(?)', [('Администратор',), ('Клиент',)])

# Вывод таблицы
cursor.execute('''
    SELECT *
    FROM Roles''')
print(cursor.fetchall())

# Создаем таблицу UsersRoles
cursor.execute('''
CREATE TABLE IF NOT EXISTS UsersRoles (
user_id INTEGER,
role_id INTEGER,
FOREIGN KEY (user_id) REFERENCES Users(id)
FOREIGN KEY (role_id) REFERENCES Roles(id)
PRIMARY KEY (user_id,  role_id)
)
''')

# Заполняем таблицу UsersRoles
with con:
    sql = 'INSERT INTO UsersRoles (user_id,  role_id) values(?, ?)'

data = [
    (1,1),
    (2,2),
    (3,1),
    (3,2),
    (4,2)
]

with con:
    con.executemany(sql, data)

# Вывод таблицы
cursor.execute('''
    SELECT *
    FROM UsersRoles''')
print(cursor.fetchall())

# Создаем таблицу Genres
cursor.execute('''
CREATE TABLE IF NOT EXISTS Genres (
id INTEGER PRIMARY KEY,
genre TEXT 
)
''')

# Заполняем таблицу Genres
with con:
    con.executemany('INSERT INTO Genres (genre) values(?)', [('Комедия',), ('Боевик',), ('Мультфильм',), ('Романтика',), ('Фантастика',), ('Фентези',), ('Драма',), ('Ужасы',)])

# Вывод таблицы
cursor.execute('''
    SELECT *
    FROM Genres''')
print(cursor.fetchall())

# Создаем таблицу AgeLimits
cursor.execute('''
CREATE TABLE IF NOT EXISTS AgeLimits (
value INTEGER PRIMARY KEY
)
''')

# Заполняем таблицу AgeLimits
with con:
    con.executemany('INSERT INTO AgeLimits (value) values(?)', [(0,), (6,), (12,), (16,), (18,), (21,)])

# Вывод таблицы
cursor.execute('''
    SELECT *
    FROM AgeLimits''')
print(cursor.fetchall())

# Создаем таблицу CinemaHalls
cursor.execute('''
CREATE TABLE IF NOT EXISTS CinemaHalls (
hallname TEXT PRIMARY KEY,
rows INTEGER NOT NULL,
columns INTEGER NOT NULL
)
''')

# Заполняем таблицу CinemaHalls
with con:
    sql = 'INSERT INTO CinemaHalls (hallname, rows, columns) values(?, ?, ?)'
# указываем данные для запроса
data = [
    ('Moon', 10, 12),
    ('Earth', 20, 18),
    ('Jupiter', 25, 28),
    ('Sun', 32, 40),
    ('Venus', 8, 12),
]

with con:
    con.executemany(sql, data)

# Вывод таблицы
cursor.execute('''
    SELECT *
    FROM CinemaHalls''')
print(cursor.fetchall())

# Создаем таблицу Movies
cursor.execute('''
CREATE TABLE IF NOT EXISTS Movies (
title TEXT PRIMARY KEY,
genre INTEGER REFERENCES Genres(id),
agelimit INTEGER REFERENCES AgeLimits(value),
description TEXT NOT NULL,
releaseStart TEXT NOT NULL,
releaseFinish TEXT,
duration TEXT NOT NULL

)
''')

# Заполняем таблицу Movies
with con:
    sql = 'INSERT INTO Movies (title, genre, agelimit, releaseStart, releaseFinish,  description, duration) values(?, ?, ?, ?, ?, ?, ?)'

data = [
    ('Шрек', 3, 12, '2024-01-19', '2024-02-10', 'Жил да был в сказочном государстве большой зеленый великан по имени Шрэк. Жил он в гордом одиночестве в лесу, на болоте, которое считал своим. Но однажды злобный коротышка лорд Фаркуад, правитель волшебного королевства, безжалостно согнал на Шрэково болото всех сказочных обитателей. И беспечной жизни зеленого великана пришел конец. Но лорд Фаркуад пообещал вернуть Шрэку болото, если великан добудет ему прекрасную принцессу Фиону, которая томится в неприступной башне, охраняемой огнедышащим драконом.', '01:25:00'),
    ('Дюна2', 5, 16, '2024-02-06', '2024-04-02', 'Герцог Пол Атрейдес присоединяется к фременам, чтобы стать Муад Дибом, одновременно пытаясь остановить наступление войны.', '02:35:00'),
    ('Кунг-фу панда 4', 3, 6, '2024-03-14', '2024-04-28', 'Продолжение приключений легендарного Воина Дракона, его верных друзей и наставника.', '01:45:00'),
    ('Онегин', 7, 12, '2024-03-07', '2024-04-18', 'Экранизация легендарного романа А.С.Пушкина', '02:16:00'),
    ('Бедные-несчастные', 1, 18, '2024-03-07', '2024-05-01', 'Из-за жестокого мужа Белла Бакстер покончила с собой, утопившись в реке. Эксцентричный учёный решает спасти женщину и пересаживает ей мозг её же нерождённого ребёнка.', '02:10:00'),
    ('Лёд 3', 4,  6, '2024-02-14', '2024-05-01', 'Надя выросла и стала фигуристкой. Она мечтает о «Кубке Льда», как когда-то мечтала ее мама. Горин возражает против спортивной карьеры дочери — он оберегает ее от любых трудностей и его можно понять: он потерял слишком много. На тайной тренировке Надя знакомится с молодым и дерзким хоккеистом из Москвы, и между ними вспыхивает первая любовь. Отец не верит в искренность чувств юноши и разлучает пару.', '02:21:00'),
    ('Мастер и Маргарита', 6, 18, '2024-01-18', '2024-03-26', 'Москва, 1930-е годы. Известный писатель на взлёте своей карьеры внезапно оказывается в центре литературного скандала. Спектакль по его пьесе снимают с репертуара, коллеги демонстративно избегают встречи, в считанные дни он превращается в изгоя. Вскоре после этого, он знакомится с Маргаритой, которая становится его возлюбленной и музой. Воодушевлённый ее любовью и поддержкой, писатель берется за новый роман, в котором персонажи — это люди из его окружения, а главный герой — загадочный Воланд, прообразом которого становится недавний знакомый иностранец. Писатель уходит с головой в мир своего романа и постепенно перестает замечать, как вымысел и реальность сплетаются в одно целое.', '02:18:00'),
    ('Территория зла', 2, 18, '2024-03-21', '2024-04-21', 'Отряд американского спецназа тайно высаживается на территорию Филиппин для выполнения секретной миссии по спасению важного заложника. С базы поддержку с воздуха осуществляют оператор беспилотника Рипер и его напарница. Вскоре ситуация принимает неожиданный оборот.','01:55:00'),
    ('Омен. Непорочная', 8, 18, '2024-03-21', '2024-04-28', 'Церковь знала лишь один случай непорочного зачатия, но, похоже, что новая монахиня Сесилия в итальянском монастыре стала второй девственницей, которая вынашивает ребенка. Местные монахи объявили о чуде, но никто точно не знает, кого на самом деле носит под сердцем девушка — нового спасителя или того, кто погрузит мир в вечную тьму.', '01:34:00'),
]

with con:
    con.executemany(sql, data)

# Вывод таблицы
cursor.execute('''
    SELECT *
    FROM Movies''')
print(cursor.fetchall())

# Создаем таблицу Schedule
cursor.execute('''
CREATE TABLE IF NOT EXISTS Schedule (
id INTEGER PRIMARY KEY,
title TEXT REFERENCES Movies(title) NOT NULL,
hall TEXT REFERENCES CinemaHalls(hallname) NOT NULL,
date TEXT NOT NULL,
time TEXT NOT NULL,
cost INTEGER NOT NULL
)
''')

# Заполняем таблицу Schedule
with con:
    sql = 'INSERT INTO Schedule (title, hall, date, time, cost) values(?, ?, ?, ?, ?)'
# указываем данные для запроса
data = [
    ('Шрек', 'Venus', '2024-01-19', '10:00:00', 500),
    ('Шрек', 'Venus', '2024-01-19', '12:40:00', 500),
    ('Шрек', 'Sun', '2024-01-22', '18:20:00', 350),
    ('Шрек', 'Sun', '2024-02-10', '16:40:00', 300),
    ('Шрек', 'Moon', '2024-02-03', '15:00:00', 280),
    ('Дюна2', 'Venus', '2024-02-06', '17:00:00', 600),
    ('Дюна2', 'Jupiter', '2024-02-06', '12:40:00', 480),
    ('Дюна2', 'Venus', '2024-02-06', '21:00:00', 600),
    ('Дюна2', 'Earth', '2024-04-02', '20:10:00', 470),
    ('Дюна2', 'Moon', '2024-04-02', '11:40:00', 350),
    ('Кунг-фу панда 4', 'Jupiter', '2024-03-14', '11:40:00', 400),
    ('Кунг-фу панда 4', 'Jupiter', '2024-03-14', '15:10:00', 430),
    ('Кунг-фу панда 4', 'Sun', '2024-03-14', '16:40:00', 450),
    ('Кунг-фу панда 4', 'Sun', '2024-03-15', '16:40:00', 450),
    ('Кунг-фу панда 4', 'Earth', '2024-03-18', '18:20:00', 400),
    ('Онегин', 'Earth', '2024-03-07', '18:20:00', 300),
    ('Онегин', 'Moon', '2024-03-07', '16:40:00', 250),
    ('Онегин', 'Moon', '2024-03-09', '16:40:00', 250),
    ('Онегин', 'Earth', '2024-03-09', '20:00:00', 270),
    ('Онегин', 'Earth', '2024-04-18', '21:00:00', 270),
    ('Бедные-несчастные', 'Moon', '2024-03-07', '18:20:00', 350),
    ('Бедные-несчастные', 'Earth', '2024-03-09', '16:40:00', 320),
    ('Бедные-несчастные', 'Sun', '2024-03-08', '21:00:00', 320),
    ('Бедные-несчастные', 'Sun', '2024-03-09', '21:00:00', 300),
    ('Бедные-несчастные', 'Venus', '2024-03-09', '21:30:00', 350),
    ('Лёд 3', 'Venus', '2024-02-14', '18:30:00', 400),
    ('Лёд 3', 'Venus', '2024-02-15', '18:30:00', 400),
    ('Лёд 3', 'Sun', '2024-02-14', '16:40:00', 350),
    ('Лёд 3', 'Sun', '2024-02-20', '11:40:00', 370),
    ('Лёд 3', 'Sun', '2024-05-01', '11:40:00', 280),
    ('Мастер и Маргарита', 'Sun', '2024-01-18', '13:30:00', 250),
    ('Мастер и Маргарита', 'Sun', '2024-01-18', '18:30:00', 300),
    ('Мастер и Маргарита', 'Sun', '2024-01-25', '13:30:00', 250),
    ('Мастер и Маргарита', 'Earth', '2024-01-28', '16:40:00', 250),
    ('Мастер и Маргарита', 'Moon', '2024-03-26', '16:40:00', 200),
    ('Территория зла', 'Sun', '2024-03-21', '16:40:00', 400),
    ('Территория зла', 'Venus', '2024-03-21', '18:30:00',450),
    ('Территория зла', 'Moon', '2024-04-21', '21:00:00', 500),
    ('Территория зла', 'Venus', '2024-04-18', '21:00:00', 500),
    ('Территория зла', 'Moon', '2024-04-20', '21:00:00', 450),
    ('Омен. Непорочная', 'Venus', '2024-03-21', '21:10:00', 500),
    ('Омен. Непорочная', 'Moon', '2024-03-27', '21:00:00', 450),
    ('Омен. Непорочная', 'Venus', '2024-04-01', '18:30:00', 450),
    ('Омен. Непорочная', 'Venus', '2024-03-27', '18:30:00', 400),
    ('Омен. Непорочная', 'Venus', '2024-03-28', '16:40:00', 400),
]

with con:
    con.executemany(sql, data)

# Вывод таблицы
cursor.execute('''
    SELECT *
    FROM Schedule''')
print(cursor.fetchall())

# Создаем таблицу Tickets
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tickets (
id INTEGER PRIMARY KEY,
session_id INTEGER REFERENCES Schedule(id) NOT NULL,
row INTEGER NOT NULL,
place INTEGER NOT NULL
)
''')

# Заполняем таблицу Tickets
with con:
    sql = 'INSERT INTO Tickets (session_id, row, place) values(?, ?, ?)'
# указываем данные для запроса
data = [
    (1, 4, 5),
    (1, 4, 6),
    (1, 4, 7),
    (6, 4, 5),
    (6, 4, 6),
    (6, 1, 7),
    (11, 12, 14),
    (11, 12, 15),
    (11, 12, 13),
    (11, 13, 14),
    (11, 13, 15),
    (16, 10, 6),
    (16, 10, 7),
    (21, 5, 5),
    (21, 5, 6),
    (21, 5, 7),
]

with con:
    con.executemany(sql, data)

# Вывод таблицы
cursor.execute('''
    SELECT *
    FROM Tickets''')
print(cursor.fetchall())

# Создаем таблицу Orders
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
id INTEGER,
ticket_id INTEGER REFERENCES Tickets(id) NOT NULL,
PRIMARY KEY (id,  ticket_id)
)
''')

# Заполняем таблицу Orders
with con:
    sql = 'INSERT INTO Orders (id ,ticket_id) values(?, ?)'
# указываем данные для запроса
data = [
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (3, 6),
    (4, 7),
    (4, 8),
    (4, 9),
    (5, 10),
    (5, 11),
    (5, 12),
    (6, 13),
    (6, 14),
    (7, 15),
    (7, 16),
    (7, 17),
]

with con:
    con.executemany(sql, data)

# Вывод таблицы
cursor.execute('''
    SELECT *
    FROM Orders''')
print(cursor.fetchall())


# Создаем таблицу Conditions
cursor.execute('''
CREATE TABLE IF NOT EXISTS Conditions (
id INTEGER PRIMARY KEY,
condition TEXT NOT NULL
)
''')

# Заполняем таблицу Conditions
with con:
    con.executemany('INSERT INTO Conditions (condition) values(?)', [('Бронь',), ('Возврат',), ('Оплачен',)])

# Вывод таблицы
cursor.execute('''
    SELECT *
    FROM Conditions''')
print(cursor.fetchall())

# Создаем таблицу OrdersStatus
cursor.execute('''
CREATE TABLE IF NOT EXISTS OrdersStatus(
id INTEGER REFERENCES Orders(id) NOT NULL,
condition INTEGER REFERENCES Conditions(id) NOT NULL
)
''')

# Заполняем таблицу OrdersStatus
with con:
    sql = 'INSERT INTO OrdersStatus (id ,condition) values(?, ?)'
# указываем данные для запроса
data = [
    (1, 3),
    (2, 3),
    (3, 3),
    (4, 3),
    (5, 2),
    (6, 3),
    (7, 1),
]

with con:
    con.executemany(sql, data)

# Вывод таблицы
cursor.execute('''
    SELECT *
    FROM OrdersStatus''')
print(cursor.fetchall())

print("\n\n_________________________________________________ЗАПРОСЫ_______________________________________________________")
#__________________________________________ЗАПРОСЫ НА ВЫБОРКУ_________________________________________________
##_________________   два запроса на выборку для связанных таблиц с условиями и сортировкой___________________________
###_______________Вывести всех пользователей, имеющих права адмиистратора в алфавитном порядке___________________________
print("\n\nВывести всех пользователей, имеющих права адмиистратора в алфавитном порядке")
cursor.execute('''
    SELECT Users.id, Users.username, Users.phone, Users.email, Users.password
    FROM Users
    JOIN UsersRoles ON (Users.id = UsersRoles.user_id)
    JOIN Roles ON (UsersRoles.role_id = Roles.id)
    WHERE Roles.userRole == "Администратор"
    ORDER BY Users.username
''')
print(cursor.fetchall())

print("\nВывести список фильмов и жанров продолжительностью больше 2 часов в порядке уменьшения возрастного рейтинга")
###_____Вывести список фильмов и жанров продолжительностью больше 2 часов в порядке уменьшения возрастного рейтинга_____
cursor.execute('''
    SELECT Movies.title, Genres.genre, Movies.agelimit
    FROM Movies
    JOIN Genres ON (Genres.id = Movies.genre)
    WHERE Movies.duration >= '02:00:00'
    ORDER BY Movies.agelimit DESC
''')
print(cursor.fetchall())

print("\nНайти номера заказов на сумму больше 1000, вывести в порядке убывания")
##_______________________________два запроса с группировкой и групповыми функциями;_____________________________________
###______________________Найти номера заказов на сумму больше 1000, вывести в порядке убывания__________________________
cursor.execute('''
    SELECT Orders.id, SUM(Schedule.cost)
    FROM Orders
    JOIN Tickets ON (Tickets.id = Orders.ticket_id)
    JOIN Schedule ON (Schedule.id = Tickets.session_id)
    GROUP BY Orders.id
    HAVING SUM(Schedule.cost) >= 1000
    ORDER BY SUM(Schedule.cost) DESC
''')
print(cursor.fetchall())

print("\nВывести список залов и среднюю целочисленную стоимость билетов в этих залах в порядке убывания")
###___________Вывести список залов и среднюю целочисленную стоимость билетов в этих залах в порядке убывания____________
cursor.execute('''
    SELECT CinemaHalls.hallname, ROUND(AVG(Schedule.cost))
    FROM CinemaHalls
    JOIN Schedule ON (Schedule.hall = CinemaHalls.hallname)
    GROUP BY CinemaHalls.hallname
    ORDER BY  AVG(Schedule.cost) DESC
''')
print(cursor.fetchall())

print("\nПодсчитать количество нераспроданных билетов с сеансов 7 марта")
##_________________________два запроса со вложенными запросами или табличными выражениями_______________________________
###_________________________Подсчитать количество нераспроданных билетов с сеансов 7 марта _____________________________
'''В таблице help подсчитывается количество купленных билетов за каждый сеанс 7 марта,
    потом от общего числа мест отнимается число мест из таблицы help'''
cursor.execute('''
    WITH help AS(
        SELECT Schedule.id, Schedule.title, Schedule.hall, COUNT(Tickets.id) AS PLACES
        FROM Schedule
        JOIN Tickets ON (Tickets.session_id = Schedule.id)
        GROUP BY Schedule.id
        HAVING Schedule.date = '2024-03-07'
    )
        SELECT help.id, help.title, rows * columns - PLACES
        FROM help
        JOIN CinemaHalls ON (help.hall = CinemaHalls.hallname)
''')
print(cursor.fetchall())

print("\nВывести список фильмов, цена на билет которых досигала когда либо отметки выше средней цены за любой билет")
###_____Вывести список фильмов, цена на билет которых досигала когда либо отметки выше средней цены за любой билет______
cursor.execute('''
    SELECT DISTINCT Schedule.title
    FROM Schedule
    WHERE Schedule.cost > (
        SELECT AVG(Schedule.cost)
        FROM Schedule
    )
    
''')
print(cursor.fetchall())


##______________________два запроса корректировки данных (обновление, добавление, удаление и пр)________________________
###_____________________________________Увеличить цену билетов будущих сеансов на 5%____________________________________
print("\nУвеличить цену билетов будущих сеансов на 5%")
#### Вывод таблицы  Schedule только с будущими сеансами
cursor.execute('''
    SELECT *
    FROM Schedule
    WHERE date > DATE()''')
print(cursor.fetchall())


#### Запрос на обновление
cursor.execute('''
    UPDATE Schedule
    SET cost = cost * 1.05
    WHERE date > DATE()
''')

#### Вывод обновленной таблицы Schedule только с будущими сеансами
cursor.execute('''
    SELECT *
    FROM Schedule
    WHERE date > DATE()''')
print(cursor.fetchall())

###________________________________Удалить все бронирования за 20 минут до начала фильма_______________________________________
print("\nУдалить все бронирования за 20 минут до начала фильма")
#### Вывод обновленной таблицы Schedule только с будущими сеансами, где у заказа стату - Бронь
cursor.execute('''
    SELECT Schedule.id, Schedule.date, Schedule.time, Orders.id
    FROM Schedule
    JOIN Tickets ON (Tickets.session_id = Schedule.id)
    JOIN Orders ON (Tickets.id = Orders.ticket_id)
    JOIN OrdersStatus ON (OrdersStatus.id = Orders.id)
    JOIN Conditions ON (Conditions.id = OrdersStatus.condition)
    WHERE Conditions.condition  = 'Бронь'
''')
print(cursor.fetchall())

#### Первый внутренний запрос находит билеты на сеансы, которые начинаются меньше чем через 20 минут
#### Второй внутренний запрос находит номера заказов со статусом - Бронь
#### В целом запрос удаляет заказы в которых есть билеты на фильм, который начинается меньше чем через 20 минут и статус заказа этих билетов является Бронь
cursor.execute('''
    DELETE 
    FROM Orders
    WHERE ticket_id IN (
        SELECT Tickets.id
        FROM Tickets
        JOIN Schedule ON (Tickets.session_id = Schedule.id)
        WHERE (Schedule.date <= DATE()) AND (Schedule.time - TIME() < '00:20:00')
    ) AND Orders.id IN (
        SELECT DISTINCT Orders.id 
        FROM Orders
        JOIN OrdersStatus ON (OrdersStatus.id = Orders.id)
        JOIN Conditions ON (Conditions.id = OrdersStatus.condition)
        WHERE Conditions.condition  = 'Бронь'
    )
''')

#### Вывод обновленной таблицы Schedule только с будущими сеансами, где у заказа стату - Бронь
cursor.execute('''
    SELECT Schedule.id, Schedule.date, Schedule.time, Orders.id
    FROM Schedule
    JOIN Tickets ON (Tickets.session_id = Schedule.id)
    JOIN Orders ON (Tickets.id = Orders.ticket_id)
    JOIN OrdersStatus ON (OrdersStatus.id = Orders.id)
    JOIN Conditions ON (Conditions.id = OrdersStatus.condition)
    WHERE Conditions.condition  = 'Бронь'
''')
print(cursor.fetchall())

con.commit()
con.close()
os.remove('cinema.db')


