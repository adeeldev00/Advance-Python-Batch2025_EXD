# #Whitespaces are important in Python. Whitespace at the start of a line is
#  called indentation. It is used to mark the start of a new code block. A block or
#  code block is a group ofstatements in a programorascript. Leading spaces
#  at the beginning of a line are used to determine the indentation level, which
#  in turn is used to determine the grouping of statements. Also, statements
#  which go together must have same indentation level.


#  A wrong indentation raises the error. For example,

#  stock_name = 'AAPL'
stock_name1 = 'GOOG'

#  # Incorrect indentation. Note a whitespace at
#  # the beginning of line.

#  print('Stock name is', stock_name) #we get error because space at start in variable

#  # Correct indentation.
print('Stock name is', stock_name1)
#  Upon running the following code, we will be presented with the following
#  error
#  File "indentation_error.py", line 2
#  print('Stock name is', stock_name)
#  ^
#  IndentationError: unexpected indent
#  1https://docs.python.org/3.6/reference/lexical_analysis.html#literals



# (hum simple ya kaha sakty hai jab bi kasi line k start par space aye ga to wo indentation error dy ga python is ko new block of code samjta hai)