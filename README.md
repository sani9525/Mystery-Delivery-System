# FastBox Delivery System

A Python-based logistics simulator that demonstrates Object-Oriented Programming principles, efficient package routing, and delivery optimization using Euclidean distance calculations.

## Project Overview

FastBox is a delivery system simulator that assigns packages to the nearest available agents, simulates deliveries, and generates comprehensive reports on agent performance. The system uses modular design with separate classes for each component, making it maintainable and scalable.

##  Features

- **Intelligent Package Assignment**: Assigns packages to agents based on proximity to warehouses
- **Distance Calculation**: Uses Euclidean distance for optimal routing
- **Delivery Simulation**: Simulates complete delivery cycles from warehouse to destination
- **Performance Analytics**: Calculates efficiency metrics for each agent
- **JSON Integration**: Reads input data and exports detailed reports
- **Interactive Menu**: User-friendly command-line interface
- **Modular Architecture**: Clean separation of concerns with dedicated modules

## Project Structure

```
fastbox-delivery-system/
│
├── main.py                 # Main entry point with interactive menu
├── models.py               # Core data models (Location, Warehouse, Agent, Package)
├── data_loader.py          # JSON file parsing and data loading
├── assignment.py           # Package-to-agent assignment logic
├── simulator.py            # Delivery simulation engine
├── reporter.py             # Report generation and export
├── base_case.json          # Sample input data
├── report.json             # Generated output report
└── README.md               # Project documentation
```

## Technical Implementation

### 1. **models.py** - Core Data Models

#### `Location` Class
Represents 2D coordinates and handles distance calculations.

**Methods:**
- `__init__(x, y)`: Initialize location with coordinates
- `distance_to(other)`: Calculate Euclidean distance to another location
  ```python
  distance = √((x₂ - x₁)² + (y₂ - y₁)²)
  ```

**Key Concepts:**
- Encapsulation of coordinate data
- Mathematical distance calculation using Pythagorean theorem

#### `Warehouse` Class
Represents storage facilities with ID and location.

**Attributes:**
- `id`: Unique warehouse identifier
- `location`: Location object with coordinates

**Key Concepts:**
- Composition (has-a relationship with Location)
- Data modeling

#### `Package` Class
Represents deliverable items.

**Attributes:**
- `id`: Unique package identifier
- `warehouse_id`: Source warehouse
- `destination`: Location object for delivery point
- `delivered`: Boolean tracking delivery status

**Key Concepts:**
- State management (delivered/not delivered)
- Association with warehouses

#### `Agent` Class
Represents delivery personnel with package management capabilities.

**Attributes:**
- `id`: Unique agent identifier
- `location`: Current position
- `packages`: List of assigned packages
- `total_distance`: Cumulative travel distance

**Methods:**
- `add_package(package)`: Assign a package to the agent
- `deliver_packages(warehouses_dict)`: Simulate delivery process
  - Travels to warehouse
  - Picks up package
  - Travels to destination
  - Updates total distance
- `get_efficiency()`: Calculate average distance per package

**Key Concepts:**
- Collection management (list of packages)
- Behavioral methods (delivery simulation)
- Performance metrics calculation

### 2. **data_loader.py** - JSON Data Management

#### `DataLoader` Class
Handles file I/O and data parsing.

**Methods:**
- `load_data()`: Main loading function with error handling
- `_parse_warehouses(data)`: Convert JSON to Warehouse objects
- `_parse_agents(data)`: Convert JSON to Agent objects
- `_parse_packages(data)`: Convert JSON to Package objects

**Key Concepts:**
- File I/O operations
- JSON parsing with `json` module
- Exception handling (FileNotFoundError, JSONDecodeError)
- Private methods (methods starting with `_`)
- Data transformation from JSON to objects

**Error Handling:**
```python
try:
    # Attempt to load and parse
except FileNotFoundError:
    # Handle missing file
except JSONDecodeError:
    # Handle invalid JSON
except Exception:
    # Handle other errors
```

### 3. **assignment.py** - Package Assignment Logic

#### `PackageAssigner` Class
Implements the nearest-agent assignment algorithm.

**Algorithm:**
1. For each package:
   - Get the warehouse location
   - Calculate distance from each agent to the warehouse
   - Assign package to the agent with minimum distance
   
**Methods:**
- `assign_packages()`: Main assignment orchestration
- `_find_nearest_agent(package)`: Find closest agent using distance comparison

