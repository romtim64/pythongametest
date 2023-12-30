import gamemap as gm
import time
class enemy:
    def __init__(self,type,health,damage,posx,posy):
        self._type = type
        self._health = health
        self._damage = damage
        self._posx = posx
        self._posy = posy
    def enemylosehp(self,damagetaken):
        self._health -= damagetaken

    def get_enemstats(self):
        return(self._type,self._health,self._damage,self._posx,self._posy)
    def enemymoves(self):
        if self._health > 0: # если враг живой
            et = self._type
            ex = self._posx
            ey = self._posy
            import random as rnd
            if et == 1:  # если тип врага 1 (рандомный) он просто ходит на 1 клетку каждый ход

                ev = rnd.randint(0, 4)  # рандомим действие врагу (0 - он стоит , 1-4 ходит в одном из направлений)

                if ev == 0:  # если 0 то стоит
                    self._posx = ex
                    self._posy = ey  # возвращаем значение координат врага

                elif ev == 1:  # если 1 то вверх
                    if ey > 0:  # если ещё есть куда идти
                        ey -= 1  # двигаться вверх
                        self._posx = ex
                        self._posy = ey
                    else:  # если некуда идти
                        ey += 1  # то он отойдёт от стены
                        self._posx = ex
                        self._posy = ey


                elif ev == 2:  # если 2 то вправо
                    if ex < 4:  # если ещё есть куда идти
                        ex += 1  # двигаться вправо
                        self._posx = ex
                        self._posy = ey
                    else:  # если некуда идти
                        ex -= 1  # то он отойдёт от стены
                        self._posx = ex
                        self._posy = ey


                elif ev == 3:  # если 3 то вниз
                    if ey < 4:  # если ещё есть куда идти
                        ey += 1  # двигаться вниз
                        self._posx = ex
                        self._posy = ey
                    else:  # если некуда идти
                        ey -= 1  # то он отойдёт от стены
                        self._posx = ex
                        self._posy = ey


                elif ev == 4:  # если 4 то влево
                    if ex > 0:  # если ещё есть куда идти
                        ex -= 1  # двигаться влево
                        self._posx = ex
                        self._posy = ey
                    else:  # если некуда идти
                        ex += 1  # то он отойдёт от стены
                        self._posx = ex
                        self._posy = ey
            elif et == 2:  # если тип врага 2 (прыгучий) то он рандомно прыгает через 1 2 или 3 клетки (если стена то врезается)
                self._posx = ex
                self._posy = ey

            elif et == 3:  # если тип врага 3 (преследующий) то он двигается в сторону игрока сокращая дистанцию
                self._posx = ex
                self._posy = ey







# свойства игрока (x,y,номер комнаты,наличие оружия,иконка,хп) (в начале он в центре карты)
player = [2, 2, 12, 0, '☺', 3, 0]
def player_moves(x, y, v, l): #движение игрока с запросом коорд и направления
    oldx = x #сохраняем старые корды на всякий случай
    oldy = y #чтобы потом можно было откатить игрока к ним
     
    if v == 'w':  # если w то вверх
        if x == 2 and y == 0 and l >= 5: #если игрок у верха комнаты по середине
            l -= 5 #двигаем его на комнату вверх
            y = 4 #двигаем игрока в нижнюю часть комнаты
            return (x, y, l) #возвращаем координаты и комнату
        else:
            if y > 0:  # если ещё есть куда идти
                y -= 1  # двигаться вверх
                return (x, y, l) #возвращаем координаты и комнату
            else:  # если некуда идти
                y = oldy  # то он вернётся как был
                return (x, y, l) #возвращаем координаты и комнату

    elif v == 'd':  # если d то вправо
        if x == 4 and y == 2 and ((l+1) % 5) != 0: #если игрок у правого бока комнаты по середине
            l += 1 #двигаем его на комнату вправо
            x = 0 #двигаем игрока в левую часть комнаты
            return (x, y, l) #возвращаем координаты и комнату
        else:
            if x < 4:  # если ещё есть куда идти
                x += 1  # двигаться вправо
                return (x, y, l) #возвращаем координаты и комнату
            else:  # если некуда идти
                x = oldx  # то он вернётся как был
                return (x, y, l) #возвращаем координаты и комнату

    elif v == 's':  # если w то вниз
        if x == 2 and y == 4 and l <= 19: #если игрок у низа комнаты по середине
            l += 5 #двигаем его на комнату вниз
            y = 0 #двигаем игрока в верхнюю часть комнаты
            return (x, y, l) #возвращаем координаты и комнату
        else:
            if y < 4:  # если ещё есть куда идти
                y += 1  # двигаться вниз
                return (x, y, l) #возвращаем координаты и комнату
            else:  # если некуда идти
                y = oldy  # то он вернётся как был
                return (x, y, l) #возвращаем координаты и комнату

    elif v == 'a':  # если d то влево
        if x == 0 and y == 2 and l != 0 and (l % 5) != 0:  # если игрок у левого бока комнаты по середине
            l -= 1  # двигаем его на комнату влево
            x = 4  # двигаем игрока в правую часть комнаты
            return (x, y, l)  # возвращаем координаты и комнату
        else:
            if x > 0:  # если ещё есть куда идти
                x -= 1  # двигаться влево
                return (x, y, l) #возвращаем координаты и комнату
            else:  # если некуда идти
                x = oldx  # то он вернётся как был
                return (x, y, l) #возвращаем координаты и комнату
    elif v != 'w' and v != 'a' and v != 's' and v != 'd':
        return (x, y, l)

