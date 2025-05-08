
# Evaluater, Orchestrater and React Agent Using LangGraph-Functional APIs

**LangGraph Agents Suite**
A collection of functional API–based agents built on LangGraph, including:

* **Orchestrator**: Coordinates data and tasks across agents.
* **React Agent**: Interacts with users in real time, responding to input and events.
* **Evaluator Agent**: Assesses outputs for quality, consistency, and compliance.

---

## 🚀 Features

* **Modular design**: Each agent exposes a clear, functional API.
* **Composable workflows**: Use the Orchestrator to chain agents into complex pipelines.
* **Real‑time interaction**: React Agent handles streaming user input and UI events.
* **Automated evaluation**: Evaluator Agent scores and filters outputs against custom criteria.
* **Type‑safe & lightweight**: Written in TypeScript with strict typing and minimal dependencies.

---

## 🏗️ Architecture Overview

1. **Orchestrator** glues everything together:

   * Accepts an **input context**.
   * Runs a sequence of **middleware** functions (which can call other agents).
   * Returns a **final result** object containing all accumulated data.

2. **React Agent** provides a **browser‑friendly** event loop:

   * Listens to **message** and **UI events**.
   * Streams responses back to the interface.
   * Can invoke the Orchestrator or Evaluator as sub‑tasks.

3. **Evaluator Agent** offers **pluggable metrics**:

   * Computes numeric or categorical **scores**.
   * Supports custom metric functions.
   * Integrates with CI/CD or monitoring dashboards.

