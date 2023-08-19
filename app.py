import requests
from bs4 import BeautifulSoup

def find_credentials(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        
        soup = BeautifulSoup(response.text, 'html.parser')
        credentials = {}

        # Find the merchant ID
        merchant_id = soup.find('input', {'name': 'merchant_id'})
        if merchant_id:
            credentials['merchant_id'] = merchant_id.get('value')

        # Find the secret key
        secret_key = soup.find('input', {'name': 'secret_key'})
        if secret_key:
            credentials['secret_key'] = secret_key.get('value')

        return credentials
    
    except requests.exceptions.RequestException as e:
        print("Error making the HTTP request:", e)
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def main():
    url = input("Enter the URL: ")
    
    if not url.startswith('http'):
        url = 'http://' + url  # Add 'http://' if missing
    
    credentials = find_credentials(url)

    if credentials:
        print("\nAPI Credentials:")
        print("Merchant ID:", credentials.get('merchant_id'))
        print("Secret Key:", credentials.get('secret_key'))
    else:
        print("\nUnable to retrieve API credentials.")

if __name__ == "__main__":
    main()
