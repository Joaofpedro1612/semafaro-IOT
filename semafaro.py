from machine import Pin
from utime import sleep

sinalVerde = Pin(17, Pin.OUT)
sinalAmarelo = Pin(16, Pin.OUT)
sinalVermelho = Pin(15, Pin.OUT)

while True:
  sinalVerde.on()
  sinalAmarelo.off()
  sinalVermelho.off()
  print("sinal verde, ligando!!!")
  sleep(20)
  sinalVerde.off()
  print("sinal verde, desligando!!!")
  sleep(0.5)
  sinalAmarelo.on()
  print("sinal amarelo, ligando!!!")
  sleep(10)
  sinalAmarelo.off()
  print("sinal amarelo, desligando!!!")
  sleep(0.5)
  sinalVermelho.on()
  print("sinal vermelho, ligando!!!")
  sleep(7)
  sinalVermelho.off()
  print("sinal vermelho, desligando!!")
  sleep(0.5)