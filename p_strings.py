#Strings in python are surrounded by either single quotation marks, or double quotation marks
#'hello' is the same as "hello"

#i can use three double quotes or three single quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


#position
a = "Hello, World!"
print(a[1])#e

#size/length
a = "Hello, World!"
print(len(a))#13

x = "The best things in life are free!"
print("free" in x) #true

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


b = "Hello, World!"
print(b[2:5])#llo
b = "Hello, World!"
print(b[:5])#Hello
b = "Hello, World!"
print(b[2:])#llo, World!

a = "Hello, World!"
print(a.upper())#upper
print(a.lower())#lower
print(a.replace("H", "J"))#Jello, World!
print(a.split(",")) # returns ['Hello', ' World!']

"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

"""



