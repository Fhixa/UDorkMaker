####################################################################################################################################################################################
####################################################################################################################################################################################
"""         oooooooooo.     .oooooo.   ooooooooo.   oooo    oooo    ooo        ooooo       .o.       oooo    oooo oooooooooooo ooooooooo.   
            `888'   `Y8b   d8P'  `Y8b  `888   `Y88. `888   .8P'     `88.       .888'      .888.      `888   .8P'  `888'     `8 `888   `Y88. 
             888      888 888      888  888   .d88'  888  d8'        888b     d'888      .8"888.      888  d8'     888          888   .d88' 
             888      888 888      888  888ooo88P'   88888[          8 Y88. .P  888     .8' `888.     88888[       888oooo8     888ooo88P'  
             888      888 888      888  888`88b.     888`88b.        8  `888'   888    .88ooo8888.    888`88b.     888    "     888`88b.    
             888     d88' `88b    d88'  888  `88b.   888  `88b.      8    Y     888   .8'     `888.   888  `88b.   888       o  888  `88b.  
            o888bood8P'    `Y8bood8P'  o888o  o888o o888o  o888o    o8o        o888o o88o     o8888o o888o  o888o o888ooooood8 o888o  o888o 
"""
####################################################################################################################################################################################
####################################################################################################################################################################################

logo = """
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓                                                        ▓▓
▓▓   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▓▓
▓▓   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▓▓
▓▓   ▒▒▒▒▒▒███▒▒▒▒▒███▒▒▒███████▒▒▒▒▒███▒▒▒▒▒▒███▒▒▒▒▒▒   ▓▓
▓▓   ▒▒▒▒▒▒███▒▒▒▒▒███▒▒▒███▒▒▒▒███▒▒█████▒▒█████▒▒▒▒▒▒   ▓▓
▓▓   ▒▒▒▒▒▒███▒▒▒▒▒███▒▒▒███▒▒▒▒███▒▒███▒████▒███▒▒▒▒▒▒   ▓▓
▓▓   ▒▒▒▒▒▒███▒▒▒▒▒███▒▒▒███▒▒▒▒███▒▒███▒▒██▒▒███▒▒▒▒▒▒   ▓▓
▓▓   ▒▒▒▒▒▒███▒▒▒▒▒███▒▒▒███▒▒▒▒███▒▒███▒▒▒▒▒▒███▒▒▒▒▒▒   ▓▓
▓▓   ▒▒▒▒▒▒███▒▒▒▒▒███▒▒▒███▒▒▒▒███▒▒███▒▒▒▒▒▒███▒▒▒▒▒▒   ▓▓
▓▓   ▒▒▒▒▒▒███████████▒▒▒███████▒▒▒▒▒███▒▒▒▒▒▒███▒▒▒▒▒▒   ▓▓
▓▓   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▓▓
▓▓   ▒▒▒▒▒ Made in BlackFly SC Lab By Unkn0wn2603 ▒▒▒▒▒   ▓▓
▓▓   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▓▓
▓▓                                                        ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

"""



operators = [
	'about:', 'after:', 'alert:', 'allinanchor:', 'allinbody:', 'allintag:', 'allintext:', 'allintitle:', 'allinurl:', 'allinintext:', 'app:', 'article:', 'attachment:', 'author:', 
	'before:', 'best:', 'bcc:', 'body:', 'book:', 
	'cache:', 'calculator:', 'call:', 'case study:', 'cc:', 'checkout:', 'city:', 'code:', 'comparison:', 'contact:', 'country:', 'customer:', 
	'daterange:', 'define:', 'demo:', 'destination:',  'diet:', 'directory:', 'discount:', 'download:', 
	'error:', 'event:', 'exercise:', 'ext:', 
	'faq:', 'feedback:', 'filename:', 'filetype:', 'fitness:', 'flight:', 'forum:', 'from:', 'fun:', 'funny:', 
	'gallery:', 'game:', 'groups:', 'guide:', 
	'hashtag:', 'health:', 'hotel:', 'how-to:', 
	'images:', 'inanchor:', 'inbody:', 'inheader:', 'inmeta:', 'inpostauthor:', 'inurl:', 'inanchor:', 'info:', 'info:', 'intag:', 'intags:', 'intext:', 'intextanchor:', 'intime:', 'intitle:', 'intitletext:', 'inurl:', 'ip:', 'job:', 'lang:', 'link:', 'linkdomain:', 'location:', 'login:', 
	'mail:', 'manual:', 'map:', 'maps:', 'movie:', 'motivation:', 'music:', 
	'news:', 'nutrition:', 'numrange:', 
	'order:', 
	'password:', 'patents:', 'payment:', 'phone:', 'phonebook:', 'price:', 'problem:', 'product:', 'purchase:', 
	'quote:', 
	'recipient:', 'register:', 'related:', 'report:', 'research:', 'restaurant:', 'review:', 
	'site:', 'siterelated:', 'siteallinurl:', 'sitecache:', 'siteext:', 'sitefiletype:', 'siteinurl:', 'sitelink:', 'siteip:', 'siteurl:', 'siteinfo:', 'solution:', 'source:', 'spreadsheets:', 'stocks:', 'store:', 'style:', 'subject:', 'support:', 
	'tags:', 'testimonial:', 'time:', 'tips:', 'to:', 'top:', 'travel:', 'tutorial:', 
	'username:', 
	'vulnerabilities:', 'vs:', 
	'warning:', 'weather:', 'whitepaper:', 'without:', 
	'zip:', 
	'blank, without any key', "Go Back / exit"]


