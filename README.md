This example uses C code within Python using the ctypes library. 

This is the simplest example of which I am aware.

    gcc -shared -fPIC test.c -o test.so
    python test.py
