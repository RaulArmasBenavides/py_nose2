@profile
def concat_strings_efficient():
    output = "".join(str(i) for i in range(80000))  
    return output
concat_strings_efficient()