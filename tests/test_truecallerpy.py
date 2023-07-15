import pytest
from truecallerpy import login, verify_otp, search, bulk_search

# Test login function
def test_login():
    phone_number = "+919912345678"
    response = login(phone_number)
    assert "status" in response

# Test verify_otp function
def test_verify_otp():
    phone_number = "+919912345678"
    response = login(phone_number)
    otp = "123456"
    response = verify_otp(phone_number, response, otp)
    assert "message" in response

# # Test search function
def test_search():
    phone_number = "+1234567890"
    country_code = "US"
    installation_id = ""
    response = search(phone_number, country_code, installation_id)
    assert "data" in response

# # Test bulk_search function
def test_bulk_search():
    phone_numbers = "+1234567890,+9876543210"
    country_code = "US"
    installation_id = "1234567890"
    response = bulk_search(phone_numbers, country_code, installation_id)
    assert "data" in response

