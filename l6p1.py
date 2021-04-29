from time import sleep
class TrafficLight:
    __color = 'Белый'

    def running(self):
        while True:
            print('Красный')
            sleep(7)
            print('Жёлтый')
            sleep(2)
            print('Зелёный')
            sleep(10)

trafficLight = TrafficLight()
trafficLight.running()