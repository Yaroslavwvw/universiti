import re

import ssl
import urllib.request

pattern = r'(\+7 [(]\d{3}[)] \d{3}-\d\d-\d\d)(.+)((?:Показать )(.+)(?: на карте))'
num_pattern = r'(\+7 [(]\d{3}[)] \d{3}-\d\d-\d\d)'
adr = r'(?:Показать )(.+)(?: на карте)'

ssl._create_default_https_context = ssl._create_unverified_context
string = urllib.request.urlopen('https://msk.spravker.ru/avtoservisy-avtotehcentry/').read().decode()
#print(string)

match = re.findall(num_pattern,  string)
match1 = re.findall(adr, string)
match2 = re.findall(pattern, string)
#match = re.finditer(adr, string)

#match = [match[i:i+4] for i in range(0, len(match), 4)]
#match = ["".join(x) for x in num_pattern.findall(string)]
#print(match[0] if match else 'Not found')
print(match)
print(len(match), len(match1))



