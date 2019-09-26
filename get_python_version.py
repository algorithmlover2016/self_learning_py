import platform
import sys

if isinstance(platform.python_version(), str):
    print(platform.python_version())

# if platform.python_version()[0] < "3" :
#     print platform.python_version()
#     print "---------------------------------"
#     print sys.version
#     print sys.version_info
#     
# else:
#     print(platform.python_version())
#     print("---------------------------------")
#     print(sys.version)
#     print(sys.version_info)
#     
outPutBytes = b"%d" % (1800)
print(outPutBytes)

from builtins import str
a = u'abc'
b = b'def'
c = b.decode()
assert isinstance(a, str) and isinstance(c, str)

assert isinstance(a.encode("utf-8"), (bytes, str))
assert isinstance(b, (bytes, str))
import json
print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
