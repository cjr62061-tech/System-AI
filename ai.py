# BHAI KA IMAGE AI - GITHUB WALA VERSION
# Tu Kuch Bhi Bolega, Ye Photo Bana Dega

import urllib.request

print("=== BHAI KA IMAGE AI - GITHUB SE CHAL RAHA HAI ===")

prompt = input("Bhai, Kaisi Photo Chahiye? Likh : ")
prompt_url = prompt.replace(" ", "%20")

url = f"https://image.pollinations.ai/prompt/{prompt_url}"
file_name = f"{prompt.replace(' ', '_')}_Bhai_Photo.jpg"

print(f"\nBhai, '{prompt}' Ki Photo Ban Rahi Hai... Ruk Ja...")

try:
    urllib.request.urlretrieve(url, file_name)
    print(f"\nHo Gaya Bhai! Photo Ban Gayi - {file_name}")
    print("Gallery Me Ja Ke Dekh!")
except Exception as e:
    print(f"\nError Aa Gaya Bhai - {e}")

print("\n=== BHAI KA AI - GITHUB ZINDABAD ===")