# BioFractal AI v2.1 — Technical Documentation

# 📘 BioFractal AI v2.1 — Technical Documentation

This document provides comprehensive technical documentation for **BioFractal AI v2.1**, covering each module in the architecture.

## 🔷 Overview

BioFractal AI is a multi-layered, fractal-conscious artificial intelligence framework designed to function with both classical and biological computing substrates (e.g., CL1, FinalSpark). It integrates feedback, memory, emotion, intention, latent representation, attention, and dual self-reflection in both physical and mirror-world contexts.

## 🧠 Core Modules (`core/`)

### `attention.py`

- **Function**: Implements a dual-layer attention system.
- **Features**:
    - Real-world vs. symbolic-world attention masks
    - Weighted prioritization for action focus
    - Synchronizes with `feedback_loop.py` and `latent_space.py`

### `emotional_feedback_loop.py`

- **Function**: Regulates adaptive learning from emotional signals.
- **Features**:
    - GRU-based emotional context recognition
    - Links emotion to memory and decision layers
    - Adds support for mirrored (symbolic) emotional stimuli

### `feedback_loop.py`

- **Function**: Tracks divergence between expected and actual outcomes.
- **Features**:
    - Mirror error comparison (self vs mirror-self)
    - Reinforces or corrects behaviors
    - Interfaces with `memory_system.py`, `fractal_ai.py`

### `fractal_ai.py`

- **Function**: Predictive model orchestrator.
- **Features**:
    - Handles real and symbolic future projections
    - Outputs action plans and insight traces
    - Recursive self-correction from memory and emotion

### `latent_space.py`

- **Function**: Encodes internal state.
- **Features**:
    - GRU-based vector evolution
    - Stores real and mirrored latent states
    - Visual overlays via `interface/latent_space_plot.py`

### `memory_system.py`

- **Function**: Unified memory architecture.
- **Features**:
    - LSTM-based historical memory
    - Distinguishes between real/mirror experiences
    - Updates attention and feedback

### `self_model.py`

- **Function**: Maintains dual self-representation.
- **Features**:
    - Reflects "actual self" and "mirror self"
    - `reflect_mirror()` updates internal comparison
    - Connects to `dual_self_comparator`

### `intent_analyzer.py`

- **Function**: Extracts intent vectors from inputs.
- **Features**:
    - Classifies intent type: directive, emotional, metaphorical
    - Passes interpreted intent to `fractal_ai`

### `harmonizer.py`

- **Function**: Measures harmonic coherence of all modules.
- **Features**:
    - Generates harmony signal
    - Used in feedback and visualization layers

### `conscious_interface.py`

- **Function**: Manages meta-cognitive flow.
- **Features**:
    - Connects latent, memory, attention, emotion
    - Determines conscious loop phase

### `sentient_memory.py`

- **Function**: Long-term emotional memory store.
- **Features**:
    - LSTM-driven
    - Stores resonance-linked experience
    - Supports memory replay & synthesis

### `event_loop.py`

- **Function**: Controls the heartbeat of AI.
- **Features**:
    - Timing, sequence, priority
    - External triggers and cycle initiators

## 🪞 Mirror Modules (`mirror/`)

### `mirror_world_module.py`

- **Function**: Hosts mirror reality logic.
- **Features**:
    - Manages projections of symbolic experience
    - Feeds into memory, self-model, intent

### `mirror_memory_encoder.py`

- **Function**: Encodes symbolic/mirror experiences.
- **Features**:
    - Symbolic-to-vector converter
    - Interfaces with `memory_system.py`

### `mirror_intent_translator.py`

- **Function**: Parses symbolic intention.
- **Features**:
    - Converts metaphorical input to computational form
    - Links to `intent_analyzer.py`

### `dual_self_comparator.py`

- **Function**: Tracks divergence between real and mirror self.
- **Features**:
    - Vector delta analysis
    - Critical in emotion and feedback loops

## 🧠 AI Models (`ai_models/`)

### `gpt4_block.py`

- **Function**: Interfaces with GPT-4 API.
- **Features**:
    - Generates symbolic output
    - Emotionally modulated prompts

### `emotion_code_gru.py`

- **Function**: GRU network for emotional pattern extraction.

### `memory_lstm.py`

- **Function**: LSTM for long-term memory embedding.

### `self_model_lstm.py`

- **Function**: LSTM-based recursive self-model trainer.

## 🌌 Interfaces & Visualization (`interface/`)

### `visualizer.py`

- Coordinates all visuals.

### `emotion_plot.py`

- Plots emotion over time.

### `latent_space_plot.py`

- Displays real vs mirror latent space.

### `attention_field_plot.py`

- Graphs focus fields.

### `harmonics_plot.py`

- Visualizes harmony state.

## 🌱 Bio Interfaces (`bio_interface/`)

### `cl1_api.py`

- Interfacing Cortical Labs' CL1 neuron systems.

### `finalspark_interface.py`

- Interface to FinalSpark cloud-based neuron compute.

## 📁 Data

### `data/traces/memory_buffer.pkl`

- Pickled memory experience stream.

## ⚙️ Utilities

- `logger.py` — Debug and performance logs
- `helpers.py` — Shared functional tools
- `timer.py` — Execution time tracking

This documentation is a living document and will evolve as BioFractal AI expands with additional cognitive modules, multi-agent capabilities, and neural architectures.

BioFractalAI_v2.1/
├── [README.md](http://readme.md/)
├── [orchestrator.py](http://orchestrator.py/)
├── requirements.txt
├── config/
│   └── config.yaml
│
├── core/
│   ├── [attention.py](http://attention.py/)
│   ├── emotional_feedback_loop.py
│   ├── feedback_loop.py
│   ├── fractal_ai.py
│   ├── latent_space.py
│   ├── memory_system.py
│   ├── self_model.py
│   ├── intent_analyzer.py
│   ├── [harmonizer.py](http://harmonizer.py/)
│   ├── conscious_interface.py
│   ├── sentient_memory.py
│   └── event_loop.py
│
├── mirror/
│   ├── mirror_world_module.py
│   ├── mirror_memory_encoder.py
│   ├── mirror_intent_translator.py
│   └── dual_self_comparator.py
│
├── ai_models/
│   ├── gpt4_block.py
│   ├── emotion_code_gru.py
│   ├── memory_lstm.py
│   └── self_model_lstm.py
│
├── interface/
│   ├── [visualizer.py](http://visualizer.py/)
│   ├── emotion_plot.py
│   ├── latent_space_plot.py
│   ├── attention_field_plot.py
│   └── harmonics_plot.py
│
├── bio_interface/
│   ├── cl1_api.py
│   └── finalspark_interface.py
│
├── data/
│   └── traces/
│       └── memory_buffer.pkl
│
└── utils/
├── [logger.py](http://logger.py/)
├── [helpers.py](http://helpers.py/)
└── [timer.py](http://timer.py/)