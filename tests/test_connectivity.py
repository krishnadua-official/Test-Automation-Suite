import pytest 
import sys
import os

from utils.network_utils import NetworkUtils
from utils.wifi_control import WifiControl

class Test_connectivity:

    def test_ping_router(self, router_config, test_results):
        router_ip = router_config["router_ip"]
        result = NetworkUtils.ping_host(router_ip, count=4)
        assert result, f"Router at {router_ip} is not reachable."
        test_results["ping_router"] = result

    def test_ping_internet(self, test_results):
        result = NetworkUtils.ping_internet(count=4)
        assert result, "Internet is not reachable."
        test_results["ping_internet"] = result

    def test_dns_resolution(self, test_results):
        domain = "google.com"
        result = NetworkUtils.dns_resolution(domain)
        assert result, f"DNS resolution failed for {domain}."
        test_results["dns_resolution"] = result

    def test_reconnect_wifi(self, router_config, test_results):
        ssid = router_config["ssid"]
        password = router_config["password"]
        result = WifiControl.reconnect_wifi(ssid, password)
        assert result, f"Failed to reconnect to WiFi SSID: {ssid}."
        test_results["reconnect_wifi"] = result
