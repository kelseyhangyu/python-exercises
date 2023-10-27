def is_two(input_value):
    return input_value == 2 or input_value == '2'
def is_vowel(string):
    return True if string.lower() in list('aeiou') else False
def is_vowel(somestring):
    if type(somestring) == str:
        if len(somestring) == 1 and somestring.isalpha():
            return somestring.lower() in list ('aeiou')
        else:
            return False
def is_vowel(x):
    """
    Return if the value passed is a vowel or not.

    Parameters
    ----------
    x : string
        Takes a single-letter string argument.

    Returns
    -------
    bool
        Returns True if the character is a vowel, and False otherwise.

    """
    vowels = ['a','e','i','o','u']
    
    # Check if string has numbers
    if x.isalpha():
        if x.lower() in vowels:
            return True
    
    # Return false if nothing else
    return False
def is_consonant(string):
    return True if string.lower() not in ['a','e','i','o','u'] else False
def accept(string):
    if string[0] in consonants:
        return string[0].upper() + string[1:]
    else:
        return string
def calculate_tip(tip_percentage, bill):
    tip = tip_percentage * bill
    return tip
def apply_discount(og_price, dis_per):
    final_price = og_price * (1 - dis_per)
    return round(final_price,2)
def handle_commas(number,):
    return int(number)
def handle_commas(number):
    if type(number) == str:
        strip_number = number.replace(',','')
        if strip_number.isdigit():
            return int(strip_number)
        else:
            return False
    else:
        return False
def get_letter_grade(number):
    if number >= 90:
        return("A")
    elif number >= 80:
        return("B")
    elif number >=70:
        return('C')
    elif number >= 60:
        return('D')
    elif 0<=number<60:
        return('F')
def remove_vowels(word):
    new_word = ''
    for letter in word:
        if not vowels(letter):
            new_word += letter
    return new_word
def cum_sum(oldlist):
    newlist = []
    c_sum = 0
    for num in oldlist:
        ''''''
        c_sum += num
        ''''''
        newlist.append(c_sum)
        
    print(f'oldlist: {oldlist}')
    print(f'newlist: {newlist}')
    
