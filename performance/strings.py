@profile
def concat_strings_inefficient():
    output = ""
    for i in range(80000):
        output += str(i)  
    return output
concat_strings_inefficient()
 