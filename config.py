"""
Configuration Management for BioFractal AI System
=================================================
Centralized configuration with environment variable support and validation.
"""

import os
from typing import Optional, Dict, Any, List
from pathlib import Path
from pydantic import BaseModel, Field, validator
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ConsciousnessConfig(BaseModel):
    """Configuration for consciousness parameters"""
    
    # Consciousness thresholds
    awareness_threshold: float = Field(default=0.5, ge=0.0, le=1.0)
    integration_threshold: float = Field(default=0.7, ge=0.0, le=1.0)
    coherence_threshold: float = Field(default=0.6, ge=0.0, le=1.0)
    
    # Emergence parameters
    emergence_window: int = Field(default=100, ge=10)
    phase_transition_threshold: float = Field(default=0.8, ge=0.0, le=1.0)
    
    # Memory configuration
    memory_capacity: int = Field(default=10000, ge=100)
    decay_rate: float = Field(default=0.01, ge=0.001, le=0.1)

class BiologicalConfig(BaseModel):
    """Configuration for biological simulation"""
    
    # Neural network parameters
    neuron_count: int = Field(default=800000, ge=1000)
    connection_probability: float = Field(default=0.1, ge=0.01, le=1.0)
    simulation_timestep: float = Field(default=0.1, ge=0.01, le=1.0)  # ms
    
    # Cortical Labs integration
    enable_dishbrain: bool = Field(default=False)
    electrode_count: int = Field(default=8000, ge=100)
    stimulation_intensity: float = Field(default=10.0, ge=1.0, le=100.0)  # μA
    
    # Brian2 specific
    brian2_threads: int = Field(default=4, ge=1, le=16)
    brian2_method: str = Field(default="euler", regex="^(euler|rk4|heun)$")

class QuantumConfig(BaseModel):
    """Configuration for quantum processing"""
    
    # Quantum device settings
    device_type: str = Field(default="simulator", regex="^(simulator|quera|ionq|rigetti)$")
    device_arn: Optional[str] = None
    n_qubits: int = Field(default=8, ge=2, le=64)
    circuit_depth: int = Field(default=4, ge=1, le=20)
    
    # Quantum algorithm parameters
    shots: int = Field(default=1000, ge=100, le=10000)
    optimization_level: int = Field(default=1, ge=0, le=3)
    
    # Entanglement and coherence
    entanglement_threshold: float = Field(default=0.5, ge=0.0, le=1.0)
    coherence_time: float = Field(default=100.0, ge=1.0)  # μs

class FractalConfig(BaseModel):
    """Configuration for fractal AI components"""
    
    # Planning parameters
    num_samples: int = Field(default=150, ge=10, le=1000)
    planning_horizon: int = Field(default=4, ge=1, le=20)
    temperature: float = Field(default=1.0, ge=0.1, le=10.0)
    
    # Fractal structure
    fractal_depth: int = Field(default=5, ge=2, le=10)
    branching_factor: int = Field(default=3, ge=2, le=10)
    
    # State space
    state_dim: int = Field(default=256, ge=64, le=2048)
    action_dim: int = Field(default=64, ge=16, le=512)

class MycelialConfig(BaseModel):
    """Configuration for mycelial networks"""
    
    # Network structure
    node_count: int = Field(default=1000, ge=10, le=100000)
    connection_radius: float = Field(default=10.0, ge=1.0, le=100.0)
    growth_rate: float = Field(default=0.1, ge=0.01, le=1.0)
    
    # Signal propagation
    decay_rate: float = Field(default=0.995, ge=0.9, le=0.999)
    signal_threshold: float = Field(default=0.2, ge=0.01, le=1.0)
    
    # Memory and trails
    trail_maxlen: int = Field(default=50, ge=10, le=1000)
    spore_lifetime: float = Field(default=3600.0, ge=60.0)  # seconds

