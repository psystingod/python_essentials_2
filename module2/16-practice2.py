number_patterns = [
    "###\n# #\n# #\n# #\n###",
    "#\n#\n#\n#\n#",
    "###\n  #\n###\n#  \n###",
    "###\n  #\n###\n  #\n###",
    "# #\n# #\n###\n  #\n  #",
    "###\n#  \n###\n  #\n###",
    "###\n#  \n###\n# #\n###",
    "###\n  #\n  #\n  #\n  #",
    "###\n# #\n###\n# #\n###",
    "###\n# #\n###\n  #\n###",
]

pattern_lines = [pattern.split("\n") for pattern in number_patterns];

mstring = "9081726359";

""""
for i in mstring:
    for j in range(10):
        if int(i) == j:
            print(number_patterns[j]);
"""

for row in range(len(pattern_lines[0])):
    output = "";
    for i in mstring:
        output += pattern_lines[int(i)][row] + " ";
    print(output);
