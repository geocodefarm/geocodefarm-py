# GeocodeFarm Python Client

A lightweight, dependency-free Python client for the [Geocode.Farm](https://www.geocode.farm/) API (v4).  
Supports both forward and reverse geocoding with simple, structured results.

> ⚡ No third-party dependencies  
> 🌍 Supports Geocode.Farm v4  
> 🧵 Easy to use and extend

---

## 🔧 Installation

```bash
pip install geocodefarm
```

Or clone from GitHub:

```bash
git clone https://github.com/geocodefarm/geocodefarm-py.git
cd geocodefarm-py
pip install .
```

---

## 🗺️ Usage

```python
from geocodefarm import GeocodeFarmClient

client = GeocodeFarmClient("your_api_key_here")

# Forward geocoding (address -> lat/lon)
result = client.forward("1600 Amphitheatre Parkway, Mountain View, CA")
print(result)

# Reverse geocoding (lat/lon -> address)
reverse = client.reverse(37.4221, -122.0841)
print(reverse)
```

---

## 📦 Response Format

All responses are normalized into this format:

```python
{
    "success": True,
    "status_code": 200,
    "lat": 37.4221,
    "lon": -122.0841,
    "accuracy": "ROOFTOP",
    "full_address": "1600 Amphitheatre Parkway, Mountain View, CA 94043, USA",
    "result": {
        "house_number": "1600",
        "street_name": "Amphitheatre Parkway",
        "locality": "Mountain View",
        "admin_2": "Santa Clara County",
        "admin_1": "California",
        "country": "United States",
        "postal_code": "94043",
        "formatted_address": "...",
        "latitude": ...,
        "longitude": ...
    }
}
```

If the request fails, `success` will be `False`, and an `error` message will be included.

---

## 🛠️ Requirements

- Python 3.7+
- No external dependencies

---

## 🪪 License

This project is released under [The Unlicense](https://unlicense.org) — public domain dedication.

---

## 🌐 Links

- [Geocode.Farm API Documentation](https://www.geocode.farm/our-apis/)
- [GitHub Repository](https://github.com/geocodefarm/geocodefarm-py)
- [PyPI Package](https://pypi.org/project/geocodefarm/)

---

## 🤝 Contributing

Pull requests are welcome. If you find bugs or want to improve the client, feel free to open an issue or PR.
