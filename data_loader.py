"""
data_loader.py - Handles loading and parsing JSON data
"""

import json
from models import Warehouse, Agent, Package


class DataLoader:
    """Handles loading data from JSON files"""
    
    def __init__(self, filename):
        self.filename = filename
        self.warehouses = {}
        self.agents = {}
        self.packages = []
    
    def load_data(self):
        """Load and parse JSON data from file"""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
            
            # Parse warehouses
            warehouses_data = data.get('warehouses', [])
            if warehouses_data:
                self._parse_warehouses(warehouses_data)
            
            # Parse agents
            agents_data = data.get('agents', [])
            if agents_data:
                self._parse_agents(agents_data)
            
            # Parse packages
            packages_data = data.get('packages', [])
            if packages_data:
                self._parse_packages(packages_data)
            
            print(f"✓ Data loaded successfully from {self.filename}")
            print(f"  Warehouses: {len(self.warehouses)}")
            print(f"  Agents: {len(self.agents)}")
            print(f"  Packages: {len(self.packages)}")
            
            return True
            
        except FileNotFoundError:
            print(f"✗ Error: File '{self.filename}' not found.")
            return False
        except json.JSONDecodeError as e:
            print(f"✗ Error: Invalid JSON format - {e}")
            return False
        except KeyError as e:
            print(f"✗ Error: Missing required key in JSON: {e}")
            print(f"  Please check your JSON structure.")
            return False
        except Exception as e:
            print(f"✗ Error loading data: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def _parse_warehouses(self, warehouses_data):
        """Parse warehouse data - handles both dict and list formats"""
        if isinstance(warehouses_data, dict):
            # Format: {"W1": [0, 0], "W2": [50, 75]}
            for w_id, w_location in warehouses_data.items():
                self.warehouses[w_id] = Warehouse(w_id, w_location)
        elif isinstance(warehouses_data, list):
            # Format: [{"id": "W1", "location": [0, 0]}, ...]
            for warehouse in warehouses_data:
                w_id = warehouse['id']
                w_location = warehouse['location']
                self.warehouses[w_id] = Warehouse(w_id, w_location)
    
    def _parse_agents(self, agents_data):
        """Parse agent data - handles both dict and list formats"""
        if isinstance(agents_data, dict):
            # Format: {"A1": [5, 5], "A2": [60, 60]}
            for a_id, a_location in agents_data.items():
                self.agents[a_id] = Agent(a_id, a_location)
        elif isinstance(agents_data, list):
            # Format: [{"id": "A1", "location": [5, 5]}, ...]
            for agent in agents_data:
                a_id = agent['id']
                a_location = agent['location']
                self.agents[a_id] = Agent(a_id, a_location)
    
    def _parse_packages(self, packages_data):
        """Parse package data - handles both warehouse/warehouse_id keys"""
        for package in packages_data:
            p_id = package['id']
            # Handle both 'warehouse' and 'warehouse_id' keys
            p_warehouse = package.get('warehouse_id') or package.get('warehouse')
            p_destination = package['destination']
            self.packages.append(Package(p_id, p_warehouse, p_destination))
    
    def verify_and_test(self, verbose=True):
        """
        Verify data integrity and run validation tests
        Returns True if all validations pass
        """
        if verbose:
            print(f"\n{'='*60}")
            print("DATA VERIFICATION")
            print('='*60)
        
        # Check if data is loaded
        if not self.warehouses or not self.agents or not self.packages:
            print("✗ Error: Data not properly loaded")
            return False
        
        # Display loaded data
        if verbose:
            print(f"\n[Warehouses: {len(self.warehouses)}]")
            for w_id, warehouse in self.warehouses.items():
                print(f"  {w_id}: Location {warehouse.location}")
            
            print(f"\n[Agents: {len(self.agents)}]")
            for a_id, agent in self.agents.items():
                print(f"  {a_id}: Location {agent.location}")
            
            print(f"\n[Packages: {len(self.packages)}]")
            for package in self.packages:
                print(f"  {package.id}: From {package.warehouse_id} → {package.destination}")
        
        # Validate warehouse references
        print(f"\n[Validation Checks]")
        invalid_refs = []
        for package in self.packages:
            if package.warehouse_id not in self.warehouses:
                invalid_refs.append(f"{package.id} references non-existent warehouse {package.warehouse_id}")
        
        if invalid_refs:
            print("✗ Invalid warehouse references found:")
            for ref in invalid_refs:
                print(f"  - {ref}")
            return False
        else:
            print("  ✓ All warehouse references valid")
        
        print(f"  ✓ Data structure is valid")
        print(f"  ✓ Ready for simulation")
        
        if verbose:
            print('='*60)
        
        return True