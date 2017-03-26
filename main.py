from TypeFormRequest import TFR
import sys

def main():
    """ create object of TFR  """
    tfr=TFR()

    """ call get form fucntion of TFR and store the json data """

    formId=tfr.get_form(sys.argv[1])
    tfr.get_data(sys.argv[1],formId[0]['id'])





if __name__=="__main__":
    main()
