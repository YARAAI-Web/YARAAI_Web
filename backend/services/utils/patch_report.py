# services/utils/patch_report.py
def prepare_report_json_for_prompt(report_json: dict) -> dict:
    if "behavior" not in report_json:
        report_json["behavior"] = {
            "processes": [],
            "summary": {}
        }
    if "network" not in report_json:
        report_json["network"] = {
            "hosts": [], "dns": [], "http": [], "tcp": [], "udp": [],
            "icmp": [], "tls": [], "smtp": [], "irc": [], "domains": [],
            "http_ex": [], "https_ex": [], "smtp_ex": [], "mitm": [],
            "dns_servers": [], "dead_hosts": [], "pcap_sha256": ""
        }
    return report_json
