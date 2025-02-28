from prometheus_client import Gauge

# Define labels for LB metrics.
LB_LABELS = [
    'uri',
    'id',
    'group',
    'enabled',
    'auto_reenable',
    'resource_name'
]

allowed_load_gauge = Gauge(
    'opensips_lb_allowed_load',
    'Allowed capacity for LB resource (max value from resources)',
    LB_LABELS
)
current_load_gauge = Gauge(
    'opensips_lb_current_load',
    'Current load for LB resource (load value from resources)',
    LB_LABELS
)

def update_lb_metrics(client):
    """
    Calls the get_lb_list() command and updates the Prometheus metrics.
    """
    data = client.get_lb_list()
    if not data or "Destinations" not in data:
        print("No Destinations found in lb_list response.")
        return

    for dest in data["Destinations"]:
        base_labels = {
            "uri": dest.get("uri", "unknown"),
            "id": str(dest.get("id", "unknown")),
            "group": str(dest.get("group", "unknown")),
            "enabled": dest.get("enabled", "unknown"),
            # Replace dashes with underscores.
            "auto_reenable": dest.get("auto-reenable", dest.get("auto_reenable", "unknown"))
        }
        for res in dest.get("Resources", []):
            labels = base_labels.copy()
            labels["resource_name"] = res.get("name", "unknown")
            allowed_load_gauge.labels(**labels).set(res.get("max", 0))
            current_load_gauge.labels(**labels).set(res.get("load", 0))
