# Contains class to represent quantity of crypto currencies. 
# In python, quantity is represented as a long() , which has infinite precision
# (as opposed to int() which is 32 bit precision which is not enough for large transactions)
# and a single unit of qty is a single unit of the smallest divisible unit of the currency
# (for example a satoshi for bitcoin).
#

def _cryptoDecimalPlace(crypto_name):
    if crypto_name.lower() in ['bitcoin', 'btc','btc_testnet']:
        return 8 
    elif crypto_name.lower() in ['dogecoin','doge','doge_testnet']:
        return 8
    elif crypto_name.lower() in ['litecoin','ltc','ltc_testnet']:
        return 8

# Converstion between qty and float is obviously not reliable, 
# Should not be used for anything that requires precision 
def convertQtyToFloat(qty,crypto_name):
    return float(qty)/10**_cryptoDecimalPlace(crypto_name)
 
def convertFloatToQty(qty_float,crypto_name):
    return long(qty_float * (10**_cryptoDecimalPlace(crypto_name)))

# Get how many base units are in a single nominal unit
# i.e, hundred million satoshis in a bitcoin
def getBaseUnitsPerNominal(crypto_name):
    return long(10)**_cryptoDecimalPlace(crypto_name)


def convertQtyToString(qty,crypto_name):
    decimal_place=_cryptoDecimalPlace(crypto_name)
    str_qty=str(qty)
    # in case less than 1 in nominal unit
    if len(str_qty) <= decimal_place:
        zeros='0.'
        for i in range(0,decimal_place-len(str_qty)):
            zeros+='0'
        str_qty=zeros+str_qty 
    # in case more than 1 in nominal unit
    elif len(str_qty) > decimal_place:
        str_qty= str_qty[0:len(str_qty)-decimal_place]+'.'+str_qty[len(str_qty)-decimal_place:] 

    # remove trailing zeros
    remove_zero_index=None
    for i in range(len(str_qty)-1,-1,-1):
        if str_qty[i]=='0':
            remove_zero_index=i
        else:
            break
    if remove_zero_index !=None:
        str_qty=str_qty[0:i+1]

    # remove trailing . 
    if str_qty[-1] == '.':
        str_qty=str_qty[0:-1]

    return str_qty

def convertStringToQty(string,crypto_name):
    split_string=_splitString(string)
    if len(split_string[1]) > _cryptoDecimalPlace(crypto_name):
        raise Exception('string contains too many decimal places') 
    int_part= _stringToLong(split_string[0])
    dec_part= _stringToDec(split_string[1],_cryptoDecimalPlace(crypto_name))
    return int_part * getBaseUnitsPerNominal(crypto_name) +  dec_part


# Below functions used for string to qty conversion 

def _splitString(string):
    string=string.strip() #remove white space
    split_string=string.split('.')
    if len(split_string) > 2:
        raise Exception('unexpected string:{}'.format(string)) 
    integer_part=split_string[0]

    if len(split_string) ==2:
        decimal_part=split_string[1]
    else:
        decimal_part='' 

    return(integer_part,decimal_part)   

def _stringToDec(string, places):
    zeros_to_add=places-len(string)
    for i in range(0,zeros_to_add):
        string+='0'
    return _stringToLong(string)


def _stringToLong(string):
    # integer part

    index=len(string)-1
    int_sum=0
    for char in string: 
        try:
            int_char=long(char)
        except ValueError:
            raise Exception('non numeric character found in string') 
        int_sum+= int_char * 10**index     
        index-=1
   
    return int_sum
