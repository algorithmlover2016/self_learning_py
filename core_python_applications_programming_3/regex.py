import re

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
