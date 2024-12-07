
import time
from spherov2.types import Color
from enum import Enum

class ColorEnum(Enum):
    RED = Color(r=255, g=0, b=0)
    GREEN = Color(r=0, g=255, b=0)
    BLUE = Color(r=0, g=0, b=255)
    WHITE = Color(r=255, g=255, b=255)
    OFF = Color(r=0, g=0, b=0)

def flash_down(sphero, color_one: Color,  color_two: Color, times: int):
    RATIO = 0.5

    for t in range(times):
      sphero.set_main_led(color_one)
      time.sleep(t * RATIO)
      sphero.set_main_led(color_two)
      time.sleep(t * RATIO)

def simple(sphero):
    sphero.set_main_led(ColorEnum.WHITE.value)
    sphero.set_speed(60)
    time.sleep(1)
    flash_down(sphero, ColorEnum.GREEN.value, ColorEnum.RED.value, 4)
    sphero.spin(360, 1)
    sphero.set_main_led(ColorEnum.WHITE.value)
    sphero.set_speed(60)
    time.sleep(1)
    sphero.set_speed(0)