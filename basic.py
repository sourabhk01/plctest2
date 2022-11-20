#Showing all the digits that are there 
digi = '0123456789'


class Ers:
    def init(s,error_n, detailed):
       
        s.error_n = error_n
        s.detailed = detailed
    
    def as_string(s):
        result  = f'{s.error_n}: {s.detailed}\n'
        return result

class wrong(Ers):
    def init(s, detailed):
        super().init( 'Incorrect Charcter', detailed)

#Token Types 

Tt_Divide      = 'Divide'
Tt_LeftParen   = 'LeftParen'
Tt_RightParen   = 'RightParen'
Tt_Mod      = 'MOD'
Tt_Less      = 'Less'
Tt_Great     = 'Great'
Tt_LessEqual   = 'LessEqual'
Tt_GreatEqual    = 'GreatEqual'
Tt_Equal     = 'Equal'
Tt_NotEqual   = 'NotEqual'
Tt_Int		= 'Int'
Tt_Float    = 'Float'
Tt_Plus     = 'Plus'
Tt_Minus    = 'Minus'
Tt_Multiply      = 'Multiply'

#type is the token type and value is the value under the type identified 
class Token:
    def init(s, t, value=None):
        s.t = t
        s.value = value
#method used to make the print statement with type of token and the value it is
    def repr(s):
        if s.value: return f'{s.t}:{s.value}'
        return f'{s.t}'

#lexer class goes through each char to see what token type it is 
class Lexical:
    def init(s, text):
        s.text = text
        s.pos = -1
        s.currentChar = None
        s.advance()

#goes to the next character in the text and if there is not another char then it wont run
    def advance(s):
        s.pos +=1
        s.currentChar = s.text[s.pos] if s.pos < len(s.text)  else None

#start with an empty list for the tokens 
    def make_tokens(s):
        tokens = []
#while loop that goes through each char and see if it matches an on these char 
        while s.currentChar != None:
            if s.currentChar in ' \t':
                s.advance()
            elif s.current in digi:
                tokens.append(s.make_number())
            elif s.currentChar == '+':
                tokens.append(Token(Tt_Plus))
                s.advance()
            elif s.currentChar == '-':
                tokens.append(Token(Tt_Minus))
                s.advance()
            elif s.currentChar == '*':
                tokens.append(Token(Tt_Multiply))
                s.advance()
            elif s.currentChar == '/':
                tokens.append(Token(Tt_Divide))
                s.advance()
            elif s.currentChar == '(':
                tokens.append(Token(Tt_LeftParen))
                s.advance()
            elif s.currentChar == ')':
                tokens.append(Token(Tt_RightParen))
                s.advance()
            elif s.currentChar == '%':
                tokens.append(Token(Tt_Mod))
                s.advance()
            elif s.currentChar == '<':
                tokens.append(Token(Tt_Less))
                s.advance()
            elif s.currentChar == '>':
                tokens.append(Token(Tt_Great))
                s.advance()
            elif s.currentChar == '<=':
                tokens.append(Token(Tt_LessEqual))
                s.advance()
            elif s.currentChar == '>=':
                tokens.append(Token(Tt_GreatEqual))
                s.advance()
            elif s.currentChar == '=':
                tokens.append(Token(Tt_Equal))
                s.advance()
            elif s.currentChar == '!=':
                tokens.append(Token(Tt_NotEqual))
                s.advance()
            else:
                pos_start = s.pos.copy()
                char = s.currentChar
                s.advance()
                return [], wrong( char )

        return tokens, None

    def make_number(s):
        num_str = ''
        decimal = 0
