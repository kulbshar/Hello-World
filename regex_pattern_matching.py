import re

s = 'foo123bar'
re.search('[0-9][0-9][0-9]', s)

re.search('[0-9][0-9][0-9]', 'foo456bar')

re.search('[0-9][0-9][0-9]', '234baz')

re.search('[0-9][0-9][0-9]', 'qux678')

print(re.search('[0-9][0-9][0-9]', '12foo34'))

s = 'foo123bar'
re.search('1.3', s)

s = 'foo13bar'
print(re.search('1.3', s))


print(re.search('^[0-9][0-9][0-9]', '12foo34'))
print(re.search('^[0-9][0-9][0-9]', '122foo34'))
print(re.search('^[0-9][0-9][0-9]', '12244foo34'))


print(re.search('^[0-9][0-9][0-9]$', '12244foo34'))


print(re.search('^[0-9][0-9][0-9]$', '123'))


print(re.search('[0-9][0-9][0-9]*', '12244foo34'))
print(re.search('[0-9][0-9][0-9]*', '12foo34'))

print(re.search('[0-9][0-9][0-9]+', '12244foo34'))
print(re.search('[0-9][0-9][0-9]+', '12foo34'))


re.search('ba[artz]', 'foobarqux')
re.search('ba[artz]', 'foobazqux')

re.search('[a-z]', 'FOObar')

re.search('[0-9][0-9]', 'foo123bar')
re.search('[0-9a-fA-f]', '--- a0 ---')


# You can complement a character class by specifying ^ as the first character, in which case it matches any
# character that isn’t in the set. In the following example, [^0-9] matches any character that isn’t a digit:
re.search('[^0-9]', '12345foo')

# If a ^ character appears in a character class
# but isn’t the first character, then it has no special meaning and matches a literal '^' character:
re.search('[#:^]', 'foo^bar:baz#qux')

# As you’ve seen, you can specify a range of characters in a character class
# by separating characters with a hyphen. What if you want the character class to
#  include a literal hyphen character? You can place it as the first or
#  last character or escape it with a backslash (\):


re.search('[-abc]', '123-456')
re.search('[abc-]', '123-456')
re.search('[ab\-c]', '123-456')


# If you want to include a literal ']' in a character class,
#  then you can place it as the first character or escape it with backslash:


re.search('[]]', 'foo[1]')

re.search('[[]', 'foo[1]')

re.search('[\]]', 'foo[1]')

re.search('[\[]', 'foo[1]')

re.search('[ab\]cd]', 'foo[1]')


# Other regex metacharacters lose their special meaning inside a character class:

re.search('[)*+|]', '123*456')
re.search('[)*+|]', '123+456')

re.search('foo.bar', 'fooxbar')
print(re.search('foo.bar', 'foobar'))

print(re.search('foo.bar', 'foo\nbar'))


# \w matches any alphanumeric word character. Word characters are uppercase and lowercase letters, digits,
# and the underscore (_) character, so \w is essentially shorthand for [a-zA-Z0-9_]:

re.search('\w', '#(.a$@&')
re.search('[a-zA-Z0-9_]', '#(.a$@&')

# \W is the opposite. It matches any non-word character and is equivalent to [^a-zA-Z0-9_]:
re.search('\W', 'a_1*3Qb')
re.search('[^a-zA-Z0-9_]', 'a_1*3Qb')

# \d matches any decimal digit character. \D is the opposite. It matches any character that isn’t a decimal digit:
re.search('\d', 'abc4def')

# \d is essentially equivalent to [0-9], and \D is equivalent to [^0-9].

re.search('\D', '234Q678')

# \s matches any whitespace character:
re.search('\s', 'foo\nbar baz')

# \S is the opposite of \s. It matches any character that isn’t whitespace:
re.search('\S', '  \n foo  \n  ')


# In this case, [\d\w\s] matches any digit, word, or whitespace character.
re.search('[\d\w\s]', '---3---')
re.search('[\d\w\s]', '---a---')
re.search('[\d\w\s]', '--- ---')

# backslash (\)
re.search('.', 'foo.bar')
re.search('\.', 'foo.bar')

s = r'foo\bar'
print(s)

re.search('\\', s)


re.search('\\\\', s)


re.search('^foo', 'foobar')
print(re.search('^foo', 'barfoo'))


re.search('bar$', 'foobar')
print(re.search('bar$', 'barfoo'))

re.search('bar\Z', 'foobar')
print(re.search('bar\Z', 'barfoo'))
