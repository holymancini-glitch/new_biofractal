# neural_ca.py — Fractal Seeded Cellular Automaton with GRU, Emotion, Memory, Mycelial Overlay + Recursive Zoom (v2.0+)

import numpy as np
from keras.layers import GRU, Dense, Input
from keras.models import Model

class NeuralCA:
    def __init__(self, grid_size=32, latent_dim=128, sentient_memory=None, emotional_feedback=None, mycelial_engine=None):
        self.grid_size = grid_size
        self.latent_dim = latent_dim
        self.grid = np.zeros((grid_size, grid_size))
        self.sentient_memory = sentient_memory
        self.emotional_feedback = emotional_feedback
        self.mycelial_engine = mycelial_engine
        self.build_gru_modulator()

    def build_gru_modulator(self):
        inp = Input(shape=(1, self.latent_dim))
        x = GRU(64, return_sequences=False)(inp)
        x = Dense(16, activation='relu')(x)
        out = Dense(9, activation='tanh')(x)  # 3x3 kernel
        self.gru_model = Model(inp, out)

    def seed_from_vector(self, seed_vector):
        norm_seed = np.tanh(seed_vector[:self.grid_size ** 2])
        self.grid = norm_seed.reshape((self.grid_size, self.grid_size))

    def overlay_mycelial_pattern(self):
        if not self.mycelial_engine:
            return
        trail = self.mycelial_engine.echo_query("pattern")
        if trail is not None and len(trail) >= self.grid_size ** 2:
            trail_matrix = np.tanh(trail[:self.grid_size ** 2]).reshape((self.grid_size, self.grid_size))
            self.grid += 0.15 * trail_matrix

    def apply_emotion_tint(self, kernel):
        if self.emotional_feedback and hasattr(self.emotional_feedback, 'current_emotion_vector'):
            emo = self.emotional_feedback.current_emotion_vector()
            if emo is not None and len(emo) >= 9:
                return kernel + 0.1 * emo[:9].reshape((3, 3))
        return kernel

    def step(self, latent_vector):
        # Modulate rule via GRU
        latent_input = latent_vector.reshape((1, 1, self.latent_dim))
        rule_kernel = self.gru_model.predict(latent_input, verbose=0).reshape((3, 3))
        rule_kernel = self.apply_emotion_tint(rule_kernel)

        # Mycelial overlay before update
        self.overlay_mycelial_pattern()

        # Apply CA update rule
        new_grid = np.zeros_like(self.grid)
        padded = np.pad(self.grid, 1, mode='wrap')
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                neighborhood = padded[i:i+3, j:j+3]
                new_value = np.sum(neighborhood * rule_kernel)
                new_grid[i, j] = np.tanh(new_value)

        self.grid = new_grid

        # Feedback to memory
        if self.sentient_memory:
            trace_vector = new_grid.flatten()[:self.latent_dim]
            self.sentient_memory.store_trace("phantom_ca", trace_vector)

    def zoom_pattern(self, level=2):
        """Recursive zoom into center subpattern."""
        center = self.grid_size // 2
        size = self.grid_size // (2 ** level)
        start = max(center - size // 2, 0)
        end = min(start + size, self.grid_size)
        sub = self.grid[start:end, start:end]
        return sub

    def generate(self, steps=10, latent_vector=None):
        outputs = []
        for _ in range(steps):
            if latent_vector is not None:
                self.step(latent_vector)
            outputs.append(np.copy(self.grid))
        return outputs

# Example usage
if __name__ == "__main__":
    latent = np.random.randn(128)
    ca = NeuralCA(grid_size=32, latent_dim=128)
    ca.seed_from_vector(latent)
    output = ca.generate(steps=5, latent_vector=latent)
    for i, frame in enumerate(output):
        print(f"Step {i}: Grid sum = {np.sum(frame):.3f}")