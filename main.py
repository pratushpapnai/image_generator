from together import Together
import requests
from PIL import Image
from io import BytesIO

key="5c66bc142dba84175f515250b853e5ad5bb77b69f6b65024984557319a73b9b3"
client = Together(api_key=key)

def image(prompt):
    response = client.images.generate(
    prompt=prompt,
    model="black-forest-labs/FLUX.1-dev",
    steps=10,
    n=4)
    img_url=response.data[0].url
    r=requests.get(img_url)
    img=Image.open(BytesIO(r.content))
    img.show()

user=input("Enter Prompt\n")   

image(user)
