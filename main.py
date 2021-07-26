import datetime
import requests 
from datetime import datetime,timedelta
import colorama

API_URL = "http://api.lunaciarover.com/stats/" 


# Tupla ("NombreDeLaCuenta",RoninWallet)
# sustituye ronin:0000... por 0x0000... 
RONINS = [
    ("ME","0xf392e0298bc19b969f131682ab46fde0f80420b8"),      
    ("MOM","0x11b707cee1a3888d17be7f5d175261c94f90f038"),   
  	
]

#slp requeridos!
TOTAL_DESIRED = 1500

def get_ronin_info(r):
    return requests.api.get(API_URL + r ).json()
def colorize_slp(slp):
    if slp > TOTAL_DESIRED:
        return colorama.Fore.GREEN + str(slp) + colorama.Fore.RESET
    elif slp > TOTAL_DESIRED*0.80:
        return colorama.Fore.YELLOW + str(slp) + colorama.Fore.RESET
    return colorama.Fore.RED + str(slp) + colorama.Fore.RESET

def print_ronin_data():
    for name,ronin in RONINS:
        ronin_data = get_ronin_info(ronin)
        print(name,":")
        print("\t",colorize_slp(ronin_data["in_game_slp"]),"slp")
        delta= timedelta(days=15) - (datetime.now()-datetime.fromtimestamp( int(ronin_data["last_claim_timestamp"])))
        if delta > timedelta(0) :
            print(colorama.Fore.YELLOW+"\t Faltan",delta.days,"dias con",delta.seconds//60//60,"horas y",(delta.seconds//60)%60,"minutos."+colorama.Fore.RESET)
        else:
            print(colorama.Fore.GREEN+"\t Claimable!"+colorama.Fore.RESET)
        

def main():
    print("SLP REQUERIDO POR DEFECTO :",TOTAL_DESIRED)
    
    print("---------------------------------")
    print_ronin_data()
    pass


if __name__ == "__main__":
    main()