def gamemapprint(ggmap, layer): #выводим карту на нужном уровне
    print('map','\n',ggmap[layer][0],'\n',ggmap[layer][1],'\n',ggmap[layer][2],'\n',ggmap[layer][3],'\n',ggmap[layer][4],'\n',sep = '')

enem1 = enemy(1,2,1,0,0)
enem2 = enemy(1,2,1,4,4)


gm.gmap[12][enem1.get_enemstats()[4]][enem1.get_enemstats()[3]] = '☻' #отрисовываем первого врага первый раз
gm.gmap[12][enem2.get_enemstats()[4]][enem2.get_enemstats()[3]] = '☻' #отрисовываем второго врага первый раз
gm.gmap[player[2]][player[0]][player[1]] = player[4] #отрисовываем игрока первый раз

fin = 0
while fin == 0: #пока игра не завершена

    if player[5] == 0: #если жизни кончились
        fin = 1 #завершаем игру первой концовкой(смерть)
        break
    if player[6] != 0: #если у игрока есть неуязвимость
        player[6] -= 1 #снимаем 1 очко неуязвимости
    else: #если неуязвимости нет
        player[4] = '☺' #поддерживаем норм модель


    pin = input('wasd to move ') #игрок вводит в консоли направление
    gm.gmap[player[2]][player[1]][player[0]] = '_' #стираем старую координату игрока

    gm.gmap[12][enem1.get_enemstats()[4]][enem1.get_enemstats()[3]] = '_'  # стираем старую координату врага
    gm.gmap[12][enem2.get_enemstats()[4]][enem2.get_enemstats()[3]] = '_'  # стираем старую координату врага

    px = player[0]
    py = player[1]

    player[0],player[1],player[2] = player_moves(player[0],player[1],pin,player[2]) #получаем новую координату по направлению

    enem1.enemymoves()  # получаем новую координату врага
    enem2.enemymoves()  # получаем новую координату врага

    if (enem1.get_enemstats()[3] == player[0]) and (enem1.get_enemstats()[4] == player[1]) and (player[6] == 0) and (player[3]==0) and (player[2] == 12): #если игрок каснулся врага и не был неуязвим, и у игрока не было оружия
        player[5] -= 1 # отнимаем жизнь
        player[6] = 3 # даём неуязвимость на 3 хода
        player[0] = px # откатываем игрока
        player[1] = py # имитируя отталкивание от врага
        player[4] = '○' # меняем модель на неуязвимую
        print(player[0],player[1],enem1.get_enemstats()[3],enem1.get_enemstats()[4])

    if (enem2.get_enemstats()[3] == player[0]) and (enem2.get_enemstats()[4] == player[1]) and (player[6] == 0) and (player[3]==0) and (player[2] == 12): #если игрок каснулся врага и не был неуязвим, и у игрока не было оружия
        player[5] -= 1 # отнимаем жизнь
        player[6] = 3 # даём неуязвимость на 3 хода
        player[0] = px # откатываем игрока
        player[1] = py # имитируя отталкивание от врага
        player[4] = '○' # меняем модель на неуязвимую
        print(player[0], player[1], enem2.get_enemstats()[3], enem2.get_enemstats()[4])

    gm.gmap[player[2]][player[1]][player[0]] = player[4] # отрисовываем игрока на новой координате
    gm.gmap[12][enem1.get_enemstats()[4]][enem1.get_enemstats()[3]] = '☻' #отрисовываем врага на новой координате
    gm.gmap[12][enem2.get_enemstats()[4]][enem2.get_enemstats()[3]] = '☻'  # отрисовываем врага на новой координате

    gamemapprint(gm.gmap,player[2]) #отрисовываем карту с новым положением игрока и монстра(в комнате игрока)

elif fin == 0:
    print('error') 
elif fin == 1:
    print('you lose')
elif fin == 2:
    print('you win')
elif fin >= 3:
    print('unknown ending') 