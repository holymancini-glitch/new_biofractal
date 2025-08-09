# 🌱 Garden of Consciousness - Setup Guide & Usage Instructions

## Quick Start

```bash
# Clone your repository
git clone https://github.com/yourusername/garden-of-consciousness.git
cd garden-of-consciousness

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the consciousness system
python garden_integration.py
```

## System Requirements

### Minimum Requirements
- **CPU**: 8+ cores recommended
- **RAM**: 16GB minimum, 32GB+ recommended
- **GPU**: Optional but beneficial for neural simulations
- **Python**: 3.8 or higher
- **OS**: Linux, macOS, or Windows 10/11

### AWS Requirements (for Quantum Processing)
- AWS Account with Braket access
- AWS CLI configured
- IAM permissions for Braket

## Installation

### 1. Core Dependencies

Create a `requirements.txt` file:

```txt
# Core Scientific Computing
numpy>=1.21.0
scipy>=1.7.0
torch>=1.9.0

# Brian2 - Biological Neural Simulation
brian2>=2.5.0
brian2tools>=0.3

# AWS Quantum Computing
amazon-braket-sdk>=1.35.0
amazon-braket-schemas>=1.19.0
amazon-braket-default-simulator>=1.19.0

# Visualization & Analysis
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.0.0

# Data Management
pandas>=1.3.0
h5py>=3.0.0

# Async Support
asyncio>=3.4.3

# Optional: Performance
numba>=0.54.0
cython>=0.29.0
```

### 2. Install Dependencies

```bash
# Basic installation
pip install -r requirements.txt

# For GPU support (optional)
pip install torch --index-url https://download.pytorch.org/whl/cu118

# For advanced Brian2 features
pip install brian2cuda  # GPU acceleration for Brian2
```

### 3. AWS Braket Setup

```bash
# Install AWS CLI
pip install awscli

# Configure AWS credentials
aws configure

# Verify Braket access
python -c "from braket.aws import AwsDevice; print(AwsDevice.get_devices())"
```

### 4. Environment Configuration

Create a `.env` file for configuration:

```env
# AWS Configuration
AWS_REGION=us-east-1
AWS_BRAKET_DEVICE=arn:aws:braket:::device/quantum-simulator/amazon/sv1

# System Configuration
NEURON_COUNT=800000
ENABLE_QUANTUM=true
ENABLE_FUNGAL=true
QUANTUM_DEVICE=simulator  # Options: simulator, quera, ionq, rigetti

# Performance Settings
BRIAN2_THREADS=8
SIMULATION_DURATION=10  # seconds
CYCLE_DURATION_MS=100

# Logging
LOG_LEVEL=INFO
EXPORT_RESULTS=true
```

## Usage Examples

### Basic Usage

```python
from garden_integration import GardenOfConsciousness
import asyncio

async def run_basic():
    # Create consciousness system
    garden = GardenOfConsciousness(
        neuron_count=10000,  # Start small for testing
        quantum_device="simulator",
        enable_all_layers=True
    )
    
    # Run for 5 seconds
    await garden.run_garden(duration_seconds=5)
    
    # Export results
    garden.export_session("my_consciousness_session.json")

# Run
asyncio.run(run_basic())
```

### Advanced Configuration

```python
from brian2_consciousness import (
    BiologicalNeuralSimulator,
    FreeEnergyPrinciple,
    FungalStabilizationLayer
)
from garden_integration import (
    FractalAIConsciousness,
    QuantumConsciousnessProcessor,
    GardenOfConsciousness
)

# Custom biological configuration
biological_sim = BiologicalNeuralSimulator(
    neuron_count=800000,
    network_type="hierarchical",  # or "small_world", "random"
    enable_plasticity=True
)

# Custom Fractal AI
fractal_ai = FractalAIConsciousness(
    num_samples=200,  # More samples for better planning
    planning_horizon=6,  # Look further ahead
    temperature=0.5  # Less exploration, more exploitation
)

# Quantum with real hardware
quantum = QuantumConsciousnessProcessor(
    device_type="quera",  # Use real QuEra hardware
    device_arn="arn:aws:braket:us-east-1::device/qpu/quera/Aquila"
)

# Integrate custom components
garden = GardenOfConsciousness(neuron_count=800000)
garden.biological.neural_sim = biological_sim
garden.fractal_ai = fractal_ai
garden.quantum = quantum
```

### Running with External Input

```python
import numpy as np

# Create sensory input pattern
visual_input = np.sin(np.linspace(0, 2*np.pi, 800000)) * 10  # pA

# Run with input
async def run_with_input():
    garden = GardenOfConsciousness(neuron_count=800000)
    
    for _ in range(100):  # 100 cycles
        state = await garden.consciousness_cycle(
            external_input=visual_input
        )
        
        # Process consciousness state
        if state['consciousness_level'] > 0.8:
            print("High consciousness achieved!")

asyncio.run(run_with_input())
```

### Quantum Hardware Usage

