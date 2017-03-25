import requests


class TFR:



    def get_form(self,API_KEY):

        api_url="https://api.typeform.com/v1/forms?key="+API_KEY
        print(api_url)
        response=requests.get(api_url)
        resposne_status=response.status_code
        print(resposne_status)
