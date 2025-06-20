import json
import socket
#The approach below makes it easy to update the configuration when testing other networks.
def setup_config():
    config = {}
    # Configuring the wifi router to run performance and connectivity tests on. 
    while True:
        router_ip = input("Please enter the router IP address: ").strip()
        if not router_ip:
            router_ip = "192.168.1.1" #default IP 

        try:
            socket.inet_aton(router_ip)
            config["router_ip"] = router_ip
            break
        except socket.error:
            print("invalid IP address format. Please try again.")

    #Below are some other configurations needed to run reconnection tests on the network. 
    #These two inputs are absolutely needed to ahead with the reconnection tests. 
    
    config["ssid"] = input("Enter WiFi SSID: ").strip()
    while not config["ssid"]:
        print("SSID is required for WiFi reconnection tests.")
        config["ssid"] = input("Enter WiFi SSID: ").strip()

    config["password"] = input("Enter WiFi password: ").strip()
    while not config["password"]:
        print("Password is required for WiFi reconnection tests.")
        config["password"] = input("Enter WiFi password: ").strip()
    
    # Save configuration
    with open('test_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"\nConfiguration saved to test_config.json:")
    print(json.dumps(config, indent=2))
    
    return config

if __name__ == "__main__":
    setup_config()
