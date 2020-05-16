## Yet another programming language
Taimoor Ali
20100217

#### How to run

Go to the main directory and run 

`python3 interpreter.py <path of the file you want to run>`

#### Functioality

This pogramming languages provide implementation of the following functionalities.

#### Variables ####

Declaration, assignment, access
Static-typing (types restricted to: int, double, char, string, bool)
Initialisation and declaration of a variable with the name of a pre existing variable generates an error.

#### Expressions ####

Numerical Operators: (+ , - , / , * , ^, % , ++, --)
Logical Operators (<, >, <=,>=, !=, ==, NOT, AND, OR)
Nested parentheses
Type (e.g. for String + Int) and division by 0 errors

#### Standard Output ####

Single object is printed with a line break.
Multiple objects separated by a delimiter (e.g. comma as in Python) are printed withspaces in between and a line break at the end

#### For Loops ####

For loops, nested for loops, also distroys the local variables and limit the global and local scope.

#### Structs ####

Structs can be declared with custom attributes and operations can be performed on them.


## Syntax to be followed

The syntax implementation can be seen inside the test cases folder. The language should obey the following syntax rules

#### Statement

All the statements should end with a semicolon 

#### Standard Output

Any thing can be printed on the console using the following syntax

`PRINT( statement1 );`

Please note that all the letters are uppercase in PRINT and the statement should end with a semicolon `;`

To print multiple things using the PRINT statments, simply seperate them with commas inside the  paranthesies i-e:

`PRINT( statement1 , statement2 );`

#### Variables

All the variable initializations should start with a data type, i-e
`INT X = 100;`
 
 The available data types are (please note that they are all upper case):

`INT STRING BOOL CHAR DOUBLE etc ..`
 
 Some examples are:

 `STRING a = "start";`
`INT b = 1;`
`DOUBLE c = 2.5;`
`BOOL d = FALSE;`
`INT e = 0;`

The variables are strictly type sensitive, i-e you can only initialze /assign variables with values of their data type 

#### Expressions ####

The language follows statndard rules for expression, as can be seen in the testcases files. You can set the precedence of operations by putting them inside paranthesis.
The expression can also be used in varaible assignment. Some of the examples are:

`STRING mystring = "theory" + "of" + "automata";`
`b++;`
`DOUBLE c = 1.5+0.5+2;`
`DOUBLE determinant = b ^ 2 - 4 * a * c;`
`DOUBLE quadratic_root1 = ( -b + determinant ^ (1/2)) / ( 2.0*a );`
`PRINT(NOT TRUE == (NOT (NOT d)) AND (TRUE != 0));`

#### Logical Operations

The logical operators can be used as 
`AND OR NOT` (with all upper case letters)

#### Increment , Decrement operations

`X++ ; y--;`

#### For loops

The for and nested for loops can be used with the following sytanx:

`FOR(INT I = 0 : I < 3 : I++){`
    `PRINT(100);`
`}`

`Please note that the seperators here are *COLONS* rather than *SEMICOLONS*`

#### STRUCTS

The structs can be defined with the keyword `STRUCT` as follows:

`STURCT PROMPT {`
`STRING MESSAGE;`
`INT ID;`
`};`

*Please notice the use of semi colon after the closing angle bracket*

##### STRUCT objects and attributes

To assign a value to a struct attribute you will have to use the `<-` operator. For example to assign a value to MESSAGE ABOVE, we will do,

`PROMT P;`
`P.MESSAGE <- "HELLO WORLD";`

Some of the example are below.

`STRUCT MyBook {`
`    INT name;`
`    BOOL U;`
`};`
``
``
`STRUCT K {`
`    INT N;`
`    BOOL U;`
`};`
``
`MyBook N;`
`N.name <- 100*90;`
`N.U <- FALSE`;



#### Error Handling

I have done maximum error handling for all the possible scenarios like

* Assigning incorrect values to varaibles,
* Redeclaraion of varaibles.
* Binary operation on two invalid data types
* Syntax error handling
* division by 0
* correct assignment of nested expression to a variable
* invalid attribute types of STRUCT objects

and many other..

