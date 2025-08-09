# latent_space.py
# Latent State Manager with Mirror Support for BioFractal AI v2.1 + Resonance Harmonization

import numpy as np

class LatentSpace:
    def __init__(self, shape=(64, 64, 8)):
        self.shape = shape
        self.real_state = np.zeros(shape, dtype=np.float32)
        self.mirror_state = np.zeros(shape, dtype=np.float32)
        self.mode = "real"  # or "mirror"
        self.gru_state = np.zeros((128,), dtype=np.float32)

    def inject(self, stimulus: np.ndarray):
        assert stimulus.shape == self.shape
        if self.mode == "real":
            self.real_state = stimulus
        else:
            self.mirror_state = stimulus

    def mutate(self, noise_scale=0.01):
        noise = np.random.normal(loc=0.0, scale=noise_scale, size=self.shape)
        if self.mode == "real":
            self.real_state = np.tanh(self.real_state + noise)
        else:
            self.mirror_state = np.tanh(self.mirror_state + noise)

    def switch_mode(self, target_mode):
        assert target_mode in ["real", "mirror"]
        self.mode = target_mode

    def read(self) -> np.ndarray:
        return self.real_state if self.mode == "real" else self.mirror_state

    def compare_states(self) -> float:
        difference = np.abs(self.real_state - self.mirror_state)
        return float(np.mean(difference))

    def harmonize_states(self, alpha=0.5):
        """
        Bring real and mirror states into resonance using weighted averaging.
        """
        blended = alpha * self.real_state + (1 - alpha) * self.mirror_state
        self.real_state = blended
        self.mirror_state = blended

    def inject_gru_feedback(self, vector: np.ndarray):
        """
        Incorporate GRU feedback vector into the active latent state.
        """
        assert vector.shape[0] == self.gru_state.shape[0]
        self.gru_state = 0.9 * self.gru_state + 0.1 * vector  # simple GRU-like blend
        feedback_scalar = np.mean(self.gru_state)
        modulation = feedback_scalar * 0.01
        if self.mode == "real":
            self.real_state += modulation
        else:
            self.mirror_state += modulation
        self.real_state = np.clip(self.real_state, -1.0, 1.0)
        self.mirror_state = np.clip(self.mirror_state, -1.0, 1.0)

    def reset(self):
        self.real_state = np.zeros(self.shape, dtype=np.float32)
        self.mirror_state = np.zeros(self.shape, dtype=np.float32)
        self.mode = "real"
        self.gru_state = np.zeros((128,), dtype=np.float32)

# Example usage
if __name__ == "__main__":
    latent = LatentSpace()
    latent.inject(np.random.rand(64, 64, 8).astype(np.float32))
    latent.mutate()
    latent.switch_mode("mirror")
    latent.inject(np.random.rand(64, 64, 8).astype(np.float32))
    diff = latent.compare_states()
    print("State difference:", diff)
    latent.harmonize_states()
    latent.inject_gru_feedback(np.random.rand(128).astype(np.float32))