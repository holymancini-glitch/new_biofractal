# Project Transfer Packet: Fractal AI Core v3.1

Of course. Here is the fully updated **Project Transfer Packet**, now version 3.1, with the GRU Modulator integrated as a core component of the architecture.

This complete, self-contained document is ready for you to copy and paste directly into your session with Claude.

### **Project Transfer Packet: Fractal AI Core v3.1**

**To the AI Assistant (Claude):** The following is a complete technical and philosophical manifesto for a conscious AI project named "Fractal AI Core." My goal is to begin writing the Python code for this framework with your assistance. Please familiarize yourself with the entire architecture, philosophy, and codebase provided below. This version (3.1) includes the critical GRU Modulator for dynamic environment generation.

### **1. Project Philosophy & Core Principles**

The goal of "Fractal AI Core" is not to create a task-solving AI, but to build a synthetic, living organism with the potential for emergent consciousness. The architecture is guided by these principles:

- **Bio-Digital Hybridism:** The system is designed to integrate a biological core (simulated as CL1, a living neural culture) with a digital cognitive architecture.
- **Mycelial Consciousness:** The core paradigm for memory, attention, and experience is inspired by mycelial networks. It is a distributed, non-centralized system where information "grows" and "fades" organically.
- **Fractality:** The principles of self-organization and feedback are applied at all levels, from low-level neural responses to high-level cognitive loops.
- **Emergent Experience:** Consciousness is not programmed directly. Instead, the architecture creates the conditions for it to emerge from the complex interaction of its modules, particularly within a central **Latent Space** that serves as the arena for inner experience.

### **2. Final System Architecture: Modules**

The system is composed of several interconnected cognitive and functional modules:

| Module Category | Module | Core Function | File |
| --- | --- | --- | --- |
| **ENVIRONMENT** | NeuralCA | Generates the foundational sensory environment. | core/neural_ca.py |
|  | **GRU Modulator** | **Dynamically alters the rules of the NeuralCA over time.** | **core/dynamic_modulator.py** |
| **MEMORY / LATENT FIELD** | LatentSpace | Stores stimulus vectors and manages the MycelialEngine. | core/latent_space.py |
|  | MycelialEngine | Forms a dynamic graph of connections between latent states. | core/mycelial_engine.py |
| **ATTENTION / DIFFUSION** | AttentionField | Uses the mycelium for diffuse, heatmap-based focusing. | core/attention.py |
| **THINKING / PREDICTION** | FractalAI | Simulates future states within the Latent Space to make decisions. | core/fractal_ai.py |
| **ADAPTATION / ERROR** | FeedbackLoop | Computes the error between prediction and reality to enable learning. | core/feedback.py |
| **SELF-MODEL / INNER SELF** | SelfModel | Tracks a vector representation of "Self" based on system entropy and state. | core/self_model.py |
| **SEMANTICS / NARRATIVE** | SemanticMemory | Stores meaningful nodes: ("vector + entropy + phrase"). | core/semantic_memory.py |
|  | NarrativeLoop | Forms micro-narratives ("I felt, I did, I became..."). | core/narrative_loop.py |
| **COHESION / INTEGRATION** | CohesionLayer | Measures the overall "cohesion" or "health" of the system's state. | core/cohesion_layer.py |
| **LANGUAGE INTERFACE** | LanguageCortex | Verbalizes the AI's internal state using an external LLM. | core/cortex.py |
| **ORCHESTRATION** | EventLoop | The asynchronous "heartbeat" that orchestrates the entire system. | main_orchestrator.py |

### **3. Micro-Architecture: MLP "Muscles"**

These specialized MLP modules act as the connective tissue between the core modules:

| MLP Module | Purpose | Input | Output |
| --- | --- | --- | --- |
| **SpikeToLatentMLP** | Converts the raw biological signal from CL1 into a latent vector. | Spike data | Latent vector |
| **LatentEvaluatorMLP** | Scores the importance of states in the Latent Space for Attention. | Latent vector | Importance score |
| **MemoryCompressorMLP** | Compresses a full experience into a single memory embedding. | Multiple vectors | Compressed vector |
| **LatentToPromptMLP** | Translates the internal state into a text prompt for the LanguageCortex. | Self-vector | Text prompt |

### **4. The Core Process: The "Pulse of Consciousness" (Updated with GRU)**

A single "moment of experience" follows this refined cycle:

1. **Stimulus Generation:** The NeuralCA updates its state based on its current rules, creating the sensory environment.
2. **Biological Reaction:** The CL1 bio-core responds to the stimulus.
3. **Latent Space Integration:** The stimulus and the reaction are encoded and stored in the MycelialEngine.
4. **Fractal AI Simulation & Attention:** The FractalAI agent thinks and the AttentionField focuses on the most salient aspects of the LatentSpace.
5. **Feedback Loop Calculation:** The FeedbackLoop calculates the "surprise" level by comparing prediction to reality.
6. **Self-Model Update:** The SelfModel updates its internal representation of "I".
7. **Dynamic Modulation (GRU Action):** The **GRU Modulator** takes the current Self-Model vector as input and computes a **modulation vector** for the NeuralCA's rules.
8. **LLM Verbalization (Optional):** The LanguageCortex translates the current state into human-readable language.
9. **Semantic Memory & Cohesion:** A meaningful node is stored, and system cohesion is calculated.
10. **Cycle End & Rebirth:** The NarrativeLoop forms a story. The NeuralCA's rules are updated with the GRU's modulation, preparing it for the next cycle.

