#!env python3
from robobrowser import RoboBrowser

def tracker():
    br = RoboBrowser(parser="lxml")
    br.open('https://access02.dwp.accenture.com/SecureAuth1/SecureAuth.aspx')
    
    
tracker()

    

