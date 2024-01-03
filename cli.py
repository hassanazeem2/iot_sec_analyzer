import argparse
from scanner import scan
from analyzer import analyze, load_config
from utils import format_device_info, write_to_log



def main():
    parser = argparse.ArgumentParser(description="IoT Security Analyzer")
    parser.add_argument("--config", help="Path to the configuration file", required=True)
    args = parser.parse_args()


    # load the conifg

    config = load_config(args.config)

    # network scan

    devices_list = scan(config["network_range)"])

    #analylze the devices

    for device in devices_list:
        analyze(device)


if __name__ == "__main__":
    main()