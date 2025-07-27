"""
Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

Authors: Shelly Zhou (sz498)
Date:   09/15/2022
"""

def exchange(old, new, amt):
    """
    Returns the amount of currency recieved in the given exchange 

    In this exchange, the user is changing amt money in currency 
    old to the currency new. The value returned represents the 
    amount in currency new.

    The value returned has type float

    Parameter old: the currency on hand
    Precondition: old is a string for a valid currency code

    Parameter new: the currency to convert to
    Precondition: new is a string for a valid currency code

    Parameter amt: amount of currency to convert 
    Precondition: amt is a float
    """
    import a1

    json= a1.query_website(old,new,amt)
    #get right hand side of json
    #get before space
    s= str(a1.get_rhs(json))
    x= a1.before_space(s)
    result=float(x)
    return result


def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    x= s.index(' ')
    y=s[:x]
    return y


def after_space(s):
    """
    Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    x=s.index(' ')
    y=s[x+1:]
    return y


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that 
    delimits it.  We typically use single quotes (') to delimit a 
    string if want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C', 
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes
    """
    s.find('"')
    x= s.find('"')
    s.index('"',x+1)
    y= s.index('"',x+1)
    result= s[x+1:y]
    return result


def get_lhs(json):
    """
    Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the 
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is
    
    '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').  

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    import a1
    s= json
    a= a1.first_inside_quotes(s)
    b= s.find(a)
    c= s.find('"',b+4)
    d= s.find('"',c+1)
    return s[c+1:d]

   


def get_rhs(json):
    """
    get_rhs(json)
    Returns the rhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the 
    string inside double quotes (") immediately following the keyword
    "rhs". For example, if the JSON is

    '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'

    then this function returns '19995.85429186 Euros' (not 
    '"38781.518240835 Euros"').  

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """

    import a1
    s = json
    a= a1.first_inside_quotes(s)
    b= s.find(a)
    c= s.find('"',b+1)
    d= s.find('"',c+1)
    e= s.find('"',d+1)
    f= s.find('"',e+1)
    g= s.find('"',f+1)
    h= s.find('"',g+1)
    i= s.find('"',h+1)
    return s[h+1:i]


def has_error(json):
    """
    Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns True if there
    is an error message. For example, if the JSON is 

    '{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'

    then the query is not valid, so this function returns True (It 
    does NOT return the message 'Currency amount is invalid.').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    x= json.count('invalid')
    y= x==1
    return (y)


def query_website(old, new, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency old to the 
    currency new. The response should be a string of the form    

    '{ "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'

    where the values old-amount and new-amount contain the value 
    and name for the old and new currencies. If the query is 
    invalid, both old-amount and new-amount will be empty, while 
    "err" will have an error message.

    Parameter old: the currency on hand
    Precondition: old is a string with no spaces or non-letters
    
    Parameter new: the currency to convert to
    Precondition: new is a string with no spaces or non-letters
    
    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    import introcs
    x='old='
    y= old
    a ='&new='
    b= new
    c='&amt='
    d= amt
    e= x+y+a+b+c+str(d)
    query= introcs.urlread('http://cs1110.cs.cornell.edu/2022fa/a1?'+e)
    return query


def is_currency(code):
    """
    Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters.
    """
    import a1

    old=code
    new=code
    amt=2.5
    a = a1.query_website(old,new,amt)
    b = a1.has_error(a)
    #b= True --> has error, code is not valid, returns False
    #b= False --> no error, code is valid, returns True
    c= b==False
    return (c)