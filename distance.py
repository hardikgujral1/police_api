from geopy.distance import geodesic as gd

Mullana =(30.274759, 77.048956)
Current =(30.250215, 77.048088)

Barara=(30.213386, 77.038901)
dist1 = float(gd(Mullana,Current).km)
dist2 = float(gd(Barara,Current).km)
print(f'The distance is : {(round(dist1,2))} KM ')
print(f'The distance is : {(round(dist2,2))} KM ')

print(f'Minimal Distance is :')
minimal_distance = dist1 if dist1 <= dist2 else dist2
print(minimal_distance)