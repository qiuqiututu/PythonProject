"""
ADB命令控制手机完成自动化
"""
import time
import subprocess
#每次操作的间隔时间取决于手机配置，配置越高时间越短
# sleep_time = 1
for j in range(4):
  i = 0
  while i <= 6:
    #用popen设置shell=True不会弹出cmd框
    process = subprocess.Popen('adb shell input keyevent KEYCODE_DPAD_DOWN',shell=True)
    # time.sleep(sleep_time)
    time.sleep(1)
    process = subprocess.Popen('adb shell input keyevent KEYCODE_DPAD_CENTER', shell=True)
    time.sleep(2)
    process = subprocess.Popen('adb shell input keyevent KEYCODE_DPAD_CENTER', shell=True)
    # time.sleep(sleep_time)
    time.sleep(1)
    # process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
    # time.sleep(sleep_time)
    i += 1
  while i<=13:
    process = subprocess.Popen('adb shell input keyevent KEYCODE_DPAD_UP', shell=True)
    time.sleep(1)
    process = subprocess.Popen('adb shell input keyevent KEYCODE_DPAD_CENTER', shell=True)
    time.sleep(2)
    process = subprocess.Popen('adb shell input keyevent KEYCODE_DPAD_CENTER', shell=True)
    time.sleep(1)
    i += 1