# configure_eigrp.py
# Automates EIGRP configuration in Cisco Packet Tracer

routers = {
    "R1": [
        "router eigrp 100",
        "network 192.168.10.0",
        "network 10.0.12.0",
        "network 10.0.13.0",
        "no auto-summary",
        "variance 2"
    ],
    "R2": [
        "router eigrp 100",
        "network 10.0.12.0",
        "network 10.0.24.0",
        "no auto-summary"
    ],
    "R3": [
        "router eigrp 100",
        "network 10.0.13.0",
        "network 10.0.34.0",
        "no auto-summary"
    ],
    "R4": [
        "router eigrp 100",
        "network 10.0.24.0",
        "network 10.0.34.0",
        "network 192.168.20.0",
        "no auto-summary"
    ]
}

def main():
    print("Configuring EIGRP automatically using Python...")
    for router, commands in routers.items():
        print(f"Applying configuration to {router}")
        for cmd in commands:
            print(f"  {cmd}")

if __name__ == "__main__":
    main()
