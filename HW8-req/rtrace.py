

class TraceRecursion:
    def __init__(self,f):
        self.f = f
        self.traceP = False
        self.countP = False
        self.indent = 0
        self.numcalls = 0

    def count(self,*args,**kargs):
        self.traceP = False
        self.countP = True
        self.numcalls = 0
        answer = self.__call__(*args,**kargs)
        print('Num calls:', self.numcalls)
        self.countP = False
        return answer

    def trace(self,*args,**kargs):
        self.traceP = True
        self.countP = True
        self.indent = 0
        self.numcalls = 0
        print('------------------- Starting recursion -------------------')
        answer = self.__call__(*args,**kargs)
        print('-------------------- Ending recursion --------------------')
        print('Num calls:', self.numcalls)
        self.countP = False
        self.traceP = False
        return answer

    def __call__(self,*args,**kargs):
        '''Conta e traccia (se richiesto) le chiamate alla funzione'''
        if self.traceP:
            indent     = '|--'*self.indent
            callstring = self.f.__name__
            if args : callstring += str(args)
            if kargs: callstring += str(kargs)
            print (indent+" entering", callstring , sep='\t')
            self.indent += 1
        if self.countP:
            self.numcalls += 1
        answer = self.f(*args,**kargs)
        if self.traceP:
            self.indent -= 1
            print(indent+' exiting ', callstring,"returns", answer, sep='\t')
        return answer

trace = TraceRecursion
