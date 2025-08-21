import subprocess
import socket
import requests
import logging

logging.basicConfig(
    filename="network_checks.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def ping_host(host: str) -> bool:
    try:
        result = subprocess.run(["ping", "-n", "1", host], capture_output=True)
        success = result.returncode == 0
        logging.info(f"Ping {host}: {'Success' if success else 'Fail'}")
        return success
    except Exception as e:
        logging.error(f"Ping {host} failed: {e}")
        return False

def check_tcp_port(host: str, port: int) -> bool:
    try:
        with socket.create_connection((host, port), timeout=3):
            logging.info(f"TCP {host}:{port} - Open")
            return True
    except Exception as e:
        logging.warning(f"TCP {host}:{port} - Closed or unreachable ({e})")
        return False

def http_get(url: str) -> int:
    try:
        response = requests.get(url, timeout=5)
        logging.info(f"HTTP GET {url} - Status {response.status_code}")
        return response.status_code
    except Exception as e:
        logging.error(f"HTTP GET {url} failed: {e}")
        return -1

