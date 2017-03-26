from TypeFormRequest import TFR
import sys

def main():
    # create object of TFR(TypeFormRequest Library)
    tfr=TFR()


    # call get form fucntion of TFR and store the formId information into formID. The argument to get_forms is the api key that is provided as command line argument
    # get_forms returns a jsonObject constaing form details
    formId=tfr.get_forms(sys.argv[1])

    # call get_data fucntion of TFR to extract the responses and store it into csv. The argument to get_data are the api key that is provided as command line argument and the formId extracted
    tfr.get_data(sys.argv[1],formId[0]['id'])





if __name__=="__main__":
    main()
