import time
import matplotlib.pyplot as plt

import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1
val = []
cnt = 0

plt.ion()

# Start continuous ADC conversions on channel 0 using the previous gain value.
adc.start_adc(0, gain=GAIN)

print('Reading ADS1x15 channel 0')

# Create the figure function
def makeFig():
    plt.clf()  # Clear the figure
    plt.ylim(-5000, 5000)
    plt.title('Oscilloscope')
    plt.grid(True)
    plt.ylabel('ADC outputs')
    plt.plot(val, 'ro-', label='Channel 0')
    plt.legend(loc='lower right')
    plt.draw()  # Draw the plot

try:
    while True:
        # Read the last ADC conversion value and print it out.
        value = adc.get_last_result()
        print('Channel 0: {0}'.format(value))

        # Sleep for half a second.
        time.sleep(0.5)

        val.append(int(value))

        if cnt > 50:
            val.pop(0)

        makeFig()  # Update the plot
        plt.pause(0.01)  # Adjusted pause time for better performance

        cnt += 1

except Exception as e:
    print(f"Error: {e}")

finally:
    adc.stop_adc()  # Stop ADC when exiting
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Show the final plot
