def return_if(bool_value):
    if bool_value:
        return None  # return bez niczego dziala tak samo
    print("po ifie")
    # tu rowniez zwroci None nawet bez uzycia return


print("if true")
return_if(True)
print("if false")
return_if(False)
