#!/usr/bin/env python3

import json, os, time, sys
from getpass import getpass

DIR = os.path.dirname(os.path.abspath(__file__))
CFG = DIR + "/config.json"
WLT = DIR + "/whitelist.txt"

RED = "\033[91m"
GRN = "\033[92m"
YLW = "\033[93m"
CYN = "\033[96m"
WHT = "\033[97m"
BLD = "\033[1m"
DIM = "\033[2m"
RST = "\033[0m"

BIG = [
"   ██████╗ ███╗   ███╗     ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ ",
"   ██╔══██╗████╗ ████║    ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗",
"   ██║  ██║██╔████╔██║    ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝",
"   ██║  ██║██║╚██╔╝██║    ██║   ██║██╔══██╗██║   ██║██║   ██║██╔══██╗",
"   ██████╔╝██║ ╚═╝ ██║    ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██████╔╝",
"   ╚═════╝ ╚═╝     ╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝ ",
]

BIG2 = [
"   ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗ ",
"  ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗",
"  ██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝",
"  ██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗",
"  ╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║",
"   ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝",
]

COLS = [RED, YLW, GRN, CYN, WHT]
def blink(txt):
	for _ in range(2):
		for c in COLS:
			sys.stdout.write("\r  " + BLD + c + txt + RST)
			sys.stdout.flush()
			time.sleep(0.06)
	sys.stdout.write("\r" + " " * 60 + "\r")
	sys.stdout.flush()

banner_first = True
def banner():
	global banner_first
	os.system("cls")
	print()
	if banner_first:
		for l in BIG:
			sys.stdout.write(BLD + CYN + l + RST + "\n")
			sys.stdout.flush()
			time.sleep(0.03)
		print()
		for l in BIG2:
			sys.stdout.write(BLD + CYN + l + RST + "\n")
			sys.stdout.flush()
			time.sleep(0.03)
		print()
		blink("  github.com/BiruxDCs/DM-Cleaner  |  discord: tengopisodecemento")
		banner_first = False
	else:
		for l in BIG: print(BLD + CYN + l + RST)
		print()
		for l in BIG2: print(BLD + CYN + l + RST)
	print(DIM + "  github.com/BiruxDCs/DM-Cleaner  |  discord: tengopisodecemento" + RST)
	print()

def get_cfg():
	d = {}
	if os.path.exists(CFG):
		f = open(CFG)
		d = json.load(f)
		f.close()
	return d

def set_cfg(d):
	f = open(CFG, "w")
	json.dump(d, f, indent=2)
	f.close()

def get_wl():
	o = []
	if os.path.exists(WLT):
		f = open(WLT)
		for x in f:
			x = x.strip()
			if x: o.append(x)
		f.close()
	return o

def set_wl(o):
	f = open(WLT, "w")
	for x in o:
		f.write(x + "\n")
	f.close()

def token_tutorial():
	print(BLD + YLW + "  how to get your token:" + RST)
	deco_line(YLW)
	for t, d in [
		("  " + WHT + "1. open " + BLD + "discord.com" + RST + WHT + " in your browser" + RST, 0.025),
		("  " + WHT + "2. hit " + BLD + "F12" + RST + WHT + " (devtools)" + RST, 0.025),
		("  " + WHT + "3. go to " + BLD + "Application -> Storage -> Local Storage" + RST, 0.025),
		("  " + WHT + "4. filter by " + BLD + "https://discord.com" + RST, 0.025),
		("  " + WHT + "5. find key " + BLD + "'token'" + RST + WHT + " and copy the value" + RST, 0.025),
	]:
		type_out(t, d)
	deco_line(YLW)
	print()
	print(YLW + "  dont share this with anyone" + RST)
	print(RED + "  self-botting = against tos, ur problem" + RST)
	print()

def type_out(t, d=0.02):
	for c in t:
		sys.stdout.write(c); sys.stdout.flush(); time.sleep(d)
	sys.stdout.write("\n")

