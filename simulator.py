""" Simulates the delivery process """


class DeliverySimulator:
    """Simulates delivery operations for all agents"""
    
    def __init__(self, agents, warehouses):
        self.agents = agents
        self.warehouses = warehouses
    
    def simulate_deliveries(self):
        """
        Simulate delivery for all agents
        Each agent picks up packages from warehouses and delivers them
        """
        print("--- Simulating Deliveries ---")
        
        for agent in self.agents.values():
            if len(agent.packages) > 0:
                agent.deliver_packages(self.warehouses)
                print(f"  {agent.id}: Delivered {len(agent.packages)} packages, "
                      f"Total distance: {agent.total_distance:.2f} units")
            else:
                print(f"  {agent.id}: No packages assigned")
        
        print("✓ Delivery simulation complete\n")
    
    def get_statistics(self):
        """Calculate and return delivery statistics"""
        total_packages = sum(len(agent.packages) for agent in self.agents.values())
        total_distance = sum(agent.total_distance for agent in self.agents.values())
        
        return {
            'total_packages': total_packages,
            'total_distance': total_distance
        }