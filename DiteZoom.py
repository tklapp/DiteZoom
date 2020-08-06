try:
    from datetime import datetime
    import time
    import schedule
    import subprocess
    import csv
    import os
    import pyautogui
except ModuleNotFoundError:
    print("Te faltan algunos modulos, revisar instrucciones")

pyautogui.FAILSAFE = True

#Creo una función que permita usar pyautogui click en Macbooks, que tienen un problema por el retina display:
def click_image(png_name):
    button = pyautogui.locateCenterOnScreen(png_name, confidence=0.95)
    x = button[0] / 2
    y = button[1] / 2
    pyautogui.moveTo(x,y)
    pyautogui.click()
    pyautogui.click()

def joinmeet(id,password = ""):
    #Abro Zoom
    os.system("open /Applications/zoom.us.app")
    time.sleep(5) #le da tiempo a la compu a abrir zoom

    #Entro a Join
    try:
        click_image("home.png")
    except TypeError:
        click_image("homenight.png")
    pyautogui.hotkey('command', 'j')

    #Escribo el id y entro
    time.sleep(1)
    pyautogui.hotkey('del')
    pyautogui.write(id)
    pyautogui.press('return')

    #Veo si hay password
    time.sleep(3)
    passw = pyautogui.locateCenterOnScreen('pass.png', confidence=0.95)
    passwnight = pyautogui.locateCenterOnScreen('passnight.png', confidence=0.95)

    if passw != None or passwnight != None:
        pyautogui.typewrite(password)
        pyautogui.press('return')
    else:
        print("No hay pass!")

    #Si puse un ID no válido
    time.sleep(3)
    invalidid = pyautogui.locateCenterOnScreen('invalidid.png', confidence=0.95)
    invalididnight = pyautogui.locateCenterOnScreen('invalididnight.png', confidence=0.95)
    if invalidid != None or invalididnight != None:
        time.sleep(5)
        pyautogui.press('return')
        print("Pusiste un invalid ID")

#Importo TimeTable
with open('Horarios.csv', newline='', encoding="utf-8-sig") as horarios:                                
    DictHorarios = csv.DictReader(horarios)                                                             
    for row in DictHorarios:                                                                            
        if row["ID"] != '':                                                                             
            todayday = datetime.today().weekday()                                                       
            if todayday == 0:                                                                           
                if row['weekday'] == 'monday':                                                          
                    ID = row['ID']                                                                      
                    password = row['Password']                                                          
                    dia = row['weekday']                                                                
                    schedule.every().monday.at(row['time']).do(joinmeet, id=ID, password=password)      
                    horario = row['time']                                                               
                    horariosplit = horario.split(":")                                                   
                    horariosuma = float(horariosplit[0])*60 + float(horariosplit[1])                    
                    now = datetime.now()                                                                
                    current_time = now.strftime("%H:%M")                                                
                    current_time_split = current_time.split(":")                                        
                    current_time_suma = float(current_time_split[0])*60 + float(current_time_split[1])  
                    if horariosuma < current_time_suma:                                                 
                        continue                                                                        
                    else:                                                                               
                        while True:                                                                     
                            schedule.run_pending()                                                      
                            time.sleep(10)                                                              
            elif todayday == 1:                                                                         
                if row['weekday'] == 'tuesday':                                                         
                    ID = row['ID']                                                                      
                    password = row['Password']                                                          
                    dia = row['weekday']                                                                
                    schedule.every().tuesday.at(row['time']).do(joinmeet, id=ID, password=password)     
                    horario = row['time']                                                               
                    horariosplit = horario.split(":")                                                   
                    horariosuma = float(horariosplit[0]) * 60 + float(horariosplit[1])                  
                    now = datetime.now()                                                                
                    current_time = now.strftime("%H:%M")                                                
                    current_time_split = current_time.split(":")                                        
                    current_time_suma = float(current_time_split[0]) * 60 + float(current_time_split[1])
                    if horariosuma < current_time_suma:                                                 
                        continue                                                                        
                    else:                                                                               
                        while True:                                                                     
                            schedule.run_pending()                                                      
                            time.sleep(10)                                                              
            elif todayday == 2:                                                                         
                if row['weekday'] == 'wednesday':                                                       
                    ID = row['ID']                                                                      
                    password = row['Password']                                                          
                    dia = row['weekday']                                                                
                    schedule.every().wednesday.at(row['time']).do(joinmeet, id=ID, password=password)   
                    horario = row['time']                                                               
                    horariosplit = horario.split(":")                                                   
                    horariosuma = float(horariosplit[0]) * 60 + float(horariosplit[1])                  
                    now = datetime.now()                                                                
                    current_time = now.strftime("%H:%M")                                                
                    current_time_split = current_time.split(":")                                        
                    current_time_suma = float(current_time_split[0]) * 60 + float(current_time_split[1])
                    if horariosuma < current_time_suma:                                                 
                        continue                                                                        
                    else:                                                                               
                        while True:                                                                     
                            schedule.run_pending()                                                      
                            time.sleep(10)                                                              
            elif todayday == 3:                                                                         
                if row['weekday'] == 'thursday':                                                        
                    ID = row['ID']                                                                      
                    password = row['Password']                                                          
                    dia = row['weekday']                                                                
                    schedule.every().thursday.at(row['time']).do(joinmeet, id=ID, password=password)    
                    horario = row['time']                                                               
                    horariosplit = horario.split(":")                                                   
                    horariosuma = float(horariosplit[0]) * 60 + float(horariosplit[1])                  
                    now = datetime.now()                                                                
                    current_time = now.strftime("%H:%M")                                                
                    current_time_split = current_time.split(":")                                        
                    current_time_suma = float(current_time_split[0]) * 60 + float(current_time_split[1])
                    if horariosuma < current_time_suma:                                                 
                        continue                                                                        
                    else:                                                                               
                        while True:                                                                     
                            schedule.run_pending()                                                      
                            time.sleep(10)                                                              
            elif todayday == 4:                                                                         
                if row['weekday'] == 'friday':                                                          
                    ID = row['ID']                                                                      
                    password = row['Password']                                                          
                    dia = row['weekday']                                                                
                    schedule.every().friday.at(row['time']).do(joinmeet, id=ID, password=password)      
                    horario = row['time']                                                               
                    horariosplit = horario.split(":")                                                   
                    horariosuma = float(horariosplit[0]) * 60 + float(horariosplit[1])                  
                    now = datetime.now()                                                                
                    current_time = now.strftime("%H:%M")                                                
                    current_time_split = current_time.split(":")                                        
                    current_time_suma = float(current_time_split[0]) * 60 + float(current_time_split[1])
                    if horariosuma < current_time_suma:                                                 
                        continue                                                                        
                    else:                                                                               
                        while True:                                                                     
                            schedule.run_pending()                                                      
                            time.sleep(10)                                                              
