
probablepeople is a python library for parsing unstructured romanized name or company strings into components, using conditional random fields.

>From the python interpreter:

>>> import probablepeople
>>> probablepeople.parse('Mr George "Gob" Bluth II') 
[('Mr', 'PrefixMarital'), 
 ('George', 'GivenName'), 
 ('"Gob"', 'Nickname'), 
 ('Bluth', 'Surname'), 
 ('II', 'SuffixGenerational')]
>>> probablepeople.parse('Sitwell Housing Inc')
[('Sitwell', 'CorporationName'),
 ('Housing', 'CorporationName'),
 ('Inc', 'CorporationLegalType')]


