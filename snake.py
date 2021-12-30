from turtle import Turtle

POSICAO_INICIAL = [(0,0),(-20,0),(-40,0)]
DISTANCIA = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    
    def __init__(self):
       self.seguimentos = []
       self.criarSnake()
       self.head = self.seguimentos[0]    

    def criarSnake(self):
        for posicao in POSICAO_INICIAL:
            self.add_segmento(posicao)
    
    def add_segmento(self, posicao):
        novoSeguimento = Turtle(shape="square")
        novoSeguimento.color("green")
        novoSeguimento.penup()
        novoSeguimento.goto(posicao)
        self.seguimentos.append(novoSeguimento)

    def extender(self):
        self.add_segmento(self.seguimentos[-1].pos())

    def mover(self):
        for num_seg in range(len(self.seguimentos) - 1, 0 , -1):
            pos_x = self.seguimentos[num_seg - 1].xcor()
            pos_y = self.seguimentos[num_seg - 1].ycor()
            self.seguimentos[num_seg].goto(pos_x,pos_y)
        self.head.fd(DISTANCIA)        
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)