**Key Concepts:**
- Algorithm implementation (nearest neighbor)
- Iteration and comparison
- Optimization (minimizing distance)

**Time Complexity:** O(n × m) where n = packages, m = agents

### 4. **simulator.py** - Delivery Simulation Engine

#### `DeliverySimulator` Class
Simulates the actual delivery operations.

**Simulation Process:**
1. For each agent with packages:
   - Start at agent's initial location
   - For each assigned package:
     - Travel to warehouse (calculate distance)
     - Travel to destination (calculate distance)
     - Accumulate total distance
   - Mark packages as delivered

**Methods:**
- `simulate_deliveries()`: Execute simulation for all agents
- `get_statistics()`: Calculate aggregate metrics

**Key Concepts:**
- Process simulation
- State changes (location updates)
- Accumulation (distance tracking)
- Statistical aggregation

### 5. **reporter.py** - Report Generation

#### `ReportGenerator` Class
Creates and exports performance reports.

**Report Structure:**
```json
{
  "A1": {
    "packages_delivered": 2,
    "total_distance": 85.32,
    "efficiency": 42.66
  },
  "best_agent": "A1"
}
```

**Methods:**
- `generate_report()`: Create report dictionary
- `_find_best_agent()`: Identify most efficient agent (lowest efficiency score)
- `save_report(report, filename)`: Export to JSON file
- `display_report(report)`: Console output formatting

**Key Concepts:**
- Data aggregation
- Performance ranking
- File writing
- Formatted output

**Efficiency Calculation:**
```
Efficiency = Total Distance / Packages Delivered
```
*Lower efficiency score = better performance*

### 6. **main.py** - Application Entry Point

#### Main Functions

**`display_menu()`**
- Renders interactive menu
- Provides user options

**`run_simulation(filename)`**
- Orchestrates complete workflow:
  1. Load data
  2. Assign packages
  3. Simulate deliveries
  4. Generate reports
  5. Display results

**`load_data_only(filename)`**
- Loads and displays data without simulation
- Useful for data validation

**`main()`**
- Main program loop
- Handles user input
- Routes to appropriate functions

**Key Concepts:**
- Control flow
- User interaction
- Function composition
- Menu-driven interface

## 🎓 OOP Concepts Demonstrated

### 1. **Encapsulation**
- Data and methods bundled in classes
- Private methods (`_parse_warehouses`)
- Controlled access to attributes

### 2. **Abstraction**
- Complex operations hidden behind simple interfaces
- `distance_to()` hides mathematical complexity
- `deliver_packages()` abstracts multi-step process

### 3. **Composition**
- Warehouse has-a Location
- Agent has-many Packages
- Package has-a destination Location

### 4. **Single Responsibility Principle**
- Each class has one clear purpose
- DataLoader only loads data
- ReportGenerator only generates reports

### 5. **Separation of Concerns**
- Each module handles distinct functionality
- Models separate from business logic
- Business logic separate from I/O

## 📊 Data Flow

```
JSON File (base_case.json)
    ↓
DataLoader (parse and create objects)
    ↓
PackageAssigner (assign packages to agents)
    ↓
DeliverySimulator (simulate deliveries)
    ↓
ReportGenerator (create and save report)
    ↓
JSON File (report.json)
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only standard library)

### Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/sani9525/Mystery-delivery-system.git
cd Mystery-delivery-system
```

2. **Verify Python installation:**
```bash
python --version
```

3. **Ensure all files are present:**
```bash
ls -la
# Should show: main.py, models.py, data_loader.py, assignment.py, 
#              simulator.py, reporter.py, base_case.json
```

## 📖 Usage Guide

### Running the Program

**Method 1: Interactive Menu**
```bash
python main.py
```

Then select from menu options:
- `1` - Run complete simulation with base_case.json
- `2` - Load and display data only
- `3` - Run simulation with custom JSON file
- `4` - Exit program

**Method 2: Direct Import**
```python
from main import run_simulation

# Run with default file
run_simulation()

# Run with custom file
run_simulation("custom_data.json")
```

### Input Data Format

Create a JSON file with the following structure:

```json
{
  "warehouses": [
    {"id": "W1", "location": [0, 0]},
    {"id": "W2", "location": [50, 75]}
  ],
  "agents": [
    {"id": "A1", "location": [5, 5]},
    {"id": "A2", "location": [60, 60]}
  ],
  "packages": [
    {
      "id": "P1",
      "warehouse_id": "W1",
      "destination": [30, 40]
    }
  ]
}
```

