""" Handles package assignment to agents """
class PackageAssigner:
    """Assigns packages to agents based on proximity"""
    
    def __init__(self, agents, warehouses, packages):
        self.agents = agents
        self.warehouses = warehouses
        self.packages = packages
    
    def assign_packages(self):
        """
        Assign each package to the nearest agent
        Uses Euclidean distance from agent to warehouse
        """
        print("\n--- Assigning Packages to Agents ---")
        
        for package in self.packages:
            nearest_agent = self._find_nearest_agent(package)
            if nearest_agent:
                nearest_agent.add_package(package)
                print(f"  {package.id} → {nearest_agent.id} (from {package.warehouse_id})")
        
        print("✓ Package assignment complete\n")
    
    def _find_nearest_agent(self, package):
        """Find the agent nearest to the package's warehouse"""
        warehouse = self.warehouses[package.warehouse_id]
        
        nearest_agent = None
        min_distance = float('inf')
        
        for agent in self.agents.values():
            distance = agent.location.distance_to(warehouse.location)
            
            if distance < min_distance:
                min_distance = distance
                nearest_agent = agent
        
        return nearest_agent