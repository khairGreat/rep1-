


try:
     
    import matplotlib 
    print(matplotlib.__version__)
       
except ImportError as error: 
    print(error) 


def concat_string( string1 : str , string2 : str )-> str :
    return f'{string1} {string2}'