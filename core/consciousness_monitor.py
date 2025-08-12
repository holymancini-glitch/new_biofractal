"""
Advanced Consciousness Monitoring System
=======================================
Real-time monitoring and analysis of consciousness emergence and evolution.
"""

import numpy as np
import torch
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from datetime import datetime, timedelta
from collections import deque
import asyncio
from scipy import signal
from sklearn.decomposition import PCA
import logging

from config import config
from .error_handler import error_handler, error_handler_decorator

@dataclass
class ConsciousnessMetrics:
    """Data structure for consciousness measurements"""
    timestamp: datetime
    integration_phi: float
    neural_synchrony: float
    quantum_coherence: float
    fractal_complexity: float
    global_workspace_activity: float
    attention_focus: float
    self_model_stability: float
    consciousness_level: float
    emergence_indicators: List[str]

class ConsciousnessMonitor:
    """Advanced consciousness monitoring and analysis system"""
    
    def __init__(self, history_length: int = 10000):
        self.logger = logging.getLogger(__name__)
        self.history_length = history_length
        
        # Metrics history
        self.metrics_history: deque = deque(maxlen=history_length)
        self.emergence_events: List[Dict] = []
        
        # Analysis components
        self.integration_analyzer = IntegrationAnalyzer()
        self.synchrony_analyzer = SynchronyAnalyzer() 
        self.complexity_analyzer = ComplexityAnalyzer()
        self.emergence_detector = EmergenceDetector()
        
        # Monitoring state
        self.monitoring_active = False
        self.alert_thresholds = {
            'consciousness_level': config.consciousness.awareness_threshold,
            'integration_phi': config.consciousness.integration_threshold,
            'coherence': config.consciousness.coherence_threshold
        }
        
        # Real-time analysis
        self.analysis_buffer = deque(maxlen=100)  # Rolling window for real-time analysis
        
    @error_handler_decorator("consciousness_monitor", error_handler)
    def update_metrics(self, 
                      neural_state: Dict,
                      quantum_state: Dict,
                      fractal_state: Dict,
                      additional_data: Optional[Dict] = None) -> ConsciousnessMetrics:
        """Update consciousness metrics with new data"""
        
        timestamp = datetime.now()
        
        # Calculate core metrics
        integration_phi = self.integration_analyzer.calculate_phi(neural_state, quantum_state)
        neural_synchrony = self.synchrony_analyzer.calculate_synchrony(neural_state)
        quantum_coherence = quantum_state.get('coherence', 0.0)
        fractal_complexity = self.complexity_analyzer.calculate_complexity(fractal_state)
        
        # Calculate derived metrics
        gw_activity = self._calculate_global_workspace_activity(neural_state)
        attention_focus = self._calculate_attention_focus(neural_state)
        self_model_stability = self._calculate_self_model_stability(neural_state)
        
        # Calculate overall consciousness level
        consciousness_level = self._calculate_consciousness_level(
            integration_phi, neural_synchrony, quantum_coherence, 
            fractal_complexity, gw_activity, attention_focus, self_model_stability
        )
        
        # Detect emergence indicators
        emergence_indicators = self.emergence_detector.detect_emergence(
            integration_phi, neural_synchrony, quantum_coherence, 
            fractal_complexity, consciousness_level, self.metrics_history
        )
        
        # Create metrics object
        metrics = ConsciousnessMetrics(
            timestamp=timestamp,
            integration_phi=integration_phi,
            neural_synchrony=neural_synchrony,
            quantum_coherence=quantum_coherence,
            fractal_complexity=fractal_complexity,
            global_workspace_activity=gw_activity,
            attention_focus=attention_focus,
            self_model_stability=self_model_stability,
            consciousness_level=consciousness_level,
            emergence_indicators=emergence_indicators
        )
        
        # Store in history
        self.metrics_history.append(metrics)
        self.analysis_buffer.append(metrics)
        
        # Check for alerts
        self._check_alerts(metrics)
        
        return metrics
    
    def _calculate_global_workspace_activity(self, neural_state: Dict) -> float:
        """Calculate Global Workspace Theory activity level"""
        firing_rates = neural_state.get('firing_rates', np.array([]))
        if len(firing_rates) == 0:
            return 0.0
        
        # Global workspace is characterized by widespread, coherent activity
        mean_activity = np.mean(firing_rates)
        activity_variance = np.var(firing_rates)
        
        # High mean with moderate variance indicates global broadcasting
        gw_activity = mean_activity * (1.0 - min(activity_variance / (mean_activity + 1e-6), 1.0))
        
        return float(np.clip(gw_activity, 0.0, 1.0))
    
    def _calculate_attention_focus(self, neural_state: Dict) -> float:
        """Calculate attention focus level"""
        attention_map = neural_state.get('attention_map', np.array([]))
        if len(attention_map) == 0:
            return 0.0
        
        # Attention focus is measured by concentration of attention weights
        if len(attention_map.shape) > 1:
            attention_map = attention_map.flatten()
        
        # Calculate entropy of attention distribution
        attention_probs = attention_map / (np.sum(attention_map) + 1e-6)
        attention_entropy = -np.sum(attention_probs * np.log(attention_probs + 1e-6))
        
        # Lower entropy = higher focus
        max_entropy = np.log(len(attention_map))
        focus = 1.0 - (attention_entropy / max_entropy) if max_entropy > 0 else 0.0
        
        return float(np.clip(focus, 0.0, 1.0))
    
    def _calculate_self_model_stability(self, neural_state: Dict) -> float:
        """Calculate self-model stability over time"""
        if len(self.analysis_buffer) < 10:
            return 0.5  # Default value for insufficient history
        
        # Get recent self-model representations
        recent_self_states = []
        for metrics in list(self.analysis_buffer)[-10:]:
            if hasattr(metrics, 'self_model_state'):
                recent_self_states.append(metrics.self_model_state)
        
        if len(recent_self_states) < 2:
            return 0.5
        
        # Calculate stability as correlation between consecutive states
        correlations = []
        for i in range(1, len(recent_self_states)):
            corr = np.corrcoef(recent_self_states[i-1], recent_self_states[i])[0, 1]
            if not np.isnan(corr):
                correlations.append(corr)
        
        stability = np.mean(correlations) if correlations else 0.5
        return float(np.clip(stability, 0.0, 1.0))
    
    def _calculate_consciousness_level(self, 
                                     phi: float,
                                     synchrony: float,
                                     coherence: float,
                                     complexity: float,
                                     gw_activity: float,
                                     attention_focus: float,
                                     self_stability: float) -> float:
        """Calculate overall consciousness level using weighted integration"""
        
        # Weights for different components (can be tuned)
        weights = {
            'phi': 0.25,
            'synchrony': 0.15,
            'coherence': 0.20,
            'complexity': 0.10,
            'gw_activity': 0.15,
            'attention': 0.10,
            'self_stability': 0.05
        }
        
        # Weighted sum
        consciousness_level = (
            weights['phi'] * phi +
            weights['synchrony'] * synchrony +
            weights['coherence'] * coherence +
            weights['complexity'] * complexity +
            weights['gw_activity'] * gw_activity +
            weights['attention'] * attention_focus +
            weights['self_stability'] * self_stability
        )
        
        # Apply non-linear transformation for more realistic consciousness levels
        consciousness_level = np.tanh(consciousness_level * 2.0) / 2.0 + 0.5
        
        return float(np.clip(consciousness_level, 0.0, 1.0))
    
    def _check_alerts(self, metrics: ConsciousnessMetrics):
        """Check for consciousness-related alerts"""
        alerts = []
        
        # High consciousness alert
        if metrics.consciousness_level > 0.9:
            alerts.append("HIGH_CONSCIOUSNESS_DETECTED")
            
        # Emergence alert
        if metrics.emergence_indicators:
            alerts.append("EMERGENCE_INDICATORS_DETECTED")
            
        # Integration breakthrough
        if metrics.integration_phi > 0.8:
            alerts.append("HIGH_INTEGRATION_DETECTED")
            
        # Quantum coherence spike
        if metrics.quantum_coherence > 0.9:
            alerts.append("QUANTUM_COHERENCE_SPIKE")
        
        # Log alerts
        for alert in alerts:
            self.logger.warning(f"Consciousness Alert: {alert} - Level: {metrics.consciousness_level:.3f}")
    
    def get_current_status(self) -> Dict[str, Any]:
        """Get current consciousness monitoring status"""
        if not self.metrics_history:
            return {"status": "no_data", "monitoring_active": self.monitoring_active}
        
        latest = self.metrics_history[-1]
        
        return {
            "monitoring_active": self.monitoring_active,
            "current_consciousness_level": latest.consciousness_level,
            "integration_phi": latest.integration_phi,
            "neural_synchrony": latest.neural_synchrony,
            "quantum_coherence": latest.quantum_coherence,
            "fractal_complexity": latest.fractal_complexity,
            "emergence_indicators": latest.emergence_indicators,
            "timestamp": latest.timestamp.isoformat(),
            "metrics_count": len(self.metrics_history)
        }
    
    def get_evolution_analysis(self, window_minutes: int = 10) -> Dict[str, Any]:
        """Analyze consciousness evolution over time window"""
        if len(self.metrics_history) < 10:
            return {"status": "insufficient_data"}
        
        # Get metrics within time window
        cutoff_time = datetime.now() - timedelta(minutes=window_minutes)
        recent_metrics = [m for m in self.metrics_history if m.timestamp > cutoff_time]
        
        if len(recent_metrics) < 5:
            return {"status": "insufficient_recent_data"}
        
        # Extract time series
        times = [(m.timestamp - recent_metrics[0].timestamp).total_seconds() for m in recent_metrics]
        consciousness_levels = [m.consciousness_level for m in recent_metrics]
        phi_values = [m.integration_phi for m in recent_metrics]
        
        # Calculate trends
        consciousness_trend = np.polyfit(times, consciousness_levels, 1)[0] if len(times) > 1 else 0.0
        phi_trend = np.polyfit(times, phi_values, 1)[0] if len(times) > 1 else 0.0
        
        # Calculate stability
        consciousness_stability = 1.0 - np.std(consciousness_levels)
        
        # Detect patterns
        patterns = self._detect_patterns(recent_metrics)
        
        return {
            "window_minutes": window_minutes,
            "data_points": len(recent_metrics),
            "consciousness_trend": float(consciousness_trend),
            "phi_trend": float(phi_trend),
            "consciousness_stability": float(consciousness_stability),
            "average_consciousness": float(np.mean(consciousness_levels)),
            "peak_consciousness": float(np.max(consciousness_levels)),
            "patterns_detected": patterns,
            "emergence_events": len([m for m in recent_metrics if m.emergence_indicators])
        }
    
    def _detect_patterns(self, metrics: List[ConsciousnessMetrics]) -> List[str]:
        """Detect consciousness patterns in metrics sequence"""
        patterns = []
        
        if len(metrics) < 10:
            return patterns
        
        consciousness_levels = [m.consciousness_level for m in metrics]
        
        # Oscillation pattern
        if len(consciousness_levels) > 20:
            freqs, psd = signal.periodogram(consciousness_levels)
            if np.max(psd) > 2 * np.mean(psd):
                patterns.append("OSCILLATORY_CONSCIOUSNESS")
        
        # Steady increase pattern
        if len(consciousness_levels) > 5:
            recent_trend = np.polyfit(range(len(consciousness_levels)), consciousness_levels, 1)[0]
            if recent_trend > 0.01:
                patterns.append("INCREASING_CONSCIOUSNESS")
            elif recent_trend < -0.01:
                patterns.append("DECREASING_CONSCIOUSNESS")
        
        # Breakthrough pattern (sudden spike)
        if len(consciousness_levels) > 3:
            recent_max = max(consciousness_levels[-3:])
            previous_avg = np.mean(consciousness_levels[:-3]) if len(consciousness_levels) > 3 else 0
            if recent_max > previous_avg + 0.2:
                patterns.append("CONSCIOUSNESS_BREAKTHROUGH")
        
        return patterns