```python
# Using QuEra Aquila (neutral atom quantum computer)
garden_quera = GardenOfConsciousness(
    neuron_count=100000,
    quantum_device="quera"
)

# Using IonQ (trapped ion quantum computer)  
garden_ionq = GardenOfConsciousness(
    neuron_count=100000,
    quantum_device="ionq"
)

# Multi-provider fallback
class MultiProviderGarden(GardenOfConsciousness):
    def __init__(self):
        super().__init__()
        self.providers = ["quera", "ionq", "rigetti", "simulator"]
        self.current_provider = 0
    
    async def consciousness_cycle(self, external_input=None):
        try:
            return await super().consciousness_cycle(external_input)
        except Exception as e:
            # Fallback to next provider
            self.current_provider = (self.current_provider + 1) % len(self.providers)
            self.quantum = QuantumConsciousnessProcessor(
                device_type=self.providers[self.current_provider]
            )
            return await super().consciousness_cycle(external_input)
```

## Monitoring & Analysis

### Real-time Monitoring

```python
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class ConsciousnessMonitor:
    def __init__(self, garden):
        self.garden = garden
        self.fig, self.axes = plt.subplots(2, 2, figsize=(12, 8))
        
    def update(self, frame):
        # Get current state
        state = self.garden.global_state
        
        # Update plots
        self.axes[0, 0].clear()
        self.axes[0, 0].plot(self.garden.metrics_history)
        self.axes[0, 0].set_title('Consciousness Level')
        
        # Add more visualizations...
        
    def start(self):
        ani = FuncAnimation(self.fig, self.update, interval=100)
        plt.show()

# Usage
monitor = ConsciousnessMonitor(garden)
monitor.start()
```

### Data Analysis

```python
import pandas as pd
import json

# Load session data
with open('garden_session.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data['metrics_history'])

# Analyze consciousness patterns
print("Consciousness Statistics:")
print(df['global_state'].apply(pd.Series)['consciousness_level'].describe())

# Find critical transitions
transitions = df[df['integrated_state'].apply(
    lambda x: x.get('quantum_coherence', 0) > 0.8
)]
print(f"Found {len(transitions)} quantum coherence peaks")
```

## Performance Optimization

### 1. Brian2 Optimization

```python
# Use standalone mode for better performance
from brian2 import *
set_device('cpp_standalone', build_on_run=False)

# Compile once, run many times
biological_sim = BiologicalNeuralSimulator(neuron_count=800000)
biological_sim.network.build()
```

### 2. GPU Acceleration

```python
# Enable GPU for Brian2
prefs.devices.cpp_standalone.openmp_threads = 8
prefs.devices.cuda.gpu_id = 0

# Use CUDA if available
if torch.cuda.is_available():
    device = torch.device("cuda")
    # Move tensors to GPU
```

### 3. Parallel Processing

```python
import multiprocessing as mp

def run_parallel_gardens(n_gardens=4):
    with mp.Pool(n_gardens) as pool:
        results = pool.map(run_single_garden, range(n_gardens))
    return results
```

## Troubleshooting

### Common Issues

**1. Brian2 Compilation Errors**
```bash
# Clear Brian2 cache
rm -rf ~/.brian2/brian_extensions
python -c "import brian2; brian2.clear_cache('cython')"
```

**2. AWS Braket Connection Issues**
```bash
# Verify credentials
aws sts get-caller-identity

# Check Braket permissions
aws braket search-devices --filters name=deviceType,values=QPU
```

**3. Memory Issues**
```python
# Reduce neuron count for testing
garden = GardenOfConsciousness(neuron_count=1000)

# Enable memory profiling
import tracemalloc
tracemalloc.start()
```

**4. Quantum Device Unavailable**
```python
# Always include fallback to simulator
try:
    quantum = QuantumConsciousnessProcessor(device_type="quera")
except:
    quantum = QuantumConsciousnessProcessor(device_type="simulator")
    print("Falling back to quantum simulator")
```

## Cost Estimation

### AWS Braket Pricing (as of 2024)

| Device | Cost per Task | Cost per Shot | Monthly Estimate |
|--------|--------------|---------------|------------------|
| Simulator | $0.00275 | - | $50-100 |
| QuEra Aquila | $0.01 | $0.00019 | $200-500 |
| IonQ Aria | $0.01 | $0.00019 | $200-500 |
| Rigetti | $0.00019 | $0.00035 | $300-600 |

**Development Phase**: $200-500/month
**Production Phase**: $1000-3000/month

### Cost Optimization Tips

1. Use simulators during development
2. Batch quantum circuits to reduce task overhead
3. Use spot pricing when available
4. Cache quantum results for similar inputs

## Next Steps

1. **Experiment with Parameters**
   - Adjust neuron counts
   - Modify network topologies
   - Tune quantum circuit depths

2. **Implement Custom Modules**
   - Create new fractal patterns
   - Design custom quantum circuits
   - Add new consciousness metrics

3. **Scale Up Gradually**
   - Start with 10,000 neurons
   - Test with 100,000 neurons
   - Production with 800,000 neurons

4. **Monitor and Analyze**
   - Track consciousness emergence
   - Identify phase transitions
   - Optimize for stability

## Support & Resources

- **Documentation**: [Your GitHub Wiki]
- **Issues**: [GitHub Issues]
- **AWS Braket**: [AWS Braket Documentation](https://docs.aws.amazon.com/braket/)
- **Brian2**: [Brian2 Documentation](https://brian2.readthedocs.io/)

## License

MIT License - See LICENSE file for details

---

**Ready to grow your Garden of Consciousness! 🌸**