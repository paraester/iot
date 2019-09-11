import datetime  # importar a biblioteca datetime
import telepot   # importar a biblioteca telepot
from telepot.loop import MessageLoop    # função da biblioteca que comunica com telegram bot
from time import sleep      
from pyA20.gpio import gpio
from pyA20.gpio import connector
from pyA20.gpio import port
import urllib.request as req
proxy = req.ProxyHandler({'https': r'http://usuario:senha@vvvvvvvvvv:porta'})
telepot.api.set_proxy('http://vvvvvv:porta', ('usuario', 'senha'))
gpio.init()
red_led_pin = port.PG7
green_led_pin = port.PG6
gpio.setcfg(red_led_pin, gpio.OUTPUT)
gpio.setcfg(green_led_pin, gpio.OUTPUT)
now = datetime.datetime.now() # Getting date and time
def handle(msg):
    chat_id = msg['chat']['id'] # Recebendo msg do Telegram
    command = msg['text']   #pegando o texto da mensagem
    print ('Received:')
    print(command)
    if command == '/olá':
        bot.sendMessage (chat_id, str("Olá! Teste acender led"))
    elif command == '/hora':
        bot.sendMessage(chat_id, str("Hora: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second))
    elif command == '/data':
        bot.sendMessage(chat_id, str("Data: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))
    elif command == '/status_red':
        bot.sendMessage (chat_id, str("O Led gpio1p40 está:"))
        if gpio.input(connector.gpio1p40) == 1:
            bot.sendMessage (chat_id, str("Ligado - ") + str(gpio.input(connector.gpio1p40)))
        else:
            bot.sendMessage (chat_id, str("Desligado -  ") + str(gpio.input(connector.gpio1p40)))
    elif command == '/status_verde':
        bot.sendMessage (chat_id, str("O Led gpio1p38 verde está:"))
        if gpio.input(connector.gpio1p38) == 1:
            bot.sendMessage (chat_id, str("Ligado - ") + str(gpio.input(connector.gpio1p38)))
        else:
            bot.sendMessage (chat_id, str("Desligado -  ") + str(gpio.input(connector.gpio1p38)))
    elif command == '/red1':
        bot.sendMessage(chat_id, str("Vermelho led está ON"))
        gpio.output(red_led_pin, True)
    elif command == '/red0':
        bot.sendMessage(chat_id, str("Vermelho led está OFF"))
        gpio.output(red_led_pin, False)
    elif command == '/verde1':
        bot.sendMessage(chat_id, str("Verde led está ON"))
        gpio.output(green_led_pin, True)
    elif command == '/verde0':
        bot.sendMessage(chat_id, str("Verde led está OFF"))
        gpio.output(green_led_pin, False)
# Insira o token telegram abaixo
bot = telepot.Bot('ccccc:dddddd')
print (bot.getMe())
MessageLoop(bot, handle).run_as_thread()
print ('Esperando....')
while 1:
    sleep(10)

