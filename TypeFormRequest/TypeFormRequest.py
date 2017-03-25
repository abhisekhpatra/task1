import requests
import csv


class TFR:



    def get_form(self,API_KEY):

        api_url="https://api.typeform.com/v1/forms?key="+API_KEY
        print(api_url)
        response=requests.get(api_url)
        resposne_status=response.status_code

        if resposne_status == 404:
             print("404 Error")
        elif resposne_status == 403:
            print("403 ERROR")

        else: return response.json();


    def get_data(selfself,API_KEY,id):
        api_url="https://api.typeform.com/v1/forms/"+id+"?key="+API_KEY
        response=requests.get(api_url)
        resposne_status=response.status_code

        if resposne_status == 404:
             print("404 Error")
        elif resposne_status == 403:
            print("403 ERROR")

        else: json=response.json()

        response_data={}
        response_data=json["fields"]

        print(response_data.keys())

        for i in response_data:
            print(i)








