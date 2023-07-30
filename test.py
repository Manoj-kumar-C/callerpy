from truecallerpy import search_phonenumber

id = 'a1i0P--gvUnRik2--BO4tOu1rSgbaByh5AeFiPbxHr-0pfASgp5Esh1Le6trWeV7'

phone_number = '9384073312'

res = (search_phonenumber(phone_number,'IN',id))

data = res["data"][0]

print(data['name'])