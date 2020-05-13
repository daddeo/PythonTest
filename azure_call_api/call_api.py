# This code will show you how to call the Computer Vision API from Python
# You can find documentation on the Computer Vision Analyze Image method here
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa
#
#
# Urls:
# Microsoft Docs (Python)
# https://docs.microsoft.com/en-us/?view=azure-python
# Computer Vision API - v2.1
# https://westus.dev.cognitive.microsoft.com/docs/services/5cd27ec07268f6c679a3e641/operations/56f91f2e778daf14a499f21b
# GitHub stuffs
# https://github.com/microsoft/c9-python-getting-started/tree/master/python-for-beginners/16%20-%20Calling%20APIs
#


# Use the requests library to simplify making a REST API call from Python
import requests

# We will need the json library to read the data passed back
# by the web service
import json

# You need to update the SUBSCRIPTION_KEY to
# they key for your Computer Vision Service
# SUBSCRIPTION_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
SUBSCRIPTION_KEY = "cf229a23c3054905b5a8ad512edfa9dd"

# You need to update the vision_service_address to the address of
# your Computer Vision Service
vision_service_address = (
    "https://canadacentral.api.cognitive.microsoft.com/vision/v2.1/"
)
# better server option, but the instructor used the canada server, so would nned a new
# Azure subscription key for the central US server
# "https://centralus.api.cognitive.microsoft.com/vision/v2.1/"

# Add the name of the function you want to call to the address
address = vision_service_address + "analyze"

# According to the documentation for the analyze image function
# There are three optional parameters: language, details & visualFeatures
parameters = {"visualFeatures": "Description,Color", "language": "en"}

# Open the image file to get a file object containing the image to analyze
# image_path = "./azure_call_api/TestImages/PolarBear.jpg"
image_path = "./azure_call_api/TestImages/Parliament_Hill.jpg"
image_data = open(image_path, "rb").read()

# According to the documentation for the analyze image function
# we need to specify the subscription key and the content type
# in the HTTP header. Content-Type is application/octet-stream when you pass in a image directly
headers = {
    "Content-Type": "application/octet-stream",
    "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
}

# According to the documentation for the analyze image function
# we use HTTP POST to call this function
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))

"""
json output (PolarBear.jpg):
{
    "color": {
        "dominantColorForeground": "White",
        "dominantColorBackground": "White",
        "dominantColors": ["White"],
        "accentColor": "595144",
        "isBwImg": false,
        "isBWImg": false
    },
    "description": {
        "tags": ["bear", "polar", "animal", "mammal", "outdoor", "water", "white", "large", "walking", "snow", "standing"],
        "captions": [{
            "text": "a large white polar bear walking in the water",
            "confidence": 0.7419735115689349
        }]
    },
    "requestId": "5389a9ec-6d46-4670-9b0e-b1412f5778b2",
    "metadata": {
        "width": 220,
        "height": 221,
        "format": "Jpeg"
    }
}

json output (Parliment_Hill.jpg)
{
    "color": {
        "dominantColorForeground": "Grey",
        "dominantColorBackground": "Black",
        "dominantColors": ["Black"],
        "accentColor": "0361C8",
        "isBwImg": false,
        "isBWImg": false
    },
    "description": {
        "tags": [
            "outdoor", "building", "large", "clock", "old", "city", "big", "front", "green", "background",
            "water", "view", "church", "river", "tower", "castle", "tall", "surrounded", "hill", "horse",
            "field", "grassy", "boat", "standing"
        ],
        "captions": [{
            "text": "a large clock tower towering over Parliament Hill",
            "confidence": 0.7462234997464777
        }]
    },
    "requestId": "0648890a-b371-45f8-838f-203951cfcc12",
    "metadata": {"width": 1024, "height": 768, "format": "Jpeg"}
}
"""

print("requestId: " + results["requestId"])

# first tag: outdoor
print("first tag: " + results["description"]["tags"][0])
print("all tags:")
# outdoor
# building
# large
# clock
# old
# city
# big
# front
# green
# background
# water
# view
# church
# river
# tower
# castle
# tall
# surrounded
# hill
# horse
# field
# grassy
# boat
# standing
for item in results["description"]["tags"]:
    print(item)

print("caption text")
# a large clock tower towering over Parliament Hill
print(results["description"]["captions"][0]["text"])