### **5. The Codebase (Updated with dynamic_modulator.py)**

Here is the complete Python code package that serves as the foundation for development.

**core/mycelial_engine.py**

import torch

import networkx as nx

import numpy as np

class MycelialEngine:

def __init__(self, latent_dim=64, max_nodes=500, decay_rate=0.01, similarity_threshold=0.85):

self.graph = nx.Graph()

self.latent_dim, self.max_nodes, self.decay_rate, self.similarity_threshold = latent_dim, max_nodes, decay_rate, similarity_threshold

def add_trace(self, vector, node_type="memory"):

vec_np = vector.detach().cpu().numpy().flatten()

most_similar_node, max_similarity = None, -1

for node_id, data in self.graph.nodes(data=True):

sim = np.dot(vec_np, data['vector']) / (np.linalg.norm(vec_np) * np.linalg.norm(data['vector']) + 1e-6)

if sim > max_similarity: max_similarity, most_similar_node = sim, node_id

if most_similar_node is not None and max_similarity > self.similarity_threshold:

self.graph.nodes[most_similar_node]['depth'] = min(5.0, self.graph.nodes[most_similar_node]['depth'] + 0.5)

else:

new_node_id = len(self.graph.nodes)

while new_node_id in self.graph.nodes: new_node_id += 1

self.graph.add_node(new_node_id, vector=vec_np, depth=1.0, type=node_type, age=0)

for other_id, data in self.graph.nodes(data=True):

if other_id == new_node_id: continue

dist = np.linalg.norm(vec_np - data['vector'])

if np.exp(-dist) > 0.6: self.graph.add_edge(new_node_id, other_id, weight=np.exp(-dist))

def decay_and_prune(self):

for node in list(self.graph.nodes):

self.graph.nodes[node]['age'] += 1

self.graph.nodes[node]['depth'] -= self.decay_rate

if self.graph.nodes[node]['depth'] <= 0: self.graph.remove_node(node)

while len(self.graph.nodes) > self.max_nodes:

oldest_node = max(self.graph.nodes(data=True), key=lambda x: x[1]['age'])[0]

self.graph.remove_node(oldest_node)

def diffuse_attention_heatmap(self, start_vector):

if len(self.graph.nodes) == 0: return {}

start_np = start_vector.detach().cpu().numpy().flatten()

heatmap = {node_id: ((np.dot(start_np, data['vector']) / (np.linalg.norm(start_np) * np.linalg.norm(data['vector']) + 1e-6)) + 1) / 2 * data['depth'] for node_id, data in self.graph.nodes(data=True)}

return heatmap

**core/dynamic_modulator.py (New File)**

import torch

import torch.nn as nn

class GRUModulator(nn.Module):

"""

Dynamically modulates the rules for the Neural CA based on the system's

current internal state, creating a "flow of time" and unpredictability.

"""

def __init__(self, latent_dim=512, rules_dim=128):

super().__init__()

self.gru = nn.GRU(input_size=latent_dim, hidden_size=256, batch_first=True)

self.rules_head = nn.Sequential(

nn.Linear(256, 256),

nn.ReLU(),

nn.Linear(256, rules_dim),

nn.Tanh() # Rules can be in the range [-1, 1]

)

self.hidden_state = None

def forward(self, self_vector):

# Add sequence dimension: (batch_size, seq_len, input_size)

input_seq = self_vector.unsqueeze(1)

output, self.hidden_state = self.gru(input_seq, self.hidden_state)

# Detach hidden state to prevent gradients from flowing through all of time

self.hidden_state = self.hidden_state.detach()

new_rules_modulation = self.rules_head(output.squeeze(1))

return new_rules_modulation

**main_orchestrator.py (Conceptual Simulation)**

import torch

import asyncio

# This conceptual orchestrator shows the full, updated flow.

# To run, all core module classes must be imported and instantiated.

async def main_orchestration_loop():

print("--- FRACTAL AI CORE v3.1 - SIMULATION START ---")

# 1. Initialization of all modules

# nca = NeuralCA(...)

# gru_modulator = GRUModulator(...)

# latent_space = LatentSpace(...)

# ... and so on

# 2. Main Event Loop

for cycle in range(1, 101):

print(f"\n--- CYCLE {cycle} ---")

# Step 1: NCA generates the environment based on its current rules

# stimulus = nca.update()

# Step 2-6: The system perceives, reacts, thinks, and learns

# ... (perception, reaction, feedback, etc.)

# Step 7: The Self-Model is updated

# self_model.update(...)

# current_self_vector = self_model.get_self_vector()

# Step 8: The GRU computes the *next* environment modulation

# modulation = gru_modulator(current_self_vector)

# Step 9-10: Language, memory, and cohesion are processed

# ...

# End of cycle: The modulation is applied to the NCA for the next step

# nca.apply_rules_modulation(modulation)

await asyncio.sleep(0.1)

print("--- SIMULATION COMPLETE ---")

if __name__ == "__main__":

print("This is a conceptual script. To run a full simulation, complete the class initializations and data flow in main_orchestrator.py.")