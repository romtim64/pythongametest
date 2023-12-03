import gamemap as gm
import random as rnd

# типы врагов и их координаты хранятся тут
enemys = [
    ['☻', 0, 0],
    ['♦', 0, 0],
    ['☼', 0, 0],
]

# свойства игрока (x,y,номер комнаты,наличие оружия,иконка,хп) (в начале он в центре карты)
player = [2, 2, 13, 0, '☺', 3, 0]

def enemy_moves(t, ex, ey): #запрос типа врага и его координат
    oldex = ex
    oldey = ey

    if t == '☻': #если тип врага 1 (рандомный) он просто ходит на 1 клетку каждый ход

        ev = rnd.randint(0,4) #рандомим действие врагу (0 - он стоит , 1-4 ходит в одном из направлений)

        if ev == 0: #если 0 то стоит
            return(ex, ey) #возвращаем значение координат врага

        elif ev == 1: #если 1 то вверх
            if ey > 0: #если ещё есть куда идти
                ey -= 1 #двигаться вверх
                return (ex, ey)
            else: #если некуда идти
                ey += 1 #то он отойдёт от стены
                return (ex, ey)


        elif ev == 2: #если 2 то вправо
            if ex < 4: #если ещё есть куда идти
                ex += 1 #двигаться вправо
                return(ex, ey)
            else: #если некуда идти
                ex -= 1 #то он отойдёт от стены
                return (ex, ey)


        elif ev == 3: #если 3 то вниз
            if ey < 4: #если ещё есть куда идти
                ey += 1 #двигаться вниз
                return(ex, ey)
            else: #если некуда идти
                ey -= 1 #то он отойдёт от стены
                return (ex, ey)


        elif ev == 4: #если 4 то влево
            if ex > 0: #если ещё есть куда идти
                ex -= 1 #двигаться влево
                return(ex, ey)
            else: #если некуда идти
                ex += 1 #то он отойдёт от стены
                return (ex, ey)


    elif t == '♦':  #если тип врага 2 (прыгучий) то он рандомно прыгает через 1 2 или 3 клетки (если стена то врезается)
        return(ex, ey)
    elif t == '☼': #если тип врага 3 (преследующий) то он двигается в сторону игрока сокращая дистанцию
        return(ex, ey)

def player_moves(x, y, v): #движение игрока с запросом коорд и направления
    oldx = x #сохраняем старые корды на всякий случай
    oldy = y #чтобы потом можно было откатить игрока к ним
     
    if v == 'w':  # если w то вверх
        if y > 0:  # если ещё есть куда идти
            y -= 1  # двигаться вверх
            return (x, y)
        else:  # если некуда идти
            y = oldy  # то он вернётся как был
            return (x, y)

    elif v == 'd':  # если d то вправо
        if x < 4:  # если ещё есть куда идти
            x += 1  # двигаться вправо
            return (x, y)
        else:  # если некуда идти
            x = oldx  # то он вернётся как был
            return (x, y)

    elif v == 's':  # если w то вниз
        if y < 4:  # если ещё есть куда идти
            y += 1  # двигаться вниз
            return (x, y)
        else:  # если некуда идти
            y = oldy  # то он вернётся как был
            return (x, y)

    elif v == 'a':  # если d то влево
        if x > 0:  # если ещё есть куда идти
            x -= 1  # двигаться влево
            return (x, y)
        else:  # если некуда идти
            x = oldx  # то он вернётся как был
            return (x, y)

def gamemapprint(ggmap, layer): #выводим карту на нужном уровне
    print('map','\n',ggmap[layer][0],'\n',ggmap[layer][1],'\n',ggmap[layer][2],'\n',ggmap[layer][3],'\n',ggmap[layer][4],'\n',sep = '')

gm.gmap[13][enemys[0][1]][enemys[0][2]] = enemys[0][0] #отрисовываем врага первый раз
gm.gmap[player[2]][player[0]][player[1]] = player[4] #отрисовываем игрока первый раз

fin = 0
while fin == 0: #пока игра не завершена

    if player[6] != 0: #если у игрока есть неуязвимость
        player[6] -= 1 #снимаем 1 очко неуязвимости
    else: #если неуязвимости нет
        player[4] = '☺' #поддерживаем норм модель
    if player[5] == 0: #если жизни кончились
        fin = 1 #завершаем игру первой концовкой(смерть)

    pin = input('wasd to move ') #игрок вводит в консоли направление
    gm.gmap[player[2]][player[1]][player[0]] = '_' #стираем старую координату игрока
    gm.gmap[13][enemys[0][2]][enemys[0][1]] = '_'  # стираем старую координату врага

    px = player[0]
    py = player[1]

    player[0],player[1] = player_moves(player[0],player[1],pin) #получаем новую координату по направлению
    enemys[0][1],enemys[0][2] = enemy_moves(enemys[0][0], enemys[0][1],enemys[0][2])  # получаем новую координату врага

    if (enemys[0][1] == player[0]) and (enemys[0][2] == player[1]) and (player[6] == 0) and (player[3]==0): #если игрок каснулся врага и не был неуязвим, и у игрока не было оружия
        player[5] -= 1 # отнимаем жизнь
        player[6] = 3 # даём неуязвимость на 3 хода
        player[0] = px # откатываем игрока
        player[1] = py # имитируя отталкивание от врага
        player[4] = '○' # меняем модель на неуязвимую

    gm.gmap[player[2]][player[1]][player[0]] = player[4] # отрисовываем игрока на новой координате
    gm.gmap[13][enemys[0][2]][enemys[0][1]] = enemys[0][0] #отрисовываем врага на новой координате

    gamemapprint(gm.gmap,player[2]) #отрисовываем карту с новым положением игрока и монстра(в комнате игрока)


if fin == 1:
    print('you lose')
elif fin == 2:
    print('you win')