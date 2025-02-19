#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re
text = 'Bekzhan,  bskmbk ajdns, 62+2+a s       af'
print(re.sub("[,. ]","*",text))