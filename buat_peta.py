import csv
from pathlib import Path
import folium

ROOT = Path(__file__).resolve().parents[1]
FILE_DATA = ROOT / "data" / "fasilitas_bengkulu.csv"
FOLDER_OUTPUT = ROOT / "outputs"
FOLDER_OUTPUT.mkdir(exist_ok=True)

WARNA = {
    "Pendidikan": "blue",
    "Kesehatan": "red",
    "Ruang Publik": "green",
    "Transportasi": "orange",
}


def main():
    with FILE_DATA.open(newline="", encoding="utf-8") as file:
        fasilitas = list(csv.DictReader(file))

    peta = folium.Map(location=[-3.80, 102.265], zoom_start=12)

    for item in fasilitas:
        try:
            lat = float(item["latitude"])
            lon = float(item["longitude"])
        except (ValueError, KeyError):
            print("Koordinat tidak valid, baris dilewati:", item)
            continue

        jenis = item["jenis"]
        folium.Marker(
            location=[lat, lon],
            tooltip=item["nama"],
            popup=f"<b>{item['nama']}</b><br>Jenis: {jenis}<br>Alamat: {item['alamat']}",
            icon=folium.Icon(color=WARNA.get(jenis, "gray"))
        ).add_to(peta)

    output = FOLDER_OUTPUT / "peta_fasilitas.html"
    peta.save(str(output))
    print(f"Jumlah fasilitas dibaca: {len(fasilitas)}")
    print(f"Peta tersimpan di: {output}")
    print("Koordinat contoh harus diverifikasi sebelum digunakan untuk kebutuhan nyata.")


if __name__ == "__main__":
    main()
