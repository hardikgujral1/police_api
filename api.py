import pandas as pd
from geopy.distance import geodesic as gd
from flask import Flask,jsonify,request
app=Flask(__name__)

ct=0
lattitude=[]
longitude=[]
distance=[]
current=(30.250574, 77.047322)
# Specify the path to your Excel file
excel_file_path = 'E:\Projects\Women Safety Trials\Police Info API\data.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Display the DataFrame
# print(df['Lattitude'][0])

for i in range(0,len(df['Lattitude'])):
    lattitude.append(df['Lattitude'][i])
for i in range(0,len(df['Longitude'])):
    longitude.append(df['Longitude'][i])

# print(lattitude)
# print(longitude)
# def minimumDistance(c_location):
#     dist = float(gd((30.381152,76.775522),c_location).km)
#     dist=round(dist,2)
#     return dist
# min=minimumDistance(current)
@app.route("/sos",methods=["GET"])
def calcDistance():
    distance=[]
    lat=request.args.get("lat")
    long=request.args.get("lon")
    c_location=(lat,long)
    for i in range(0,len(lattitude)):
        f_location=(lattitude[i],longitude[i])
        # print(f_location)l
        dist = float(gd(f_location, c_location).km)
        dist=round(dist,2)
        distance.append(dist)
        # print(dist)
    
    minimumDistance=min(distance)
    index=distance.index(minimumDistance)
    print(index)
    print(f'Nearest Police Station : {df["Police Post"][index]}')
    print(f"Officer Incharge : {df['Name of Officers'][index]}")
    print(f"Contact Number : {df['Phone No'][index]}")

    station1=df["Police Post"][index]
    incharge1=df['Name of Officers'][index]
    contact1=int(df['Phone No'][index])

    

    # print(distance)
    n_distance=distance.copy()
    n_distance.remove(minimumDistance) #finding next nearest police station
    # print(n_distance)
    # print(distance)
    n_minimumDistance=min(n_distance)
    print(n_minimumDistance)
    n_index=distance.index(n_minimumDistance)
    # print(n_index)
    print()
    print(f'Next Nearest Police Station : {df["Police Post"][n_index]}')
    print(f" Officer Incharge : {df['Name of Officers'][n_index]}")
    print(f"Contact Number : {df['Phone No'][n_index]}")
    station2=df["Police Post"][n_index]
    incharge2=df['Name of Officers'][n_index]
    contact2=int(df['Phone No'][n_index])

    return jsonify({'Nearest Station' : station1 ,"Officer Incharge": incharge1,"Contact Number":contact1

    },{'Nearest Station' : station2 ,"Officer Incharge": incharge2,"Contact Number":contact2})
app.run()
# calcDistance(current)
