import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
LED1 = 26
LED2 = 19
LED3 = 13
LED4 = 6
LED5 = 5

print ("Ultrasonic Sensor Test!")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)
GPIO.setup(LED5,GPIO.OUT)


GPIO.output(TRIG,False)
GPIO.output(LED1,False)
GPIO.output(LED2,False)
GPIO.output(LED3,False)
GPIO.output(LED4,False)
GPIO.output(TRIG,False)

def calc_distance(pulse_end,pulse_start):
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance,2)
	print ("Distance: " + str(distance) +" cm")
	return distance

def pulse_time():
	GPIO.output(TRIG,True)
	time.sleep(0.00001)
	GPIO.output(TRIG,False)
	while GPIO.input(ECHO) == 0:
		pulse_start = time.time()
	while GPIO.input(ECHO) == 1:
		pulse_end = time.time()
	return pulse_end, pulse_start

def led_on(cm):
	if cm > 25:
		GPIO.output(LED1,False)
		GPIO.output(LED2,False)
		GPIO.output(LED3,False)
		GPIO.output(LED4,False)
		GPIO.output(LED5,False)
	elif cm < 25 and cm >= 20:
		GPIO.output(LED1,True)
		GPIO.output(LED2,False)
		GPIO.output(LED3,False)
		GPIO.output(LED4,False)
		GPIO.output(LED5,False)
	elif cm < 20 and cm >= 15:
		GPIO.output(LED1,True)
		GPIO.output(LED2,True)
		GPIO.output(LED3,False)
		GPIO.output(LED4,False)
		GPIO.output(LED5,False)
	elif cm < 15 and cm >= 10:
		GPIO.output(LED1,True)
		GPIO.output(LED2,True)
		GPIO.output(LED3,True)
		GPIO.output(LED4,False)
		GPIO.output(LED5,False)
	elif cm < 10 and cm >= 5:
		GPIO.output(LED1,True)
		GPIO.output(LED2,True)
		GPIO.output(LED3,True)
		GPIO.output(LED4,True)
		GPIO.output(LED5,False)
	else:
		GPIO.output(LED1,True)
		GPIO.output(LED2,True)
		GPIO.output(LED3,True)
		GPIO.output(LED4,True)
		GPIO.output(LED5,True)
	return

print ("Waiting for 2s...")
time.sleep(2)

while True:
	try:
		pulse_end, pulse_start = pulse_time()
		distance = calc_distance(pulse_end,pulse_start)
		led_on(distance)
		time.sleep(0.5)
	except(KeyboardInterrupt):
		GPIO.cleanup()
