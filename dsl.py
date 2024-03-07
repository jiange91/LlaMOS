from dataclasses import dataclass

@dataclass
class Module:
    name: str
    def forward(self, x):
        pass

@dataclass
class Node:
    model_name: str
    start_point: Gate
    end_point: Gate
    