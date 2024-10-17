import time
import matplotlib.pyplot as plt


from Adafruit_ADS1x15 import ADS1115

adc = ADS1115()
GAIN = 1
val = []
cnt = 0

plt.ion()

adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0')

def makeFig():
    plt.ylim(-5000, 5000)
    plt.title('Osciloscope')
    plt.grid(True)
    plt.ylabel('ADC outputs')
    plt.plot(val, 'ro-', label='Channel 0')
    plt.legend(loc='lower right')

fig, ax = plt.subplots()
line, = ax.plot(val)

while True:
    value = adc.get_last_result()
    print('Channel 0: {0}'.format(value))
    time.sleep(0.5)
    val.append(int(value))
    
    plt.pause(0.000001)
    cnt += 1
    if cnt > 50:
        val.pop(0)
        line.set_data(range(len(val)), val)
        ax.relim()
        ax.autoscale_view()
