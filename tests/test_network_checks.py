import json
import pytest
from src.network_checks import ping_host, check_tcp_port, http_get


with open("config.json") as f:
    config = json.load(f)

@pytest.mark.parametrize("host", config["hosts"])
def test_ping_hosts(host):
    assert ping_host(host) is True

@pytest.mark.parametrize("tcp_check", config["tcp_checks"])
def test_tcp_ports(tcp_check):
    assert check_tcp_port(tcp_check["host"], tcp_check["port"]) is True

@pytest.mark.parametrize("url", config["urls"])
def test_http_get(url):
    status = http_get(url)
    assert status == 200
