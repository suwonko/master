# -*- coding: UTF-8 -*-

from init import initialize_program

def main():
    initialize_program()
    
    import sys
    encode = sys.getdefaultencoding()
    print(encode)
    print("Python 버전:", sys.version)







if __name__ == "__main__":
    main()