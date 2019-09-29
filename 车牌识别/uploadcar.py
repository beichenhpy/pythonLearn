import json
def upload_car(carnumber):
    filename='carnumber.json'
    with open(filename,'w') as carnumber1:
        json.dump(carnumber,carnumber1)