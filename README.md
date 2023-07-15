# [Truecallerpy](https://github.com/sumithemmadi/truecallerpy)

[![PyPI - Implementation](https://img.shields.io/pypi/v/truecallerpy?style=flat-square)](https://pypi.org/project/truecallerpy)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/truecallerpy?style=flat-square)](https://pypi.org/project/truecallerpy)
[![Downloads](https://pepy.tech/badge/truecallerpy)](https://pepy.tech/project/truecallerpy)
[![PyPI - License](https://img.shields.io/pypi/l/truecallerpy?style=flat-square)](https://github.com/sumithemmadi/truecallerpy/edit/main/LICENSE.md)

TruecallerPy is a Python package that provides functionalities to interact with the Truecaller API. It allows you to perform login, OTP verification, and phone number search using Truecaller.

**Table of Contents:**

- [Truecallerpy](#truecallerpy)
  - [Requirements](#requirements)
  - [Command Line Usage](#command-line-usage)
    - [Installation](#installation)
    - [Login](#login)
    - [InstallationId](#installationid)
    - [Searching a Number](#searching-a-number)
    - [Bulk Phone Number Search with cli](#bulk-phone-number-search-with-cli)
  - [Basic Usage](#basic-usage)
    - [Login Function](#login-function)
    - [OTP Verification](#otp-verification)
    - [Phone Number Search](#phone-number-search)
    - [Bulk Phone Number Search](#bulk-phone-number-search)
  - [Contributing](#contributing)
  - [License](#license)
  - [Support](#support)

## Requirements

To use the TruecallerPy package, you need to meet the following requirements:

- Valid Mobile Number (Phone number verification for Truecaller)
- Truecaller InstallationId

## Command Line Usage

### Installation

You can install the TruecallerPy package using pip:

```bash
pip install truecallerpy
```

### Login

To log in to your Truecaller account, use the following command:

```bash
truecallerpy login
```

If you encounter any errors, try running the command with administrative privilege (e.g., `sudo truecallerpy login` on Linux or running the command prompt as administrator on Windows).

### InstallationId

To retrieve your Truecaller InstallationId, use the following command:

```bash
truecallerpy --installationid
```

You can also specify the `-i` flag to print only the InstallationId:

```bash
truecallerpy -i -r
```

### Searching a Number

To search for a phone number using Truecaller, use the following command:

```bash
truecallerpy -s [number]
```

For example:

```bash
truecallerpy -s 1234567890
```

The command will return a JSON response containing information about the phone number.

You can use the `-r` flag to get the raw output (JSON) instead of the formatted output. For example:

```bash
truecallerpy -s 1234567890 -r
```

You can also use additional flags to extract specific information. For example, to print only the name associated with the phone number, use the `--name` flag:

```bash
truecallerpy -s 1234567890 --name
```

Similarly, you can use the `--email` flag to print only the email associated with the phone number.

### Bulk Phone Number Search with cli

To perform a bulk search for multiple phone numbers, use the `--bs` flag followed by the numbers separated by commas. For example:

```bash
truecallerpy --bs 9912345678,+14051234567,+919987654321
```

In addition to the CLI, you can also use the TruecallerPy package in your Python code. The package provides various functions such as `login`, `verify_otp`, `search_phonenumber`, and `bulk_search`.

## Basic Usage

### Login Function

The `login` function is used to log in to the Truecaller service. It takes a phone number in international format as a parameter and returns a dictionary containing the login response details.

```python
from truecallerpy import login

phone_number = "+1234567890"
response = login(phone_number)
print(response)
```

The `login` function returns a dictionary with the following keys:

- `status` (int): The status code of the login request.
- `message` (str): A message indicating the status of the login request.
- `domain` (str): The domain associated with the phone number.
- `parsedPhoneNumber` (int): The phone number without the country code.
- `parsedCountryCode` (str): The country code associated with the phone number.
- `requestId` (str): The unique identifier for the login request.
- `method` (str): The method used for sending the OTP.
- `tokenTtl` (int): The time-to-live (TTL) value for the OTP token in seconds.

### OTP Verification

The `verify_otp` function is used to verify the mobile number with the OTP (One-Time Password) received.

```python
from truecallerpy import verify_otp

phone_number = "+1234567890"
json_data = {
   # JSON response from the login function
}
otp = "123456"

response = verify_otp(phone_number, json_data, otp)
print(response)
```

The `verify_otp` function returns a dictionary with the following keys:

- `status` (int): The status code of the OTP verification.
- `message` (str): A message indicating the result of the OTP verification.
- `installationId` (str): The installation ID associated with the verified number.
- `ttl` (int): The time-to-live (TTL) value for the verification result in seconds.
- `userId` (int): The user ID associated with the verified number.
- `suspended` (bool): Indicates whether the account is suspended.
- `phones` (list): List of phone numbers associated with the user, each containing `phoneNumber`, `countryCode`, and `priority` keys.

### Phone Number Search

The `search_phonenumber` function allows you to search for a phone number using the Truecaller API.

```python
from truecallerpy import search_phonenumber

phone_number = "+1234567890"
country_code = "US"
installation_id = "Your installation ID"

response = search_phonenumber(phone_number, country_code, installation_id)
print(response)
```

The `search_phonenumber` function returns a dictionary containing information about the phone number.

### Bulk Phone Number Search

The `bulk_search` function allows you to perform a bulk search for a list of phone numbers using the Truecaller API.

```python
from truecallerpy import bulk_search

phone_numbers = "+1234567890,9876543210"
country_code = "US"
installation_id = "Installation ID"

response = bulk_search(phone_numbers, country_code, installation_id)
print(response)
```

The `bulk_search` function returns a dictionary containing information about the phone numbers.

## Contributing

Contributions to the TruecallerPy package are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.

## License

This project is licensed under the MIT License.

## Support

If you need any assistance or have questions, please contact [sumithemmadi244@gmail.com](mailto:sumithemmadi244@gmail.com).

Feel free to customize the documentation template according to your package's features and requirements. Provide detailed explanations and examples for each function, along with the necessary parameters and return types.