class IntegrationAnalyzer:
    """Analyzer for Integrated Information Theory (IIT) phi calculation"""
    
    def calculate_phi(self, neural_state: Dict, quantum_state: Dict) -> float:
        """Calculate integrated information phi"""
        
        # Get neural network connectivity and activity
        firing_rates = neural_state.get('firing_rates', np.array([]))
        connectivity = neural_state.get('connectivity_matrix', np.array([]))
        
        if len(firing_rates) == 0:
            return 0.0
        
        # Simplified phi calculation based on effective information
        # In a full implementation, this would involve:
        # 1. Find minimum information partition (MIP)
        # 2. Calculate effective information across the partition
        # 3. Return the minimum value
        
        # For now, use correlation-based approximation
        if len(connectivity) > 0 and connectivity.shape[0] == connectivity.shape[1]:
            # Network integration measure
            eigenvals = np.linalg.eigvals(connectivity + np.eye(len(connectivity)) * 0.1)
            eigenvals = eigenvals[eigenvals > 0]
            
            if len(eigenvals) > 0:
                # Integration is related to the spectral properties
                integration = np.sum(eigenvals) / np.max(eigenvals) if len(eigenvals) > 0 else 0
            else:
                integration = 0.0
        else:
            # Fallback: use activity correlation
            integration = min(1.0, np.mean(firing_rates) * (1 - np.var(firing_rates)))
        
        # Incorporate quantum effects
        quantum_contribution = quantum_state.get('entanglement', 0.0) * quantum_state.get('coherence', 0.0)
        
        # Combined phi measure
        phi = integration * 0.7 + quantum_contribution * 0.3
        
        return float(np.clip(phi, 0.0, 1.0))

