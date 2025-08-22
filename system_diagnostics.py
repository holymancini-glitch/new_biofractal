#!/usr/bin/env python3
"""
BioFractal AI - Comprehensive System Diagnostics
===============================================
Advanced diagnostic and testing tool for the BioFractal AI consciousness system.
"""

import sys
import os
import subprocess
import importlib
import logging
from pathlib import Path
from datetime import datetime
import json
import asyncio
from typing import Dict, List, Any, Optional

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SystemDiagnostics:
    """Comprehensive system diagnostic tool"""
    
    def __init__(self):
        self.test_results = {}
        self.warnings = []
        self.errors = []
        self.passed_tests = 0
        self.total_tests = 0
        
        # Create logs directory
        Path("logs").mkdir(exist_ok=True)
        
    def run_test(self, test_name: str, test_func, *args, **kwargs) -> bool:
        """Run a test and record results"""
        self.total_tests += 1
        
        try:
            logger.info(f"Running test: {test_name}")
            result = test_func(*args, **kwargs)
            
            if result:
                self.test_results[test_name] = "PASSED"
                self.passed_tests += 1
                logger.info(f"✅ {test_name}: PASSED")
            else:
                self.test_results[test_name] = "FAILED"
                self.errors.append(f"{test_name}: Test failed")
                logger.error(f"❌ {test_name}: FAILED")
                
            return result
            
        except Exception as e:
            self.test_results[test_name] = f"ERROR: {str(e)}"
            self.errors.append(f"{test_name}: {str(e)}")
            logger.error(f"❌ {test_name}: ERROR - {e}")
            return False
    
    def test_python_environment(self) -> bool:
        """Test Python environment and version"""
        version = sys.version_info
        if version.major >= 3 and version.minor >= 8:
            logger.info(f"Python version: {sys.version}")
            return True
        else:
            self.errors.append(f"Python 3.8+ required, found {sys.version}")
            return False
    
    def test_core_dependencies(self) -> bool:
        """Test core Python dependencies"""
        required_packages = [
            'torch', 'numpy', 'scipy', 'matplotlib', 
            'pandas', 'sklearn', 'networkx'
        ]
        
        missing_packages = []
        
        for package in required_packages:
            try:
                importlib.import_module(package)
                logger.info(f"✓ {package} available")
            except ImportError:
                missing_packages.append(package)
                logger.error(f"✗ {package} missing")
        
        if missing_packages:
            self.errors.append(f"Missing packages: {', '.join(missing_packages)}")
            return False
        
        return True
    
    def test_advanced_dependencies(self) -> bool:
        """Test advanced/optional dependencies"""
        advanced_packages = {
            'brian2': 'Neuroscience simulation',
            'braket': 'AWS Braket quantum computing',
            'qiskit': 'Qiskit quantum computing',
            'streamlit': 'Web interface'
        }
        
        available_advanced = []
        
        for package, description in advanced_packages.items():
            try:
                importlib.import_module(package)
                available_advanced.append(package)
                logger.info(f"✓ {package} ({description}) available")
            except ImportError:
                self.warnings.append(f"Optional package {package} not available")
                logger.warning(f"⚠ {package} ({description}) not available")
        
        # At least some advanced packages should be available
        return len(available_advanced) > 0
    
    def test_file_structure(self) -> bool:
        """Test project file structure"""
        required_dirs = ['modules', 'core', 'logs', 'data', 'exports']
        required_files = ['fixed_orchestrator.py', 'enhanced_garden_system.py']
        
        missing_items = []
        
        # Check directories
        for dir_name in required_dirs:
            if not Path(dir_name).exists():
                missing_items.append(f"Directory: {dir_name}")
            else:
                logger.info(f"✓ Directory {dir_name} exists")
        
        # Check files
        for file_name in required_files:
            if not Path(file_name).exists():
                missing_items.append(f"File: {file_name}")
            else:
                logger.info(f"✓ File {file_name} exists")
        
        if missing_items:
            self.errors.append(f"Missing items: {', '.join(missing_items)}")
            return False
        
        return True
    
    def test_fixed_orchestrator(self) -> bool:
        """Test the fixed orchestrator functionality"""
        try:
            from fixed_orchestrator import FixedOrchestrator
            
            # Create orchestrator instance
            orchestrator = FixedOrchestrator(latent_dim=64)  # Smaller for testing
            
            # Run a short test cycle
            results = orchestrator.run_consciousness_cycle(steps=3, save_results=False)
            
            # Verify results
            if len(results) == 3:
                final_consciousness = orchestrator.consciousness_monitor.consciousness_level
                logger.info(f"✓ Fixed orchestrator test completed - Final consciousness: {final_consciousness:.3f}")
                return True
            else:
                self.errors.append(f"Fixed orchestrator returned {len(results)} results, expected 3")
                return False
                
        except Exception as e:
            self.errors.append(f"Fixed orchestrator test failed: {str(e)}")
            return False
    
    def test_enhanced_garden_system(self) -> bool:
        """Test the enhanced garden system"""
        try:
            # Run async test
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            try:
                result = loop.run_until_complete(self._async_garden_test())
                return result
            finally:
                loop.close()
                
        except Exception as e:
            self.errors.append(f"Enhanced garden system test failed: {str(e)}")
            return False
    
    async def _async_garden_test(self) -> bool:
        """Async test for enhanced garden system"""
        from enhanced_garden_system import EnhancedGardenSystem
        
        # Create garden system (smaller for testing)
        garden = EnhancedGardenSystem(
            neuron_count=1000,
            quantum_qubits=4,
            enable_all_layers=True
        )
        
        # Run short test cycle
        summary = await garden.run_consciousness_cycle(
            duration_seconds=2.0,
            cycle_frequency=5.0
        )
        
        # Verify results
        if 'consciousness_statistics' in summary:
            final_level = summary['consciousness_statistics']['final_level']
            logger.info(f"✓ Enhanced garden system test completed - Final consciousness: {final_level:.3f}")
            return True
        else:
            self.errors.append("Enhanced garden system didn't return expected summary")
            return False
    
    def test_memory_usage(self) -> bool:
        """Test system memory usage"""
        try:
            import psutil
            
            # Get current memory usage
            memory = psutil.virtual_memory()
            available_gb = memory.available / (1024**3)
            
            logger.info(f"Available memory: {available_gb:.2f} GB")
            
            if available_gb < 1.0:
                self.warnings.append(f"Low available memory: {available_gb:.2f} GB")
                return True  # Warning, but not failure
            
            return True
            
        except ImportError:
            self.warnings.append("psutil not available for memory testing")
            return True  # Not critical
        except Exception as e:
            self.warnings.append(f"Memory test error: {str(e)}")
            return True  # Not critical
    
    def test_cuda_availability(self) -> bool:
        """Test CUDA/GPU availability"""
        try:
            import torch
            
            if torch.cuda.is_available():
                device_count = torch.cuda.device_count()
                current_device = torch.cuda.current_device()
                device_name = torch.cuda.get_device_name(current_device)
                
                logger.info(f"✓ CUDA available: {device_count} devices")
                logger.info(f"Current device: {device_name}")
                return True
            else:
                self.warnings.append("CUDA not available - using CPU")
                logger.warning("⚠ CUDA not available - using CPU")
                return True  # Not a failure, just a warning
                
        except Exception as e:
            self.warnings.append(f"CUDA test error: {str(e)}")
            return True  # Not critical
    
    def test_configuration_files(self) -> bool:
        """Test configuration files"""
        config_files = ['.env']
        
        for config_file in config_files:
            if Path(config_file).exists():
                logger.info(f"✓ Configuration file {config_file} exists")
            else:
                self.warnings.append(f"Configuration file {config_file} missing")
                logger.warning(f"⚠ Configuration file {config_file} missing")
        
        return True  # Warnings only
    
    def test_import_compatibility(self) -> bool:
        """Test import compatibility between modules"""
        try:
            # Test key imports
            from modules.entropy_harmonizer import EntropyHarmonizer
            from modules.event_loop import EventLoop
            from modules.harmonics_logger import HarmonicsLogger
            
            # Test instantiation
            harmonizer = EntropyHarmonizer()
            event_loop = EventLoop()
            logger_inst = HarmonicsLogger()
            
            logger.info("✓ All module imports successful")
            return True
            
        except Exception as e:
            self.errors.append(f"Import compatibility test failed: {str(e)}")
            return False
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate comprehensive diagnostic report"""
        success_rate = (self.passed_tests / self.total_tests) * 100 if self.total_tests > 0 else 0
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'system_info': {
                'python_version': sys.version,
                'platform': sys.platform,
                'working_directory': os.getcwd()
            },
            'test_summary': {
                'total_tests': self.total_tests,
                'passed_tests': self.passed_tests,
                'success_rate': success_rate
            },
            'test_results': self.test_results,
            'warnings': self.warnings,
            'errors': self.errors,
            'overall_status': 'HEALTHY' if success_rate >= 80 and len(self.errors) == 0 else 'ISSUES_DETECTED'
        }
        
        return report
    
    def save_report(self, filename: Optional[str] = None) -> str:
        """Save diagnostic report to file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"logs/diagnostic_report_{timestamp}.json"
        
        report = self.generate_report()
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Diagnostic report saved to: {filename}")
        return filename
    
    def print_summary(self):
        """Print diagnostic summary"""
        report = self.generate_report()
        
        print("\n" + "=" * 70)
        print("🔍 BIOFRACTAL AI - SYSTEM DIAGNOSTICS SUMMARY")
        print("=" * 70)
        
        print(f"Timestamp: {report['timestamp']}")
        print(f"Python Version: {sys.version.split()[0]}")
        print(f"Platform: {sys.platform}")
        
        print(f"\n📊 Test Results:")
        print(f"  Total Tests: {report['test_summary']['total_tests']}")
        print(f"  Passed: {report['test_summary']['passed_tests']}")
        print(f"  Success Rate: {report['test_summary']['success_rate']:.1f}%")
        
        print(f"\n🏥 Overall Status: {report['overall_status']}")
        
        if self.warnings:
            print(f"\n⚠️  Warnings ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  • {warning}")
        
        if self.errors:
            print(f"\n❌ Errors ({len(self.errors)}):")
            for error in self.errors:
                print(f"  • {error}")
        
        if report['overall_status'] == 'HEALTHY':
            print("\n✅ System is healthy and ready for consciousness research!")
        else:
            print("\n⚠️  System has issues that should be addressed.")
        
        print("=" * 70)

