import discord
import time
import datetime
from random import*

#crée la fonction pour générer le texte aléatoirement dées
file=open("scripts_makerat.txt")
a=file.readlines()

def txt_random():
    txt2=a[randint(0,len(a))]
    txt1=a[randint(0,len(a))]
    while txt2 == txt1:
        txt2=a[randint(0,len(a))]
    return txt1,txt2

#crée la fonction pour générer le texte aléatoirement a partire du nain
file_nain=open("réplique_nain.txt")
nain=file_nain.readlines()

def nain_txt_random():
    mot=nain[randint(0,len(nain))]
    return mot



#importe le token
file  = open("token.txt","r",encoding="utf8")
atoken=file.readlines()
token=str(atoken[0])
file.close()


intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author != client.user and ("Nain de maison" in message.content or "nain de maison" in message.content or "nain" in message.content or "Nain" in message.content or message.content == "esclavagiste"):

            chose_nain=nain_txt_random()
            await message.channel.send(chose_nain)




    if message.channel.name == 'lancer-de-dés' :

        if message.author == client.user:
            return


### AFFICHE LE TEXTE ###
        if "Lance" in message.content or "lance" in message.content or "lanse" in message.content or "lense" in message.content or "dés" in message.content or "Dés" in message.content or "Maskérath" in message.content:

            n=randint(1,100)

            await message.channel.send("-------------------------------------------------------------------------------")
            phrase=txt_random()
            await message.channel.send(phrase[0])
            time.sleep(0.3)
            await message.channel.send(phrase[1])
            time.sleep(0.1)
            print("ok")


            if n<=25:
                await message.channel.send("Wow...Que dire... I N C R O Y A B L E !")
                re="...?!! "
            elif n<=50 :
                await message.channel.send("hmm...bien !")
                re="!!"
            elif n<=85 :
                await message.channel.send("pueh...bof.")
                re="..."
            else:
                await message.channel.send("oulala...ouch")
                re="....?  eew "

            time.sleep(0.1)

            await message.channel.send(str(n)+" "+re)



async def on_message(message):
    if message.channel.name == 'lancer-de-dés':

        if message.author == client.user:
            message.channel.send("ok")


### AFFICHE LE TEXTE ###

client.run(token)
