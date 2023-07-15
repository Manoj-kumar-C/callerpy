import phonenumbers
from phonenumbers import region_code_for_country_code
import requests

def verify_otp(phone_number, json_data, otp):
    """
    Verify the OTP (One-Time Password) for phone number verification.

    Args:
        phone_number (str): The phone number in international format.
        json_data (dict): The JSON response data from the login request containing the requestId.
        otp (str): The OTP to verify.

    Returns:
        dict: The verification response containing the result of the OTP verification.

    Raises:
        ValueError: If the phone number is invalid.
        requests.exceptions.RequestException: If an error occurs during the API request.
    """
    try:
        parsed_number = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValueError("Phone number should be in international format.")

        country_code = str(region_code_for_country_code(
            parsed_number.country_code))
        dialing_code = parsed_number.country_code
        phone_number = str(parsed_number.national_number)

        post_data = {
            "countryCode": country_code,
            "dialingCode": dialing_code,
            "phoneNumber": phone_number,
            "requestId": json_data["requestId"],
            "token": otp,
        }

        headers = {
            "content-type": "application/json; charset=UTF-8",
            "accept-encoding": "gzip",
            "user-agent": "Truecaller/11.75.5 (Android;10)",
            "clientsecret": "lvc22mp3l1sfv6ujg83rd17btt",
        }

        url = "https://account-asia-south1.truecaller.com/v1/verifyOnboardingOtp"

        response = requests.post(url, json=post_data, headers=headers)
        return response.json()

    except phonenumbers.phonenumberutil.NumberParseException:
        raise ValueError("Invalid phone number.")
