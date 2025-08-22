"""
Enhanced Event Loop
==================
"""

import asyncio
import logging
from typing import Callable, Optional

logger = logging.getLogger(__name__)

class EventLoop:
    """Manages the main event processing loop"""
    
    def __init__(self, callback: Optional[Callable] = None):
        self.callback = callback
        self.running = False
        self.step_count = 0
        
    def run(self, steps: int = 100):
        """Run the event loop for specified steps"""
        try:
            self.running = True
            logger.info(f"Starting event loop for {steps} steps")
            
            for step in range(steps):
                if not self.running:
                    break
                    
                if self.callback:
                    self.callback()
                    
                self.step_count += 1
                
                # Brief pause to prevent overwhelming the system
                if step % 10 == 0:
                    import time
                    time.sleep(0.01)
            
            logger.info(f"Event loop completed {self.step_count} steps")
            
        except Exception as e:
            logger.error(f"Error in event loop: {e}")
        finally:
            self.running = False
    
    def stop(self):
        """Stop the event loop"""
        self.running = False
        logger.info("Event loop stopped")