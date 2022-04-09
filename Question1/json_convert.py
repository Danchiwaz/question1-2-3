# converting data to json 
# i will use dummy data just for simplicty 

import json

daniel_data ={
    "name":"Daniel Maina Wachira",
    "tel_number":"0712747209",
    "area_of_residence":"Nairobi Kenya",
    "intership_expected":"interIntel",
    "profession":"Software Engineer"

}

convert_to_json = json.dumps(daniel_data)

print(convert_to_json)