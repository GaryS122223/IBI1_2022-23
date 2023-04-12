import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
if seq.startswith ('ATG'):
  lst=re.findall('TAA|TAG|TGA',seq)
  print(len(lst))
else:
  print(0)
