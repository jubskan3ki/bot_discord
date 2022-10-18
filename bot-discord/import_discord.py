import discord
from webbrowser import get
from discord.ext import commands
from discord.utils import get
client = commands.Bot(command_prefix="$")
Help_channel = client.get_channel(978273304089608202)

class Tree:
    def __init__(self, question, key, end):
        self.question = question
        self.key = key
        self.children = []
        self.parent = None
        self.end = end

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def testChild(self, key):
        for child in self.children:
            if child.key in key:
                return child
        if key == "return":
            return self.parent
        elif key == "reset":
            return Node1
        return self

    def question_bot(self):
        return self.question




Node1 = Tree("start", "key", 0)

Node2 = Tree("bien/mal", "start", 0)

Node3_1 = Tree("mélée/range", "bien", 0)

Node4_1 = Tree("magie/arme", "mélée", 0)

Node5_1 = Tree("element", "magie", 0)

Node6_1 = Tree("elementaire de feu", "feu", 1)

Node6_2 = Tree("elementaire d'eau", "eau", 1)

Node6_3 = Tree("elementaire de terre", "terre", 1)

Node6_4 = Tree("elementaire d'air", "air", 1)

Node6_5 = Tree("elementaire de lumière", "lumière", 1)

Node5_2 = Tree("defense/attaque", "arme", 0)

Node6_6 = Tree("guerrier", "defense", 1)

Node6_7 = Tree("Paladin", "attaque", 1)

Node4_2 = Tree("magie/arme", "range", 0)

Node5_3 = Tree("taper/non", "magie", 0)

Node6_8 = Tree("element", "taper", 0)
            
Node7_1 = Tree("mage de feu", "feu", 1)

Node7_2 = Tree("mage d'eau", "eau", 1)

Node7_3 = Tree("mage de terre", "terre", 1)

Node7_4 = Tree("mage d'air", "air", 1)

Node6_9 = Tree("Druide", "non", 1)

Node5_4 = Tree("taper/non", "arme", 0)

Node6_10 = Tree("archer", "taper", 1)

Node6_11 = Tree("Barde", "non", 1)

Node3_2 = Tree("mélée/range", "mal", 0)

Node4_3 = Tree("magie/arme", "mélée", 0)

Node5_5 = Tree("element", "magie", 0)

Node6_12 = Tree("elementaire de poison", "poison", 1)

Node6_13 = Tree("elementaire de sang", "sang", 1)

Node6_14 = Tree("elementaire de tenèbre", "tenèbre", 1)

Node5_6 = Tree("defense/attaque", "arme", 0)

Node6_15 = Tree("Troll", "defense", 1)

Node6_16 = Tree("Orc", "attaque", 1)

Node4_4 = Tree("magie/arme", "range", 0)

Node5_7 = Tree("taper/non", "magie", 0)

Node6_17 = Tree("element", "taper", 0)

Node7_5 = Tree("mage de poison", "poison", 1)

Node7_6 = Tree("mage de sang", "sang", 1)

Node7_7 = Tree("mage de tenèbre", "tenèbre", 1)

Node6_18 = Tree("necromentien", "non", 1)

Node5_8 = Tree("Chasseur", "range", 1)


Node1.add_child(Node2)

Node2.add_child(Node3_1)

Node3_1.add_child(Node4_1)

Node4_1.add_child(Node5_1)

Node5_1.add_child(Node6_1)

Node5_1.add_child(Node6_2)

Node5_1.add_child(Node6_3)

Node5_1.add_child(Node6_4)

Node5_1.add_child(Node6_5)

Node4_1.add_child(Node5_2)

Node5_2.add_child(Node6_6)

Node5_2.add_child(Node6_7)

Node3_1.add_child(Node4_2)

Node4_2.add_child(Node5_3)

Node5_3.add_child(Node6_8)

Node6_8.add_child(Node7_1)

Node6_8.add_child(Node7_2)

Node6_8.add_child(Node7_3)

Node6_8.add_child(Node7_4)

Node5_3.add_child(Node6_9)

Node4_2.add_child(Node5_4)

Node5_4.add_child(Node6_10)

Node5_4.add_child(Node6_11)

Node2.add_child(Node3_2)

Node3_2.add_child(Node4_3)

Node4_3.add_child(Node5_5)

Node5_5.add_child(Node6_12)

Node5_5.add_child(Node6_13)

Node5_5.add_child(Node6_14)

Node4_3.add_child(Node5_6)

Node5_6.add_child(Node6_15)

Node5_6.add_child(Node6_16)

Node3_2.add_child(Node4_4)

Node4_4.add_child(Node5_7)

Node5_7.add_child(Node6_17)

Node6_17.add_child(Node7_5)

Node6_17.add_child(Node7_6)

Node6_17.add_child(Node7_7)

Node5_7.add_child(Node6_18)

Node4_4.add_child(Node5_8)




@client.command()
async def start(ctx, arg):
    def check(m):
        return int(m.author.id) == int(ctx.message.author.id) and int(m.channel.id) == int(ctx.message.channel.id)
    reponse = Node1.testChild(arg)
    level = Node2
    if reponse != Node1:
        await ctx.send(f"{reponse.question_bot()}")
        while reponse.end == 0:
            msg = await client.wait_for("message", check=check)
            reponse = reponse.testChild(msg.content)
            if level == reponse:
                await ctx.send(f"je ne comprend pas, veuillez rééssayer")
            else:
                await ctx.send(f"{reponse.question_bot()}")
                level = reponse
    else:
        await ctx.send(f"je ne comprend pas, veuillez réessayer")




client.run("OTc4MjI4ODY5Mjc2NTEyMzA2.GPiUHt.ApO6k3Xy84k5eNlA0vtof3vYUEbvUi2W3MqoNw")