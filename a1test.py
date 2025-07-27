"""
Test script for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1.

Authors: Shelly Zhou (sz498)
Date:   09/15/2022
"""
import introcs
import a1

def testA():
    """
    Test procedure for Part A
    Test cases for functions before_space and after_space.
    Expect to return s before the first space 
    and s after first space
    """
    #testing one space
    result= a1.before_space('4.502 Euros')
    introcs.assert_equals('4.502', result)
    #testing more than one space
    result = a1.before_space('4.502  Euros')
    introcs.assert_equals('4.502', result)
    #testing starting with a space
    result= a1.before_space(' 4.502Euros')
    introcs.assert_equals('', result)
    #testing starting with space
    result= a1.before_space(' 4.502 Euros ')
    introcs.assert_equals('', result)

    #testing one space
    result= a1.after_space('4.502 Euros')
    introcs.assert_equals('Euros', result)
    #testing two one spaces
    result= a1.after_space('4.502  Euros')
    introcs.assert_equals(' Euros', result)
    #testing starting with a space
    result= a1.after_space(' 4.502 Euros')
    introcs.assert_equals('4.502 Euros', result)
    #testing space at the end the string
    result= a1.after_space('4.502Euros ')
    introcs.assert_equals('', result)


def testB():
    """
    Test procedure for Part B
    Testing first_inside_quotes, get_lhs, get_rhs, 
    and has_error.
    """
    #testing one inside quotes
    result= a1.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result)
    #testing two inside quotes
    result= a1.first_inside_quotes('A "B C" "D C"')
    introcs.assert_equals('B C', result)
    #testing only inside quotes
    result= a1.first_inside_quotes('"BC"')
    introcs.assert_equals('BC', result)
    #testing empty quotes
    result= a1.first_inside_quotes('A""')
    introcs.assert_equals('', result)

    #testing get_lhs for 2.5 USD to CUP:
    result=a1.get_lhs(('{ "lhs" : "2.5 United States Dollars",\
     "rhs" : "64.375 Cuban Pesos", "err" : "" }'))
    introcs.assert_equals('2.5 United States Dollars', result)
    #testing get_lhs with no old
    result=a1.get_lhs(('{ "lhs" : "", "rhs" : "",\
     "err" : "Source currency code is invalid." }'))
    introcs.assert_equals('', result)
    #testing get_lhs with no new
    result=a1.get_lhs(('{ "lhs" : "", "rhs" : "",\
     "err" : "Exchange currency code is invalid." }'))
    introcs.assert_equals('', result)
    #tesing get_lhs USD to USD
    result=a1.get_lhs(('{ "lhs" : "2.5 United States Dollars",\
     "rhs" : "2.5 United States Dollars", "err" : "" }'))
    introcs.assert_equals('2.5 United States Dollars', result)
    #testing get_lhs with no currency amt
    result=a1.get_lhs(('{ "lhs" : "", "rhs" : "",\
     "err" : "Currency amount is invalid." }'))
    introcs.assert_equals('', result)

    #testing get_rhs USD to CUP
    result=a1.get_rhs(('{ "lhs" : "2.5 United States Dollars",\
     "rhs" : "64.375 Cuban Pesos", "err" : "" }'))
    introcs.assert_equals('64.375 Cuban Pesos', result)
    #testing get_rhs with everything missing
    result=a1.get_rhs(('{ "lhs" : "", "rhs" : "",\
     "err" : "Source currency code is invalid." }'))
    introcs.assert_equals('', result)
    #testing get_rhs with no new
    result=a1.get_rhs(('{ "lhs" : "", "rhs" : "",\
     "err" : "Exchange currency code is invalid." }'))
    introcs.assert_equals('', result)
    #testing get_rhs with no old
    result=a1.get_rhs(('{ "lhs" : "", "rhs" : "",\
     "err" : "Source currency code is invalid." }'))
    introcs.assert_equals('', result)
    #testing get_rhs with no currency amt
    result=a1.get_rhs(('{ "lhs" : "", "rhs" : "",\
     "err" : "Currency amount is invalid." }'))
    introcs.assert_equals('', result)
    #tesing USD to USD
    result=a1.get_rhs(('{ "lhs" : "2.5 United States Dollars",\
     "rhs" : "2.5 United States Dollars", "err" : "" }'))
    introcs.assert_equals('2.5 United States Dollars', result)

    #testing has_error with no error 2.5 USD to CUP
    result=a1.has_error(('{ "lhs" : "2.5 United States Dollars",\
     "rhs" : "64.375 Cuban Pesos", "err" : "" }'))
    introcs.assert_equals(False, result)
    #testing has_error with no amt
    result=a1.has_error(('{ "lhs" : "", "rhs" : "",\
     "err" : "Currency amount is invalid." }'))
    introcs.assert_equals(True, result)
    #testing has_error with no new
    result=a1.has_error(('{ "lhs" : "", "rhs" : "",\
     "err" : "Exchange currency code is invalid." }'))
    introcs.assert_equals(True, result)
    #testing has_error with no old
    result=a1.has_error(('{ "lhs" : "", "rhs" : "",\
     "err" : "Source currency code is invalid." }'))
    introcs.assert_equals(True, result)


