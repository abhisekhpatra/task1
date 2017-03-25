from TypeFormRequest import TFR
import sys

def main():

    tfr=TFR()
    tfr.get_form(sys.argv[1])



if __name__=="__main__":
    main()
