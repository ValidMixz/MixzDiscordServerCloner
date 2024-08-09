import discord #line:1
from colorama import Fore ,init ,Style #line:2
import asyncio #line:3
import sys ,json #line:4
with open ("./utils/config.json","r")as json_file :#line:6
  data =json .load (json_file )#line:7
  logs_enabled =data ["logs"]#line:8
def clear_line (n =1 ):#line:11
  O0O0O0O000O000OOO ='\033[1A'#line:12
  OO0000OOO0OO00000 ='\x1b[2K'#line:13
  for _OO00000O000000O00 in range (n ):#line:14
    print (O0O0O0O000O000OOO ,end =OO0000OOO0OO00000 )#line:15
def logs (OOO0O000O00O0OOOO ,OOOO00000OO00O00O ,number =None ):#line:18
  if logs_enabled :#line:19
    OO0OOOOO0O0OOO000 ={'add':('[+]',Fore .GREEN ),'delete':('[-]',Fore .RED ),'warning':('[WARNING]',Fore .YELLOW ),'error':('[ERROR]',Fore .RED )}#line:25
    O0OOOO0OO0O0O00OO ,O0O0O000OO000O00O =OO0OOOOO0O0OOO000 .get (OOOO00000OO00O00O ,('[?]',Fore .RESET ))#line:26
    if number is not None :#line:28
      print (f" {O0O0O000OO000O00O}{O0OOOO0OO0O0O00OO}{Style.RESET_ALL} {OOO0O000O00O0OOOO}")#line:29
    else :#line:30
      print (f" {O0O0O000OO000O00O}{O0OOOO0OO0O0O00OO}{Style.RESET_ALL} {OOO0O000O00O0OOOO}")#line:31
      clear_line ()#line:32
