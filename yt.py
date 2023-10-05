from pytube import YouTube
from time import sleep



def printLow(Str):
    for char in Str:
        print(char, end='', flush=True)
        sleep(.01)
        
        
r='\033[1;31m' 
g='\033[32;1m' 
y='\033[1;33m'
w='\033[1;37m' 



printLow(f"""\n{y}@BOOS_TOOLS""")
    
   
link = input(f'\n\n{g}[?] {y}masukkan tautan {r}- {w}')
if "https://" not in link :
    printLow(f"\n{g}[-] {r}Klik tautan atau video YouTube")
    link = input(f'\n\n{g}[?] {y}masukkan tautan{r}- {w}')
kir = YouTube(link)


printLow(f"""\n{y}Info:
    {g}[+] {y}nama video: {w}({kir.title})
    {g}[+] {y}Penayangan video: {w}({kir.views})
    {g}[+] {y}Durasi video (sec): {w}({kir.length})
""")



x = input(f'\n{g}[?] {r}anda ingin mengunduh(Y/n) {y}- {w}')
if x.lower() == "y" :
    printLow(f"\n{g}[+] {y}memuat ...\n")
    ys = kir.streams.get_highest_resolution()
    ys.download()
    printLow(f"{g}[+] {y}selesai!\n")
elif x.lower() == "n" :
    printLow(f"\n{g}[-] {r}جار?. !\n")
else:
    printLow(f"{r}kesalahanأ!\n")