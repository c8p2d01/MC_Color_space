import variables as var
import numpy as np
import json

class BlockVariant:
    model_id: str
    block_id: str
    groups: list[str]
    def __init__(self, id):
        self.model_id = id
        self.fields = {}
        self.textures = []
        self.pixels = []
        self.summons = []
        self.properties = []
        self.groups = []

    def __getitem__(self, key):
        return self.fields.get(key)

    def __setitem__(self, key, value):
        self.fields[key] = value

    def __repr__(self):
        return json.dumps(self.fields, indent=4)


class Block():
    variants: list[BlockVariant]
    id: str

    def __init__(self, id):
        self.id = id
        self.variants = []

    def add_texture(self, texture):
        self.textures.append(texture)

    def get(self):
        return self

if __name__ == "__main__":
    pass
