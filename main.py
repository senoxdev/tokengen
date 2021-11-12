import random, string
import webbrowser
import time
import requests

print("""MEKSI T0K3N G3N""")
time.sleep(2)
print("DISCLAIMER: MADE BY MEKSIKANECA")
time.sleep(3)
print("Discord server : https://discord.gg/nqJ2qWEvcm\n")
time.sleep(0.2)

num=input('Колко токени искате да генерирате: ')

f=open("Tokens.txt","w", encoding='utf-8')

print("Изчакайте да се генерират")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(17))
   x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(3))
   w = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(27))
   f.write('ODg4ODI')
   f.write(y)
   f.write('.')
   f.write('YUY')
   f.write(x)
   f.write('.')
   f.write(w)
   f.write("\n")

f.close()

# CHECKER


with open("Tokens.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" RANDOM | {} ".format(line.strip("\n")))
            break
        else:
        	print(" RANDOM | {} ".format(line.strip("\n")))
print("GG ENJOY; .")
input("TOKENS GENERATED, GO TO Tokens.txt")