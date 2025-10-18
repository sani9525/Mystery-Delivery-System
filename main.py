"""Main entry point for FastBox Delivery System"""

from data_loader import DataLoader
from assignment import PackageAssigner
from simulator import DeliverySimulator
from reporter import ReportGenerator


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("       FASTBOX DELIVERY SYSTEM")
    print("="*50)
    print("1. Run Complete Simulation")
    print("2. Load and Verify Data Only")
    print("3. Run Simulation with Custom File")
    print("4. Test and Validate JSON File")
    print("5. Exit")
    print("="*50)


def run_simulation(filename="base_case.json"):
    """
    Run the complete delivery simulation
    
    Steps:
    1. Load data from JSON file
    2. Assign packages to nearest agents
    3. Simulate deliveries
    4. Generate and save report
    """
    print(f"\nStarting simulation with file: {filename}\n")
    
    # Step 1: Load data
    loader = DataLoader(filename)
    if not loader.load_data():
        return False
    
    # Step 2: Assign packages to agents
    assigner = PackageAssigner(loader.agents, loader.warehouses, loader.packages)
    assigner.assign_packages()
    
    # Step 3: Simulate deliveries
    simulator = DeliverySimulator(loader.agents, loader.warehouses)
    simulator.simulate_deliveries()
    
    # Step 4: Generate and save report
    reporter = ReportGenerator(loader.agents)
    report = reporter.generate_report()
    reporter.display_report(report)
    reporter.save_report(report)
    
    # Display statistics
    stats = simulator.get_statistics()
    print(f"Total Packages Processed: {stats['total_packages']}")
    print(f"Total Distance Traveled: {stats['total_distance']:.2f} units\n")
    
    return True


def load_data_only(filename="base_case.json"):
    """Load and display data without running simulation"""
    print(f"\nLoading data from: {filename}\n")
    
    loader = DataLoader(filename)
    if loader.load_data():
        loader.verify_and_test(verbose=True)
        return True
    return False


def test_and_validate(filename):
    """
    Comprehensive testing and validation of JSON file
    Includes all steps with detailed verification
    """
    print(f"\n{'='*60}")
    print(f"TESTING AND VALIDATING: {filename}")
    print('='*60)
    
    # Step 1: Load data
    print("\n[Step 1] Loading data...")
    loader = DataLoader(filename)
    if not loader.load_data():
        print("❌ FAILED: Could not load data")
        return False
    
    # Step 2: Verify data integrity
    print("\n[Step 2] Verifying data integrity...")
    if not loader.verify_and_test(verbose=True):
        print("❌ FAILED: Data validation failed")
        return False
    
    # Step 3: Assign packages
    print(f"\n[Step 3] Assigning packages to agents...")
    assigner = PackageAssigner(loader.agents, loader.warehouses, loader.packages)
    assigner.assign_packages()
    
    # Verify assignments
    total_assigned = 0
    print(f"\n[Assignment Verification]")
    for agent in loader.agents.values():
        print(f"  {agent.id}: {len(agent.packages)} package(s) assigned")
        total_assigned += len(agent.packages)
    
    if total_assigned != len(loader.packages):
        print(f"  ❌ ERROR: {total_assigned} assigned but {len(loader.packages)} total packages")
        return False
    else:
        print(f"  ✓ All {total_assigned} packages assigned correctly")
    
    # Step 4: Simulate deliveries
    print(f"\n[Step 4] Simulating deliveries...")
    simulator = DeliverySimulator(loader.agents, loader.warehouses)
    simulator.simulate_deliveries()
    
    # Step 5: Display performance metrics (without saving report)
    print(f"\n[Step 5] Calculating performance metrics...")
    reporter = ReportGenerator(loader.agents)
    report = reporter.generate_report()
    
    # Display report (but don't save)
    reporter.display_report(report)
    
    # Verify statistics
    stats = simulator.get_statistics()
    print(f"\n[Statistics]")
    print(f"  Total Packages Processed: {stats['total_packages']}")
    print(f"  Total Distance Traveled: {stats['total_distance']:.2f} units")
    print(f"  Average Distance per Package: {stats['total_distance']/stats['total_packages']:.2f} units")
    
    # Verify all packages delivered
    delivered_count = sum(1 for pkg in loader.packages if pkg.delivered)
    print(f"\n[Delivery Verification]")
    print(f"  Packages Delivered: {delivered_count}/{len(loader.packages)}")
    
    if delivered_count == len(loader.packages):
        print(f"  ✓ All packages delivered successfully!")
    else:
        print(f"  ❌ ERROR: Not all packages were delivered")
        return False
    
    print(f"\n{'='*60}")
    print(f"✅ TEST PASSED: {filename}")
    print('='*60 + "\n")
    
    return True


def main():
    """Main program loop"""
    while True:
        display_menu()
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            run_simulation()
        
        elif choice == "2":
            load_data_only()
        
        elif choice == "3":
            filename = input("Enter JSON filename: ").strip()
            if filename:
                run_simulation(filename)
            else:
                print("Invalid filename!")
        
        elif choice == "4":
            filename = input("Enter JSON filename to test: ").strip()
            if filename:
                test_and_validate(filename)
            else:
                print("Invalid filename!")
        
        elif choice == "5":
            print("\nThank you for using FastBox Delivery System!")
            print("Goodbye! 👋\n")
            break
        
        else:
            print("\n✗ Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()