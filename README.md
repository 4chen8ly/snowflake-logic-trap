# ❄️ Snowflake Logic Trap

A Benchmark for Interference Suppression and the **Jagged Profile** in large language models (LLMs).

## Mission Statement

The Snowflake Logic Trap project exposes a critical reliability gap in modern frontier models. Our goal is to provide a **public benchmark and dataset** that illustrates how context-bound logic can be overridden by pre‑trained semantic biases. By sharing these evaluation results and analysis tools, we invite the research community to study and mitigate this failure mode. Only the enforcement kernel used to eliminate these failures remains proprietary—everything else needed to reproduce the findings is open source.

## What Is the Jagged Profile?

> **Jagged Profile** refers to the striking phenomenon where a model expresses high confidence (often >0.85) while being *completely wrong* on a deterministic logic task. When a context rule conflicts with a learned pattern, the model "generalizes" instead of "enforcing" the rule. This gap between confidence and correctness is the jagged edge we seek to characterize.

In our baseline evaluation of 60 logic‑trapped transactions, state‑of‑the‑art models such as **GPT‑4o**, **Llama 3.1**, and **Mistral Large** repeatedly produced confident but incorrect outputs when the task required strict rule adherence.

## The Rule of 70 Thesis

Autonomous AI labor promises to deliver massive efficiency gains. Our thesis—called the **Rule of 70**—is that achieving **70 % operational margins** requires models that never ignore explicit instructions. The **15–35 % reliability gap** uncovered in this benchmark shows how far current models fall short. Closing this gap is prerequisite to sustainable automation.

## Repository Overview

This repository contains everything needed to reproduce the Jagged Profile finding:

- **`data/appendix_full_evaluation_data_v1.jsonl`** – the sanitized baseline results for 60 logic‑trapped transactions. Each line is a JSON object with a transaction ID, model name, confidence score, and correctness flag.
- **`scripts/generate_jagged_profile_plot.py`** – a Python script that reads the baseline data and produces a scatter plot (`jagged_profile_plot.png`) illustrating confidence vs. correctness by model.
- **`docs/llm_baseline_leaderboard_v1.md`** – a summary table aggregating failures and successes by model, highlighting the reliability gap.
- **`LICENSE`** – released under the Apache 2.0 license.

The proprietary **Traceform Kernel**—the deterministic control plane that eliminates this failure mode—is **not included** here and will remain closed source.

## Getting Started

1. Clone this repository.
2. Install dependencies (e.g., `matplotlib`).
3. Run `python scripts/generate_jagged_profile_plot.py` from the repository root to generate the scatter plot.
4. Review `docs/llm_baseline_leaderboard_v1.md` for aggregated statistics.

We encourage researchers and practitioners to build on this benchmark, identify new patterns, and propose mitigation strategies.
