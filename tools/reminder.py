import time
import random
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
import dateutil.relativedelta

end_contest = datetime.fromisoformat('2020-09-30 23:59:00.000')
dt2 = datetime.fromtimestamp(time.time())

rd = dateutil.relativedelta.relativedelta (end_contest, dt2)

DISCORD_IDEX = 0 #test: 2
DESC_INDEX = 0
DISCORD_HOOK   =[ 'x' ]


rule = 'https://discordapp.com/channels/637075986726518794/651199972221517824/755186852750950421'
post = [ 'https://cdn.discordapp.com/attachments/637075986726518796/759941463940923422/unknown.png',
            'https://cdn.discordapp.com/attachments/755183696176480306/757736934180388915/image0.jpg',
            'https://cdn.discordapp.com/attachments/755183696176480306/757736934448824350/image1.jpg',
            'https://cdn.discordapp.com/attachments/755183696176480306/757736934931169310/image3.jpg',
            'https://cdn.discordapp.com/attachments/755183696176480306/758876516578361375/0924202213.jpg',
            'https://cdn.discordapp.com/attachments/755183696176480306/758876637919051816/0924201834f.jpg',
            'https://cdn.discordapp.com/attachments/755183696176480306/759468887225270272/20200925_222548.jpg',
            'https://cdn.discordapp.com/attachments/755183696176480306/759468910994522136/20200925_171138.jpg',
            'https://cdn.discordapp.com/attachments/755183696176480306/759894989177880595/IMG_3005.jpg',
            'https://cdn.discordapp.com/attachments/755183696176480306/759894994831015936/D826012-sRGB_4096.JPG'
]
post_link = 'https://discordapp.com/channels/637075986726518794/755183696176480306/755705401613221908'
vote_link = 'https://discordapp.com/channels/637075986726518794/727872214371926076/727873608491204678'
left = "{0} days and {1} hours".format(rd.days, rd.hours)

desc = [ "Our 3D Printing contest is almost over!\n\nAnyone can submit a print!\nYou have {0} left before deadline!\n\n[See full contest rules]({1})\n[See posted prints]({2})\n".format(left, rule, post_link),
         "Our 3D Printing contest is now over it's now time to vote!\n\nAnyone can vote!\nYou have {0} left before deadline!\n\n[See submited prints]({1})\n\n[See full rules]({2})\n".format(left, vote_link, rule),
         "Our 3D Printing contest is now over it's now time to vote!\n\nAnyone can vote!\n\n[See submited prints]({1})\n\n[See full rules]({2})\n".format(left, vote_link, rule)
       ]

#print(desc)

embed = DiscordEmbed(title="3DMeltdown 3D Printing contest reminder!", description=desc[DESC_INDEX], color=0xa21d1d)
#    embed.set_author(name='3DMeltdown - Contest reminder!', url='https://discordapp.com/channels/637075986726518794/651199972221517824/674832873857220618')
embed.set_footer(text='3DMeltdown contest friendly reminder every 6h', icon_url="https://cdn.discordapp.com/emojis/673897582375993365.png")

for h in DISCORD_HOOK[DISCORD_IDEX]:
    embed.set_thumbnail(url=random.choice(post))
    webhook = DiscordWebhook(url=h)
    webhook.add_embed(embed)
    webhook.execute()
    webhook.remove_embed(0)
    time.sleep(1)
