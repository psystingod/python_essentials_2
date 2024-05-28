word1 = "donut";
word2 = "Nabucodonosor";
word3 = "";

for w in word1:
    word3 += word2[word2.find(w)];

if word1 == word3:
    print("Yes.")
else:
    print("No.")
print(word3);

"""

word = input("Enter the word you wish to find: ").upper()
strn = input("Enter the string you wish to search through: ").upper()

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start) 
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Yes")
else:
	print("No")

"""