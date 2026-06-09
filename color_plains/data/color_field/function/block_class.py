import variables as var

class BlockVariant():
    block_ids: list[str]
    textures: dict[str, str]
    groups: list[str]
    summons: list[str]

    def __init__(self, id):
        self.block_ids = []
        self.groups = []
        self.textures = {}
        self.summons = []

        self.block_ids.append(id)
        self.textures = {
            "particle": "",
            "down": "",
            "up": "",
            "north": "",
            "east": "",
            "south": "",
            "west": ""
        }

class Block():
    textures: list[str]
    variants: list[BlockVariant]
    id: str

    def __init__(self, id):
        self.id = id
        self.textures = []
        self.variants = []

    def add_texture(self, texture):
        self.textures.append(texture)

    def get(self):
        return self

if __name__ == "__main__":
    pass
