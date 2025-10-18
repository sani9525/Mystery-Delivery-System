""" Generates and saves delivery reports """
import json


class ReportGenerator:
    """Generates reports from delivery simulation results"""
    
    def __init__(self, agents):
        self.agents = agents
    
    def generate_report(self):
        """Generate a comprehensive delivery report"""
        report = {}
        
        # Calculate metrics for each agent
        for agent in self.agents.values():
            report[agent.id] = {
                "packages_delivered": len(agent.packages),
                "total_distance": round(agent.total_distance, 2),
                "efficiency": round(agent.get_efficiency(), 2)
            }
        
        # Find the best agent (lowest efficiency = best)
        best_agent = self._find_best_agent()
        report["best_agent"] = best_agent
        
        return report
    
    def _find_best_agent(self):
        """Find the most efficient agent"""
        best_agent = None
        best_efficiency = float('inf')
        
        for agent in self.agents.values():
            if len(agent.packages) > 0:  # Only consider agents with deliveries
                efficiency = agent.get_efficiency()
                if efficiency < best_efficiency:
                    best_efficiency = efficiency
                    best_agent = agent.id
        
        return best_agent
    
    def save_report(self, report, filename="report.json"):
        """Save report to JSON file"""
        try:
            with open(filename, 'w') as file:
                json.dump(report, file, indent=2)
            print(f"✓ Report saved to {filename}")
            return True
        except Exception as e:
            print(f"✗ Error saving report: {e}")
            return False
    
    def display_report(self, report):
        """Display report in a formatted way"""
        print("\n" + "="*50)
        print("           DELIVERY REPORT")
        print("="*50)
        
        for agent_id, metrics in report.items():
            if agent_id != "best_agent":
                print(f"\n{agent_id}:")
                print(f"  Packages Delivered: {metrics['packages_delivered']}")
                print(f"  Total Distance: {metrics['total_distance']} units")
                print(f"  Efficiency: {metrics['efficiency']} units/package")
        
        print(f"\n{'='*50}")
        print(f"  🏆 Best Agent: {report['best_agent']}")
        print("="*50 + "\n")