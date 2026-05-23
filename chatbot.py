import json


def load_faq():
    """
    Membaca data FAQ dari file JSON.
    """
    with open("data/faq.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


# Memuat data FAQ dari JSON
faq_data = load_faq()


def preprocess(text):
    """
    Mengubah teks menjadi huruf kecil agar pencarian
    keyword tidak sensitif terhadap huruf besar/kecil.
    """
    return text.lower()


def get_bot_response(user_input):
    """
    Mencari jawaban berdasarkan keyword
    yang terdapat dalam input pengguna.
    """
    text = preprocess(user_input)

    for item in faq_data:
        for keyword in item["keywords"]:
            if keyword.lower() in text:
                return item["response"]

    return fallback_response()


def fallback_response():
    """
    Jawaban default jika pertanyaan tidak ditemukan.
    """
    return (
        "Maaf, saya belum memahami pertanyaan Anda.\n\n"
        "Silakan tanyakan tentang:\n"
        "- KRS\n"
        "- UKT\n"
        "- Skripsi\n"
        "- Akademik\n"
        "- Cuti Kuliah"
    )