def transition():
	for c in [RED, YLW, GRN, CYN, WHT]:
		sys.stdout.write("\r  " + c + "█" * 50 + RST)
		sys.stdout.flush()
		time.sleep(0.015)
	sys.stdout.write("\r" + " " * 52 + "\r")
	sys.stdout.flush()

def deco_line(c=GRN):
	print("  " + DIM + c + "─" * 46 + RST)

def tab_header(text):
	os.system("cls")
	transition()
	print()
	w2 = 42
	txt = " " + text + " "
	pad = (w2 - len(txt)) // 2
	sys.stdout.write(DIM + CYN + "  ╔" + "═" * w2 + "╗" + RST + "\n")
	sys.stdout.flush()
	time.sleep(0.03)
	sys.stdout.write("  ║" + " " * pad + BLD + WHT + txt + RST + " " * (w2 - pad - len(txt)) + "║" + "\n")
	sys.stdout.flush()
	time.sleep(0.03)
	sys.stdout.write(DIM + CYN + "  ╚" + "═" * w2 + "╝" + RST + "\n")
	sys.stdout.flush()
	time.sleep(0.03)
	print()

def bar(p, t, w=20):
	f = int(p / t * w) if t else 0
	return "[" + GRN + "█" * f + DIM + "░" * (w - f) + RST + "]"

def leave_all(tok, wl):
	import discord

	class Bot(discord.Client):
		def __init__(self):
			super().__init__()
			self.done = False
			self.out = ""

		async def on_ready(self):
			print(GRN + "  logged: " + BLD + str(self.user) + RST)
			gs = []
			for c in self.private_channels:
				if "GroupChannel" in str(type(c)):
					gs.append(c)
			tot = len(gs)
			deco_line(GRN)
			print(DIM + "  found " + str(tot) + " groups" + RST)
			deco_line(GRN)
			if not gs:
				self.done = True
				self.out = "none"
				await self.close()
				return
			print()
			left = 0; skip = 0; err = 0; n = 0
			for g in gs:
				gid = str(g.id)
				nm = g.name
				if nm is None: nm = "Unnamed"
				if gid in wl:
					skip += 1
					sys.stdout.write("  " + DIM + "SKIP [" + gid + "] " + nm + RST + "  " + bar(skip + left + err, tot) + " " + str(skip + left + err) + "/" + str(tot) + "   \n")
					sys.stdout.flush()
				else:
					try:
						await g.leave()
						left += 1; n += 1
						sys.stdout.write("  " + GRN + "LEFT - " + nm + " x" + str(n) + RST + "  " + bar(skip + left + err, tot) + " " + str(skip + left + err) + "/" + str(tot) + "   \n")
						sys.stdout.flush()
					except:
						err += 1
						sys.stdout.write("  " + RED + "FAIL [" + gid + "] " + nm + RST + "  " + bar(skip + left + err, tot) + " " + str(skip + left + err) + "/" + str(tot) + "   \n")
						sys.stdout.flush()
			print()
			deco_line(CYN)
			print("  " + CYN + "left: " + WHT + str(left) + RST + CYN + " | skip: " + WHT + str(skip) + RST + CYN + " | err: " + WHT + str(err) + RST)
			deco_line(CYN)
			self.out = str(left) + "/" + str(skip) + "/" + str(err)
			self.done = True
			await self.close()

	x = Bot()
	try: x.run(tok)
	except discord.LoginFailure:
		print(RED + "  bad token" + RST); return
	except Exception as e:
		print(RED + "  err: " + str(e) + RST); return
	while not x.done: time.sleep(0.1)
	return x.out

def fetch_groups(tok):
	import discord
	o = []
	class F(discord.Client):
		def __init__(self):
			super().__init__()
			self.rdy = False
		async def on_ready(self):
			nonlocal o
			o = [c for c in self.private_channels if "GroupChannel" in str(type(c))]
			self.rdy = True
			await self.close()
	x = F()
	s = ["|", "/", "-", "\\"]
	sys.stdout.write("  " + DIM + CYN + "scanning" + RST + " ")
	sys.stdout.flush()
	try:
		import threading
		def spin():
			i = 0
			while not x.rdy:
				sys.stdout.write("\r  " + CYN + "scanning " + WHT + s[i % 4] + RST + " ")
				sys.stdout.flush()
				time.sleep(0.1)
				i += 1
		t = threading.Thread(target=spin, daemon=True)
		t.start()
		x.run(tok)
	except: return None
	sys.stdout.write("\r  " + GRN + "scanning done" + RST + "   \n")
	sys.stdout.flush()
	return o

