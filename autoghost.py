import string
import xchat
__module_name__ = "Autoghost"
__module_version__ = "0.1.0"
__module_description__ = "Ghost old session automatically."

display = (__module_name__ + " " + __module_version__ + " has been loaded.",)

def lineprint(line):
    print("\0034autoghost: " + line + "\003")

def nickchange(word, word_eol, userdata):
	desired_nick = xchat.get_prefs("irc_nick1")
	password = xchat.get_info("nickserv")
	if xchat.get_info("nick") is desired_nick:
		lineprint("Got desired nick now: "+desired_nick)
		return xchat.EAT_ALL
	return xchat.EAT_NONE

def ghost(word, word_eol, userdata):
	desired_nick = xchat.get_prefs("irc_nick1")
	password = xchat.get_info("nickserv")
	lineprint("Desired nickname "+desired_nick+" is taken.")
	if password:
		lineprint("Attempting to ghost old session.")
		xchat.command("msg nickserv ghost "+desired_nick+" "+password)
		return xchat.EAT_ALL
	else:
		lineprint("But we have no password!")
		return xchat.EAT_NONE

def notice(word, word_eol, userdata):
	password = xchat.get_info("nickserv")
	desired_nick = xchat.get_prefs("irc_nick1")

	if "This nickname is registered" in word_eol[0]:
		if password:
			lineprint("Registered nickname. Attempting to auto-identify.")
			xchat.command("msg nickserv identify "+password)
			return xchat.EAT_ALL
		else:
			lineprint("Registered nickname, but we have no password!")
			return xchat.EAT_NONE

	elif "has been ghosted" or "Ghost with your nick" in word_eol[0]:
		lineprint("Ghosting successful. Setting nick to "+desired_nick)
		xchat.command("nick "+desired_nick)
		return xchat.EAT_ALL
	
	elif "is not a registered nickname." in word_eol[0] or "Your nick isn't registered." in word_eol[0]:
		lineprint("Not using desired nick. Setting nick to "+desired_nick)
		xchat.command("nick "+desired_nick)
		return xchat.EAT_ALL

	elif "You are already identified." in word_eol[0] or "You are already logged in" in word_eol[0]:
		return xchat.EAT_ALL

	return xchat.EAT_NONE

def servertext(word, word_eol, userdata):
	if "ickname" in word_eol[0] and "in use" in word_eol[0]:
		return ghost([],[],[])

	elif "while banned on channel" in word_eol[0]:
		for w in word:
			if '\#' in w:
				lineprint("Channel "+word+" prevents unregistered users from nick changes. Leaving, changing nick, rejoining.")
				xchat.command("leave "+word)
				xchat.command("nick "+xchat.get_prefs("irc_nick1")
				xchat.command("join "+word)
				return xchat.EAT_ALL
		
	return xchat.EAT_NONE

for line in display:
	lineprint(line)

xchat.hook_print("Notice", notice)
xchat.hook_print("Nick Failed", ghost)
xchat.hook_print("Nick Clash", ghost)
xchat.hook_print("Your Nick Changing", nickchange)
xchat.hook_print("Server Text", servertext)