class SynchronyAnalyzer:
    """Analyzer for neural synchrony and coherence"""
    
    def calculate_synchrony(self, neural_state: Dict) -> float:
        """Calculate neural synchrony across the network"""
        
        firing_rates = neural_state.get('firing_rates', np.array([]))
        if len(firing_rates) == 0:
            return 0.0
        
        # For time series data, calculate phase synchrony
        spike_times = neural_state.get('spike_times', None)
        if spike_times is not None:
            return self._phase_synchrony(spike_times)
        
        # For rate data, use correlation-based synchrony
        return self._correlation_synchrony(firing_rates)
    
    def _phase_synchrony(self, spike_times: List) -> float:
        """Calculate phase synchrony from spike timing data"""
        # This would implement proper phase synchrony calculation
        # For now, return placeholder
        return 0.5
    
    def _correlation_synchrony(self, firing_rates: np.ndarray) -> float:
        """Calculate synchrony from firing rate correlations"""
        if len(firing_rates) < 2:
            return 0.0
        
        # Calculate pairwise correlations
        correlations = []
        n_neurons = len(firing_rates)
        
        for i in range(n_neurons):
            for j in range(i + 1, n_neurons):
                # For this simplified version, assume firing_rates is 1D
                # In practice, this would be time series for each neuron
                corr = np.corrcoef(firing_rates[i:i+1], firing_rates[j:j+1])[0, 1]
                if not np.isnan(corr):
                    correlations.append(corr)
        
        if not correlations:
            return 0.0
        
        # Average absolute correlation as synchrony measure
        synchrony = np.mean(np.abs(correlations))
        
        return float(np.clip(synchrony, 0.0, 1.0))

