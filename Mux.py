def mux_letters(inputstring,numberoftimes):
    outputstring= ""
    for letters in inputstring:
        for count in range(numberoftimes):
            outputstring= (outputstring+letters)
    return outputstring 

inputstring= "finally done"
numberoftimes= 6 
extra=mux_letters(inputstring,numberoftimes)
print(extra)