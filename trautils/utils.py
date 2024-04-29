import sys
import pickle
import datetime

def print_progress(message: str, rate: float):
    '''Printing progress'''
    if rate < 0: rate = 0
    if rate > 1: rate = 1
    percent = rate * 100
    sys.stdout.write('\r')
    sys.stdout.write('{} {:.2f} % [{:<50s}]'.format(message, percent, '=' * int(percent / 2)))
    sys.stdout.flush()


def save(obj, filename: str):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)


def load(filename: str):
    with open(filename, 'rb') as file:
        return pickle.load(file)

class Timer:
    def __init__(self):
        self.current_time = None

    def tic(self):
        self.current_time = datetime.datetime.now()

    def toc(self, prompt="Elapsed: ", return_timespan=False):
        if return_timespan:
            return datetime.datetime.now() - self.current_time
        else:
            print(f'{prompt}{datetime.datetime.now() - self.current_time}')

    @staticmethod
    def timespan_str(timespan: datetime.timedelta):
        total = timespan.seconds
        second = total % 60 + timespan.microseconds / 1e+06
        total //= 60
        minute = int(total % 60)
        total //= 60
        hour = int(total % 60)
        return f'{hour:02d}:{minute:02d}:{second:05.2f}'