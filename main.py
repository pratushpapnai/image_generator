from together import Together
import requests
from PIL import Image
from io import BytesIO

key=#"get your api key from Together"
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
