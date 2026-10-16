import requests
apiKey = 'b8375e0464ab049f6b329bc8ed3f1bbe'

selectedIP = input("Enter the IP address to track (Leave empty if you would like to use your own): ")

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
    
    # 5. Use the data
    print(f"Request Successful! (Status Code: {response.status_code})")
    print(f"IP Address: {ip_data['ip']}")
    print(f"Country:      {ip_data['country_name']}")
    print(f"City:      {ip_data['region_code']}, {ip_data['city']}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")