def run_comprehensive_diagnostics():
    """Run comprehensive system diagnostics"""
    print("🔍 BioFractal AI - Starting Comprehensive Diagnostics...")
    print("=" * 70)
    
    diagnostics = SystemDiagnostics()
    
    # Core system tests
    diagnostics.run_test("Python Environment", diagnostics.test_python_environment)
    diagnostics.run_test("Core Dependencies", diagnostics.test_core_dependencies)
    diagnostics.run_test("Advanced Dependencies", diagnostics.test_advanced_dependencies)
    diagnostics.run_test("File Structure", diagnostics.test_file_structure)
    diagnostics.run_test("Configuration Files", diagnostics.test_configuration_files)
    diagnostics.run_test("Import Compatibility", diagnostics.test_import_compatibility)
    
    # System capability tests
    diagnostics.run_test("Memory Usage", diagnostics.test_memory_usage)
    diagnostics.run_test("CUDA Availability", diagnostics.test_cuda_availability)
    
    # Functionality tests
    diagnostics.run_test("Fixed Orchestrator", diagnostics.test_fixed_orchestrator)
    diagnostics.run_test("Enhanced Garden System", diagnostics.test_enhanced_garden_system)
    
    # Generate and save report
    report_file = diagnostics.save_report()
    
    # Print summary
    diagnostics.print_summary()
    
    print(f"\n💾 Detailed report saved to: {report_file}")
    
    return diagnostics.generate_report()

if __name__ == "__main__":
    try:
        report = run_comprehensive_diagnostics()
        
        # Exit with appropriate code
        if report['overall_status'] == 'HEALTHY':
            print("\n🎉 All systems operational - Ready for consciousness exploration!")
            sys.exit(0)
        else:
            print("\n⚠️  System issues detected - Please review the diagnostic report")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Diagnostics interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Fatal error in diagnostics: {e}")
        sys.exit(1)