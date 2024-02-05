# Импортируем необходимые библиотеки

import random
from urllib import response
import telebot
import sqlite3
import pandas as pd
import telebot
from telebot import types
# Получаем токен бота от BotFather


# Создаем объект бота с помощью библиотеки pyTelegramBotAPI
bot = telebot.TeleBot('6731864682:AAGyKCXDcYLo20vMrj7PFoipk01fh8bVbmU')

# Создаем подключение к базе данных SQLite
conn = sqlite3.connect('users.db', check_same_thread=False)
cur = conn.cursor()

# Создаем таблицу users, если ее еще нет
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    height REAL,
    weight REAL,
    age REAL,
    gender TEXT,
    preferences TEXT,
    activity REAL,
    allergies TEXT
    
)
''')
conn.commit()

df = pd.read_csv("recipe_dat.csv")



df["Calories"] = df["Calories"].replace(" кКал", "", regex=True)
df["Proteins"] = df["Proteins"].replace(" г", "", regex=True)
df["Fats"] = df["Fats"].replace(" г", "", regex=True)
df["Carbohydrates"] = df["Carbohydrates"].replace(" г", "", regex=True)

df["Calories"] = df["Calories"].astype(float)
df["Proteins"] = df["Proteins"].astype(float)
df["Fats"] = df["Fats"].astype(float)
df["Carbohydrates"] = df["Carbohydrates"].astype(float)

# задаем норму потребления углеводов, белков и жиров в граммах для пользователя
daily_carbs = 250
daily_proteins = 150
daily_fats = 80

def calculate_nutrients(dish, grams):
    calories = df.loc[df["Dish Name"] == dish, "Calories"].values[0] * grams / 100
    proteins = df.loc[df["Dish Name"] == dish, "Proteins"].values[0] * grams / 100
    fats = df.loc[df["Dish Name"] == dish, "Fats"].values[0] * grams / 100
    carbs = df.loc[df["Dish Name"] == dish, "Carbohydrates"].values[0] * grams / 100
    recipe=df.loc[df["Dish Name"] == dish, "Ingredients"].values[0]
    return calories, proteins, fats, carbs, recipe



# Создаем словарь для хранения временных данных о пользователях
temp_data = {}
temp_ans = {}
flag=True
# Определяем обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    global flag
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    # Проверяем, есть ли пользователь в базе данных
    user_id = message.from_user.id
    cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cur.fetchone()
    if user:
        # Если есть, то приветствуем его по имени
        flag=False
        bot.send_message(user_id, f'{user[1]}, я готов к работе! Если хочешь начать, то напиши "да"')
        
    else:
        # Если нет, то начинаем процесс регистрации
        bot.send_message(user_id, 'Привет! Я - AmetCare, умный конструктор сбалансированного рациона. Давай знакомиться. Как тебя зовут?')
        # Создаем пустой словарь для хранения данных о новом пользователе
        temp_data[user_id] = {}
temp_ans={}
list2=10
gramss=0
#@bot.message_handler(commands=['begin'])


    
# Определяем обработчик всех текстовых сообщений
@bot.message_handler(content_types=['text'])
def text(message):
    global temp_data, temp_ans,list2,gramss
    # Получаем идентификатор и текст сообщения
    user_id = message.from_user.id
    text = message.text
    @bot.callback_query_handler(func=lambda call: True)
    def callback_worke(call):
        global temp_data, temp_ans,list2,gramss
        
        if call.data=='one':
            temp_ans['answer']='1'
        elif call.data=='two':
            temp_ans['answer']='2'
        elif call.data == '11':
            temp_ans['otvet']='1'
        elif call.data == '22':
            temp_ans['otvet']='2'
        elif call.data == 'd1':
            list2=0
        elif call.data == 'd2':
            list2=1
        elif call.data == 'd3':
            list2=2
        elif call.data == 'd4':
            list2=3
        elif call.data == 'd5':
            list2=4
        elif call.data == '50':
            gramss=50
        elif call.data == '100':
            gramss=100
        elif call.data == '150':
            gramss=150
        elif call.data == '200':
            gramss=200
        elif call.data == '250':
            gramss=250
        elif call.data == '300':
            gramss=300
        elif call.data == '350':
            gramss=350
        elif call.data == '400':
            gramss=400
        elif call.data == '450':
            gramss=450
        elif call.data == '500':
            gramss=500
        elif call.data == "man": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(user_id, f'Принято! Выбран мужской пол.')
            temp_data[user_id]['gender'] = 'мужской'
            
        elif call.data == 'woman':
            bot.send_message(user_id, f'Принято! Выбран женский пол.')
            temp_data[user_id]['gender'] = 'женский'
        elif call.data=='one':
            temp_ans['answer']='1'
        elif call.data=='two':
            temp_ans['answer']='2'    
        elif call.data == "1": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(user_id, f'Принято!')
            temp_data[user_id]['activity'] = 1.2
            
        elif call.data == '2':
            bot.send_message(user_id, f'Принято!')
            temp_data[user_id]['activity'] = 1.38
            
        elif call.data == '3':
            bot.send_message(user_id, f'Принято!')
            temp_data[user_id]['activity'] = 1.46
            
        elif call.data == '4':
            bot.send_message(user_id, f'Принято!')
            temp_data[user_id]['activity'] = 1.55
            
        elif call.data == '5':
            bot.send_message(user_id, f'Принято!')
            temp_data[user_id]['activity'] = 1.64
            
        elif call.data == '6':
            bot.send_message(user_id, f'Принято!')
            temp_data[user_id]['activity'] = 1.73
            
        elif call.data == '7':
            bot.send_message(user_id, f'Принято!')
            temp_data[user_id]['activity'] = 1.9

    # Проверяем, на каком этапе регистрации находится пользователь
    if flag:
        if 'name' not in temp_data[user_id]:
            # Если пользователь еще не ввел свое имя, то запоминаем его
            temp_data[user_id]['name'] = text
            # И спрашиваем его рост
            bot.send_message(user_id, 'Какой у тебя рост (в сантиметрах)?')
        elif 'height' not in temp_data[user_id]:
            # Если пользователь еще не ввел свой рост, то пытаемся его преобразовать в число
            try:
                height = float(text)
                # Если все ок, то запоминаем его
                temp_data[user_id]['height'] = height
                # И спрашиваем его вес
                bot.send_message(user_id, 'Какой у тебя вес (в килограммах)?')
            except ValueError:
                # Если не получилось, то просим ввести корректное значение
                bot.send_message(user_id, 'Пожалуйста, введи свой рост в сантиметрах, используя только цифры и точку.')
        elif 'weight' not in temp_data[user_id]:
            # Если пользователь еще не ввел свой вес, то пытаемся его преобразовать в число
            try:
                weight = float(text)
                # Если все ок, то запоминаем его
                temp_data[user_id]['weight'] = weight
                # И спрашиваем его пол
                
                bot.send_message(user_id, 'Сколько тебе лет?')
                #bot.send_message(user_id, 'Какой у тебя пол? Мужской или женский?')
            except ValueError:
                # Если не получилось, то просим ввести корректное значение
                bot.send_message(user_id, 'Пожалуйста, введи свой вес в килограммах, используя только цифры и точку.')
        elif 'age' not in temp_data[user_id]:
            try:
                age = float(text)
                # Если все ок, то запоминаем его
                temp_data[user_id]['age'] = age
                # И спрашиваем его пол
                
                
                #bot.send_message(user_id, 'Какой у тебя пол? Мужской или женский?')
            except ValueError:
                # Если не получилось, то просим ввести корректное значение
                bot.send_message(user_id, 'Пожалуйста, введите ваш возраст, используя только цифры и точку.')

            # Если пользователь еще не ввел свой пол, то проверяем, что он ввел один из допустимых вариантов
            keyboard = types.InlineKeyboardMarkup() #наша клавиатура
            key_yes = types.InlineKeyboardButton(text='Мужской', callback_data='man') #кнопка «Да»
            keyboard.add(key_yes); #добавляем кнопку в клавиатуру
            key_no= types.InlineKeyboardButton(text='Женский', callback_data='woman')
            keyboard.add(key_no)
            question = 'Укажите свой пол'
            bot.send_message(user_id, text=question, reply_markup=keyboard)

            #@bot.callback_query_handler(func=lambda call: True)
            #def callback_worker(call):
            #    global temp_data, temp_ans
            #    
            #        
            #    bot.edit_message_reply_markup(user_id, call.message.message_id)
        
            
            while 'gender' not in temp_data[user_id]:
                pass
            bot.send_message(user_id, 'Какие у тебя гастрономические предпочтения? Например, любимая кухня.')
            
        elif 'preferences' not in temp_data[user_id]:
            
        
            temp_data[user_id]['preferences'] = text
            
            keyboard = types.InlineKeyboardMarkup() #наша клавиатура
            key_1 = types.InlineKeyboardButton(text='Физическая нагрузка минимальна', callback_data='1') #кнопка «Да»
            keyboard.add(key_1); #добавляем кнопку в клавиатуру
            key_2= types.InlineKeyboardButton(text='Тренировки средней тяжести 3 раза в неделю', callback_data='2')
            keyboard.add(key_2)
            key_3= types.InlineKeyboardButton(text='Тренировки средней тяжести 5 раз в неделю', callback_data='3')
            keyboard.add(key_3)
            key_4= types.InlineKeyboardButton(text='Интенсивные тренировки 5 раз в неделю', callback_data='4')
            keyboard.add(key_4)
            key_5= types.InlineKeyboardButton(text='Тренировки каждый день', callback_data='5')
            keyboard.add(key_5)
            key_6= types.InlineKeyboardButton(text='Интенсинвные тренировки каждый день или по 2 раза в день', callback_data='6')
            keyboard.add(key_6)
            key_7= types.InlineKeyboardButton(text='Ежедневная нагрузка + физическая работа', callback_data='7')
            keyboard.add(key_7)
            question = 'Укажи свою примерную категорию физической нагрузки'
            bot.send_message(user_id, text=question, reply_markup=keyboard)

            while 'activity' not in temp_data[user_id]:
                pass
            
            bot.send_message(user_id, 'Есть ли у тебя какие-нибудь аллергии? Если да, то перечисли их через запятую. Если нет, то напиши "нет".')
        elif 'allergies' not in temp_data[user_id]:
            # Если пользователь еще не ввел свои аллергии, то запоминаем их
            temp_data[user_id]['allergies'] = text
            # И завершаем процесс регистрации
            bot.send_message(user_id, 'Спасибо за регистрацию! Теперь я знаю о тебе больше. Уверен, мы подружимся!')
            # Сохраняем данные о пользователе в базу данных
            cur.execute('''
            INSERT INTO users (user_id, name, height, weight, age, gender, preferences, activity, allergies)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, temp_data[user_id]['name'], temp_data[user_id]['height'], temp_data[user_id]['weight'],temp_data[user_id]['age'], temp_data[user_id]['gender'], temp_data[user_id]['preferences'], temp_data[user_id]['activity'],temp_data[user_id]['allergies']))
            conn.commit()
            # Удаляем временные данные о пользователе из словаря
            del temp_data[user_id]
            start(message)
    elif text.lower()=='да':
        cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        user = cur.fetchone()

        
        if user[5]=='мужской':
            callory=round((user[3]*10+user[2]*6.25-user[4]*5+5)*user[7],0)
        else:
            callory=round((user[3]*10+user[2]*6.25-user[4]*5-161)*user[7],0)
        # Выводим имя на экран или делаем с ним что-то еще
        bot.send_message(user_id, f'Твоя суточная норма каллорий составляет {callory} Ккал')
        daily_calories = callory
        def recommend_dish(current_calories, current_proteins, current_fats, current_carbs):
            # создаем пустой список для хранения подходящих блюд
            suitable_dishes = []
            # перебираем все блюда из таблицы
            for dish in df["Dish Name"]:
                # для каждого блюда подбираем такую граммовку, чтобы не превысить суточную норму калорий
                max_grams = (daily_calories - current_calories) / df.loc[df["Dish Name"] == dish, "Calories"].values[0] * 100
                # если граммовка положительная, то блюдо подходит
                if max_grams > 10:
                    # добавляем блюдо и граммовку в список подходящих блюд
                    suitable_dishes.append((dish, max_grams))
            # если список подходящих блюд не пустой, то выбираем из него случайное блюдо
            if suitable_dishes:
                dish, max_grams = random.choice(suitable_dishes)
                # для выбранного блюда подбираем такую граммовку, чтобы приблизиться к норме потребления углеводов, белков и жиров в граммах
                # для этого минимизируем функцию ошибки, которая равна сумме квадратов отклонений от нормы потребления углеводов, белков и жиров
                def error_function(grams):
                    calories, proteins, fats, carbs, recipe = calculate_nutrients(dish, grams)
                    total_proteins = current_proteins + proteins
                    total_fats = current_fats + fats
                    total_carbs = current_carbs + carbs
                    protein_error = (total_proteins - daily_proteins) ** 2
                    fat_error = (total_fats - daily_fats) ** 2
                    carb_error = (total_carbs - daily_carbs) ** 2
                    return protein_error + fat_error + carb_error
                # используем метод золотого сечения для поиска минимума функции ошибки на отрезке [0, max_grams]
                # задаем точность поиска
                epsilon = 0.01
                # задаем константу золотого сечения
                phi = (1 + 5 ** 0.5) / 2
                # инициализируем границы отрезка
                a = 0
                b = max_grams
                # инициализируем точки деления отрезка
                x1 = b - (b - a) / phi
                x2 = a + (b - a) / phi
                # инициализируем значения функции ошибки в точках деления
                y1 = error_function(x1)
                y2 = error_function(x2)
                # повторяем пока длина отрезка больше заданной точности
                while abs(b - a) > epsilon:
                    # сравниваем значения функции ошибки в точках деления
                    if y1 < y2:
                        # выбираем левую половину отрезка
                        b = x2
                        # пересчитываем правую точку деления
                        x2 = x1
                        y2 = y1
                        # находим новую левую точку деления
                        x1 = b - (b - a) / phi
                        y1 = error_function(x1)
                    else:
                        # выбираем правую половину отрезка
                        a = x1
                        # пересчитываем левую точку деления
                        x1 = x2
                        y1 = y2
                        # находим новую правую точку деления
                        x2 = a + (b - a) / phi
                        y2 = error_function(x2)
                # берем среднее арифметическое границ отрезка как оптимальную граммовку
                optimal_grams = (a + b) / 2
                # округляем граммовку до целого числа
                optimal_grams = round(optimal_grams)
                # добавляем проверку на граммовку больше 450 грамм
                # если граммовка больше 450 грамм, то уменьшаем ее до 450 грамм
                if optimal_grams > 350:
                    optimal_grams = 350
                # добавляем проверку на суточную норму калорий
                # если рекомендованное блюдо с граммовкой закрывает суточную норму калорий, то уменьшаем граммовку так, чтобы оставалось 10% от суточной нормы калорий
                        # подсчитываем калории, белки, жиры и углеводы для выбранного блюда и граммовки
                calories, proteins, fats, carbs, recipe = calculate_nutrients(dish, optimal_grams)
                # возвращаем рекомендованное блюдо, граммовку и питательные вещества
                return dish, optimal_grams, calories, proteins, fats, carbs, recipe
            # если список подходящих блюд пустой, то возвращаем None
            else:
                return None
        def print_recommendation(dish, grams, calories, proteins, fats, carbs, recipe):
            bot.send_message(user_id, f"Рекомендуемое блюдо: {dish} \nГраммовка: {grams} г \nКалории: {round(calories,2)} ккал \nБелки: {round(proteins,2)} г \nЖиры: {round(fats,2)} г \nУглеводы: {round(carbs,2)} г \nИнгредиенты: {recipe}")
        # инициализируем текущие значения калорий и питательных веществ для пользователя
        current_calories = 0
        current_proteins = 0
        current_fats = 0
        current_carbs = 0    
        while True:
            # выводим текущие значения калорий и питательных веществ для пользователя
            bot.send_message(user_id, f"Текущая калорийность: {round(current_calories,2)} ккал из {daily_calories} ккал")
            # если текущая калорийность не равна нулю, то выводим текущее соотношение белков, жиров и углеводов
            if current_calories != 0:
                # находим сумму текущих белков, жиров и углеводов, умноженную на 4
                total_nutrients = (current_proteins + current_fats + current_carbs)
                # делим текущее количество белков, жиров и углеводов на сумму нутриентов и умножаем на 100, чтобы получить проценты
                bot.send_message(user_id, f"Текущее соотношение белков, жиров и углеводов: {round(current_proteins / total_nutrients * 100)}% : {round(current_fats / total_nutrients * 100)}% : {round(current_carbs / total_nutrients * 100)}%")

            # иначе, выводим сообщение, что соотношение пока не определено
            keyboard = types.InlineKeyboardMarkup() #наша клавиатура
            key_one = types.InlineKeyboardButton(text='Самостоятельно', callback_data='one') #кнопка «Да»
            keyboard.add(key_one); #добавляем кнопку в клавиатуру
            key_two= types.InlineKeyboardButton(text='Получить рекомендацию', callback_data='two')
            keyboard.add(key_two)
            question = 'Ты хочешь выбрать блюдо самостоятельно или получить рекомендацию от AmetCare?'
            bot.send_message(user_id, text=question, reply_markup=keyboard)
            # спрашиваем пользователя, хочет ли он выбрать блюдо сам или получить рекомендацию от программы
            #bot.send_message(user_id, "Вы хотите выбрать блюдо самостоятельно или получить рекомендацию от программы? (введите 1 или 2)\n1. Самостоятельно\n2. Рекомендация\n")
            while 'answer' not in temp_ans:
                pass
                
            if temp_ans['answer'] == '1':
                del temp_ans['answer']
                bot.send_message(user_id,"Вот список всех некоторых блюд:")
                list1=[]
                a=random.randint(0,870)
                for i in range(a,a+5):
                    #bot.send_message(user_id,df["Dish Name"][i])
                    list1.append(df["Dish Name"][i])
                
                keyboard = types.InlineKeyboardMarkup() #наша клавиатура
                key_dish1 = types.InlineKeyboardButton(text=f'{list1[0]}', callback_data='d1') #кнопка «Да»
                keyboard.add(key_dish1); #добавляем кнопку в клавиатуру
                key_dish2= types.InlineKeyboardButton(text=f'{list1[1]}', callback_data='d2')
                keyboard.add(key_dish2)
                key_dish3= types.InlineKeyboardButton(text=f'{list1[2]}', callback_data='d3')
                keyboard.add(key_dish3)
                key_dish4= types.InlineKeyboardButton(text=f'{list1[3]}', callback_data='d4')
                keyboard.add(key_dish4)
                key_dish5= types.InlineKeyboardButton(text=f'{list1[4]}', callback_data='d5')
                keyboard.add(key_dish5)
                question = 'Какое блюдо ты выберешь?'
                bot.send_message(user_id, text=question, reply_markup=keyboard)
                while list2==10:
                    pass
                dish=list1[list2]
                list2=10
                # проверяем, есть ли такое блюдо в таблице
                if dish in df["Dish Name"].values:
                    # спрашиваем пользователя, сколько грамм он хочет потребить
                    
                    keyboard = types.InlineKeyboardMarkup() #наша клавиатура
                    key_50 = types.InlineKeyboardButton(text='50 грамм', callback_data='50') #кнопка «Да»
                    keyboard.add(key_50); #добавляем кнопку в клавиатуру
                    key_100 = types.InlineKeyboardButton(text=f'100 грамм', callback_data='100') #кнопка «Да»
                    keyboard.add(key_100); #добавляем кнопку в клавиатуру
                    key_150 = types.InlineKeyboardButton(text=f'150 грамм', callback_data='150') #кнопка «Да»
                    keyboard.add(key_150); #добавляем кнопку в клавиатуру
                    key_200 = types.InlineKeyboardButton(text=f'200 грамм', callback_data='200') #кнопка «Да»
                    keyboard.add(key_200); #добавляем кнопку в клавиатуру
                    key_250 = types.InlineKeyboardButton(text=f'250 грамм', callback_data='250') #кнопка «Да»
                    keyboard.add(key_250); #добавляем кнопку в клавиатуру
                    key_300 = types.InlineKeyboardButton(text=f'300 грамм', callback_data='300') #кнопка «Да»
                    keyboard.add(key_300); #добавляем кнопку в клавиатуру
                    key_350 = types.InlineKeyboardButton(text=f'350 грамм', callback_data='350') #кнопка «Да»
                    keyboard.add(key_350); #добавляем кнопку в клавиатуру
                    key_400 = types.InlineKeyboardButton(text=f'400 грамм', callback_data='400') #кнопка «Да»
                    keyboard.add(key_400); #добавляем кнопку в клавиатуру
                    key_450 = types.InlineKeyboardButton(text=f'450 грамм', callback_data='450') #кнопка «Да»
                    keyboard.add(key_450); #добавляем кнопку в клавиатуру
                    key_500 = types.InlineKeyboardButton(text=f'500 грамм', callback_data='500') #кнопка «Да»
                    keyboard.add(key_500); #добавляем кнопку в клавиатуру
                    question = f"Какую порцию блюда '{dish}' ты предпочтешь?"
                    bot.send_message(user_id, text=question,reply_markup=keyboard)
                    while gramss==0:
                        pass
                    grams = gramss
                    gramss=0
                    # преобразуем ввод пользователя в целое число
                    
                    # подсчитываем калории, белки, жиры и углеводы для выбранного блюда и граммовки
                    calories, proteins, fats, carbs, recipe = calculate_nutrients(dish, grams)
                    # проверяем, не превышает ли выбранное блюдо суточную норму калорий
                    if current_calories + calories > daily_calories:
                        bot.send_message(user_id,f"Выбранное блюдо превышает суточную норму калорий на {current_calories + calories - daily_calories} ккал. Пожалуйста, выбери другое блюдо или уменьши граммовку.")
                        continue
                    # обновляем текущие значения калорий и питательных веществ для пользователя
                    current_calories += calories
                    current_proteins += proteins
                    current_fats += fats
                    current_carbs += carbs
                    # выводим выбранное блюдо, граммовку и питательные вещества на экран
                    print_recommendation(dish, grams, calories, proteins, fats, carbs, recipe)
                else:
                    # если такого блюда нет в таблице, то выводим сообщение об ошибке
                    
                    bot.send_message(user_id,"Такого блюда нет в таблице, пожалуйста, выбери другое блюдо")
                    continue
            elif temp_ans['answer'] == '2':
                del temp_ans['answer']
                # получаем рекомендованное блюдо, граммовку и питательные вещества от функции
                recommendation = recommend_dish(current_calories, current_proteins, current_fats, current_carbs)
                # если функция вернула None, то значит, что нет подходящих блюд
                if recommendation is None:
                    bot.send_message(user_id,"Нет подходящих блюд для следующего приема пищи, пожалуйста, выбери другой вариант")
                    continue
                # иначе, распаковываем рекомендацию в переменные
                else:
                    dish, grams, calories, proteins, fats, carbs, recipe = recommendation
                    # обновляем текущие значения калорий и питательных веществ для пользователя
                    current_calories += calories
                    current_proteins += proteins
                    current_fats += fats
                    current_carbs += carbs
                    # выводим рекомендованное блюдо, граммовку и питательные вещества на экран
                    print_recommendation(dish, grams, calories, proteins, fats, carbs, recipe)
            # если пользователь ввел что-то другое, то выводим сообщение об ошибке
            else:
                bot.send_message(user_id,"Неверный выбор, пожалуйста, введи 1 или 2")
                continue
            # спрашиваем пользователя, хочет ли он продолжить приемы пищи или закончить программу
            #bot.send_message(user_id, "Вы хотите продолжить приемы пищи или закончить программу? (введите 1 или 2)\n1. Продолжить\n2. Закончить\n")
            keyboard = types.InlineKeyboardMarkup() #наша клавиатура
            key_11 = types.InlineKeyboardButton(text='Продолжить', callback_data='11') #кнопка «Да»
            keyboard.add(key_11); #добавляем кнопку в клавиатуру
            key_22= types.InlineKeyboardButton(text='Закончить', callback_data='22')
            keyboard.add(key_22)
            question = 'Ты хочешь продолжить приемы пищи или закончить программу?'
            bot.send_message(user_id, text=question, reply_markup=keyboard)
            while 'otvet' not in temp_ans:
                pass
            # если пользователь выбрал 1, то продолжаем цикл
            if temp_ans['otvet'] == "1":
                del temp_ans['otvet']
                continue
                
            # если пользователь выбрал 2, то завершаем цикл и программу
            elif temp_ans['otvet'] == "2":
                del temp_ans['otvet']
                bot.send_message(user_id,"Спасибо за использование программы, до новых встреч!")
                break
            # если пользователь ввел что-то другое, то выводим сообщение об ошибке и продолжаем цикл
            else:
                bot.send_message(user_id,"Неверный выбор, пожалуйста, введи 1 или 2")
                continue

    #Определяем обработчик команды /exchange



# Запускаем бота
bot.polling()



