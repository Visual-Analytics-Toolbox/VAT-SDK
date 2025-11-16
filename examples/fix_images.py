from vaapi.client import Vaapi
import os

if __name__ == "__main__":
    client = Vaapi(
        base_url=os.environ.get("VAT_API_URL"),
        api_key=os.environ.get("VAT_API_TOKEN"),
    )

    img_generator = client.image.list(limit=100)
    print(img_generator.count)

    for i, img in enumerate(img_generator):
        #print(img.image_url)
        new_url = img.image_url.replace("_BerlinUnited_", "_Berlin United_")
        new_url = new_url.replace("_SPQR_", "_SPQR Team_")
        print(new_url)
        client.image.update(id=img.id, image_url=new_url)