def menu_box(title, options, st=None):
	W = 44
	def nocol(s):
		r = ""; i = 0
		while i < len(s):
			if s[i] == "\033":
				i += 1
				while i < len(s) and s[i] != "m": i += 1
			else: r += s[i]
			i += 1
		return r

	lines = []
	lines.append(BLD + CYN + "  ┌" + "─" * W + "┐" + RST)
	lines.append(BLD + CYN + "  │" + RST + " " + BLD + WHT + title + RST + " " * (W - len(title) - 1) + CYN + "│" + RST)
	if st:
		lines.append(BLD + CYN + "  ├" + "─" * W + "┤" + RST)
		v = nocol(st)
		lines.append(BLD + CYN + "  │" + RST + " " + st + " " * (W - len(v) - 1) + CYN + "│" + RST)
	lines.append(BLD + CYN + "  ├" + "─" * W + "┤" + RST)
	for k, v in options:
		ln = "  " + GRN + k + RST + " " + WHT + v + RST
		vv = "  " + k + " " + v
		lines.append(BLD + CYN + "  │" + RST + ln + " " * (W - len(vv)) + CYN + "│" + RST)
	lines.append(BLD + CYN + "  └" + "─" * W + "┘" + RST)
	for l in lines:
		sys.stdout.write(l + "\n")
		sys.stdout.flush()
		time.sleep(0.025)

