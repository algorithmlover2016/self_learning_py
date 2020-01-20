import re
# reference https://docs.python.org/zh-cn/3/library/re.html

# (?x) and groups() group() group(id)
# reference https://www.zhihu.com/question/40865347
print(re.search(r'''(?x)
            \((\d{3})\) # areacode
            [ ]         # space
            (\d{3})     # prefix
            -           # dash
            (\d{4})     # number
            ''',
            '(800) 555-1212').groups())

print(re.search(r'''(?x)
            \((\d{3})\) # areacode
            [ ]         # space
            (\d{3})     # prefix
            -           # dash
            (\d{4})     # number
            ''',
            '(800) 555-1212').group())



# want to split the regex expression, should use (?x), it will ignore all whitespace, if you need, tag it explictly
print(bool(re.match(r'''(?x)\((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})
                [ ]
                (?P=areacode)-(?P=prefix)-(?P=number)
                [ ]
                1(?P=areacode)(?P=prefix)(?P=number)''', \
'(800) 555-1212 800-555-1212 18005551212')))

# areacode prefix number notations are content not regex
print(bool(re.match(r'''\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)''', \
                '(800) 555-1212 800-555-1212 18005551212')))
print(bool(re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)', \
                '(800) 555-1212 800-555-4321 18005551212')))

# retrieve them by \g<name>
print(re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', \
            '(\g<areacode>) \g<prefix>-xxxx', \
            '(800) 555-1212'))

# (?=) and (?!)

# print(re.findall(r'\w+(?= van Rossum),', \
# none will matched
# print(re.findall(r'\w+(?= van Rossum) van Rossum,', \
# will match the same line as the next print sentence
print(re.findall(r'\w+(?= van Rossum)', \
            """
            Guido van Rossum,
            Tim Peters,
            Alex Martelli,
            Just van Rossum,
            Raymond Hettinger
            """))

print(re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)', \
        """
        sales@phptr.com,
        postmaster@phptr.com,
        eng@phptr.com,
        noreply@phptr.com,
        admin@phptr.com
        """))

print(['%s@awe.com' % e.group(1) for e in \
        re.finditer(r'(?m)^\s+(?!noreply|postmaster)(\w+)', \
        """
        sales@phptr.com,
        postmaster@phptr.com,
        eng@phptr.com,
        noreply@phptr.com,
        admin@phptr.com
        """)])

print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy')))
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'yx')))
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xx')))

# group
print(re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', \
            '(800) 555-1212').groupdict())

mSearch = re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', \
            '(800) 555-1212')

print(mSearch.groupdict().get("prefix"))
print(mSearch.group("prefix"))
print(mSearch.group())


