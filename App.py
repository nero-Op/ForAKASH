from pyrogram import Client
rexhacks =open("api.csv").read()
rehacks1 = rexhacks.split()
alf = open("Phone.csv","r").read()
alf1 = alf.split()
app0 = Client("Akash/"+str(rehacks1[0]),int(rehacks1[1]),str(rehacks1[2]),phone_number=str(alf1[0]))
app1 = Client("Akash/"+str(rehacks1[3]),int(rehacks1[4]),str(rehacks1[5]),phone_number=str(alf1[1]))
app2 = Client("Akash/"+str(rehacks1[6]),int(rehacks1[7]),str(rehacks1[8]),phone_number=str(alf1[2]))
apps = ['app0', 'app1', 'app2']