def main():
	c = get_cfg()
	tok = c.get("token")

	while True:
		wl = get_wl()
		banner()

		if tok:
			st = GRN + "Token: " + BLD + "OK" + RST + DIM + " | " + RST + "Whitelist: " + BLD + str(len(wl)) + RST
		else:
			st = YLW + "Token: " + BLD + "NO" + RST + DIM + " | " + RST + "Whitelist: " + BLD + str(len(wl)) + RST

		menu_box("MENU", [
			("1.", "Leave all groups"),
			("2.", "Select groups to keep"),
			("3.", "Set token"),
			("4.", "Exit"),
			("5.", "Credits / License"),
		], st=st)
		print()

		ch = input(BLD + "  > " + RST).strip()

		if ch == "1":
			tab_header("LEAVE ALL GROUPS")
			if not tok:
				print(RED + "  need a token first" + RST)
				input("  enter..."); continue
			deco_line(RED)
			print(YLW + "  this leaves ALL non-whitelisted groups" + RST)
			deco_line(RED)
			a = input(BLD + "  sure? (y/n): " + RST).strip().lower()
			if a != "y":
				print(DIM + "  cancelled" + RST)
				input("  enter..."); continue
			r = leave_all(tok, wl)
			if r: print(GRN + "  done: " + r + RST)
			input(DIM + "\n  enter..." + RST)

		elif ch == "2":
			tab_header("SELECT GROUPS TO KEEP")
			if not tok:
				print(RED + "  need token first" + RST)
				input("  enter..."); continue
			gs = fetch_groups(tok)
			if gs is None:
				print(RED + "  couldnt get groups" + RST)
				input("  enter..."); continue
			if not gs:
				print(YLW + "  no groups" + RST)
				input("  enter..."); continue
			deco_line(GRN)
			print("  " + WHT + "found " + BLD + str(len(gs)) + RST + WHT + " groups:" + RST)
			deco_line(GRN)
			print()
			for g in gs:
				gid = str(g.id)
				nm = g.name or "Unnamed"
				rc = ", ".join([str(x) for x in g.recipients])
				tag = GRN + " [KEPT]" + RST if gid in wl else ""
				print("    [" + DIM + gid + RST + "] " + CYN + nm + RST + " - " + rc + tag)
			print()
			deco_line(YLW)
			print("  " + DIM + "whitelist: " + (", ".join(wl) if wl else "empty") + RST)
			deco_line(YLW)
			i = input(YLW + "\n  ids to keep (csl, all=all, enter=nothing): " + RST).strip()
			if i.lower() == "all":
				nw = [str(x.id) for x in gs]
				set_wl(nw)
				deco_line(GRN)
				print(GRN + "  saved " + BLD + str(len(nw)) + RST + GRN + " ids to whitelist" + RST)
				deco_line(GRN)
			elif i:
				nw = [x.strip() for x in i.split(",") if x.strip()]
				set_wl(nw)
				deco_line(GRN)
				print(GRN + "  saved " + BLD + str(len(nw)) + RST + GRN + " ids to whitelist" + RST)
				deco_line(GRN)
			else:
				print(DIM + "  unchanged" + RST)
			input(DIM + "\n  enter..." + RST)

		elif ch == "3":
			tab_header("SET TOKEN")
			token_tutorial()
			nt = getpass(YLW + "  paste token: " + RST)
			if nt:
				c["token"] = nt
				set_cfg(c)
				tok = nt
				deco_line(GRN)
				print(GRN + "  token saved" + RST)
				deco_line(GRN)
			input(DIM + "\n  enter..." + RST)

		elif ch == "4":
			tab_header("EXIT")
			print(YLW + "  " + BLD + "bye!" + RST)
			time.sleep(0.5)
			break

		elif ch == "5":
			while True:
				tab_header("CREDITS / LICENSE")
				lx = [
					BLD + CYN + "  ┌────────────────────────────────────────────┐" + RST,
					BLD + CYN + "  │" + RST + " " + BLD + WHT + "CREDITS / LICENSE / AGREEMENTS" + RST + "       " + CYN + "│" + RST,
					BLD + CYN + "  ├────────────────────────────────────────────┤" + RST,
					BLD + CYN + "  │" + RST + "  " + GRN + "1." + RST + " " + WHT + "License (BFSL v1.0)" + RST + "             " + CYN + "│" + RST,
					BLD + CYN + "  │" + RST + "  " + GRN + "2." + RST + " " + WHT + "Terms of use" + RST + "                   " + CYN + "│" + RST,
					BLD + CYN + "  │" + RST + "  " + GRN + "3." + RST + " " + WHT + "Copy Discord user" + RST + "              " + CYN + "│" + RST,
					BLD + CYN + "  │" + RST + "  " + GRN + "4." + RST + " " + WHT + "Back" + RST + "                           " + CYN + "│" + RST,
					BLD + CYN + "  └────────────────────────────────────────────┘" + RST,
				]
				for l in lx:
					sys.stdout.write(l + "\n"); sys.stdout.flush(); time.sleep(0.025)
				print()
				cc = input(BLD + "  > " + RST).strip()
				if cc == "1":
					os.system("start https://github.com/BiruxDCs/DM-Cleaner/blob/main/LICENSE")
					deco_line(GRN)
					print(GRN + "  opened license page" + RST)
					deco_line(GRN)
					input("  enter...")
				elif cc == "2":
					os.system("start https://github.com/BiruxDCs/DM-Cleaner/blob/main/README.md")
					deco_line(GRN)
					print(GRN + "  opened terms page" + RST)
					deco_line(GRN)
					input("  enter...")
				elif cc == "3":
					user = "tengopisodecemento"
					os.system("echo " + user + " | clip")
					deco_line(GRN)
					print(GRN + "  copied " + BLD + "'" + user + "'" + RST + GRN + " to clipboard" + RST)
					deco_line(GRN)
					print(WHT + "  paste it in Discord to add me" + RST)
					input("  enter...")
				elif cc == "4":
					break
				else:
					print(RED + "  invalid" + RST)
					time.sleep(1)

		else:
			print(RED + "  invalid" + RST)
			time.sleep(1)

if __name__ == "__main__":
	try: main()
	except KeyboardInterrupt: print(YLW + "\n  bye" + RST)
	except Exception as e: print(RED + "\n  " + str(e) + RST)
