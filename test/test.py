import unittest
from noid.pynoid import *
import re

class PynoidTests(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_naa_append(self):
        noid = mint(naa='abc')
        self.assertTrue(noid.startswith('abc/'))

    def test_scheme_append(self):
        schemes = ['doi:', 'ark:/', 'http://']
        for scheme in schemes:
            noid = mint(scheme=scheme)
            self.assertTrue(noid.startswith(scheme))
    
    def test_mint_short_term(self):
        noid = mint()
        self.assertTrue(noid.startswith(SHORT))

    def test_mint_ns(self):
        ns = range(10)
        for n in ns:
            self.assertEqual(mint('d', n), DIGIT[n])
        ns = range(29)
        for n in ns:
            self.assertEqual(mint('e', n), XDIGIT[n])

    def test_namespace_overflow(self):
        self.assertRaises(NamespaceError, mint, template='d', n=10)
        self.assertRaises(NamespaceError, mint, template='e', n=29)

    def test_mint_z_rollover(self):
        self.assertEqual(mint('zd', 10), '10')        
        self.assertEqual(mint('ze', 29), '10')

    def test_validate_valid(self):
        valid = 'test31wqw0wsr'
        validScheme = 'ark:/test31wqw0wsr'
        self.assertTrue(validate(valid))
        self.assertTrue(validate(validScheme))

    def test_validate_invalid(self):
        invalid = 'test31qww0wsr'
        invalidScheme = 'ark:/test31qww0wsr'
        self.assertRaises(ValidationError, validate, invalid)
        self.assertRaises(ValidationError, validate, invalidScheme)

    def test_checkdigit(self):
        self.assertEqual(mint('eek', 100), '3f0')
        self.assertRaises(ValidationError, validate, 'f30')


if __name__ == '__main__':
    unittest.main()
        
