@profile
def concat_strings_efficient():
    output = "".join(str(i) for i in range(80000))  
    return output

if __name__ == "__main__":
    concat_strings_efficient()