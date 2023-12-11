import pandas as pd
from geopy.distance import geodesic as gd

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
def calcDistance(c_location):
    for i in range(0,len(lattitude)):
        f_location=(lattitude[i],longitude[i])
        # print(f_location)
        dist = float(gd(f_location, c_location).km)
        dist=round(dist,2)
        distance.append(dist)
        # print(dist)
calcDistance(current)
minimumDistance=min(distance)
index=distance.index(minimumDistance)
print(index)
print(f'Nearest Police Station : {df["Police Post"][index]}')
print(f"Officer Incharge : {df['Name of Officers'][index]}")
print(f"Contact Number : {df['Phone No'][index]}")
print(distance)
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