op_len = len(operators)
Colum_of_printing = 5
blank_v, exit_v = op_len-1, op_len


from termcolor import colored
run_code_main = True
import random
import os

TL = [
                    "UT-ANF",           # 0
                    ".txt",             # 1
                    "ignore",           # 2
                    "utf-8",            # 3
                    "attributes",       # 4
        ]

def write_to_file(text, filename, directory, extension=True, append=True, newline=False, subfolder=None):
    if True:
        if newline:
            text += "\n"
        if extension and not filename.endswith(TL[1]):
            filename += TL[1]
        if subfolder:
            output_dir = os.path.join(TL[0], subfolder)
            output_dir = os.path.join(output_dir, directory)
        else:
            output_dir = os.path.join(TL[0], directory)
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, filename)
        mode = "a" if append else "w"
        with open(file_path, mode, encoding=TL[3], errors=TL[2]) as output_file:
            output_file.write(text)
        # print("written")
        return True, filename, file_path



symbols = ["AND", "OR", "NOT", "-", "*", "~", "|", "..", "$", "#", "@", "+", "[]", "()", "..."]

symbol_count = 0

def print_operators_in_columns(operators, num_columns):
	num_operators = len(operators)
	num_rows = (num_operators + num_columns - 1) // num_columns
	for i in range(num_rows):
		for j in range(num_columns):
			index = i + j * num_rows
			if index < num_operators:
				number = str(index + 1).zfill(3)
				operator = operators[index]
				den = f"{number}. {operator}"
				xden = 20 - len(den)
				dxn = " " * xden
				if den.startswith(f"{blank_v}"):
					print(colored(den, "light_cyan"), end=f"{dxn}")
				elif den.startswith(f"{exit_v}"):
					print(colored(den, "light_red"), end=f"{dxn}")
				else:
					print(colored(den, "light_green"), end=f"{dxn}")
		print()


def choose_operator():
	while run_code_main:
		try:
			print("\n")
			print(colored("Choose an operator", on_color="on_yellow"))
			print("\n")
			print_operators_in_columns(operators, Colum_of_printing)
			print(colored("\nEnter the number of the operator ", "light_blue"), end= "")
			choice = int(input(" : "))
			if choice == blank_v:
				return ""
			if choice == exit_v:
				return "exit"
			return operators[choice - 1]
		except:
			print(colored("Wrong input, Try with correct Choice"))


def choose_text():
	while run_code_main:
		filename = input("\nEnter the file name: ")
		if os.path.isfile(filename):
			return filename
		elif os.path.isfile(filename + ".txt"):
			return filename + ".txt"
		else:
			print("\nFile not found. Please try again.")



def choose_quote_option():
	while run_code_main:
		choice = input(colored("\nDo you want to include quotes for your input? (yes/no): ", "blue"))
		choice = choice.lower()
		if choice in ["yes", "y", "yeah", "yep", "absolutely", "sure", "definitely", "of course", "indeed", "yup"]:
			print(colored("Great! Quotes will make your input more dramatic!", "green"))
			return True
		elif choice in ["no", "n", "nope", "nah", "not really", "never", "nay"]:
			print(colored("Alright! No quotes, straight to the point!", "green"))
			return False
		else:
			print(colored("Hmm, I didn't quite catch that. Could you please respond with a clear 'yes' or 'no'?", "red"))


