#Wallpaper Birthday Automation
#I always forget birthdays, so I wanted to make a program that did the
#remembering for me in the least obtrusive way I could think of.

#The idea is that the program keeps a dictionary of names and birthdays,
#and that when a birthday is approaching (default set to 3 days away)
#it will open the current wallpaper, edit in a message of the approaching
#birthday, save it, and reload the registry.

from PIL import Image, ImageDraw, ImageFont
from datetime import date
from pathlib import Path
import os, ctypes, shutil, datetime
today = datetime.date.today()

#We take the dictionary of birthdays and find bdays happening in the next 3 days
def upcomingBirthdays():
    global var2
    global allBirthdays
    allBirthdays = {'Jacob': date(today.year, 1, 19),
                    'Arno': date(today.year, 11, 2),
                    'Bill': date(today.year, 6, 13),
                    'John': date(today.year, 10, 26),
                    'Sarah': date(today.year, 4, 8)}
    for i in allBirthdays.values():
        delta1 = today - i
        if delta1.days <= 3:
            var2 = i
            return var2
#We take the dictionary's items and turn them into a list. This is so we can find the name
#that corresponds with the returned var2 birthday        
def findName(birthdayDict, returnedDate):
    listNames = list()
    listEntries = birthdayDict.items()
    for item  in listEntries:
        if item[1] == returnedDate:
            listNames.append(item[0])
    return  listNames

upcomingBirthdays()
listNames = findName(allBirthdays, var2)
for n in listNames:
    var3 = n
delta = var2 - today

#We change directory to the themes folder where we copy TranscodedWallpapercopy
#over TranscodedWallpaper so that each runthrough is a clean slate. If
#the files are a different size, it means the user changed their background
#and the copy must be deleted and recreated.
os.chdir('C:\\Users\[insert user]\AppData\Roaming\Microsoft\Windows\Themes')
copy = Path('C:\\Users\[insert user]\AppData\Roaming\Microsoft\Windows\Themes\TranscodedWallpapercopy.jpg')
if copy.is_file():
    True
else:
    shutil.copyfile('TranscodedWallpaper', 'TranscodedWallpapercopy.jpg')
size1 = os.path.getsize('TranscodedWallpaper')
size2 = os.path.getsize('TranscodedWallpapercopy.jpg')
if size1 != size2:
    os.remove('TranscodedWallpapercopy.jpg')
    shutil.copyfile('TranscodedWallpaper', 'TranscodedWallpapercopy.jpg')
else:
    shutil.copyfile('TranscodedWallpapercopy.jpg', 'TranscodedWallpaper')


wallpaperIm = Image.open('TranscodedWallpaper')
draw = ImageDraw.Draw(wallpaperIm)
fontsFolder = 'C:\\windows\fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 24)
#Messages are written depending on how many days until the next birthday
if 1 <= delta.days <= 3:
    draw.text((1900, 1200), var3 + "'s" + ' birthday is in ' + str(delta.days) + ' days', fill='white', font=arialFont)
if delta.days == 0:
    draw.text((1900, 1200), "It's " + var3 + "'s birthday!" , fill='white', font=arialFont)
wallpaperIm.save('TranscodedWallpaper.bmp')
if os.name == 'nt':
    os.remove('TranscodedWallpaper')
    os.rename('TranscodedWallpaper.bmp', 'TranscodedWallpaper')
    os.system("RUNDLL32.EXE user32.dll, UpdatePerUserSystemParameters")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\[insert user]\AppData\Roaming\Microsoft\Windows\Themes\TranscodedWallpaper" , 0)


