import barcode_driver
barcode = barcode_driver.barcode()

try:
    while True:
        barcode_input = barcode.read() 
        print(barcode_input)
except KeyboardInterrupt:
pass
