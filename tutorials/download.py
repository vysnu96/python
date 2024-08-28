import requests
import shutil
def download_image():
    try:
        BASE_URL = "https://openweathermap.org/img/wn/"
        path = r"C:\Users\vishnuvardhan.j.DC\Documents\python\tutorials\Telegram\images"
        num_list = ['01','02','03','04','05','06','07','08','09','10','11','13','50']
        for i in num_list:
            response = requests.get(f"{BASE_URL}{i}n@2x.png", stream=True)
            # response.raise_for_status()
            with open(f"{i}n", 'wb') as out_file:
                # Copy the response stream to the file
                shutil.copyfileobj(response.raw, out_file)
            print(f"Image successfully downloaded")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the image: {e}")

download_image()