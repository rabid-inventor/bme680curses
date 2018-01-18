
import time, curses, random 
import bme680
sensor = bme680.BME680()

sensor.set_temperature_oversample(bme680.OS_8X)
PREFIX_SELECTED= '_X_' 
PREFIX_DESLECTED= '___'

screen = curses.initscr()

screen.erase()
screen.border(0)
screen.keypad(1)

data = [0,0,0,0]
#print (range(data))
def draw(dataset):
  screen.erase()
  for colombs in range(len(dataset)):
    #print(colombs)
    #print(range(data[colombs]))
    screen.addstr(0,0, str(sensor.data.temperature))
    for lines in range(data[colombs]):
      screen.addstr(36 - lines,(colombs),'|',curses.A_BOLD)
  
  screen.refresh()
a = 0 
while 1:
  sensor.get_sensor_data()
  a =  (sensor.data.temperature-20)*3
  if len(data) >= 100:
    data.pop()
  data.insert(0, int(a) )
  #data.pop()
  draw(data)
  time.sleep(0.2)

time.sleep(1)
screen.erase ()
curses.initscr()
curses.nocbreak()
curses.echo()
curses.endwin()





