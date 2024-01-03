def format_device_info(device):
    """Format device information for display."""
    return f"Device: {device['name']} ({device['ip_address']})"

def write_to_log(message):
    """Write messages to a log file."""
    with open('logfile.txt', 'a') as log_file:
        log_file.write(message + '\n')