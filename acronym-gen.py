def main():

    phrase = input ("Enter a phrase: ")
    words = phrase.split()

    acronym = ""
    for word in words:
      acronym += word[0].upper()

    print ("The acronym to your phrase is ", acronym)
    
main()
