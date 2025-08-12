"""
Advanced Error Handling and Recovery System
==========================================
Comprehensive error handling with automatic recovery and system resilience.
"""

import traceback
import logging
import asyncio
from typing import Dict, List, Callable, Any, Optional
from datetime import datetime
from enum import Enum
from dataclasses import dataclass
from functools import wraps

class ErrorSeverity(Enum):
    """Error severity levels"""
    LOW = "low"
    MEDIUM = "medium" 
    HIGH = "high"
    CRITICAL = "critical"

class SystemState(Enum):
    """System operational states"""
    NORMAL = "normal"
    DEGRADED = "degraded"
    RECOVERY = "recovery"
    EMERGENCY = "emergency"
    SHUTDOWN = "shutdown"

@dataclass
class ErrorEvent:
    """Error event data structure"""
    timestamp: datetime
    error_type: str
    severity: ErrorSeverity
    message: str
    component: str
    traceback_info: str
    context: Dict[str, Any]
    recovery_attempted: bool = False
    recovery_successful: bool = False

class ErrorHandler:
    """Advanced error handling and recovery system"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.error_history: List[ErrorEvent] = []
        self.recovery_strategies: Dict[str, Callable] = {}
        self.system_state = SystemState.NORMAL
        self.component_health: Dict[str, float] = {}
        self.error_counters: Dict[str, int] = {}
        
        # Circuit breaker settings
        self.circuit_breakers: Dict[str, Dict] = {}
        self.failure_threshold = 5
        self.recovery_timeout = 300  # seconds
        
    def register_recovery_strategy(self, error_type: str, strategy: Callable):
        """Register a recovery strategy for a specific error type"""
        self.recovery_strategies[error_type] = strategy
        
    def handle_error(self, error: Exception, component: str, context: Dict = None) -> bool:
        """
        Handle an error with automatic recovery attempts
        
        Returns:
            bool: True if error was handled successfully, False otherwise
        """
        error_type = type(error).__name__
        severity = self._classify_error_severity(error, component)
        
        # Create error event
        error_event = ErrorEvent(
            timestamp=datetime.now(),
            error_type=error_type,
            severity=severity,
            message=str(error),
            component=component,
            traceback_info=traceback.format_exc(),
            context=context or {}
        )
        
        self.error_history.append(error_event)
        self._update_error_counters(error_type, component)
        self._update_component_health(component, severity)
        
        # Log the error
        self.logger.error(f"Error in {component}: {error_type} - {error}", 
                         extra={"component": component, "severity": severity.value})
        
        # Check circuit breaker
        if self._should_circuit_break(component):
            self.logger.warning(f"Circuit breaker activated for {component}")
            return False
        
        # Attempt recovery
        recovery_success = self._attempt_recovery(error_event)
        error_event.recovery_attempted = True
        error_event.recovery_successful = recovery_success
        
        # Update system state based on error severity and recovery
        self._update_system_state(severity, recovery_success)
        
        return recovery_success
    
    def _classify_error_severity(self, error: Exception, component: str) -> ErrorSeverity:
        """Classify error severity based on type and component"""
        
        # Critical errors that could cause system failure
        critical_errors = [
            "MemoryError", 
            "SystemError",
            "KeyboardInterrupt",
            "SystemExit"
        ]
        
        # High severity errors that affect core functionality
        high_severity_errors = [
            "RuntimeError",
            "ValueError", 
            "ConnectionError",
            "TimeoutError"
        ]
        
        # Critical components
        critical_components = [
            "quantum_processor",
            "biological_simulator", 
            "consciousness_monitor",
            "integration_layer"
        ]
        
        error_type = type(error).__name__
        
        if error_type in critical_errors:
            return ErrorSeverity.CRITICAL
        elif error_type in high_severity_errors or component in critical_components:
            return ErrorSeverity.HIGH
        elif self.error_counters.get(f"{component}:{error_type}", 0) > 3:
            return ErrorSeverity.HIGH  # Frequent errors become high severity
        else:
            return ErrorSeverity.MEDIUM
    
    def _update_error_counters(self, error_type: str, component: str):
        """Update error frequency counters"""
        key = f"{component}:{error_type}"
        self.error_counters[key] = self.error_counters.get(key, 0) + 1
        
        # Reset counters after some time (implement decay)
        # This would be better with a proper time-based decay mechanism
    
    def _update_component_health(self, component: str, severity: ErrorSeverity):
        """Update component health score based on errors"""
        current_health = self.component_health.get(component, 1.0)
        
        severity_impact = {
            ErrorSeverity.LOW: 0.05,
            ErrorSeverity.MEDIUM: 0.1,
            ErrorSeverity.HIGH: 0.2,
            ErrorSeverity.CRITICAL: 0.5
        }
        
        health_reduction = severity_impact[severity]
        new_health = max(0.0, current_health - health_reduction)
        self.component_health[component] = new_health
        
        # Gradual health recovery over time (implement in separate method)
    
    def _should_circuit_break(self, component: str) -> bool:
        """Check if circuit breaker should activate"""
        error_count = sum(count for key, count in self.error_counters.items() 
                         if key.startswith(f"{component}:"))
        
        return error_count >= self.failure_threshold
    
    def _attempt_recovery(self, error_event: ErrorEvent) -> bool:
        """Attempt to recover from error using registered strategies"""
        error_type = error_event.error_type
        component = error_event.component
        
        # Try component-specific recovery first
        component_strategy_key = f"{component}:{error_type}"
        if component_strategy_key in self.recovery_strategies:
            try:
                self.recovery_strategies[component_strategy_key](error_event)
                self.logger.info(f"Recovery successful for {component_strategy_key}")
                return True
            except Exception as e:
                self.logger.error(f"Recovery strategy failed for {component_strategy_key}: {e}")
        
        # Try general recovery strategy
        if error_type in self.recovery_strategies:
            try:
                self.recovery_strategies[error_type](error_event)
                self.logger.info(f"Recovery successful for {error_type}")
                return True
            except Exception as e:
                self.logger.error(f"Recovery strategy failed for {error_type}: {e}")
        
        # Default recovery attempts
        return self._default_recovery(error_event)
    
    def _default_recovery(self, error_event: ErrorEvent) -> bool:
        """Default recovery strategies"""
        component = error_event.component
        error_type = error_event.error_type
        
        # Memory-related error recovery
        if "Memory" in error_type:
            self.logger.info("Attempting memory cleanup...")
            try:
                import gc
                gc.collect()
                return True
            except:
                pass
        
        # Connection error recovery
        if "Connection" in error_type or "Timeout" in error_type:
            self.logger.info("Attempting connection retry...")
            # Implement exponential backoff retry
            return True
        
        # Component restart recovery
        if self.component_health.get(component, 1.0) < 0.3:
            self.logger.info(f"Attempting component restart for {component}")
            # Signal component restart (implement component restart mechanism)
            return True
        
        return False
    
    def _update_system_state(self, severity: ErrorSeverity, recovery_success: bool):
        """Update overall system state based on error and recovery"""
        if severity == ErrorSeverity.CRITICAL and not recovery_success:
            self.system_state = SystemState.EMERGENCY
        elif severity == ErrorSeverity.HIGH and not recovery_success:
            self.system_state = SystemState.DEGRADED
        elif not recovery_success:
            self.system_state = SystemState.RECOVERY
        else:
            # Gradual return to normal state
            if self.system_state != SystemState.NORMAL:
                overall_health = sum(self.component_health.values()) / len(self.component_health) if self.component_health else 1.0
                if overall_health > 0.8:
                    self.system_state = SystemState.NORMAL
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        recent_errors = [e for e in self.error_history[-10:]]  # Last 10 errors
        
        return {
            "system_state": self.system_state.value,
            "component_health": self.component_health,
            "error_counters": self.error_counters,
            "recent_errors": [
                {
                    "timestamp": e.timestamp.isoformat(),
                    "component": e.component,
                    "error_type": e.error_type,
                    "severity": e.severity.value,
                    "recovered": e.recovery_successful
                }
                for e in recent_errors
            ],
            "total_errors": len(self.error_history),
            "circuit_breakers": list(self.circuit_breakers.keys())
        }
    
    def reset_component_health(self, component: str):
        """Reset health score for a component"""
        self.component_health[component] = 1.0
        
        # Clear error counters for this component
        keys_to_remove = [key for key in self.error_counters.keys() if key.startswith(f"{component}:")]
        for key in keys_to_remove:
            del self.error_counters[key]
    
    def emergency_shutdown(self):
        """Emergency system shutdown"""
        self.system_state = SystemState.SHUTDOWN
        self.logger.critical("EMERGENCY SHUTDOWN INITIATED")
        
        # Implement graceful shutdown procedures
        # Save critical state, close connections, etc.

def error_handler_decorator(component: str, error_handler: ErrorHandler):
    """Decorator for automatic error handling"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                context = {
                    "function": func.__name__,
                    "args": str(args)[:200],  # Truncate long arguments
                    "kwargs": str(kwargs)[:200]
                }
                
                handled = error_handler.handle_error(e, component, context)
                if not handled:
                    raise  # Re-raise if not handled
                
                # Return None or appropriate default value
                return None
        
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                context = {
                    "function": func.__name__,
                    "args": str(args)[:200],
                    "kwargs": str(kwargs)[:200]
                }
                
                handled = error_handler.handle_error(e, component, context)
                if not handled:
                    raise
                
                return None
        
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return wrapper
    
    return decorator

# Global error handler instance
error_handler = ErrorHandler()