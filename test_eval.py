import sys
import os
sys.path.insert(0, os.path.abspath('Lib'))
from annotationlib import ForwardRef

ref = ForwardRef("__import__('os').system('echo VULNERABLE')")
try:
    ref.evaluate()
except Exception as e:
    print(e)
