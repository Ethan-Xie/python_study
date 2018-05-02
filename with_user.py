
def show():
    print('123')  #1
    yield
    print('456')  #3

with show():
    print('9999')  #2