"""
Enhanced Harmonics Logger
========================
"""

import logging
from typing import Any, Dict, List
from datetime import datetime
from pathlib import Path
import json

logger = logging.getLogger(__name__)

class HarmonicsLogger:
    """Logs harmonic and system data"""
    
    def __init__(self, log_file: str = "logs/harmonics.jsonl"):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(exist_ok=True)
        self.entries = []
        
    def log(self, tick: int, entropy_score: float, delta: float, coherence: float):
        """Log harmonics data"""
        try:
            entry = {
                'timestamp': datetime.now().isoformat(),
                'tick': tick,
                'entropy_score': entropy_score,
                'delta': float(delta),
                'coherence': coherence
            }
            
            self.entries.append(entry)
            
            # Write to file periodically
            if len(self.entries) % 10 == 0:
                self._write_to_file()
                
        except Exception as e:
            logger.error(f"Error logging harmonics: {e}")
    
    def _write_to_file(self):
        """Write entries to file"""
        try:
            with open(self.log_file, 'a') as f:
                for entry in self.entries:
                    f.write(json.dumps(entry) + '\n')
            self.entries = []  # Clear after writing
        except Exception as e:
            logger.error(f"Error writing harmonics log: {e}")
    
    def get_recent_entries(self, count: int = 100) -> List[Dict]:
        """Get recent log entries"""
        return self.entries[-count:] if count < len(self.entries) else self.entries