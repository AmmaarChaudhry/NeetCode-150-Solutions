#This is a cheesy way that works because the question will only include Ascii chars for its strings
#If it were to incl UNICODE this would not work

def encode(strs: List[str]) -> str:
    big_string = ""
    for word in strs:
        big_string = big_string + "/" + word
    big_string = big_string + "/"
    big_string = big_string[1:]
    print(big_string)
    return big_string
        



def decode(s: str) -> List[str]:
    decoded_string = []
    temp_string = ""
    for chars in s:
        if chars != "/":
            temp_string = temp_string + chars
        else:
            decoded_string.append(temp_string)
            temp_string = ""
        
    #print(decoded_string)
    return decoded_string
    
test = encode(["Hello", "World", "My", "Name", "Is"])
print(decode(test))


