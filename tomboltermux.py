import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Tombol Tambahan Termux ')
print(a+'\t  UP, Down, Right, Left, CTRL ')
print(b+'\t  Bye :   Media IT')
print('\t Web : https://yt-mediait.blogspot.com')
print('\t Youtube : https://www.youtube.com/channel/UCoSKB1q90siWxbEVkMoyeMw')
print('\t Github : https://github.com/kumpulanremaja')
print('\t Instagram : instagram.com/arroichanulwahid')
print(a+'-'*50)
print('\nProses ...')
sleep(1)
print(b+'\n[!] Mengambil File Default Termux')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Menambahkan File Tombol Tambahan Termux ...')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Memproses Tombol  !')
sleep(1)
print(b+'\n[!] Tunggu Sebentar ya ... Jangan Lupa Subscribe Channel Youtube Media IT')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Proses Selesai !!! '+c+'\n\nPlease Subscribe Channel Media IT\n')
sleep(2)
os.system('clear')
os.system('xdg-open https://www.youtube.com/channel/UCzsADl8XRJeZXJ6CKZLX5KQ')
