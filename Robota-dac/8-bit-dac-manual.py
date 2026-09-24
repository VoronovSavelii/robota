import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# dac_bits = [22, 27, 17, 26, 25, 21, 20, 16]
dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.3
0

GPIO.setup(dac_bits, GPIO.OUT)

# duty = 0.0
# for i in dac_bits:
#     pwm = GPIO.PWM(i, 200)
#     pwm.start(duty)

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.0 - {dynamic_range:.2f} В)")
        print("устанавливаем 0.0 В")
        return 0
    
    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    binary_str = format(number, '08b')

    bits_list = [int(bit) for bit in binary_str]
    for index, bit in enumerate(bits_list):
        GPIO.output(dac_bits[index], bit)

    print(f"Число на вход ЦАП: {number}, биты: {bits_list}")

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()