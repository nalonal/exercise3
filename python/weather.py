import requests,json
from datetime import datetime
import time

from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

def getdata(namakota):
    hasil = requests.post("https://api.openweathermap.org/data/2.5/weather?q="+namakota+"&appid=d5f11f21e3d4617bc66950d463fdeb4b")
    output = hasil.json() 
    ini_hasil = {}
    #mengambil waktu sekarang
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    st = datetime.fromtimestamp(ts)
    waktu = st.isoformat(timespec='microseconds')

    #sesuaikan bagian ini
    ini_hasil['kota'] = namakota
    ini_hasil['cuaca'] = output["weather"][0]["main"]
    ini_hasil['cuaca_deskripsi'] = output["weather"][0]["description"]
    ini_hasil['temperatur'] = output['main']['temp']
    ini_hasil['temperatur_min'] = output['main']['temp_min']
    ini_hasil['temperatur_max'] = output['main']['temp_max']
    ini_hasil["waktu"] = waktu
    #end sesuaikan
    return ini_hasil

def panggilsuhu():
    daftar_kota = ["Bali","Lombok","Labuan Bajo","Medan","Bandung"]
    for kota in daftar_kota:
        update_suhu = getdata(kota)
        producer.send('laporan_cuaca', value=update_suhu)
        print(update_suhu)

while True:
    # code goes here
    panggilsuhu()
    time.sleep(1800) #ambil data setiap 30 menit

