
from pathlib import Path
from datetime import datetime


def simpan_laporan(isi):
    folder_output = Path(__file__).resolve().parent.parent / "output"
    folder_output.mkdir(parents=True, exist_ok=True)

    file_laporan = folder_output / "riwayat.txt"

    with file_laporan.open("a", encoding="utf-8") as file:
        waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        file.write(f"[{waktu}]\n{isi}\n\n")
