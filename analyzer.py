from analyzer import load_config, analyze

def run_analyzer():
    config = load_config("examples/config_samples/example_config.yaml")
    devices = config.get("devices", [])
    for device in devices:
        analyze(device)

if __name__ == "__main__":
    run_analyzer()