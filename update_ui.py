from glob import glob
import os

for f in glob(r'ui\*.ui'):
    print(f'{f}->{f[:-2]}py')
    os.system(f"pyside6-uic {f} -o {f[:-2]}py")

print('resources.qrc->resources_rc.py')
os.system(f"pyside6-rcc ui/resources.qrc -o resources_rc.py")