class Cloner :#line:35
  @staticmethod #line:37
  async def guild_create (O000O0OOOO000O0OO :discord .Guild ,O0O00O00O00O0OOOO :discord .Guild ):#line:38
    try :#line:39
      try :#line:40
        OOO0OOOO00OO0O000 =await O0O00O00O00O0OOOO .icon_url_as (format ='jpg').read ()#line:41
      except discord .errors .DiscordException :#line:42
        logs (f"Can't read icon image from {O0O00O00O00O0OOOO.name}",'error')#line:43
        OOO0OOOO00OO0O000 =None #line:44
      await O000O0OOOO000O0OO .edit (name =f'{O0O00O00O00O0OOOO.name}')#line:45
      if OOO0OOOO00OO0O000 is not None :#line:46
        try :#line:47
          await O000O0OOOO000O0OO .edit (icon =OOO0OOOO00OO0O000 )#line:48
          logs (f"Guild Icon Changed: {O000O0OOOO000O0OO.name}",'add')#line:49
        except Exception :#line:50
          logs (f"Error While Changing Guild Icon: {O000O0OOOO000O0OO.name}",'error')#line:51
    except discord .errors .Forbidden :#line:52
      logs (f"Error While Changing Guild Icon: {O000O0OOOO000O0OO.name}",'error')#line:53
    logs (f"Cloned server: {O000O0OOOO000O0OO.name}",'add',True )#line:54
  @staticmethod #line:56
  async def roles_create (O00OOOOOOO0OOO00O :discord .Guild ,OO0OOOOOOO0OOO00O :discord .Guild ):#line:57
    O000OOO0000O00O00 =[O0000000OO0O00000 for O0000000OO0O00000 in OO0OOOOOOO0OOO00O .roles if O0000000OO0O00000 .name !="@everyone"]#line:58
    O000OOO0000O00O00 .reverse ()#line:59
    O00OOOOO00000000O =len (O000OOO0000O00O00 )#line:60
    for O000O000OOO00000O in O000OOO0000O00O00 :#line:61
      try :#line:62
        O00000OOO0O0OO00O ={'name':O000O000OOO00000O .name ,'permissions':O000O000OOO00000O .permissions ,'colour':O000O000OOO00000O .colour ,'hoist':O000O000OOO00000O .hoist ,'mentionable':O000O000OOO00000O .mentionable }#line:69
        await O00OOOOOOO0OOO00O .create_role (**O00000OOO0O0OO00O )#line:70
        logs (f"Created Role {O000O000OOO00000O.name}",'add')#line:71
      except (discord .Forbidden ,discord .HTTPException )as OOOOO0OOOOOO0OO0O :#line:72
        logs (f"Error creating role {O000O000OOO00000O.name}: {OOOOO0OOOOOO0OO0O}",'error')#line:73
    logs (f"Created Roles: {O00OOOOO00000000O}",'add',True )#line:74
  @staticmethod #line:76
  async def channels_delete (O0O0OO000OOO00OOO :discord .Guild ):#line:77
    OOO00000OO0O0000O =O0O0OO000OOO00OOO .channels #line:78
    OO0O0O0O0O0O0OO0O =len (OOO00000OO0O0000O )#line:79
    for OO000OO0OOOO0000O in OOO00000OO0O0000O :#line:80
      try :#line:81
        await OO000OO0OOOO0000O .delete ()#line:82
        logs (f"Deleted Channel: {OO000OO0OOOO0000O.name}",'delete')#line:83
      except (discord .Forbidden ,discord .HTTPException )as O0OOOOO0O00000OO0 :#line:84
        logs (f"Error deleting channel {OO000OO0OOOO0000O.name}: {O0OOOOO0O00000OO0}",'error')#line:85
    logs (f"Deleted Channels: {OO0O0O0O0O0O0OO0O}",'delete',True )#line:86
  @staticmethod #line:88
  async def categories_create (O0000000O0O00OO00 :discord .Guild ,OO0OO0O00OOO0OOOO :discord .Guild ):#line:90
    OO0O0O00O0OOOOO00 =OO0OO0O00OOO0OOOO .categories #line:91
    for O0OOOOO0O00O00O0O in OO0O0O00O0OOOOO00 :#line:92
      try :#line:93
        OOOO0O0O0O0OOOO0O ={discord .utils .get (O0000000O0O00OO00 .roles ,name =O00OOO0OOO000O0OO .name ):OOOO0000OO0OOOOO0 for O00OOO0OOO000O0OO ,OOOO0000OO0OOOOO0 in O0OOOOO0O00O00O0O .overwrites .items ()}#line:97
        OOOOOOOO0O0O0O0O0 =await O0000000O0O00OO00 .create_category (name =O0OOOOO0O00O00O0O .name ,overwrites =OOOO0O0O0O0OOOO0O )#line:99
        await OOOOOOOO0O0O0O0O0 .edit (position =O0OOOOO0O00O00O0O .position )#line:100
        logs (f"Created Category: {O0OOOOO0O00O00O0O.name}",'add')#line:101
      except discord .Forbidden :#line:102
        logs (f"Error creating category {O0OOOOO0O00O00O0O.name}",'error')#line:103
      except discord .HTTPException :#line:104
        logs (f"Error creating category {O0OOOOO0O00O00O0O.name}",'error')#line:105
    logs (f"Created Categories: {len(OO0O0O00O0OOOOO00)}",'add',True )#line:106
  @staticmethod #line:108
  async def channels_create (OOO0O0OOO00OOOOOO :discord .Guild ,O0000000OOO0OO0O0 :discord .Guild ):#line:110
    OO0O00O0O000O00OO =O0000000OOO0OO0O0 .text_channels +O0000000OOO0OO0O0 .voice_channels #line:111
    O0OOOO0O00000O000 ={discord .TextChannel :OOO0O0OOO00OOOOOO .create_text_channel ,discord .VoiceChannel :OOO0O0OOO00OOOOOO .create_voice_channel }#line:115
    O0O00000OO00OO0OO =len (OO0O00O0O000O00OO )#line:116
    for O000OO0OO0O0O0O00 in OO0O00O0O000O00OO :#line:117
      await asyncio .sleep (0.2 )#line:118
      O000000O000O00O0O =discord .utils .get (OOO0O0OOO00OOOOOO .categories ,name =getattr (O000OO0OO0O0O0O00 .category ,"name",None ))#line:121
      OOO000O0OO000O0O0 ={}#line:122
      for OO000O0O0O0O0OOO0 ,O00O000000O00OO0O in O000OO0OO0O0O0O00 .overwrites .items ():#line:123
        O0OO0O0O0000OOOO0 =discord .utils .get (OOO0O0OOO00OOOOOO .roles ,name =OO000O0O0O0O0OOO0 .name )#line:124
        OOO000O0OO000O0O0 [O0OO0O0O0000OOOO0 ]=O00O000000O00OO0O #line:125
      try :#line:126
        OOO00OOOO00OO00OO =await O0OOOO0O00000O000 [type (O000OO0OO0O0O0O00 )](name =O000OO0OO0O0O0O00 .name ,overwrites =OOO000O0OO000O0O0 ,position =O000OO0OO0O0O0O00 .position )#line:130
        if O000000O000O00O0O is not None :#line:131
          await OOO00OOOO00OO00OO .edit (category =O000000O000O00O0O )#line:132
        logs (f"Created {'Text' if type(O000OO0OO0O0O0O00) == discord.TextChannel else 'Voice'} Channel: {O000OO0OO0O0O0O00.name}",'add')#line:135
      except (discord .Forbidden ,discord .HTTPException ,Exception )as O0OOOOO000O00OO0O :#line:136
        logs (f"Error While Creating Channel {O000OO0OO0O0O0O00.name}: {O0OOOOO000O00OO0O}",'error')#line:137
    logs (f"Created Channels: {O0O00000OO00OO0OO}",'add',True )#line:138
  @staticmethod #line:140
  async def emojis_create (O000OOO0O0OO0O000 :discord .Guild ,O0O0O0O0OO000O000 :discord .Guild ):#line:141
    O0O0O0000O0OOOOO0 :discord .Emoji #line:142
    OOO000O00O0OOO0OO =len (O0O0O0O0OO000O000 .emojis )#line:143
    for O0O0O0000O0OOOOO0 in O0O0O0O0OO000O000 .emojis :#line:144
      try :#line:145
        await asyncio .sleep (0.2 )#line:146
        O0O000OOO0O0O0OOO =await O0O0O0000O0OOOOO0 .url .read ()#line:147
        await O000OOO0O0OO0O000 .create_custom_emoji (name =O0O0O0000O0OOOOO0 .name ,image =O0O000OOO0O0O0OOO )#line:148
        logs (f"Created Emoji {O0O0O0000O0OOOOO0.name}",'add')#line:149
      except discord .Forbidden :#line:150
        logs (f"Error While Creating Emoji {O0O0O0000O0OOOOO0.name} ",'error')#line:151
      except discord .HTTPException :#line:152
        logs (f"Error While Creating Emoji {O0O0O0000O0OOOOO0.name}",'error')#line:153
    logs (f"Created Emojis: {OOO000O00O0OOO0OO}",'add',True )#line:154
