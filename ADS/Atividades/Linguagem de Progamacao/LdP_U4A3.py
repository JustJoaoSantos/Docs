# assert 
def sum_numbers(n):
    assert sum([1, 2, 3, 4]) == 10
    assert sum([-1, 0, 1]) == 0
    assert sum([]) == 0
    return sum(n)
    
teste = sum_numbers([1, 2, 3, 5])
print(teste)

# doctest
def sum_numbers_doctest(n):
    '''
    Soma os numeros em uma lista
    
    Exemplos:
    >>>sum_numbers_doctest([1, 2, 3, 4])
    10
    >>>sum_numbers_doctest([-1, 0, 1])
    0
    >>>sum_numbers_doctest([])
    0
    '''
    return sum(n)

if __name__ == "__main__":
    import doctest 
    doctest.testmod()
    
# unittest
def sum_numbers_unittest(n):
    return sum(n)
    
class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers_positive(self):
        self.assertEqual(sum_numbers_unittest([1, 2, 3, 4]), 10)
        
    def test_sum_numbers_mixed(self):
        self.assertEqual(sum_numbers_unittest([-1, 0, 1]), 0)
        
    def test_sum_numbers_empty(self):
        self.assertEqual(sum_numbers_unittest([]), 0)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)