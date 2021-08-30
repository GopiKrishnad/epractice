mac = "00:xx:xx:xx:1A:00"
# This will increment last two element of mac
varhex = "0" # starting hex value
varxhex = mac[len(mac)-2]
for x in range(0, 2):
  y = int(varxhex, 16)
  mac_list = list(mac)
  mac_list[-2] = '{:X}'.format(y)
  mac = ''.join(mac_list)
  y = y + 1
  varxhex = hex(y)
  varhex = mac[-1] # starting hex value
  # mac_left = mac[0:len(mac)-1]
  # print(mac_left)
  for i in range(0, 16):      # how many times you want to increment
      j = int(varhex, 16)     # define i as the decimal equivalent of varhex

      print ('{}{:X}'.format(mac[0:len(mac)-1], j))          # print out the incremented value, but in hex form
      j = j + 1
      varhex = hex(j)         # increment varhex by 1
