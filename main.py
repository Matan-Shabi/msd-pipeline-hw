"""
Subnet Calculator (CLI version)
Performs subnet allocation and subnet mask calculations based on user input.
"""



__version__ = "9.0.0"



import ipaddress
from typing import List

def calculate_subnets(network_address: str, subnet_mask: str, dept_computers: List[int]) -> str:
    """Calculate subnets for each department based on the number of computers."""
    try:
        network = ipaddress.ip_network(f"{network_address}/{subnet_mask}", strict=False)
        departments = {f"Department {i + 1}": computers for i, computers in enumerate(dept_computers)}

        sorted_departments = sorted(departments.items(), key=lambda x: x[1], reverse=True)

        subnets = []
        current_subnet = network
        for dept, hosts in sorted_departments:
            required_size = hosts + 2  # network + broadcast
            bits_needed = (required_size - 1).bit_length()
            prefix_length = 32 - bits_needed
            subnet = ipaddress.ip_network((current_subnet.network_address, prefix_length))
            subnets.append((dept, subnet))
            current_subnet = ipaddress.ip_network(
                (int(subnet.network_address) + (1 << (32 - prefix_length)), prefix_length))

        result = ""
        for dept, subnet in subnets:
            result += f"{dept}:\n"
            result += f"  Subnet: {subnet}\n"
            result += f"  Subnet Mask: {subnet.netmask}\n"
            result += f"  Network ID: {subnet.network_address}\n"
            result += f"  Broadcast Address: {subnet.broadcast_address}\n"
            result += f"  Address Range: {list(subnet.hosts())[0]} - {list(subnet.hosts())[-1]}\n"
            result += f"  Best CIDR Notation: /{subnet.prefixlen}\n\n"

        return result
    except ValueError as e:
        return f"Error: {e}"


def calculate_subnet_masks(host_counts: List[int]) -> str:
    """Calculate subnet masks from a list of host counts."""
    try:
        result = ""
        for num_hosts in host_counts:
            if num_hosts < 1:
                raise ValueError("Number of hosts must be at least 1")
            bits = (num_hosts - 1).bit_length()
            mask_bits = 32 - bits
            subnet_mask = ipaddress.IPv4Network(f"0.0.0.0/{mask_bits}").netmask
            result += f"For {num_hosts} hosts:\n"
            result += f"  Subnet Mask: {subnet_mask}\n"
            result += f"  CIDR Notation: /{mask_bits}\n\n"
        return result
    except ValueError as e:
        return f"Error: {e}"


def main():
    """Main CLI entry point."""
    print("Subnet Calculator CLI")
    print("1. Subnet allocation for departments")
    print("2. Calculate subnet masks for host counts")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        network = input("Enter network address (e.g. 192.168.1.0): ")
        cidr = input("Enter subnet mask in CIDR (e.g. 24): ")
        dept_str = input("Enter computers per department (comma-separated): ")
        depts = [int(x.strip()) for x in dept_str.split(",") if x.strip().isdigit()]
        print("\n" + calculate_subnets(network, cidr, depts))

    elif choice == "2":
        host_str = input("Enter host counts (comma-separated): ")
        hosts = [int(x.strip()) for x in host_str.split(",") if x.strip().isdigit()]
        print("\n" + calculate_subnet_masks(hosts))

    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
