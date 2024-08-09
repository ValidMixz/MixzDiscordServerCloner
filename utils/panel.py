from rich .console import Console #line:1
from rich .table import Table #line:2
from rich .text import Text #line:3
from rich .style import Style #line:4
from rich .panel import Panel as RichPanel #line:5
import json #line:6
def Panel ():#line:8
    with open ("./utils/config.json","r")as OO0O0O0O000O0OO0O :#line:9
        O000OOO0O0OO0000O =json .load (OO0O0O0O000O0OO0O )#line:10
    print (" ")#line:11
    OOO0OO000O0O000OO =Style (color ="green",bold =True )#line:13
    O00OOOO0000O00O0O =Style (color ="red",bold =True )#line:14
    OO0O0000O0O00OOOO =Table (title ="Discord Server Cloner By Mixzondc",show_header =True ,header_style ="bold")#line:17
    OO0O0000O0O00OOOO .add_column ("Setting",style ="cyan",no_wrap =True ,width =30 )#line:18
    OO0O0000O0O00OOOO .add_column ("Status",justify ="center",width =10 )#line:19
    for OOOO0OO000OO0OOO0 ,OO0O0OO0000O0000O in O000OOO0O0OO0000O ["copy_settings"].items ():#line:21
        OO0O0000O0O00OOOO .add_row (OOOO0OO000OO0OOO0 .capitalize (),Text ("ON"if OO0O0OO0000O0000O else " OFF",style =OOO0OO000O0O000OO if OO0O0OO0000O0000O else O00OOOO0000O00O0O ))#line:22
    OO0O0000000O00OO0 =Console ()#line:24
    OO0O0000000O00OO0 .print (OO0O0000O0O00OOOO )#line:25
    O000O00000OOO00OO ="""Discord has removed the functionality for bots to create a server automatically. You will have to create a server manually and provide the server ID and the server you want to clone."""#line:28
    OO0O0000000O00OO0 .print (RichPanel (O000O00000OOO00OO ,style ="bold blue",width =47 ))#line:29
    OOO0OO00O0OO000O0 ="1.0"#line:32
    OO0O0000000O00OO0 .print (RichPanel (f"Version: {OOO0OO00O0OO000O0}",style ="bold magenta",width =47 ))#line:33
def Panel_Run (OO0OOOOOO0OOOO000 ,OOO000OO0000O0OO0 ):#line:36
    with open ("./utils/config.json","r")as O0O0OO000OOOOO0O0 :#line:37
        OOO00O0000000O000 =json .load (O0O0OO000OOOOO0O0 )#line:38
    print (" ")#line:39
    O00O0O000O0OOO0OO =Style (color ="green",bold =True )#line:41
    O00000OO00OOO0OO0 =Style (color ="red",bold =True )#line:42
    O0O0O00O0OO0OOOOO =Table (title ="Discord Server Cloner By Mixzondc",show_header =True ,header_style ="bold")#line:45
    O0O0O00O0OO0OOOOO .add_column ("Cloner is Running...",style ="cyan",no_wrap =True ,width =30 )#line:46
    O0O0O00O0OO0OOOOO .add_column ("Status",justify ="center",width =10 )#line:47
    for O00O000O0OOOOO00O ,O00O0OOO0OO0000OO in OOO00O0000000O000 ["copy_settings"].items ():#line:49
        O0O0O00O0OO0OOOOO .add_row (O00O000O0OOOOO00O .capitalize (),Text ("ON"if O00O0OOO0OO0000OO else " OFF",style =O00O0O000O0OOO0OO if O00O0OOO0OO0000OO else O00000OO00OOO0OO0 ))#line:50
    O0OOO0OOOOOO00000 =Table (show_header =False ,header_style ="bold",show_lines =False ,width =47 )#line:53
    O0OOO0OOOOOO00000 .add_column (justify ="center")#line:54
    O0OOO0OOOOOO00000 .add_row (f"[bold magenta]Server ID: [green]{OO0OOOOOO0OOOO000}")#line:55
    O0OOO0OOOOOO00000 .add_row (f"[bold magenta]Logged in as: [green]{OOO000OO0000O0OO0}")#line:56
    OO000O0OO0O0000O0 =Console ()#line:58
    OO000O0OO0O0000O0 .print (O0O0O00O0OO0OOOOO )#line:59
    OO000O0OO0O0000O0 .print (O0OOO0OOOOOO00000 )#line:60
    OOOO0O0OOOO0O00OO ="""Discord has removed the functionality for bots to create a server automatically. You will have to create a server manually and provide the server ID and the server you want to clone."""#line:63
    OO000O0OO0O0000O0 .print (RichPanel (OOOO0O0OOOO0O00OO ,style ="bold blue",width =47 ))#line:64
    OOO000O0000O000O0 ="2.0.1"#line:67
    OO000O0OO0O0000O0 .print (RichPanel (f"Version: {OOO000O0000O000O0}",style ="bold magenta",width =47 ))#line:68