class SystemConfig(BaseModel):
    """Main system configuration"""
    
    # Environment
    environment: str = Field(default="development", regex="^(development|testing|production)$")
    debug: bool = Field(default=True)
    log_level: str = Field(default="INFO", regex="^(DEBUG|INFO|WARNING|ERROR|CRITICAL)$")
    
    # Performance
    max_workers: int = Field(default=4, ge=1, le=32)
    enable_gpu: bool = Field(default=True)
    memory_limit_gb: float = Field(default=8.0, ge=1.0, le=128.0)
    
    # Data paths
    data_dir: Path = Field(default=Path("data"))
    models_dir: Path = Field(default=Path("models"))
    logs_dir: Path = Field(default=Path("logs"))
    exports_dir: Path = Field(default=Path("exports"))
    
    # Integration flags
    enable_quantum: bool = Field(default=True)
    enable_biological: bool = Field(default=True)
    enable_mycelial: bool = Field(default=True)
    enable_visualization: bool = Field(default=True)
    
    @validator('data_dir', 'models_dir', 'logs_dir', 'exports_dir')
    def create_directories(cls, v):
        v.mkdir(parents=True, exist_ok=True)
        return v

class BioFractalConfig(BaseModel):
    """Complete BioFractal AI configuration"""
    
    system: SystemConfig = SystemConfig()
    consciousness: ConsciousnessConfig = ConsciousnessConfig()
    biological: BiologicalConfig = BiologicalConfig()
    quantum: QuantumConfig = QuantumConfig()
    fractal: FractalConfig = FractalConfig()
    mycelial: MycelialConfig = MycelialConfig()
    
    # API Keys and secrets (loaded from environment)
    aws_access_key_id: Optional[str] = Field(default_factory=lambda: os.getenv("AWS_ACCESS_KEY_ID"))
    aws_secret_access_key: Optional[str] = Field(default_factory=lambda: os.getenv("AWS_SECRET_ACCESS_KEY"))
    cortical_labs_api_key: Optional[str] = Field(default_factory=lambda: os.getenv("CORTICAL_LABS_API_KEY"))
    
    def save_config(self, filepath: str):
        """Save configuration to file"""
        with open(filepath, 'w') as f:
            f.write(self.json(indent=2))
    
    @classmethod
    def load_config(cls, filepath: str) -> 'BioFractalConfig':
        """Load configuration from file"""
        with open(filepath, 'r') as f:
            return cls.parse_raw(f.read())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return self.dict()

# Global configuration instance
config = BioFractalConfig()

# Configuration validation
def validate_config():
    """Validate the current configuration"""
    errors = []
    
    # Check quantum device availability
    if config.quantum.device_type != "simulator" and not config.aws_access_key_id:
        errors.append("AWS credentials required for quantum hardware access")
    
    # Check biological integration requirements  
    if config.biological.enable_dishbrain and not config.cortical_labs_api_key:
        errors.append("Cortical Labs API key required for DishBrain integration")
    
    # Check resource requirements
    import torch
    if config.system.enable_gpu and not torch.cuda.is_available():
        errors.append("GPU enabled but CUDA not available")
    
    # Memory requirements
    total_neurons = config.biological.neuron_count
    estimated_memory_gb = total_neurons * 8 * 4 / (1024**3)  # Rough estimate
    if estimated_memory_gb > config.system.memory_limit_gb:
        errors.append(f"Estimated memory usage ({estimated_memory_gb:.2f}GB) exceeds limit ({config.system.memory_limit_gb}GB)")
    
    if errors:
        raise ValueError("Configuration validation failed:\n" + "\n".join(f"- {error}" for error in errors))
    
    return True

# Export for easy import
__all__ = [
    'config',
    'BioFractalConfig',
    'SystemConfig',
    'ConsciousnessConfig',
    'BiologicalConfig',
    'QuantumConfig',
    'FractalConfig',
    'MycelialConfig',
    'validate_config'
]