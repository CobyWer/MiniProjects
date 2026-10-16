import requests
apiKey = 'b8375e0464ab049f6b329bc8ed3f1bbe'

selectedIP = input("Enter the IP address to track (Leave empty if you would like to use your own): ")



def CoordinatesToMaps(latitude, longitude):
    link = f"https://www.google.com/maps/@{latitude},{longitude},1583m/"
    return link

# 1. Define the API endpoint URL
if selectedIP:
    url = f"https://api.apilayer.net/ipstack/{selectedIP}?access_key={apiKey}"
else:
    selectedIP = requests.get('https://api.ipify.org').text
    url = f"https://api.apilayer.net/ipstack/{selectedIP}?access_key={apiKey}"

try:
    # 2. Send the HTTP GET request
    response = requests.get(url)
    
    # 4. Parse the JSON response into a Python dictionary
    ip_data = response.json()
    
    print(f"IP Address: {ip_data['ip']}")
    print(f"Country:      {ip_data['country_name']}")
    print(f"City:      {ip_data['region_code']}, {ip_data['city']}")

    print("\nUse this link to see where you are located!")
    print(CoordinatesToMaps(ip_data['latitude'], ip_data['longitude']))

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")

    



