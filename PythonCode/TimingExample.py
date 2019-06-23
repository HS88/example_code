import time

class Timer:    
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
		
try:
	with Timer() as t:
        #Do whatever
		for i in range(0,100000):
			print('')
finally:
    print('Request took %.03f sec.' % t.interval)