from flask import Flask, jsonify
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor, as_completed

app = Flask(__name__)

# Kategori saham beserta nama perusahaan yang benar
CATEGORIES = {
    "LQ45": [
        ("BBCA.JK", "Bank Central Asia"),
        ("BBRI.JK", "Bank Rakyat Indonesia"),
        ("BMRI.JK", "Bank Mandiri"),
        ("TLKM.JK", "Telkom Indonesia"),
        ("ASII.JK", "Astra International"),
    ],
    "BANK": [
        ("BBCA.JK", "Bank Central Asia"),
        ("BBRI.JK", "Bank Rakyat Indonesia"),
        ("BMRI.JK", "Bank Mandiri"),
        ("BBNI.JK", "Bank Negara Indonesia"),
        ("ARTO.JK", "Bank Jago"),
    ],
    "TECH": [
        ("GOTO.JK", "GoTo Gojek Tokopedia"),
        ("BUKA.JK", "Bukalapak"),
        ("EMTK.JK", "Elang Mahkota Teknologi"),
        ("BELI.JK", "Beli Beli"),
        ("WIRG.JK", "Wir Asia"),
    ],
}

def fetch_stock(sym, company_name):
    """Ambil data satu saham. Dipanggil secara paralel."""
    try:
        ticker = yf.Ticker(sym)
        info = ticker.fast_info

        current_price = info.last_price or 0
        prev_close = info.previous_close or 0

        change_pct = 0
        if prev_close > 0:
            change_pct = ((current_price - prev_close) / prev_close) * 100

        return {
            "symbol": sym.replace(".JK", ""),
            "companyName": company_name,
            "currentPrice": round(current_price, 2),
            "changePercent": round(change_pct, 2),
        }
    except Exception as e:
        print(f"Error fetching {sym}: {e}")
        return {
            "symbol": sym.replace(".JK", ""),
            "companyName": company_name,
            "currentPrice": 0,
            "changePercent": 0,
        }

@app.route('/api/finance/<category>')
def get_finance_data(category):
    category_key = category.upper()
    stocks = CATEGORIES.get(category_key)

    if not stocks:
        return jsonify({"error": "Kategori tidak ditemukan"}), 404

    result = []
    # Ambil semua data saham secara PARALEL menggunakan ThreadPool
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_stock, sym, name): sym for sym, name in stocks}
        for future in as_completed(futures):
            data = future.result()
            if data:
                result.append(data)

    # Urutkan sesuai urutan asli
    original_order = [sym.replace(".JK", "") for sym, _ in stocks]
    result.sort(key=lambda x: original_order.index(x["symbol"]) if x["symbol"] in original_order else 99)

    return jsonify(result)

if __name__ == '__main__':
    # Python service berjalan di port 5050
    app.run(port=5050, debug=False)