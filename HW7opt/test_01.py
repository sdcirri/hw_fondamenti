
import testlib
import isrecursive
from ddt import file_data, ddt, data, unpack
import sys

# scommentare la seconda riga per disabilitare timeout e abilitare print
DEBUG=True
DEBUG=False

TIMEOUT=1 * 2

@ddt
class Test(testlib.TestCase):

    def do_test(self, doRecTest, string, expected):
        '''Test implementation
            - doRecTest: do the recursion step
            - string:    string containing the sequence
            - expected:  expected answer
            TIMEOUT=0.1 seconds per test
        '''
        # first we check that the code is recursive
        if doRecTest:
            try:
                import program01 as program
                isrecursive.decorate_module(program)
                program.ex1(string)
            except isrecursive.RecursionDetectedError:
                pass
            else:
                raise Exception("Recursion not present")
            finally:
                isrecursive.undecorate_module(program)
                del program
                del sys.modules['program01']

        # then we compute the result
        if DEBUG:
                import program01 as program
                result   = program.ex1(string)
        else:
            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.forbidden_function('builtins.open'), \
                    self.check_imports(allowed=['program01','_io']), \
                    self.timeout(TIMEOUT), \
                    self.timer(TIMEOUT):
                import program01 as program
                result   = program.ex1(string)

        # and check the result
        self.assertIsInstance(result,  set,      "the result should be a set / il risultato prodotto deve essere un insieme")
        for x in result:
            self.assertIsInstance(x,   str,      "all its elements should be strings / gli elementi dell'insieme devono essere stringhe")
        self.assertEqual(result,       expected, "the returned set is wrong / l'insieme restituito non e' corretto")
        return 1

    @data(
        (False, ' '.join(['1']*1),                             { '1' } ),
        (False, ' '.join(['1']*2)+' 2',                        { '2' } ),
        (False, ' '.join(['1']*7),                             { '1' } ),
        (False, ' '.join(['1']*8)+' 2',                        { '2' } ),
        (True,  '2 2 1 2 3',                                   { '1 2 3', '2 1 3' } ),
        (False, '1 2 1 2 2',                                   { '2' } ),
        (True,  '1 2 1 2 1 2 3',                               { '1 2 3', '2 1 3'} ),
        (True,  '1 2 0 1 0 0 1',                               { '2 0 1', '2 1 0', '1 2 0'} ),   # esempio
        (True,  '3 3 2 3 2 3 2 3 1',                           { '3 2 1', '2 3 1'} ),
        (True,  '1 2 3 1 2 3 1 2 3',                           { '1 2 3', '1 3 2', '2 1 3', '2 3 1', '3 1 2', '3 2 1'} ),
        (True,  '1 2 3 2 2 1 1 3 3',                           { '1 2 3', '1 3 2', '2 1 3', '2 3 1', '3 2 1'} ),
        (True,  '1 1 2 2 3 3 1 2 3',                           { '1 2 3', '1 3 2', '2 3 1', '2 1 3', '3 1 2'} ),
        (True,  '1 2 1 2 1 2 1 2 1 2 3',                       { '1 2 3', '2 1 3'} ),
        (True,  '1 1 2 1 1 3 1 1 4 1 5',                       { '1 2 3 4 5', '2 1 3 4 5', '2 3 1 4 5', '2 3 4 1 5'} ),
        (True,  '1 2 3 4 7 5 7 6 7 8 9 8 8 6 9 5 9 4 3 2 1',   { '7 8 9', '7 9 8' } ),
        (True,  '1 2 1 3 1 4 1 5 1 6 1 7 1 8 1 9 10 9 10 9 10 1 8 1 7 1 6 1 5 1 4 1 3 1 2 1 11', {'9 10 11', '10 9 11'} ),
        (True,  '1 '*5 + '4 '*2 + '2 '*5 + '3 '*5 + '4 '*3 + '6',   { '1 4 2 3 6', '1 2 3 4 6'} ),
        (False, '1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11 10 10 9 9 8 8 7 7 6 6 5 5 4 4 3 3 2 2 1 1', { '11' }),
    )
    @unpack
    def test_data(self, doRecTest, sequence, expected):
        return self.do_test(doRecTest, sequence, expected)

if __name__ == '__main__':
    Test.main()
