import sys
#membuat tuple
logsapps = ("user1 login", "user2 login")
print(logsapps)
print("memiliki ukuran tuple", sys.getsizeof(logsapps))

logsapps_list = ["user1 login", "user2 login"]
print(logsapps_list)
print("memiliki ukuran list", sys.getsizeof(logsapps_list))

#logsapps.append("user3 login") #error karena tuple tidak bisa diubah
#logsapps [0] = "user1 logout" #error karena tuple tidak bisa diubah
#logsapps.remove("user1 login") #error karena tuple tidak bisa diubah

#pembuktian bahwa tuple bisa di akses dengan index
print(logsapps[0])
print(logsapps[-1])

#slice dan copy
print(logsapps[0:1])
backup_logsapps = logsapps[:]
print(backup_logsapps)

usr1, usr2 = logsapps
print(usr1)
print(usr2)