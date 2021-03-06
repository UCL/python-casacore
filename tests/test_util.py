import unittest2 as unittest
from pyrap.util import substitute


def f1(arg):
    a = 3
    s = substitute('subs as $a $arg', locals=locals())
    print(a, arg, s)


class TestUtil(unittest.TestCase):
    def test_util(self):
        a = 1
        b = 2
        p = "$((a+b)*(a+b))"
        s = substitute(p, locals=locals())
        print("a=%d, b=%d, %s => %s" % (a, b, p, s))
        f1(23)
        f1('xyz')
