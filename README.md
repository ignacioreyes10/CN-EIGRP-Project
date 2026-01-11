# EIGRP Load Balancing and Redundancy Setup
Team Members: Javier Muela and Ignacio Reyes de Toro

## Introduction

The goal of this project is to implement a redundant routed network using the Enhanced Interior Gateway Routing Protocol (EIGRP) and to automate its configuration using Python. EIGRP allows routers to dynamically exchange routing information, support load balancing, and provide fast convergence in case of link failure.

The network topology is designed in Cisco Packet Tracer, while the routing configuration is applied automatically through a Python script. This approach reflects a NetDevOps methodology, where network configuration is managed through code instead of manual CLI commands.

The project demonstrates how traffic can be distributed across multiple network paths and how the network continues to operate when one of the links fails, showing how automation can simplify network management and reduce configuration errors.

VM Specifications: 
To ensure a stable development environment we deployed a virtualized workstation using Oracle VirtualBox. The guest operating system is Ubuntu, configurated to provide the necessary computational resources to run Cisco Packet Tracer and Python automation scripts simultaneously without performance degradation.

Network Topology Design:
We have designed a diamond-shaped redundant topology to evaluate EIGRP's performance. The network consists of four Cisco 2911 routers and two end-user workstations. This specific layout was chosen to simulate a real-world enterprise environment where a Head Office (R1) connects to a Branch Office (R4) through two distinct service providers (R2 and R3). This architecture is ideal for demonstrating Successor and Feasible Successor selection, as well as testing both equal and unequal cost load balancing by modifying interface bandwidths.

Interface Mapping and Verification:
To ensure network consistency, we strictly followed a predefined port-mapping scheme. The core router (R1) distributes traffic through GigabitEthernet 0/1 to the upper path (R2) and through GigabitEthernet 0/2 to the lower path (R3). This physical segmentation is crucial for EIGRP to identify multiple valid paths to the destination network (192.168.40.0/24). All interfaces have been manually addressed and enabled, establishing the physical foundation for the dynamic routing protocol.

Here are the execution instructions for anyone reading:

  1. Launch the Environment: Open the provided .pkt file in Cisco Packet Tracer within the Ubuntu VM.

  2. API Readiness: Ensure the "External Network Access" is enabled in Packet Tracer settings to allow the Python script to communicate with the simulation.

  3. Run Automation: Open the Linux Terminal and execute the script: python3 configure_eigrp.py.

  4. Observation: Watch the Command Line Interface (CLI) of the routers. The teacher will see the EIGRP configurations being applied automatically in real-time.

  5. Validation: Once the script finishes, perform a ping between PC-A and PC-B to verify end-to-end connectivity.