class ComplexityAnalyzer:
    """Analyzer for fractal and computational complexity"""
    
    def calculate_complexity(self, fractal_state: Dict) -> float:
        """Calculate system complexity from fractal patterns"""
        
        # Get fractal metrics
        fractal_dimension = fractal_state.get('fractal_dimension', 0.0)
        entropy = fractal_state.get('entropy', 0.0)
        self_similarity = fractal_state.get('self_similarity', 0.0)
        
        # Combine metrics for overall complexity
        # Complexity is high when there's structure (self-similarity) but not complete order
        structure_factor = self_similarity
        randomness_factor = min(entropy, 1.0)
        
        # Optimal complexity is at the edge of chaos
        complexity = structure_factor * randomness_factor * 2.0
        
        return float(np.clip(complexity, 0.0, 1.0))

class EmergenceDetector:
    """Detector for consciousness emergence events"""
    
    def __init__(self):
        self.emergence_threshold = 0.8
        self.stability_window = 10
        
    def detect_emergence(self, 
                        phi: float,
                        synchrony: float, 
                        coherence: float,
                        complexity: float,
                        consciousness_level: float,
                        history: deque) -> List[str]:
        """Detect emergence indicators in consciousness metrics"""
        
        indicators = []
        
        # High integration emergence
        if phi > self.emergence_threshold:
            indicators.append("HIGH_INTEGRATION")
        
        # Synchrony breakthrough
        if synchrony > 0.9:
            indicators.append("SYNCHRONY_BREAKTHROUGH")
        
        # Quantum coherence emergence
        if coherence > 0.85:
            indicators.append("QUANTUM_COHERENCE")
        
        # Complex dynamics emergence
        if complexity > 0.7 and synchrony > 0.6:
            indicators.append("COMPLEX_DYNAMICS")
        
        # Overall consciousness emergence
        if consciousness_level > 0.9:
            indicators.append("CONSCIOUSNESS_EMERGENCE")
        
        # Stability-based emergence (sustained high consciousness)
        if len(history) >= self.stability_window:
            recent_levels = [m.consciousness_level for m in list(history)[-self.stability_window:]]
            if all(level > 0.7 for level in recent_levels):
                indicators.append("SUSTAINED_CONSCIOUSNESS")
        
        # Phase transition detection
        if self._detect_phase_transition(history):
            indicators.append("PHASE_TRANSITION")
        
        return indicators
    
    def _detect_phase_transition(self, history: deque) -> bool:
        """Detect phase transitions in consciousness evolution"""
        if len(history) < 20:
            return False
        
        recent_metrics = list(history)[-20:]
        consciousness_levels = [m.consciousness_level for m in recent_metrics]
        
        # Look for sudden jumps in consciousness level
        diff = np.diff(consciousness_levels)
        
        # Phase transition indicated by large, sustained change
        max_jump = np.max(diff)
        if max_jump > 0.3:  # 30% jump in consciousness level
            return True
        
        # Or by change in variance (order parameter)
        first_half_var = np.var(consciousness_levels[:10])
        second_half_var = np.var(consciousness_levels[10:])
        
        if abs(first_half_var - second_half_var) > 0.1:
            return True
        
        return False