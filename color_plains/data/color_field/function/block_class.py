import variables as var

class BlockVariant():
    identifier: str
    textures: dict[str, str]

    def __init__(self, id):
        self.identifier = id
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

    id: str
    textures: list[str]
    variants: list[BlockVariant]

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
