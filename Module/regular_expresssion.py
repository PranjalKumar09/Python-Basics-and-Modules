import re

pattern = r"[A-Z]+yclone"
text = '''India, officially the Republic of India (ISO: Bhārat Gaṇarājya),[22] is a country in South Asia. It is the seventh-largest country by area; the most populous country as of June 2023;[23][24] and from the time of its independence in 1947, the world's most populous democracy.[25][26][27] Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[j] China, Dyclone Cyclone Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia.'''

match = re.search(pattern , text) # search matches first occurence found 
print (match) # <re.Match object; span=(0, 0), match=''>

# if not found it returns None




match1 = re.finditer(pattern , text) # find match all occurence found
print (match1) # <callable_iterator object at 0x000002AEDEBD6C20>
"""for item in match1:
    print(item) """
""" <re.Match object; span=(463, 470), match='Dyclone'>
<re.Match object; span=(471, 478), match='Cyclone'> """

for item in match1:
    print(item.span()) # item.span() type is tuple
    print(text[match.span()[0]:match.span()[1]])
    """(463, 470)
Dyclone
(471, 478)
Dyclone"""
    


"""Character	Description	Example	Try it
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group"""

"""
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
"""


"""  
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"

r"ain\b"	

\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"

r"ain\B"	

\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string
"""

""" span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match 





 re.sub() replaces all occurrences of the string 
 
 re.sub(word / pattern _to_replace , word_to_place , string_content)"""