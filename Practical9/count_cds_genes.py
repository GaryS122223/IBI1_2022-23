import re
number = 0
seq = ""
user_choice = input("give me a type of stop codons(TAA, TAG or TGA):")
given_genes = open("C:/Users/DELL/OneDrive/桌面/lesson/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
save = open(f"C:/Users/DELL/OneDrive/桌面/lesson/{user_choice}_genes.fa", "w")
datalines = given_genes.readlines()

for line in datalines:
if re.match(">", line):
if number > 0:
save.write(name + " " + str(number) + "\n")
number = 0
name = line.split(" ")[0].strip(">")
seq = ""
seq += line.strip("\n")
for i in range(len(line) // 3):
if re.match(user_choice, line[3i:3i+3]):
number += 1

save.close()
given_genes.close()
