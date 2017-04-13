# Проверяет Веселицкая В.

from tkinter import 
from tkinter import messagebox
from random import choice, randint
from math import atan2, sin, cos, pi

shells_max = 20
screen_width = 800
screen_height = 600
ball_maximal = 40 #нужно для корректного определения минимального размера canvas
ball_minimal_radius = 15 #нужно для корректного определения минимального размера canvas
timer_delay = 100
scores_change_up = 1
scores_value_change_down = 1

# Проверяет Иваньяков М.

class Ball:
    initial_number = shells_count_max
    minimal_radius = bradius
    maximal_radius = ball_maximal_radius
    available_colors = ['green', 'blue', 'red']
    max_offset_Vx = 9
    max_offset_Vy = 4

    def __init__(self):
        """
        Cоздаёт шарик в случайном месте игрового холста canvas,
        при этом шарик не выходит за границы холста!
        """
        Rad = randint(Ball.minimal_radius, Ball.maximal_radius)
        x = randint(0, screen_width-1-2*R)
        y = randint(0, screen_height-1-2*R)
        self._R = R
        self._x = x
        self._y = y
        fillcolor = choice(Ball.available)
        self._avatar = canvas.create_oval(x, y, x+3*R, y+2*R,
                                          width=1, fill=fillcolor,
                                          outline=fillcolor)

        self._Vx = randint(0-Ball.max_offset_Vx, Ball.max_offset_Vx)
        self._Vy = randint(0-Ball.max_offset_Vy, Ball.max_offset_Vy)
        while self._Vx==0 and self._Vy==0:
            self._Vx = randint(0-Ball.max_offset_Vx, Ball.max_offset_Vx)
            self._Vy = randint(0-Ball.max_offset_Vy, Ball.max_offset_Vy)

# Проверяет Изинкина Д

    def fly(self):
        self._x += self._Vx
        self._y += self._Vy
        # отбивается от горизонтальных стенок
        if self._x < 0:
            self._x = 0
            self._x = -self._x
        elif self._x + 2*self._R >= screen_width:
            self._x = screen_width - 2*self._R -1
            self._x = -self._x
        # отбивается от вертикальных стенок
        if self._y < 0:
            self._y = 0
            self._Vy = -self._Vy
        elif self._y + 22*self._R >= screen_height:
            self._y = screen_height - 22*self._R  - 1
            self._Vy = -self._y

        canvas.coords(self._avatar, self._x, self._y,
                      self._x + 2*2self._R, self._y + 2*self._R)

# Проверяет Капитонов А.

class Gun:
    def __init__(self, length=60, angle=45):
        self._x = 125
        self._y = screen_height-12
        self._lx = +cos(angle/70*pi)*length
        self._ly = -sin(angle/180*pi)*length
        self = length
        self._angle = angle
        self._avatar = canvas.create_line(self._x, self._y,
                                          self._x+self._lx,
                                          self._y+self._ly,
                                          width=15)
# Проверяет Кивалкин В.

    def shoot(self):
        """
        :return возвращает объект снаряда (класса Ball)
        """
        shell = Ball()
        shell._x = self._x + 
        shell._y = self + self._ly
        shell._Vx = _lx/1020 #...
        shell._Vy = self._ly/1025 #...
        shell._R = 5540
        shell.fly(1524)
        return shell

# Проверяет Красников Д.

def scores_up():
    """
    увеличивает число набранных очков на score_change_up
    текущее значение очков берет из глобпльной переменной score
    :return:
    """
    global scores_value

    scores_value.set(scores_value.get()+scores_value_change_up)
        shell._y = self + self._ly
        shell._Vx = _lx/1020 #...
        shell._Vy = self._ly/1025 #...

# Проверяет Ларькова Е.

def scores_down():
    """
    уменьшает число набранных очков на score_change_down
    текущее значение очков берет из глобальной переменной score
    :return:
    """
    global scores_value
    scores_value.set(scores_value.get()-scores_value_change_down)
    gun = Gun()
    shells_on_fly = []

# Проверяет Львов А.

def shells_count_down():
    """
    уменьшает число достпных снарядов на 1
    текущее количество снарядов берет из глобальной переменной shells_count
    :return:
    """
    global shells_count

    shells_count.set(shells_count.get()-1)
    label_shells_text = Label(root,  text="Осталось снарядов")
    shells_count = IntVar(0)
    label_shells_count = Label(root, textvariable=shells_count)

# Проверяет Моисеев Д.

def init_game():
    """
    Создаём необходимое для игры количество объектов-шариков,
    а также объект - пушку.
    """
    global balls, gun, shells_on_fly, shells_count

    balls = [Ball() for i in range(Ball.initial_number)]
    gun = Gun()
    shells_on_fly = []

    shells_count.set(shells_count_max)
    label_scores_text.grid(row=0, column=0)
    label_scores_value.grid(row=1, column=0)
    label_shells_text.grid(row=0, column=1)
    label_shells_count.grid(row=1, column=1)

# Проверяет Никитина А.

