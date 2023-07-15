import requests
from phonenumbers import parse

def search_phonenumber(phoneNumber, countryCode, installationId):
    """
    Search for a phone number using Truecaller API.

    Args:
        phoneNumber (str): The phone number to search.
        countryCode (str): The country code of the phone number.
        installationId (str): The installation ID for authorization.

    Returns:
        dict: The search result containing information about the phone number.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the API request.
    """
    phone_number = parse(str(phoneNumber), str(countryCode))
    significant_number = phone_number.national_number

    headers = {
        "content-type": "application/json; charset=UTF-8",
        "accept-encoding": "gzip",
        "user-agent": "Truecaller/11.75.5 (Android;10)",
        "Authorization": f"Bearer {installationId}"
    }
    params = {
        "q": str(significant_number),
        "countryCode": phone_number.country_code,
        "type": 4,
        "locAddr": "",
        "placement": "SEARCHRESULTS,HISTORY,DETAILS",
        "encoding": "json"
    }
    response = requests.get(
        "https://search5-noneu.truecaller.com/v2/search", params=params, headers=headers)

    response_data = response.json()
    return response_data


def bulk_search(phoneNumbers, countryCode, installationId):
    """
    Perform bulk search for a list of phone numbers using Truecaller API.

    Args:
        phoneNumbers (list[str]): The list of phone numbers to search.
        countryCode (str): The country code of the phone numbers.
        installationId (str): The installation ID for authorization.

    Returns:
        dict: The bulk search result containing information about the phone numbers.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the API request.
    """
    headers = {
        "content-type": "application/json; charset=UTF-8",
        "accept-encoding": "gzip",
        "user-agent": "Truecaller/11.75.5 (Android;10)",
        "Authorization": f"Bearer {installationId}"
    }
    params = {
        "q": phoneNumbers,
        "countryCode": countryCode,
        "type": 14,
        "placement": "SEARCHRESULTS,HISTORY,DETAILS",
        "encoding": "json"
    }
    response = requests.get(
        "https://search5-noneu.truecaller.com/v2/bulk", params=params, headers=headers)

    response_data = response.json()
    return response_data
