# Showing all the digits that are there
digi = '0123456789'


class Ers:
	def init(s, error_n, detailed):
		s.error_n = error_n
		s.detailed = detailed

	def as_string(s):
		result = f'{s.error_n}: {s.detailed}\n'
		return result


class wrong(Ers):
	def init(s, detailed):
		super().init('Incorrect Charcter', detailed)



# type is the token type and value is the value under the type identified
class Token:
	def init(s, t, value=None):
		s.t = t
		s.value = value

	# method used to make the print statement with type of token and the value it is
	def repr(s):
		if s.value: return f'{s.t}:{s.value}'
		return f'{s.t}'


# lexer class goes through each char to see what token type it is
class Lexical:
	# Token Types

	# keywords is a list which stores key-value pairs of in-built keywords and their replacements
	keywords = { #if, else, print,
		"for": "FOR",
		"while": "WHILE",
		"return": "RETURN",
		"or": "OR",
		"none": "NONE",
		"and": "AND",
		"not": "NOT",
		"try": "TRY",
		"class": "CLASS",
		"false": "FALSE",
		"def": "DEF",
		"if" : "IF",
		"else" : "ELSE",
		"print" : "PRINT",
		 }

	keywords_keys = keywords.keys()

	tokens = {
		'=': 'Equal',
		'+': 'Addition',
		'-': 'Subtraction',
		'/': 'Division',
		'*': 'Multiplication',
		'<': 'Less than',
		'>': 'Greater than',
		'%': 'Modular',
		'<=': 'Less than/Equal',
		'>=': 'Greater Than/Equal',
		'int': 'integer type',
		'float': 'Floating point',
		'char': 'Character type',
		'long': 'long int',
		'str': 'string',
		':': 'colon',
		';': 'semi-colon',
		'.': 'dot',
		',': 'comma',
	}

	token_keys = tokens.keys()

	def init(s, text):
		s.text = text
		s.pos = -1
		s.currentChar = None
		s.advance()

	# goes to the next character in the text and if there is not another char then it wont run
	def advance(s):
		s.pos += 1
		s.currentChar = s.text[s.pos] if s.pos < len(s.text) else None

	# function to check lexeme s in a file and return its list
	def check_file(s, tokens, keywords):

		lexeme_list = []
		file = open("factorial.py")
		file_content = file.split("\n")
		for line in file_content:
			tokens = line.split(' ')
			print("Tokens:", tokens)
			# searches for the information above and names the lexeme
			for token in tokens:
				if token in tokens.keys():
					lexeme_list.append(f"Token: {tokens[token]}")
				elif token in keywords.keys():
					lexeme_list.append(f"Keyword: {keywords[token]}")
		return lexeme_list


	# function to generate tokens and their respective values
	def check_tokens(s):
		keywords = []
		tokens = []
		# while loop that goes through each char and see if it matches an on these char
		while s.currentChar != None:
			if s.currentChar in ' \t':
				s.advance()
			elif s.current in digi:
				tokens.append(s.make_number())
			elif s.currentChar == '+':
				tokens.append(Token(tokens["+"]))
				s.advance()
			elif s.currentChar == '-':
				tokens.append(Token(tokens["-"]))
				s.advance()
			elif s.currentChar == '*':
				tokens.append(Token(tokens["*"]))
				s.advance()
			elif s.currentChar == '/':
				tokens.append(Token(tokens["/"]))
				s.advance()
			elif s.currentChar == '(':
				tokens.append(Token(tokens["("]))
				s.advance()
			elif s.currentChar == ')':
				tokens.append(Token(tokens[")"]))
				s.advance()
			elif s.currentChar == '%':
				tokens.append(Token(tokens["%"]))
				s.advance()
			elif s.currentChar == '<':
				tokens.append(Token(tokens["<"]))
				s.advance()
			elif s.currentChar == '>':
				tokens.append(Token(tokens[">"]))
				s.advance()
			elif s.currentChar == '<=':
				tokens.append(Token(tokens["<="]))
				s.advance()
			elif s.currentChar == '>=':
				tokens.append(Token(tokens[">="]))
				s.advance()
			elif s.currentChar == '=':
				tokens.append(tokens["="])
				s.advance()
			elif s.currentChar == '!=':
				tokens.append(tokens["!="])
				s.advance()
			else:
				pos_start = s.pos.copy()
				char = s.currentChar
				s.advance()

			# Calling check_file() to process all lexemes in a file
		lexeme_list = s.check_file(tokens, keywords)

		print("Lexeme list in file: ",lexeme_list)

		return tokens, None

	def make_number(s):
		num_str = ''
		decimal = 0
