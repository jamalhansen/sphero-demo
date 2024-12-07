from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from toy.actions import simple, flash_down, Color

sphero = scanner.find_toy()
with SpheroEduAPI(sphero) as droid:
    flash_down(droid, Color(r=255, g=0, b=0), Color(r=0, g=255, b=0), 4)
