# phase_attention_modulator.py — Modulates Attention by Internal Phase State

import torch
import torch.nn as nn

class PhaseAttentionModulator(nn.Module):
    def __init__(self, hidden_size, phase_vector_dim=8):
        super(PhaseAttentionModulator, self).__init__()
        self.phase_embedding = nn.Linear(phase_vector_dim, hidden_size)
        self.gate = nn.Sequential(
            nn.Linear(hidden_size * 2, hidden_size),
            nn.Tanh(),
            nn.Linear(hidden_size, 1),
            nn.Sigmoid()
        )

    def forward(self, attention_weights, hidden_state, phase_vector):
        # phase_vector: (batch, phase_vector_dim)
        phase_encoded = self.phase_embedding(phase_vector)  # (batch, hidden_size)
        combined = torch.cat((hidden_state, phase_encoded), dim=-1)  # (batch, hidden_size * 2)
        mod_gate = self.gate(combined)  # (batch, 1)
        modulated_weights = attention_weights * mod_gate  # scaled attention
        return modulated_weights, mod_gate