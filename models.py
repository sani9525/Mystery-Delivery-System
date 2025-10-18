""" Data models for the FastBox delivery system """

import math

class Location:
    """Represents a 2D location with x and y coordinates"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, other):
        """Calculate Euclidean distance to another location"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def __repr__(self):
        return f"({self.x}, {self.y})"


class Warehouse:
    """Represents a warehouse with an ID and location"""
    
    def __init__(self, id, location):
        self.id = id
        self.location = Location(location[0], location[1])
    
    def __repr__(self):
        return f"Warehouse({self.id}, {self.location})"


class Package:
    """Represents a package with ID, warehouse, and destination"""
    
    def __init__(self, id, warehouse_id, destination):
        self.id = id
        self.warehouse_id = warehouse_id
        self.destination = Location(destination[0], destination[1])
        self.delivered = False
    
    def __repr__(self):
        return f"Package({self.id}, Warehouse: {self.warehouse_id}, Dest: {self.destination})"


class Agent:
    """Represents a delivery agent"""
    
    def __init__(self, id, location):
        self.id = id
        self.location = Location(location[0], location[1])
        self.packages = []
        self.total_distance = 0.0
    
    def add_package(self, package):
        """Assign a package to this agent"""
        self.packages.append(package)
    
    def deliver_packages(self, warehouses_dict):
        """
        Simulate delivery of all assigned packages
        Returns the total distance traveled
        """
        current_location = self.location
        
        for package in self.packages:
            # Find the warehouse location
            warehouse = warehouses_dict[package.warehouse_id]
            
            # Travel to warehouse
            distance_to_warehouse = current_location.distance_to(warehouse.location)
            self.total_distance += distance_to_warehouse
            current_location = warehouse.location
            
            # Travel to destination
            distance_to_destination = current_location.distance_to(package.destination)
            self.total_distance += distance_to_destination
            current_location = package.destination
            
            # Mark package as delivered
            package.delivered = True
        
        return self.total_distance
    
    def get_efficiency(self):
        """Calculate efficiency as average distance per package"""
        if len(self.packages) == 0:
            return 0.0
        return self.total_distance / len(self.packages)
    
    def __repr__(self):
        return f"Agent({self.id}, Location: {self.location}, Packages: {len(self.packages)})"