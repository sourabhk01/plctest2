Lexical Analyzer
Rules
Code starts with Start and ends with End. Each lexeme is seperated by a space.
Statements
Assignment
Delaration
Condition
Loops
Token List
Mathematical Operations
Token Code	Operation	Regex
ADD	+	+
SUB	-	-
Multiply	*	*
Modulus	%	%
Division	/	/
OPEN	(	)
CLOSE	)	)
Comparisions
Token Code	Operation	Regex
LessThan	<	<
GreaterThan	>	>
LessThenEqualto	<=	<=
GreaterThenEqualto	>=	>=
Equal	==	==
NotEqual	!=	!=
Integer Types
Token Code	Size
XS	1 byte
S	2 bytes
L	4 bytes
XL	8 bytes
Keywords
Token Code	Regex
VAR	[a-zA-Z_]{6,8}
COND	cond
RERUN	rerun
START	start
END	end
Other
Token Code	Operation	Regex
ASSIGNMENT	=	=
CODEBLOCKSTART	{	{
CODEBLOCKEND	}	}
Priority Order
()
*
-
+
/
Production Rules
<Program> --> Start <stmt_list> End
<stmt_list> --> {<stmt> `;`}
<stmt> --> <if_stmt> | <while_stmt> | <as_s>  | <declaration>
<if_stmt> --> cond <bool> `{` { <stmt> ';'} `}`
<while_stmt> --> rerun `{` <bool> { <stmt> ';' } `}`
<as_s> --> <var> `=` <expression> `;`
<declaration> --> <datatype> <var> `;`

<datatype> --> (XS|S|L|XL)
<var> -->  [a-zA-Z_]{6,8}                       // Variable Naming restriction
<expression> --> <term> { (`*`|`\`|`%` ) <term> }
<term> --> <term> { (`+`|`-`) <term> }
<factor> --> [0-9]+ | <var>  | `(` <expression> `)`
<bool> --> <expression> (`<=`|`>=` | `<` | `>`) <expression>


E -> E + T          Expression + Term
E -> E - T          Expression - Term
E -> T              Some expression can be a term
T -> T * F          Term * Factor
T -> T / F          Term / Factor
T -> F              Some Terms can be Factors
F -> -F             Unary Minus
F -> +F             Unary Plus
F ->( E )           Factor can be an Expression in parentheses
F -> c              Factor can be a constant
