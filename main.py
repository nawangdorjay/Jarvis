#!/usr/bin/env python3
"""JARVIS CLI Entry Point"""
import sys
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.memory import MemoryAgent
from agents.voice import VoiceAgent

def main():
    print("🤖 JARVIS activated...")
    # Initialize agents
    planner = PlannerAgent()
    executor = ExecutorAgent()
    memory = MemoryAgent()
    voice = VoiceAgent()
    print("All systems operational.")

if __name__ == "__main__":
    main()