**Field Descriptions:**
- `warehouses`: Array of warehouse objects with ID and [x, y] coordinates
- `agents`: Array of agent objects with ID and starting [x, y] location
- `packages`: Array of package objects with ID, source warehouse, and destination

### Output Format

The system generates `report.json`:

```json
{
  "A1": {
    "packages_delivered": 2,
    "total_distance": 85.32,
    "efficiency": 42.66
  },
  "A2": {
    "packages_delivered": 2,
    "total_distance": 120.12,
    "efficiency": 60.06
  },
  "A3": {
    "packages_delivered": 1,
    "total_distance": 50.00,
    "efficiency": 50.00
  },
  "best_agent": "A1"
}
```

## Testing

### Test with Different Scenarios

**1. Single Agent, Multiple Packages:**
```json
{
  "warehouses": [{"id": "W1", "location": [0, 0]}],
  "agents": [{"id": "A1", "location": [5, 5]}],
  "packages": [
    {"id": "P1", "warehouse_id": "W1", "destination": [10, 10]},
    {"id": "P2", "warehouse_id": "W1", "destination": [20, 20]}
  ]
}
```

**2. Multiple Agents, Single Package:**
Test competition for package assignment.

**3. Edge Cases:**
- Empty packages array
- Single package, single agent
- Agents at same location

### Validation Checklist

- [ ] Total packages delivered = Total packages in input
- [ ] All agents have non-negative distances
- [ ] Best agent has lowest efficiency score
- [ ] Report.json is valid JSON
- [ ] Console output is readable and informative

## 🔍 Key Algorithms

### 1. Euclidean Distance Calculation
```python
def distance_to(self, other):
    return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
```

**Complexity:** O(1)

### 2. Nearest Agent Assignment
```python
def _find_nearest_agent(self, package):
    min_distance = float('inf')
    nearest_agent = None
    
    for agent in self.agents.values():
        distance = agent.location.distance_to(warehouse.location)
        if distance < min_distance:
            min_distance = distance
            nearest_agent = agent
    
    return nearest_agent
```

**Complexity:** O(n) where n = number of agents

### 3. Delivery Simulation
```python
def deliver_packages(self, warehouses_dict):
    current_location = self.location
    
    for package in self.packages:
        warehouse = warehouses_dict[package.warehouse_id]
        
        # Agent → Warehouse
        distance = current_location.distance_to(warehouse.location)
        self.total_distance += distance
        current_location = warehouse.location
        
        # Warehouse → Destination
        distance = current_location.distance_to(package.destination)
        self.total_distance += distance
        current_location = package.destination
        
        package.delivered = True
```

**Complexity:** O(m) where m = number of packages per agent

## 📈 Performance Metrics

### Efficiency Score
```
Efficiency = Total Distance Traveled / Number of Packages Delivered
```

- **Lower is Better**: Indicates more efficient routing
- **Units**: Distance units per package
- **Use Case**: Compare agent performance

### Best Agent Selection
- Agents with 0 packages are excluded
- Minimum efficiency score wins
- Ties are broken by first occurrence

## 🛠️ Extending the System

### Adding New Features

**1. Add Priority Packages:**
```python
class Package:
    def __init__(self, id, warehouse_id, destination, priority=1):
        # Add priority attribute
        self.priority = priority
```

**2. Add Time-Based Simulation:**
```python
class Agent:
    def __init__(self, id, location, speed=1.0):
        self.speed = speed
    
    def calculate_delivery_time(self):
        return self.total_distance / self.speed
```

**3. Add Route Visualization:**
```python
def visualize_routes(self):
    # Use matplotlib to plot routes
    pass
```

## 🐛 Troubleshooting

### Common Issues

**1. FileNotFoundError**
```
Solution: Ensure base_case.json is in the same directory as main.py
```

**2. JSONDecodeError**
```
Solution: Validate JSON format using jsonlint.com
```

**3. No Packages Assigned**
```
Solution: Check that warehouse_id in packages matches existing warehouse IDs
```

**4. Import Errors**
```
Solution: Ensure all .py files are in the same directory
```

## 📚 Learning Resources

This project demonstrates concepts from:
- Object-Oriented Programming
- Data Structures (Lists, Dictionaries)
- File I/O Operations
- JSON Parsing
- Algorithm Design (Greedy Assignment)
- Software Architecture (Modular Design)
