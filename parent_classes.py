import re
import execute

class Compiler:

    def __int__(s, filename):
        s.file = filename

    # method to take input file and convert to string
    def input_file(s):
        s.file_content = s.file.read()

class Lexer(Compiler):
    def __int__(s, filename):
        super().__int__(filename)

    # create list from parent class' string(file_content)
    def convert_string_to_tokens(s):
        tokens_list = s.file_content.split(" ")
        # ignore block comments
        for i in tokens_list:
            if i != i.re.sub(r"'''","",i):
                tokens_list.remove(i)

        # ignore single line comments
        tokens_list.remove('#')

        special_symbols = {
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

        variable_identfier = []
        for i in tokens_list:
            if i == '=' and (i+1 != '='):       # and condition to ignore any comparison since it uses ==
                variable_identfier.append(i - 1)

        function_identifier = []
        for i in tokens_list:
            if i == 'def':
                function_identifier.append(i + 1) # the next token will the the function name

