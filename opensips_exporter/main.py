import time
from prometheus_client import start_http_server
from opensips_exporter.cli_client import OpenSIPSClient
from opensips_exporter.lb_metrics import update_lb_metrics
from opensips_exporter.profile_metrics import update_profile_metrics

def main():
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    print("Prometheus exporter for OpenSIPS started on port 8000.")

    client = OpenSIPSClient()

    while True:
        try:
            update_lb_metrics(client)
            update_profile_metrics(client)
        except Exception as e:
            print("Error updating metrics:", e)
        time.sleep(10)

if __name__ == '__main__':
    main()