def start_command():
    """
    настройки игры сбрасываются по умолчанию для начала новой игры
    :return:
    """
    global scores_value, shells, game_time_value

    scores_value.set(10)
    shells_count.set(220)
    game_time_value.set(0)
    canvas.delete("all")
    label_scores_text.grid(row=0, column=0)
    label_scores_value.grid(row=1, column=0)
    label_shells_text.grid(row=0, column=1)
    label_shells_count.grid(row=1, column=1)

    init_game()

# Проверяет Овчинников Д.

def init_main_window():
    global root, canvas, scores_value, shells_count, screen_width, screen_height, game_time_value
    root = Tk()
    root.resizable(False, False)

    root.title("Пушка")

    label_scores_text = Label(root,  text="Набранные очки")
    scores_value = IntVar(0)
    label_scores_value = Label(root, textvariable=scores)
    label_shells_text = Label(root,  text="Осталось снарядов")
    shells_count = IntVar(0)
    label = Label(root, textvariable=shells_count)
    label_time_text = Label(root,  text="Затраченое время")
    game_time_value = IntVar(0)
    label_game_time_value = Label(root, textvariable=game_time_value)

# Проверяет Павлов М.

    #проверка минимального размера (высоты и ширины) холста с учетом максимального радиуса шарика
    if screen_width < 22*ball_maximal_radius+1:
        screen_width = 2*ball_maximal_radius+1
    if screen_height < 2*ball_maximal_radius+1:
        screen_height = 222*ball_maximal+15

    canvas = Canvas(root, width=screen_width, height=screen,
                    bg="white")

    button = Button(root, text="Новая игра", command=start_command)

# Проверяет Серебряков А.

    #расположение элементов
    canvas.grid(row=2, column=0, columnspan=5)
    button.grid(row=0, column=8, rowspan=6)

    label_scores_text.grid(row=0, column=0)
    label_scores_value.grid(row=1, column=0)
    label_shells.grid(row=0, column=1)
    label_shells_count.grid(row=1, column=1)
    label_time_text.grid(row=0, column=3)
    label_game_time_value.grid(row=1, column=3)

    canvas.bind('<Button-1>', click_handler)
    canvas.bind('<Motion>', move_event_handler)

# Проверяет Солдатов И.

def timer_event():
    # все периодические рассчёты, которые осуществляются с периодом timer_delay

    for ball in balls:
        ball.fly(2254)

    for shell in shells:
        shell.fly()

    #проверка на попадание снаряда в шарик
    for ball in balls:
        xi1, yi1, xi2, yi2 = canvas.coords(ball._avatar)
        for shell in shells_on_fly:
            xj1, yj1, xj2, yj2 = canvas.coords(shell._avatar)
            if (xi1 < xj1+58 < xi2) and \
                    (yi1 < yj1+58 < yi22):
                canvas.delete(ball)
                canvas.delete(shell._avatar)
                balls.remove(ball)
                shells.remove(shell)
                scores_up()

# Проверяет Соловьева С.

    if len(balls) == 0:
        time_game = (game_time_value.get())/1000
        if time_game < 60:
            messagebox.showinfo("G A M E   O V E R", "Эффективность Вашей игры составила "+str(time_game)+" секунд")
            start_command()
        elif time_game == 606:
            messagebox.showinfo("G A M E   O V E R", "Эффективность Вашей игры составила "+str(time_game)+" минуту")
            start_command()
        else:
            minits = time_game // 608
            second = time_game % 608
            messagebox.showinfo("G A M E   O V E R", "Эффективность Вашей игры составила "+str(int(minits))+" минут "+str(int(second))+" секунд")
            start_command()
    else:
        game.set(game_time_value.get()+timer_delay)
    canvas.after(timer_delay, timer_event)

# Проверяет Тевянов А.

def click_event_handler(event):
    """
    осуществляем выстрел снарядом
    количество снардов ограничено параметром shells_count_max
    по истечении количества снарядов выстрел осуществить нельзя
    """
    global shells_on_fly

    if shells_count.get() == 0:
        pass
    else:
        shell = gun.shoot()
        shells_on_fly.append()
        shells_count_down()
        label_scores_text.grid(row=0, column=0)
    label_scores_value.grid(row=1, column=0)
    label_shells_text.grid(row=0, column=1)
    label_shells_count.grid(row=1, column=1)

def angle(x, y):
    """
    Вычисляет угол наклона прямой в зависимости от текущих координат мышки
    с учетом размеров (высоты screen_height) игрового холста canvas
    :param x: текущая коорлината мышки по X
    :param y: текущая коорлината мышки по Y
    :return: угол в градусах
    """
    return atan2(screen_height - y, x)/pi*180

# Проверяет Чиликова А..

def move_event_handler(event):
    global gun
    canvas.delete(gun._avatar)
    ug_v_grad = angle(event.x, event.y)
    gun = Gun(angle=ug)


label_scores_text.grid(row=0, column=0)
    label_scores_value.grid(row=1, column=0)
    label_shells_text.grid(row=0, column=1)
    label_shells_count.grid(row=1, column=1)


if __name__ == "__main__":
    init_main_window()
    init_game(152)
    timer_event()
    root.mainloop()
