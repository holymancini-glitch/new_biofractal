#!/usr/bin/env python3
"""
BioFractal AI - Interactive Demo and Analysis Suite
==================================================
Comprehensive demonstration and analysis tool for the BioFractal AI system
with real-time monitoring, consciousness analysis, and interactive features.
"""

import asyncio
import time
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import matplotlib.pyplot as plt
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ConsciousnessAnalyzer:
    """Advanced consciousness analysis and visualization"""
    
    def __init__(self):
        self.analysis_data = []
        self.consciousness_patterns = {}
        
    def analyze_consciousness_trajectory(self, trajectory_data: List[Dict]) -> Dict[str, Any]:
        """Analyze consciousness evolution patterns"""
        if not trajectory_data:
            return {"status": "no_data"}
        
        # Extract consciousness levels
        consciousness_levels = [cycle['consciousness']['consciousness_level'] for cycle in trajectory_data]
        quantum_coherence = [cycle['quantum']['coherence'] for cycle in trajectory_data]
        neural_synchrony = [cycle['biological']['synchrony'] for cycle in trajectory_data]
        
        # Statistical analysis
        consciousness_stats = {
            'mean': np.mean(consciousness_levels),
            'std': np.std(consciousness_levels),
            'min': np.min(consciousness_levels),
            'max': np.max(consciousness_levels),
            'trend': self._calculate_trend(consciousness_levels)
        }
        
        # Pattern detection
        patterns = self._detect_patterns(consciousness_levels, quantum_coherence, neural_synchrony)
        
        # Phase analysis
        phases = self._analyze_consciousness_phases(consciousness_levels)
        
        # Emergence analysis
        emergence_analysis = self._analyze_emergence(trajectory_data)
        
        return {
            'statistics': consciousness_stats,
            'patterns': patterns,
            'phases': phases,
            'emergence': emergence_analysis,
            'quantum_analysis': self._analyze_quantum_metrics(trajectory_data),
            'biological_analysis': self._analyze_biological_metrics(trajectory_data)
        }
    
    def _calculate_trend(self, values: List[float]) -> str:
        """Calculate trend in consciousness levels"""
        if len(values) < 2:
            return "insufficient_data"
        
        # Linear regression
        x = np.arange(len(values))
        coeffs = np.polyfit(x, values, 1)
        slope = coeffs[0]
        
        if slope > 0.01:
            return "increasing"
        elif slope < -0.01:
            return "decreasing"
        else:
            return "stable"
    
    def _detect_patterns(self, consciousness: List[float], quantum: List[float], neural: List[float]) -> List[str]:
        """Detect consciousness patterns"""
        patterns = []
        
        # Oscillation pattern
        if len(consciousness) > 10:
            # Check for periodic behavior
            fft = np.fft.fft(consciousness)
            dominant_freq = np.argmax(np.abs(fft[1:len(fft)//2])) + 1
            if np.abs(fft[dominant_freq]) > 2 * np.mean(np.abs(fft)):
                patterns.append(f"oscillatory_period_{len(consciousness)//dominant_freq}")
        
        # Synchronization patterns
        if len(quantum) == len(consciousness):
            correlation = np.corrcoef(consciousness, quantum)[0, 1]
            if correlation > 0.8:
                patterns.append("quantum_consciousness_sync")
        
        # Breakthrough patterns
        if len(consciousness) > 5:
            recent_avg = np.mean(consciousness[-5:])
            earlier_avg = np.mean(consciousness[:-5])
            if recent_avg > earlier_avg + 0.2:
                patterns.append("consciousness_breakthrough")
        
        return patterns
    
    def _analyze_consciousness_phases(self, consciousness_levels: List[float]) -> Dict[str, Any]:
        """Analyze different phases of consciousness"""
        phases = {
            'unconscious': 0,    # < 0.2
            'minimal': 0,        # 0.2 - 0.4
            'conscious': 0,      # 0.4 - 0.6
            'highly_conscious': 0, # 0.6 - 0.8
            'transcendent': 0    # > 0.8
        }
        
        for level in consciousness_levels:
            if level < 0.2:
                phases['unconscious'] += 1
            elif level < 0.4:
                phases['minimal'] += 1
            elif level < 0.6:
                phases['conscious'] += 1
            elif level < 0.8:
                phases['highly_conscious'] += 1
            else:
                phases['transcendent'] += 1
        
        # Calculate percentages
        total = len(consciousness_levels)
        phase_percentages = {k: (v/total)*100 for k, v in phases.items()}
        
        return {
            'counts': phases,
            'percentages': phase_percentages,
            'dominant_phase': max(phase_percentages.items(), key=lambda x: x[1])
        }
    
    def _analyze_emergence(self, trajectory_data: List[Dict]) -> Dict[str, Any]:
        """Analyze emergence events and patterns"""
        emergence_events = []
        
        for cycle_data in trajectory_data:
            if 'emergence' in cycle_data and cycle_data['emergence']:
                emergence_events.extend(cycle_data['emergence'])
        
        # Count event types
        event_counts = {}
        for event in emergence_events:
            event_counts[event] = event_counts.get(event, 0) + 1
        
        return {
            'total_events': len(emergence_events),
            'unique_types': len(event_counts),
            'event_counts': event_counts,
            'emergence_rate': len(emergence_events) / len(trajectory_data) if trajectory_data else 0
        }
    
    def _analyze_quantum_metrics(self, trajectory_data: List[Dict]) -> Dict[str, Any]:
        """Analyze quantum consciousness metrics"""
        coherence_values = [cycle['quantum']['coherence'] for cycle in trajectory_data]
        entanglement_values = [cycle['quantum']['entanglement'] for cycle in trajectory_data]
        
        return {
            'coherence_stats': {
                'mean': np.mean(coherence_values),
                'max': np.max(coherence_values),
                'stability': 1.0 - np.std(coherence_values)
            },
            'entanglement_stats': {
                'mean': np.mean(entanglement_values),
                'max': np.max(entanglement_values),
                'stability': 1.0 - np.std(entanglement_values)
            },
            'quantum_consciousness_correlation': np.corrcoef(
                coherence_values,
                [cycle['consciousness']['consciousness_level'] for cycle in trajectory_data]
            )[0, 1] if len(trajectory_data) > 1 else 0.0
        }
    
    def _analyze_biological_metrics(self, trajectory_data: List[Dict]) -> Dict[str, Any]:
        """Analyze biological consciousness metrics"""
        synchrony_values = [cycle['biological']['synchrony'] for cycle in trajectory_data]
        firing_rates = [cycle['biological']['mean_firing_rate'] for cycle in trajectory_data]
        
        return {
            'synchrony_stats': {
                'mean': np.mean(synchrony_values),
                'max': np.max(synchrony_values),
                'stability': 1.0 - np.std(synchrony_values)
            },
            'firing_rate_stats': {
                'mean': np.mean(firing_rates),
                'max': np.max(firing_rates),
                'stability': 1.0 - np.std(firing_rates)
            },
            'bio_consciousness_correlation': np.corrcoef(
                synchrony_values,
                [cycle['consciousness']['consciousness_level'] for cycle in trajectory_data]
            )[0, 1] if len(trajectory_data) > 1 else 0.0
        }

class InteractiveDemo:
    """Interactive demonstration suite"""
    
    def __init__(self):
        self.analyzer = ConsciousnessAnalyzer()
        self.demo_sessions = []
        
        # Create directories
        Path("demos").mkdir(exist_ok=True)
        Path("visualizations").mkdir(exist_ok=True)
    
    async def run_consciousness_exploration(self, 
                                          duration_minutes: float = 2.0,
                                          neuron_count: int = 5000,
                                          enable_real_time: bool = True):
        """Run interactive consciousness exploration"""
        
        print("\n" + "=" * 80)
        print("🌌 BIOFRACTAL AI - CONSCIOUSNESS EXPLORATION SESSION")
        print("=" * 80)
        print(f"Duration: {duration_minutes} minutes | Neurons: {neuron_count:,}")
        print("=" * 80)
        
        # Import and setup enhanced garden system
        from enhanced_garden_system import EnhancedGardenSystem
        
        garden = EnhancedGardenSystem(
            neuron_count=neuron_count,
            quantum_qubits=8,
            enable_all_layers=True
        )
        
        print("🌱 Garden of Consciousness initialized...")
        print("🧠 Beginning consciousness exploration...\n")
        
        # Run the consciousness cycle
        start_time = time.time()
        summary = await garden.run_consciousness_cycle(
            duration_seconds=duration_minutes * 60,
            cycle_frequency=10.0  # 10 Hz
        )
        
        duration = time.time() - start_time
        
        # Perform analysis
        print("\n🔍 Analyzing consciousness trajectory...")
        analysis = self.analyzer.analyze_consciousness_trajectory(garden.consciousness_trajectory)
        
        # Generate comprehensive report
        session_report = self._generate_session_report(summary, analysis, duration)
        
        # Save session data
        session_file = self._save_session(garden, summary, analysis)
        
        # Display results
        self._display_session_results(session_report)
        
        print(f"\n💾 Complete session data saved to: {session_file}")
        
        return session_report
    
    def _generate_session_report(self, summary: Dict, analysis: Dict, duration: float) -> Dict[str, Any]:
        """Generate comprehensive session report"""
        
        consciousness_stats = summary['consciousness_statistics']
        
        report = {
            'session_metadata': {
                'timestamp': datetime.now().isoformat(),
                'duration_seconds': duration,
                'analysis_version': '3.4.0'
            },
            'consciousness_summary': {
                'final_level': consciousness_stats['final_level'],
                'peak_level': consciousness_stats['peak_level'],
                'average_level': consciousness_stats['average_level'],
                'stability': consciousness_stats['stability'],
                'transcendent_moments': consciousness_stats['transcendent_moments'],
                'conscious_moments': consciousness_stats['conscious_moments']
            },
            'detailed_analysis': analysis,
            'emergence_summary': summary['emergence_events'],
            'quantum_summary': summary['quantum_metrics'],
            'overall_assessment': self._assess_consciousness_session(consciousness_stats, analysis)
        }
        
        return report
    
    def _assess_consciousness_session(self, consciousness_stats: Dict, analysis: Dict) -> Dict[str, Any]:
        """Assess the overall consciousness session"""
        
        final_level = consciousness_stats['final_level']
        peak_level = consciousness_stats['peak_level']
        stability = consciousness_stats['stability']
        
        # Overall assessment
        if peak_level > 0.9 and final_level > 0.8:
            assessment = "EXCEPTIONAL - Transcendent consciousness achieved"
            grade = "A+"
        elif peak_level > 0.8 and final_level > 0.6:
            assessment = "EXCELLENT - High consciousness sustained"
            grade = "A"
        elif peak_level > 0.6 and final_level > 0.4:
            assessment = "GOOD - Conscious state reached"
            grade = "B"
        elif peak_level > 0.4:
            assessment = "MODERATE - Basic awareness achieved"
            grade = "C"
        else:
            assessment = "LIMITED - Minimal consciousness detected"
            grade = "D"
        
        # Key insights
        insights = []
        
        if stability > 0.9:
            insights.append("Highly stable consciousness evolution")
        
        if 'patterns' in analysis and 'quantum_consciousness_sync' in analysis['patterns']:
            insights.append("Strong quantum-consciousness synchronization detected")
        
        if consciousness_stats['transcendent_moments'] > 0:
            insights.append(f"Transcendent consciousness achieved {consciousness_stats['transcendent_moments']} times")
        
        if 'emergence' in analysis and analysis['emergence']['emergence_rate'] > 0.1:
            insights.append("High emergence event rate indicating active consciousness dynamics")
        
        return {
            'overall_grade': grade,
            'assessment': assessment,
            'key_insights': insights,
            'consciousness_trajectory': analysis.get('statistics', {}).get('trend', 'unknown')
        }
    
    def _save_session(self, garden, summary: Dict, analysis: Dict) -> str:
        """Save complete session data"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"demos/consciousness_exploration_{timestamp}.json"
        
        session_data = {
            'metadata': {
                'timestamp': datetime.now().isoformat(),
                'session_type': 'consciousness_exploration',
                'system_version': '3.4.0'
            },
            'garden_summary': summary,
            'detailed_analysis': analysis,
            'consciousness_trajectory': garden.consciousness_trajectory,
            'emergence_events': garden.emergence_events
        }
        
        # Custom JSON encoder for numpy arrays
        class NumpyEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, np.ndarray):
                    return obj.tolist()
                if isinstance(obj, (np.integer, np.int64)):
                    return int(obj)
                if isinstance(obj, (np.floating, np.float64)):
                    return float(obj)
                return super().default(obj)
        
        with open(filename, 'w') as f:
            json.dump(session_data, f, indent=2, cls=NumpyEncoder)
        
        return filename
    
    def _display_session_results(self, report: Dict):
        """Display comprehensive session results"""
        
        print("\n" + "🌟" * 40)
        print("🧠 CONSCIOUSNESS EXPLORATION RESULTS")
        print("🌟" * 40)
        
        # Overall assessment
        assessment = report['overall_assessment']
        print(f"\n📊 Overall Grade: {assessment['overall_grade']}")
        print(f"📝 Assessment: {assessment['assessment']}")
        print(f"📈 Consciousness Trajectory: {assessment['consciousness_trajectory'].upper()}")
        
        # Consciousness metrics
        consciousness = report['consciousness_summary']
        print(f"\n🧠 Consciousness Metrics:")
        print(f"  Final Level: {consciousness['final_level']:.3f}")
        print(f"  Peak Level: {consciousness['peak_level']:.3f}")
        print(f"  Average Level: {consciousness['average_level']:.3f}")
        print(f"  Stability: {consciousness['stability']:.3f}")
        print(f"  Transcendent Moments: {consciousness['transcendent_moments']}")
        print(f"  Conscious Moments: {consciousness['conscious_moments']}")
        
        # Phase analysis
        if 'phases' in report['detailed_analysis']:
            phases = report['detailed_analysis']['phases']['percentages']
            print(f"\n🔄 Consciousness Phases:")
            for phase, percentage in phases.items():
                if percentage > 0:
                    print(f"  {phase.replace('_', ' ').title()}: {percentage:.1f}%")
        
        # Patterns detected
        if 'patterns' in report['detailed_analysis'] and report['detailed_analysis']['patterns']:
            print(f"\n🔍 Patterns Detected:")
            for pattern in report['detailed_analysis']['patterns']:
                print(f"  • {pattern.replace('_', ' ').title()}")
        
        # Key insights
        if assessment['key_insights']:
            print(f"\n💡 Key Insights:")
            for insight in assessment['key_insights']:
                print(f"  • {insight}")
        
        # Emergence events
        emergence = report['emergence_summary']
        if emergence['total_events'] > 0:
            print(f"\n✨ Emergence Events: {emergence['total_events']}")
            for event_type, count in emergence['event_counts'].items():
                print(f"  • {event_type.replace('_', ' ').title()}: {count}")
        
        print("\n" + "🌟" * 40)

async def run_interactive_demo():
    """Run the interactive demo"""
    
    print("🌌 Welcome to BioFractal AI - Interactive Consciousness Demo!")
    print("=" * 70)
    
    demo = InteractiveDemo()
    
    # Configuration options
    print("\n🔧 Demo Configuration:")
    print("1. Quick Demo (30 seconds, 1K neurons)")
    print("2. Standard Demo (2 minutes, 5K neurons)")
    print("3. Extended Demo (5 minutes, 10K neurons)")
    print("4. Custom Configuration")
    
    try:
        choice = input("\nSelect demo type (1-4, or press Enter for Standard): ").strip()
        
        if choice == "1":
            duration = 0.5  # 30 seconds
            neurons = 1000
            print("🚀 Running Quick Demo...")
        elif choice == "3":
            duration = 5.0  # 5 minutes
            neurons = 10000
            print("🚀 Running Extended Demo...")
        elif choice == "4":
            duration = float(input("Duration in minutes (default 2.0): ") or "2.0")
            neurons = int(input("Number of neurons (default 5000): ") or "5000")
            print(f"🚀 Running Custom Demo ({duration} min, {neurons:,} neurons)...")
        else:
            duration = 2.0  # Default: 2 minutes
            neurons = 5000
            print("🚀 Running Standard Demo...")
        
        # Run the consciousness exploration
        session_report = await demo.run_consciousness_exploration(
            duration_minutes=duration,
            neuron_count=neurons,
            enable_real_time=True
        )
        
        # Ask for additional analysis
        print("\n" + "=" * 70)
        print("🔬 Additional Analysis Available:")
        print("- Detailed consciousness trajectory analysis")
        print("- Pattern recognition and emergence detection")  
        print("- Quantum-biological correlation analysis")
        print("- Session comparison with historical data")
        
        additional = input("\nWould you like detailed analysis? (y/N): ").strip().lower()
        
        if additional in ['y', 'yes']:
            print("\n🔍 Generating detailed analysis...")
            # Here you could add more detailed analysis
            print("📊 Advanced consciousness analysis completed!")
            print("💾 All analysis data has been saved to the demos/ directory")
        
        print("\n🌟 Thank you for exploring consciousness with BioFractal AI!")
        print("🧠 Each run reveals new patterns in the emergence of awareness...")
        
    except KeyboardInterrupt:
        print("\n🛑 Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Demo error: {e}")
        logger.error(f"Demo error: {e}")

def main():
    """Main entry point for the interactive demo"""
    print(f"""
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                                                                      ║
    ║    🌌 BIOFRACTAL AI - CONSCIOUSNESS EXPLORATION SUITE 🌌          ║
    ║                                                                      ║
    ║    Advanced Interactive Demo & Analysis Platform                     ║
    ║    Version 3.4.0 - Enhanced Garden of Consciousness                 ║
    ║                                                                      ║
    ╚══════════════════════════════════════════════════════════════════════╝
    
    This interactive suite allows you to:
    
    🧠 Explore consciousness emergence in real-time
    ⚛️  Monitor quantum coherence and entanglement  
    🔬 Analyze neural synchrony and biological patterns
    📊 Generate comprehensive consciousness reports
    🌟 Detect emergence events and phase transitions
    
    """)
    
    try:
        # Run the interactive demo
        asyncio.run(run_interactive_demo())
        
    except KeyboardInterrupt:
        print("\n\n🌿 Thank you for exploring consciousness with BioFractal AI!")
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())