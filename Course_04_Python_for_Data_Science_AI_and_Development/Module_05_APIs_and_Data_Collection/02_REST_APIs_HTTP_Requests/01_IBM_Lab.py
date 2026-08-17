"""
IBM DAPC - Course 04
Module 05 - APIs and Data Collection

Lab 02 - REST APIs and HTTP Requests

Purpose:
Practice HTTP GET and POST requests, URL parameters,
JSON responses, request/response information,
error handling, and file downloads.
"""

import requests

# =========================================================
# 1. Basic GET Request
# =========================================================

url = "https://www.ibm.com/"

response = requests.get(url, timeout=10)

print("Status Code:")
print(response.status_code)

print("\nRequest URL:")
print(response.url)

print("\nResponse Headers:")
print("Content-Type:", response.headers.get("Content-Type"))
print("Content-Encoding:", response.headers.get("Content-Encoding"))
print("Date:", response.headers.get("Date"))

print("\nEncoding:")
print(response.encoding)

print("\nFirst 100 Characters:")
print(response.text[:100])


# =========================================================
# 2. Request Headers
# =========================================================

print("\nRequest Headers:")
print("User-Agent:", response.request.headers.get("User-Agent"))
print("Accept:", response.request.headers.get("Accept"))


# =========================================================
# 3. Request Body
# =========================================================

print("\nRequest Body:")
print(response.request.body)


# =========================================================
# 4. Status Code Check
# =========================================================

if response.status_code == 200:
    print("\nRequest successful.")
else:
    print("\nRequest failed.")


# =========================================================
# 5. GET Request with URL Parameters
# =========================================================

url = "https://httpbin.org/get"

payload = {"name": "Varghese", "ID": "123"}

try:
    get_response = requests.get(url, params=payload, timeout=10)

    print("\nGenerated URL:")
    print(get_response.url)

    print("\nStatus Code:")
    print(get_response.status_code)

    if get_response.ok:

        get_data = get_response.json()

        print("\nResponse:")
        print(get_data)

        print("\nJSON Data Type:")
        print(type(get_data))

        print("\nArguments:")
        print(get_data["args"])

    else:

        print("\nRequest failed.")

        print("Status:", get_response.status_code)

        print("Content-Type:", get_response.headers.get("Content-Type"))

        print("Response:", get_response.text[:200] or "<empty response>")


except requests.exceptions.Timeout:

    print("\nRequest timed out.")
    print("The server did not respond within 10 seconds.")


except requests.exceptions.RequestException as error:

    print("\nRequest failed:")
    print(error)


# =========================================================
# 6. POST Request
# =========================================================

url_post = "https://httpbin.org/post"

post_payload = {"name": "Varghese", "ID": "123"}

try:

    post_response = requests.post(url_post, data=post_payload, timeout=10)

    print("\nPOST Status Code:")
    print(post_response.status_code)

    if post_response.ok:

        post_data = post_response.json()

        print("\nPOST Response:")
        print(post_data)

        print("\nPOST Request Body:")
        print(post_response.request.body)

        print("\nPOST Form Data:")
        print(post_data["form"])

    else:

        print("\nPOST Request Failed.")

        print("Status:", post_response.status_code)

        print("Response:", post_response.text[:200] or "<empty response>")


except requests.exceptions.Timeout:

    print("\nPOST request timed out.")


except requests.exceptions.RequestException as error:

    print("\nPOST request failed:")
    print(error)


# =========================================================
# 7. Download a File
# =========================================================

file_url = "https://httpbin.org/image/png"

try:

    file_response = requests.get(file_url, timeout=30)

    print("\nFile Download Status:")
    print(file_response.status_code)

    file_response.raise_for_status()

    with open("httpbin_image.png", "wb") as file:
        file.write(file_response.content)

    print("File downloaded successfully.")
    print("Saved as: httpbin_image.png")


except requests.exceptions.Timeout:

    print("\nFile download timed out.")


except requests.exceptions.RequestException as error:

    print("\nFile download failed:")
    print(error)
