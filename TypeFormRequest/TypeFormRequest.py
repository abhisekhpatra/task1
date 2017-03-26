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



    def get_data(self,API_KEY,id):

        api_url="https://api.typeform.com/v1/form/"+id+"?key="+API_KEY
        response=requests.get(api_url)
        resposne_status=response.status_code
        if resposne_status == 404:
             print("404 Error")
        elif resposne_status == 403:
             print("403 ERROR")

        else: json=response.json()


        response_data=json["responses"]
        headers=self.get_headers(json)
        # open a file for writing
        answers = open('Data.csv', 'wb')
        csvwriter = csv.writer(answers)

        csvwriter.writerow(headers)

        for response in response_data:

             row=response["answers"]
             csvrow=[]

             print("jsonrow-->")
             print(row)
             if len(row)==0: continue
             for j in range(len(headers)):
                 if(headers[j] in row.keys()): csvrow.append(row[headers[j]])
                 else: csvrow.append("")
             csvwriter.writerow(csvrow)

        answers.close()





    def get_headers(self,data):
        questions=data["questions"]
        header=[]
        for q in questions:
            str=q["id"]
            # print(str)
            header.append(str)

        return header




