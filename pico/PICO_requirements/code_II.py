
import lcd_rgb
import time

if __name__ == "__main__":
    #lcd_rgb.demo()
    while True:

        lcd_rgb.clear_screen()
        lcd_rgb.show()

        time.sleep(1)