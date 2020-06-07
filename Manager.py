import os
import webbrowser
import keyboard
import time

#Remove old image files if they exist
if (os.path.isfile("HTNE_image.jpg")):
    os.remove("HTNE_image.jpg")
if(os.path.isfile("HTNE_stage.jpg")):
    os.remove("HTNE_stage.jpg")

#The Manager will then go to the google colab in chrome and analyze an image.
#Here you will be prompted for an image.
url = 'https://colab.research.google.com/drive/17EUBn6HO_AMS5Ecx7oNSbEeV1SPBVziu#scrollTo=sqfO0s1Pe3YD'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)
print("Launching Colab...")
time.sleep(20)

#Once the Runtime Type is reset, the manager runs the colab code.
keyboard.press_and_release('Ctrl + F9')
time.sleep(10)
print("Waiting...")
keyboard.press_and_release('Tab') 
keyboard.press_and_release('Enter')

#Then it must wait until the resulting file is downloaded and the code is run.
#You,t he user, must put that file in the same directory as this project.
while not (os.path.isfile("HTNE_stage.jpg")):
    print("Waiting For Stage...")
    time.sleep(20)
    continue

#Once downloaded, the manager runs the game code with the new image file
print("Launching Game...")
os.system('cmd /c "python HTNE_Game.py"')
