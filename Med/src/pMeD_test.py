import pMeD
import unittest
from test import test_support


class TestLoadFileFunctions(unittest.TestCase):

    # def setUp(self):
    #    requests = []
        
    def test_loadFile(self):
        pMeD.load_employees()
        
        print pMeD.employees.__len__()
        self.assertTrue(pMeD.employees.__len__() == 5)
        
        pMeD.print_list(pMeD.employees)



class TestEmployeeObject(unittest.TestCase):

    def test_loadFile(self):
        self.assertTrue(pMeD.employees.__len__() == 0)



def test_main():
    test_support.run_unittest(TestLoadFileFunctions,
                              TestEmployeeObject)

if __name__ == '__main__':
    test_main()