x_count = 1
def get_input(operator, include_quotes):
	global x_count
	xct = f"Replaceable{x_count}"
	if include_quotes:
		xct = f"\"{xct}\""
	x_count += 1
	return f"{operator}{xct}"

def choose_symbol():
	while run_code_main:
		try:
			global symbol_count
			if symbol_count == 0:
				pass
			else:
				print(colored("You have choosed a symble just now,\nAnd dork cannot contain multiple symble in Same place", "yellow"))
				return ""
			print(colored("\nChoose a symbol:", "light_magenta"))
			print(colored("""
[01] AND    [02] OR	   [03] NOT
[04] -		[05] *	   [06] ~
[07] |		[08] ..	   [09] $
[10] #		[11] @	   [12] +
[13] []	    [14] ()	   [15] ...
[16] Go  back  without  any  symble
""", "light_magenta"))
			choice = int(input(colored("\nEnter the number of the symbol: ", "light_magenta")))
			if choice == 16:
				return ""

			symbol_count += 1
			return symbols[choice - 1]
		except:
			print(colored("Wrong input, Try with correct Choice"))


def combination_maker(template, replace_list):
    import itertools
    combinations = itertools.product(*replace_list)
    result = []
    for combination in combinations:
        current_template = template
        for i, item in enumerate(combination):
            placeholder = f"Replaceable{i+1}"
            current_template = current_template.replace(placeholder, item)
        result.append(current_template)
    return result

def dorkmaker():
	CL = ["green", "yellow", "blue", "magenta", "cyan", "light_grey", "dark_grey", "light_green", "light_yellow", "light_blue", "light_magenta", "light_cyan"]
	RC = random.choice(CL)
	print(colored(logo, RC))
	tex_file = []
	x_count = 1
	tool_run = True
	# while tool_run:
	try:
		operator = choose_operator()
		if operator == "exit":
			tool_run = False
		include_quotes = choose_quote_option()
		file_name = choose_text()
		tex_file.append(file_name)
		result = get_input(operator, include_quotes)


		global symbol_count
		while tool_run:
			print(colored(F"\nCurrent result: {result}", "light_blue"))
			print(colored("Choose the next step:", "light_green"))
			print(colored("1. Choose a symbol", "light_green"))
			print(colored("2. Choose an operator", "light_green"))
			print(colored("3. EXPORT RESULT ", "light_blue"))
			print(colored("4. EXIT TOOL", "light_red"))
			choice = int(input(colored("\nEnter your choice: ", "blue")))

			if choice == 1:
				symbol = choose_symbol()
				if symbol == "[]":
					result += "[" + input(colored("Enter the range of characters: ", "light_green")) + "]"
				elif symbol == "()":
					result += "(" + input(colored("Enter the grouped operator or text: ", "light_green")) + ")"
				elif symbol == '""':
					result += '"' + input(colored("Enter the grouped operator or text: ", "light_green")) + '"'
				elif symbol == "...":
					result += "..."	# elif symbol == "":	#	 print(colored("\nSymbol can only be used after an operator or text.\n", "red"))
				else:
					result += " " + symbol
			elif choice == 2:
				operator = choose_operator()
				if operator != "exit":
					include_quotes = choose_quote_option()
					file_name = choose_text()
					tex_file.append(file_name)
					result += " " + get_input(operator, include_quotes)
					symbol_count = 0

			elif choice == 3:
				break
			elif choice == 4:
				tool_run == False
				break

		if tool_run:
			all_dorks = []
			for tf in tex_file:
				temp_list = []
				with open(tf, 'r') as file:
						lines = file.readlines()
						for line in lines:
							rl = line.strip()
							if rl not in temp_list:
								temp_list.append(rl)
				all_dorks.append(temp_list)
				# print(len(temp_list))
			# print("total len --")
			# print(len(all_dorks))
			result_list = combination_maker(result, all_dorks)
			print(colored(f"Total combination of dork is now : {len(result_list)}", "yellow"))
			print(colored(f"Saving in a file", "yellow"))

			for ll in result_list:
				write_to_file(ll, "Dorks Made", "DORK MAKER", newline=True)
				# print(colored(ll, "blue"))
		else:
			print(colored("Exiting", "green"))

	except:
		input(colored("Error Occured, Try Again Later :", "red"))
			
dorkmaker()