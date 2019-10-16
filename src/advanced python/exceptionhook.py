import sys

def my_exceptionhook(type, value, traceback):
    print('Unhandled error:', type, value, traceback)

sys.excepthook =  my_exceptionhook

print("before exception")
try:
    raise RuntimeError("Fuck we are dead.......")
except expression as identifier:
    print("I am ending gracefullys")
raise RuntimeError("Fuck we are dead.......")

print("After exception")