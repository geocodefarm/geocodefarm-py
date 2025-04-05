import urllib.parse
import urllib.request
import json


class GeocodeFarmClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.user_agent = "GeocodeFarmSDK-Py/4.0"

    def forward(self, address: str) -> dict:
        url = "https://api.geocode.farm/forward/"
        params = {"key": self.api_key, "addr": address}
        response = self._make_request(url, params)
        return self._handle_response(response, "forward")

    def reverse(self, lat: float, lon: float) -> dict:
        url = "https://api.geocode.farm/reverse/"
        params = {"key": self.api_key, "lat": lat, "lon": lon}
        response = self._make_request(url, params)
        return self._handle_response(response, "reverse")

    def _make_request(self, url: str, params: dict) -> dict:
        full_url = f"{url}?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(full_url, headers={"User-Agent": self.user_agent})

        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                http_status = response.getcode()
                data = json.loads(response.read().decode())
                return {"http_status": http_status, "data": data}
        except Exception as e:
            return {"http_status": 0, "error": str(e)}

    def _handle_response(self, response: dict, query_type: str) -> dict:
        if "data" not in response or not isinstance(response["data"], dict):
            return {
                "success": False,
                "status_code": response.get("http_status", 0),
                "error": response.get("error", "Invalid response from server")
            }

        data = response["data"]
        status = data.get("STATUS", {}).get("status", "FAILED")
        if status != "SUCCESS":
            return {
                "success": False,
                "status_code": response["http_status"],
                "error": f"API returned failure: {status}"
            }

        result = {}
        if query_type == "reverse":
            result_data = data.get("RESULTS", {}).get("result", [{}])[0]
            result = {
                "house_number": result_data.get("house_number"),
                "street_name": result_data.get("street_name"),
                "locality": result_data.get("locality"),
                "admin_2": result_data.get("admin_2"),
                "admin_1": result_data.get("admin_1"),
                "country": result_data.get("country"),
                "postal_code": result_data.get("postal_code"),
                "formatted_address": result_data.get("formatted_address"),
                "latitude": result_data.get("latitude"),
                "longitude": result_data.get("longitude"),
                "accuracy": data.get("RESULTS", {}).get("result", {}).get("accuracy"),
            }
        else:
            result_data = data.get("RESULTS", {}).get("result", {})
            coords = result_data.get("coordinates", {})
            address = result_data.get("address", {})
            result = {
                "house_number": address.get("house_number"),
                "street_name": address.get("street_name"),
                "locality": address.get("locality"),
                "admin_2": address.get("admin_2"),
                "admin_1": address.get("admin_1"),
                "country": address.get("country"),
                "postal_code": address.get("postal_code"),
                "formatted_address": address.get("full_address"),
                "latitude": coords.get("lat"),
                "longitude": coords.get("lon"),
                "accuracy": result_data.get("accuracy"),
            }

        return {
            "success": True,
            "status_code": response["http_status"],
            "lat": result["latitude"],
            "lon": result["longitude"],
            "accuracy": result["accuracy"],
            "full_address": result["formatted_address"],
            "result": result
        }
