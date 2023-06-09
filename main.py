import folium
from folium.plugins import Search

# Create a map centered on India
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Define the cities and their coordinates
cities = {
    'Mumbai, Maharashtra': [19.0760, 72.8777],
    'Delhi, Delhi': [28.7041, 77.1025],
    'Bengaluru, Karnataka': [12.9716, 77.5946],
    'Kolkata, West Bengal': [22.5726, 88.3639],
    'Chennai, Tamil Nadu': [13.0827, 80.2707],
    'Hyderabad, Telangana': [17.3850, 78.4867],
    'Ahmedabad, Gujarat': [23.0225, 72.5714],
    'Pune, Maharashtra': [18.5204, 73.8567],
    'Surat, Gujarat': [21.1702, 72.8311],
    'Jaipur, Rajasthan': [26.9124, 75.7873],
    'Lucknow, Uttar Pradesh': [26.8467, 80.9462],
    'Kanpur, Uttar Pradesh': [26.4499, 80.3319],
    'Nagpur, Maharashtra': [21.1458, 79.0882],
    'Indore, Madhya Pradesh': [22.7196, 75.8577],
    'Thane, Maharashtra': [19.2183, 72.9781],
    'Bhopal, Madhya Pradesh': [23.2599, 77.4126],
    'Patna, Bihar': [25.5941, 85.1376],
    'Vadodara, Gujarat': [22.3072, 73.1812],
    'Ghaziabad, Uttar Pradesh': [28.6692, 77.4538],
    'Ludhiana, Punjab': [30.9010, 75.8573],
    'Agra, Uttar Pradesh': [27.1767, 78.0081],
    'Nashik, Maharashtra': [20.0110, 73.7903],
    'Faridabad, Haryana': [28.4089, 77.3178],
    'Meerut, Uttar Pradesh': [28.9845, 77.7064],
    'Rajkot, Gujarat': [22.3039, 70.8022],
    'Varanasi, Uttar Pradesh': [25.3176, 82.9739],
    'Srinagar, Jammu and Kashmir': [34.0836, 74.7973],
    'Aurangabad, Maharashtra': [19.8762, 75.3433],
    'Dhanbad, Jharkhand': [23.7957, 86.4304],
    'Amritsar, Punjab': [31.6340, 74.8723],
    'Allahabad, Uttar Pradesh': [25.4358, 81.8463],
    'Ranchi, Jharkhand': [23.3441, 85.3096],
    'Howrah, West Bengal': [22.5958, 88.2636],
    'Coimbatore, Tamil Nadu': [11.0168, 76.9558],
    'Vijayawada, Andhra Pradesh': [16.5062, 80.6480],
    'Chandigarh, Chandigarh': [30.7333, 76.7794],
    'Mysore, Karnataka': [12.2958, 76.6394],
    'Jodhpur, Rajasthan': [26.2389, 73.0243],
    'Guwahati, Assam': [26.1445, 91.7362],
    'Navi Mumbai, Maharashtra': [19.0330, 73.0297],
    'Gwalior, Madhya Pradesh': [26.2183, 78.1828],
    'Bareilly, Uttar Pradesh': [28.3670, 79.4304],
    'Moradabad, Uttar Pradesh': [28.8389, 78.7768],
    'Bhubaneswar, Odisha': [20.2961, 85.8245],
    'Jamshedpur, Jharkhand': [22.8046, 86.2029],
    'Aligarh, Uttar Pradesh': [27.8974, 78.0880],
    'Kochi, Kerala': [9.9312, 76.2673],
    'Cuttack, Odisha': [20.4625, 85.8830],
    'Ajmer, Rajasthan': [26.4499, 74.6399],
    'Kolhapur, Maharashtra': [16.7049, 74.2433]
}

# Define the villages and their coordinates
villages = {
    'Dharnai, Bihar': [25.0456, 85.0573],
    'Mawlynnong, Meghalaya': [25.1867, 91.7476],
    'Hiware Bazar, Maharashtra': [19.3825, 74.1240],
    'Punsari, Gujarat': [22.9385, 73.3520],
    'Shani Shingnapur, Maharashtra': [19.7682, 74.4774],
    'Shergaon, Arunachal Pradesh': [27.0297, 92.3316],
    'Chappar, Rajasthan': [27.0099, 75.9235],
    'Malana, Himachal Pradesh': [32.0856, 77.3142],
    'Kodinhi, Kerala': [11.8794, 75.6894],
    'Madhapur, Telangana': [17.4467, 78.3756],
    'Lachen, Sikkim': [27.7477, 88.6909],
    'Mana, Uttarakhand': [30.8779, 79.6006],
    'Mandawa, Rajasthan': [28.0667, 75.1500],
    'Chiktan, Jammu and Kashmir': [34.2602, 76.2025],
    'Darang, Himachal Pradesh': [32.1466, 76.4525],
    'Hemis, Jammu and Kashmir': [33.9046, 77.8107],
    'Nubra, Jammu and Kashmir': [34.5115, 77.6250],
    'Hunsur, Karnataka': [12.2979, 76.2880],
    'Dholavira, Gujarat': [23.8859, 70.1793],
    'Dhanushkodi, Tamil Nadu': [9.1550, 79.4133],
    'Cherrapunji, Meghalaya': [25.3000, 91.7167],
    'Khonoma, Nagaland': [25.7180, 94.8310],
    'Sualkuchi, Assam': [26.1606, 91.6112],
    'Khirsu, Uttarakhand': [30.4629, 78.7827],
    'Valparai, Tamil Nadu': [10.3280, 76.9510],
    'Nongstoin, Meghalaya': [25.5170, 91.2661],
    'Ziro, Arunachal Pradesh': [27.5845, 93.8287],
    'Majuli, Assam': [26.9959, 94.2222],
    'Mawphlang, Meghalaya': [25.6617, 91.9367],
    'Mirik, West Bengal': [26.8925, 88.1825],
    'Pelling, Sikkim': [27.3233, 88.2646],
    'Ravangla, Sikkim': [27.3229, 88.3644],
    'Kibber, Himachal Pradesh': [32.3600, 78.0040],
    'Malom, Manipur': [24.7693, 93.8959]
}

# Create a feature group for cities
city_group = folium.FeatureGroup(name='Cities')

# Add markers for cities
for city, location in cities.items():
    folium.Marker(location=location, popup=city, icon=folium.Icon(color='blue')).add_to(city_group)

# Create a feature group for villages
village_group = folium.FeatureGroup(name='Villages')

# Add markers for villages
for village, location in villages.items():
    folium.Marker(location=location, popup=village, icon=folium.Icon(color='green')).add_to(village_group)

# Add the feature groups to the map
city_group.add_to(india_map)
village_group.add_to(india_map)

# Add search functionality
search = Search(layer=city_group, geom_type='Point', placeholder='Search for cities', collapsed=False, search_zoom=10)
india_map.add_child(search)

# Add search functionality for villages
village_search = Search(layer=village_group, geom_type='Point', placeholder='Search for villages', collapsed=False, search_zoom=10)
india_map.add_child(village_search)

# Add layer control
folium.LayerControl().add_to(india_map)

# Save the map as an HTML file
india_map.save('india_map.html')