def testC():
    """
    Test procedure for Part C
    Test cases for query_website(old, new, amt)
    Should return json from website
    """
    #testing USD to CUP
    result=a1.query_website('USD','CUP',2.5)
    introcs.assert_equals('{ "lhs" : "2.5 United States Dollars", '
    +'"rhs" : "64.375 Cuban Pesos", "err" : "" }', result)
    #testing USD to USD
    result=a1.query_website('USD','USD',2.5)
    introcs.assert_equals('{ "lhs" : "2.5 United States Dollars", '
    +'"rhs" : "2.5 United States Dollars", "err" : "" }', result)
    #testing no old
    result=a1.query_website('','USD',2.5)
    introcs.assert_equals('{ "lhs" : "", "rhs" : "", '
    +'"err" : "Source currency code is invalid." }', result)
    #testing no new
    result=a1.query_website('USD','',2.5)
    introcs.assert_equals('{ "lhs" : "", "rhs" : "", '
    +'"err" : "Exchange currency code is invalid." }', result)
    #testing zero amount
    result=a1.query_website('USD','CUP',0.0)
    introcs.assert_equals('{ "lhs" : "0 United States Dollars", '
    +'"rhs" : "0 Cuban Pesos", "err" : "" }', result)
    #testing non-existent currency
    result=a1.query_website('ABC','USD',6.0)
    introcs.assert_equals('{ "lhs" : "", "rhs" : "", '
    +'"err" : "Source currency code is invalid." }', result)


def testD():
    """
    Test procedure for Part D
    Testing 3 letters for is_currency
    return 'True' if valid and 'False' for invalid
    Testing exchange(old, new, amt) 
    and expect converted amt from old to new
    """
    #testing is_currency for valid currency
    result=a1.is_currency('USD')
    introcs.assert_equals(True,result)
    #testing is_currency for non-valid currency
    result=a1.is_currency('ABC')
    introcs.assert_equals(False,result)

    #testing exchange(old, new, amt) 'USD' to 'CUP'
    result=a1.exchange('USD','CUP',2.5)
    introcs.assert_floats_equal(64.375, result)
    #testing exchange 'BMD' to 'BTC'
    result=a1.exchange('BMD','BTC', 1600)
    introcs.assert_floats_equal(0.080584544, result)
    #testing exchange USD to USD
    result=a1.exchange('USD','USD',2.5)
    introcs.assert_floats_equal(2.5, result)
    #testing exchange amt 0.0
    result=a1.exchange('BMD','BTC', 0.0)
    introcs.assert_floats_equal(0.0, result)


testA()
testB()
testC()
testD()
print('Module a1 passed all these tests.')