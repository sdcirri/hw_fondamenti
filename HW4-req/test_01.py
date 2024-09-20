import testlib
import random
from ddt import file_data, ddt, data, unpack

# change this variable to True to disable timeout and enable print
DEBUG=True
DEBUG=False

WARP = 2   # test VM
WARP = 1   # your PC

import pronouncing # preload

@ddt
class Test(testlib.TestCase):
    def do_test(self, poemfile, outputfile, tau, expectedfile, expectedsync, timeout):
        """Test implementation
        - poemfile:		text file containing the input poem
        - outputfile:	text file you must write the output matrix
        - tau:			max distance of two events
        - expectedfile:	expected result - file
        - expectedsync: expected result - sync value
        - timeout:      variable timeout depending on test
        """
        TIMEOUT = timeout * WARP   # warp factor 
        if DEBUG:
                import program01 as program
                result = program.PoemSync(poemfile, outputfile, tau)
        else:
            with    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.check_imports(allowed=['program01','_io', 'pronouncing', 'math', 'encodings.utf_8']), \
                    self.timeout(TIMEOUT), \
                    self.timer(TIMEOUT):
                import program01 as program
                result = program.PoemSync(poemfile, outputfile, tau)
        self.assertEqual(type(result), float,
                         ('The output type should be: float\n'
                          '[Il tipo di dato in output deve essere: float]'))
        self.assertEqual(result, expectedsync,
                         ('The return value is incorrect\n'
                          '[Il valore di ritorno è errato]'))
        with open(expectedfile, encoding='utf8') as f: txt_a = f.read()
        with open(outputfile,   encoding='utf8') as f: txt_b = f.read()
        lines_a = [l.strip() for l in txt_a.splitlines()]
        lines_b = [l.strip() for l in txt_b.splitlines()]
        # TODO: usare una diff
        msg = 'The texts differ: ' + expectedfile + ' ' + outputfile
        self.assertEqual(lines_a, lines_b, msg)
        return 1

    def test_example_0(self):
        poemfile     = "poems/example.txt"
        outputfile   = "test_example.out.txt"
        tau          = 2
        expectedfile = "poems/example.exp.txt"
        expectedsync = 1.004154
        timeout      = 1
        return self.do_test(poemfile, outputfile, tau, expectedfile, expectedsync, timeout)

    @data ( # ID,       tau,  expectedsync, timeout
            ( '02',      2,   0.915513,     0.5 ),
            ( '06',      2,   0.546026,     0.5 ),
            ( '01',      2,   0.886818,     0.5 ),
            ( '08',     15,   0.156752,     0.5 ),
            ( '05',      2,   0.796107,     0.5 ),
            ( '07',      2,   0.864993,     0.5 ),
            ( '03',      2,   0.84305 ,     0.5 ),
            ( '09',    10,   0.011507,     14  ), # 12s
            ( '04',     2,   0.846562,     15  ), # 12s
            ( '04.200',  7,   0.960865,      1  ),  # 1s
        )
    @unpack
    def test_example(self, ID, tau, expectedsync, timeout):
        poemfile     = f"poems/text{ID}.txt"
        outputfile   = f"test_text{ID}.out.txt"
        expectedfile = f"poems/text{ID}.exp.txt"
        return self.do_test(poemfile, outputfile, tau, expectedfile, expectedsync, timeout)

    ######################### SECRET TESTS START HERE! #########################


if __name__ == '__main__':
    Test.main()

