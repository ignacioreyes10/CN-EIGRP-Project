# EIGRP Load Balancing and Redundancy Setup

## Introduction

The goal of this project is to implement a redundant routed network using the Enhanced Interior Gateway Routing Protocol (EIGRP) and to automate its configuration using Python. EIGRP allows routers to dynamically exchange routing information, support load balancing, and provide fast convergence in case of link failure.

The network topology is designed in Cisco Packet Tracer, while the routing configuration is applied automatically through a Python script. This approach reflects a NetDevOps methodology, where network configuration is managed through code instead of manual CLI commands.

The project demonstrates how traffic can be distributed across multiple network paths and how the network continues to operate when one of the links fails, showing how automation can simplify network management and reduce configuration errors.

VM Specifications: 
To ensure a stable development environment we deployed a virtualized workstation using Oracle VirtualBox. The guest operating system is Ubuntu, configurated to provide the necessary computational resources to run Cisco Packet Tracer and Python automation scripts simultaneously without performance degradation.
