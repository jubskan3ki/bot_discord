from webbrowser import get
import discord
from discord.ext import commands
from discord.utils import get
bot = commands.Bot(command_prefix="$")


class story:
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
            return Node_story_1
        return self

    def question_bot(self):
        return self.question


Node_story_1 = story("start", "key", 0)

Node_story_2 = story(
    "Vous devez choisir entre Élementaire / Mage / Guerrier / Paladin / Druide / Archer / Barde / Troll / Orc / Nécromancien / Chasseur", "start", 0)

Node_story_3_1 = story("vous voulez mourir ou vivre?(mourir/vivre)", "Élementaire", 0)

Node_story_3_2 = story("vous voulez mourir ou vivre?(mourir/vivre)", "Mage", 0)

Node_story_3_3 = story("vous voulez mourir ou vivre?(mourir/vivre)", "Guerrier", 0)

Node_story_3_4 = story("vous voulez mourir ou vivre?(mourir/vivre)", "Paladin", 0)

Node_story_3_5 = story("vous voulez mourir ou vivre?(mourir/vivre)", "Druide", 0)

Node_story_3_6 = story("vous voulez mourir ou vivre?(mourir/vivre)", "Archer", 0)

Node_story_3_7 = story("vous voulez mourir ou vivre?(mourir/vivre)", "Barde", 0)

Node_story_3_8 = story("vous voulez mourir ou vivre?(mourir/vivre)", "Troll", 0)

Node_story_3_9 = story("vous voulez mourir ou vivre?(mourir/vivre)", "Orc", 0)

Node_story_3_10 = story("vous voulez mourir ou vivre?(mourir/vivre)",
                 "Nécromancien", 0)

Node_story_3_11 = story("vous voulez mourir ou vivre?(mourir/vivre)", "Chasseur", 0)


Node_story_4_1_2 = story("vous êtes mort ", "mourir", 1)

Node_story_4_2_2 = story("vous êtes mort", "mourir", 1)

Node_story_4_3_2 = story("vous êtes mort", "mourir", 1)

Node_story_4_4_2 = story("vous êtes mort", "mourir", 1)

Node_story_4_5_2 = story("vous êtes mort", "mourir", 1)

Node_story_4_6_2 = story("vous êtes mort", "mourir", 1)

Node_story_4_7_2 = story("vous êtes mort", "mourir", 1)

Node_story_4_8_2 = story("vous êtes mort", "mourir", 1)

Node_story_4_9_2 = story("vous êtes mort", "mourir", 1)

Node_story_4_10_2 = story("vous êtes mort", "mourir", 1)

Node_story_4_11_2 = story("vous êtes mort", "mourir", 1)


Node_story_4_1_1 = story(
    "vous avez survécu, une vielle dame apparaît que faites-vous ? **(l'aide/tuer)**", "vivre", 0)

Node_story_4_2_1 = story(
    "vous avez survécu, une vielle dame apparaît que faites-vous ? **(l'aide/tuer)**", "vivre", 0)

Node_story_4_3_1 = story(
    "vous avez survécu, une vielle dame apparaît que faites-vous ? **(l'aide/tuer)**", "vivre", 0)

Node_story_4_4_1 = story(
    "vous avez survécu, une vielle dame apparaît que faites-vous ? **(l'aide/tuer)**", "vivre", 0)

Node_story_4_5_1 = story(
    "vous avez survécu, une vielle dame apparaît que faites-vous ? **(l'aide/tuer)**", "vivre", 0)

Node_story_4_6_1 = story(
    "vous avez survécu, une vielle dame apparaît que faites-vous ? **(l'aide/tuer)**", "vivre", 0)

Node_story_4_7_1 = story(
    "vous avez survécu, une vielle dame apparaît que faites-vous ? **(l'aide/tuer)**", "vivre", 0)

Node_story_4_8_1 = story(
    "vous avez survécu, une vielle dame apparaît que faites-vous ? **(l'aide/tuer)**", "vivre", 0)

Node_story_4_9_1 = story(
    "vous avez survécu, une vielle dame apparaît que faites-vous ? **(l'aide/tuer)**", "vivre", 0)

Node_story_4_10_1 = story(
    "vous avez survécu, une vielle dame apparaît que faites-vous ? **(l'aide/tuer)**", "vivre", 0)

Node_story_4_11_1 = story(
    "vous avez survécu, une vielle dame apparaît que faites-vous ? **(l'aide/tuer)**", "vivre", 0)


Node_story_5_1_2 = story(
    "La vielle dame vous a tuer, vous êtes mort", "l'aide", 1)

Node_story_5_2_2 = story(
    "Vous avez osé tuer une pauvre vielle dame...?\nles mages n'ont aucune limite quand il s'agit d'être lamentable, la prison vous attends", "tuer", 1)

Node_story_5_3_2 = story(
    "La vielle dame vous a tuer, vous êtes mort et pitoyable", "l'aide", 1)

Node_story_5_4_2 = story(
    "quel mauvais Paladin vous êtes partie en prison", "tuer", 1)

Node_story_5_5_2 = story(
    "quel mauvais Druide vous êtes partie en prison", "tuer", 1)

Node_story_5_6_2 = story("La grand mere vous a tuer , vous êtes mort", "l'aide", 1)

Node_story_5_7_2 = story(
    "quel mauvais Barde vous êtes partie en prison", "tuer", 1)

Node_story_5_8_2 = story("La grand mere vous a tuer , vous etes mort", "l'aide", 1)

Node_story_5_9_2 = story("La grand mere vous a tuer , vous etes mort", "l'aide", 1)

Node_story_5_10_2 = story(
    "quel mauvais necromentien vous etes partie en prison", "tuer", 1)

Node_story_5_11_2 = story(
    "quel mauvais Chasseur vous etes partie en prison", "tuer", 1)


Node_story_5_1_1 = story(
    "Félicitation la grand mère a bien été neutralisé, tu es sain et sauf. Mais son fils apprend la nouvelle est veut votre mort que voulez vous faire ? **(le tuer / le console)**", "tuer", 0)

Node_story_5_2_1 = story(
    "Quel gentleman/lady vous êtes, la vielle dame vous offre une friandise.\n son fils veut vous donner une potion l'acceptez-vous  ? (non / oui)", "l'aide", 0)

Node_story_5_3_1 = story(
    "Félicitation ! l'ancêtre a bien été neutralisé, vous êtes sain et sauf. \nMais son fils apprend l'effroyable nouvelle et veut votre tête, que comptez-vous faire ? **(le tuer / le console)**", "tuer", 0)

Node_story_5_4_1 = story(
    "Quel gentleman/lady vous êtes, la vielle dame vous offre une friandise.\n son fils veut vous donner une potion l'acceptez-vous  ? **(non / oui)**", "l'aide", 0)

Node_story_5_5_1 = story(
    "Quel gentleman/lady vous êtes, la vielle dame vous offre une friandise.\n son fils veut vous donner une potion l'acceptez-vous  ? **(non / oui)**", "l'aide", 0)

Node_story_5_6_1 = story(
    "Félicitation ! l'ancêtre a bien été neutralisé, vous êtes sain et sauf. \nMais son fils apprend l'effroyable nouvelle et veut votre tête, que comptez-vous faire ? **(le tuer / le console)**", "tuer", 0)

Node_story_5_7_1 = story(
    "Quel gentleman/lady vous êtes, la vielle dame vous offre une friandise.\n son fils veut vous donner une potion l'acceptez-vous  ? (non / oui)", "l'aide", 0)

Node_story_5_8_1 = story(
    "Félicitation ! l'ancêtre a bien été neutralisé, vous êtes sain et sauf. \nMais son fils apprend l'effroyable nouvelle et veut votre tête, que comptez-vous faire ? **(le tuer / le console)**", "tuer", 0)

Node_story_5_9_1 = story(
    "Félicitation ! l'ancêtre a bien été neutralisé, vous êtes sain et sauf. \nMais son fils apprend l'effroyable nouvelle et veut votre tête, que comptez-vous faire ? **(le tuer / le console)**", "tuer", 0)

Node_story_5_10_1 = story(
    "Quel gentleman/lady vous êtes, la vielle dame vous offre une friandise.\n son fils veut vous donner une potion l'acceptez-vous  ? **(non / oui)**", "l'aide", 0)

Node_story_5_11_1 = story(
    "Quel gentleman/lady vous êtes, la vielle dame vous offre une friandise.\n son fils veut vous donner une potion l'acceptez-vous  ? **(non / oui)**", "l'aide", 0)


Node_story_6_1_2 = story(
    "Son fantome vous a maudit ! vous agonisez dans les mort 24 heures qui suivent", "le tuer", 1)

Node_story_6_2_2 = story(
    "vous étiez en réalité souffrant d'un cancer appelé 'scénario' vous succombez donc à vos blessures ", "non", 1)

Node_story_6_3_2 = story(
    "Le jeune homme vous tue par vengance, logique vous aviez tout de même tué sa seule famille", "le console", 1)

Node_story_6_4_2 = story(
    "Bravo ! vous êtes mort, la potion contenait un poison ", "oui", 1)

Node_story_6_5_2 = story(
    "vous étiez en réalité souffrant d'un cancer appelé 'scénario' vous succombez donc à vos blessures", "non", 1)

Node_story_6_6_2 = story(
    "Son fantome vous a maudit ! vous agonisez dans les 24 heures qui suivent", "le tuer", 1)

Node_story_6_7_2 = story(
    "vous étiez en réalité souffrant d'un cancer appelé 'scénario' vous succombez donc à vos blessures", "non", 1)

Node_story_6_8_2 = story(
    "Le jeune homme vous tue par vengance, logique vous aviez tout de même tué sa seule famille", "le console", 1)

Node_story_6_9_2 = story(
    "Le jeune homme vous tue par vengance, logique vous aviez tout de même tué sa seule famille", "le console", 1)

Node_story_6_10_2 = story(
    "Bravo ! vous êtes mort, la potion contenait un poison ", "oui", 1)

Node_story_6_11_2 = story(
    "Bravo ! vous êtes mort, la potion contenait un poison ", "oui", 1)


Node_story_6_1_1 = story(
    "Le jeune homme se calme, car il se souvenu qu'il détestait sa grand mère mais vous conseil de fuir . Voulez vous fuir ? **(non / oui)** ", "le console", 0)

Node_story_6_2_1 = story(
    "vous étiez gravement blessé la potion vous a soigner, \nle fils s'avérait être en realité un grand chevalier, et vous propose de le rejoindre dans l'armée du roi, acceptez_vous ? **(non / oui)**", "oui", 0)

Node_story_6_3_1 = story(
    "Vous aviez bien fait, si vous ne l'aviez pas fait vous seriez mort, \nmais quelques minutes plus tard des soldats au service du petit fils de la vielle dame vous ont entendu, \nqu'allez-vous faire ? **(les combattre / se rendre)**", "le tuer", 0)

Node_story_6_4_1 = story(
    "elle était empoissonné vous avez bien fait, voulez-vous vous venger ? **(non / oui)**", "non", 0)

Node_story_6_5_1 = story(
    "vous étiez gravement blessé la potion vous a soigner, \nle fils s'avérait être en realité un grand chevalier, et vous propose de le rejoindre dans l'armée du roi, acceptez_vous ? **(non / oui)**", "oui", 0)

Node_story_6_6_1 = story(
    "Le jeune homme se calme, car il se souvenu qu'il détestait sa grand mère mais vous conseil de fuir . Voulez vous fuir ? **(non / oui)**", "le console", 0)

Node_story_6_7_1 = story(
    "vous étiez gravement blessé la potion vous a soigner, \nle fils s'avérait être en realité un grand chevalier, et vous propose de le rejoindre dans l'armée du roi, acceptez_vous ? **(non / oui)** ", "oui", 0)

Node_story_6_8_1 = story(
    "Vous aviez bien fait, si vous ne l'aviez pas fait vous seriez mort \nmais quelques minutes plus tard des soldats au service du petit fils de la vielle dame vous ont entendu, \nqu'allez-vous faire ? **(se rendre / se battre)**", "le tuer", 0)

Node_story_6_9_1 = story(
    "Vous aviez bien fait, si vous ne l'aviez pas fait vous seriez mort \nmais quelques minutes plus tard des soldats au service du petit fils de la vielle dame vous ont entendu, \nqu'allez-vous faire ? **(se rendre / se battre)**", "le tuer", 0)

Node_story_6_10_1 = story(
    "elle était empoissonné vous avez bien fait, voulez-vous vous venger ? (non / oui)", "non", 0)

Node_story_6_11_1 = story(
    "elle était empoissonné vous avez bien fait, voulez-vous vous venger ? (non / oui)", "non", 0)


Node_story_7_1_2 = story(
    "le fils s'avérait être en realité un grand chevalier, et voue tue sans difficulté", "non", 1)

Node_story_7_2_2 = story(
    "c'était une embuscade , vous êtes mort  ", "oui", 1)

Node_story_7_3_2 = story(
    "vous êtes trop faible pour vous battre contre ces soldats ,vous êtes donc logiquement mort", "les combattre", 1)

Node_story_7_4_2 = story(
    "trop clément, il vous on tuer ", "oui", 1)

Node_story_7_5_2 = story(
    "Déçu de votre refus, le chevalier estime que vous ne méritez pas de vivre", "non", 1)

Node_story_7_6_2 = story(
    "vous avez trebucher chute fatal vous etes mort ", "oui", 1)

Node_story_7_7_2 = story(
    "Déçu de votre refus, le chevalier estime que vous ne méritez pas de vivre ", "non", 1)

Node_story_7_8_2 = story(
    "ils étaient sans pitié et vous ont tuer", "se rendre ", 1)

Node_story_7_9_2 = story(
    "vous êtes trop faible contre eux , vous êtes mort ", "se battre", 1)

Node_story_7_10_2 = story(
    "2 contre 1 !? parce-que vous penseriez avoir le niveau ? ridicule ! vous êtes MORT... ", "oui", 1)

Node_story_7_11_2 = story(
    "2 contre 1 !? parce-que vous penseriez avoir le niveau ? ridicule ! vous êtes MORT... ", "oui", 1)


Node_story_7_1_1 = story(
    "Grâce à votre grande vitesse vous aviez survécu, félicitation ! mais la culpabilité vous ronge... voulez-vous vous suicider ? **(non / oui)** ", "oui", 0)

Node_story_7_2_1 = story(
    "C'était un test, et vous l'aviez reussi !!! \nils voudraient vous marier a sa soeur, acceptez-vous  ? **(non / oui)** ", "non", 0)

Node_story_7_3_1 = story(
    "Ému par votre sens de l'honneur, il vous demande de les rejoindre, vous voulez accepter ? **(non / oui)**", "se rendre", 0)

Node_story_7_4_1 = story(
    "Leur chatiment est merité, les tentatives d'assasinat doivent être puni, mais l'armée vous veut vous arrêter, qu'aller-vous faire ? **(se battre / s'expliquer)**", "non", 0)


Node_story_7_5_1 = story(
    "Si fière de vous avoir recruter, ils veulent faire la fête en votre compagnie,  accepter-vous ? **(non / oui)**", "oui", 0)

Node_story_7_6_1 = story(
    "Ému par votre sens de l'honneur, il vous demande de les rejoindre, vous voulez accepter ? **(non / oui)**", "non", 0)

Node_story_7_7_1 = story(
    "Si fière de vous avoir recruté, ils veulent faire la fête en votre compagnie, vous accepter ? **(non / oui)**", "oui", 0)

Node_story_7_8_1 = story(
    "Votre force les impresionne, et veulent faire de vous un mercenaire, acceptez-vous ? **(non / oui)**", "se battre", 0)

Node_story_7_9_1 = story(
    "Ému par votre sens de l'honneur, il vous demande de devenir mercenaire voulez vous acrcepte ? **(non / oui)**", "se rendre", 0)

Node_story_7_10_1 = story(
    "Ému par votre clémence, ils vous donne leurs richesses, acceptez-vous ? **(non / oui)**", "non", 0)

Node_story_7_11_1 = story(
    "Ému par votre clémence, ils vous donne leurs richesses, acceptez-vous ? **(non / oui)**", "non", 0)


Node_story_8_1_2 = story(
    "le fils vous rattrape vous êtes mort.", "non", 1)

Node_story_8_2_2 = story(
    "c'était une tueuse en série vous êtes mort célibataire.", "oui", 1)

Node_story_8_3_2 = story(
    "il n'avaient pas le choix, vous aviez tout de même commis des crimes, vous êtes mort.", "non", 1)

Node_story_8_4_2 = story(
    "énervé il vous tue.", "se battre", 1)

Node_story_8_5_2 = story(
    "Vous ne supportez pas l'alcool, vous mourrez d'ivresse.", "oui", 1)

Node_story_8_6_2 = story(
    "vous pensiez vraiment avoir chance de rentrer à l'armée ? ne rêver pas, vous êtes mort", "oui", 1)

Node_story_8_7_2 = story(
    "accablé par votre manque de respect, il vous tue.", "non", 1)

Node_story_8_8_2 = story(
    "accablé par votre culot, il vous tue.", "oui ", 1)

Node_story_8_9_2 = story(
    "ils étaient trop énervé pour vous épargner, donc il vous ont donc tuer.", "non", 1)

Node_story_8_10_2 = story(
    "c'était évidemment un piège, vous êtes mort.", "oui", 1)

Node_story_8_11_2 = story(
    "Vous leurs avez manqués de respect, ils s'énervent et vous tue.", "non", 1)


Node_story_8_1_1 = story(
    "le fils vous rattrape et vous sauve, félicitation ! vous avez survecu !", "oui", 1)

Node_story_8_2_1 = story(
    "votre chasteté vous a sauvé ! felicitation vous avez survécu ! ", "non", 1)

Node_story_8_3_1 = story(
    "vous avez rejoint l'armée, félicitation vous avez survecu !", "oui", 1)

Node_story_8_4_1 = story(
    "vos arguments et votre motivation les touches, on vous libère, félicitation vous avez survécu !", "s'expliquer", 1)

Node_story_8_5_1 = story(
    "votre sérieux les rends admiratif,  félicitation vous avez survécu !", "non", 1)

Node_story_8_6_1 = story(
    "accepte votre décicion, et decide de vous libérer, félicitation vous avez survécu", "non", 1)

Node_story_8_7_1 = story(
    "Vous faite la fête avec l'armée, félicitation vous avez survécu !", "oui", 1)

Node_story_8_8_1 = story(
    "Impréssionné par votre courage, on vous libère, félicitation vous avez survécu !", "non", 1)

Node_story_8_9_1 = story(
    "vous finissez par rejoindre l'armée, félicitation vous avez survécu", "oui", 1)

Node_story_8_10_1 = story(
    "votre clémence est légendaire, ils vous suivront même en enfer, félicitation vous avez survécu !", "non", 1)

Node_story_8_11_1 = story(
    "vous êtes riche, libre et surtout vivant ! félicitation vous avez survécu ?", "oui", 1)


Node_story_1.add_child(Node_story_2)

Node_story_2.add_child(Node_story_3_1)

Node_story_2.add_child(Node_story_3_2)

Node_story_2.add_child(Node_story_3_3)

Node_story_2.add_child(Node_story_3_4)

Node_story_2.add_child(Node_story_3_5)

Node_story_2.add_child(Node_story_3_6)

Node_story_2.add_child(Node_story_3_7)

Node_story_2.add_child(Node_story_3_8)

Node_story_2.add_child(Node_story_3_9)

Node_story_2.add_child(Node_story_3_10)

Node_story_2.add_child(Node_story_3_11)


Node_story_3_1.add_child(Node_story_4_1_1)

Node_story_3_1.add_child(Node_story_4_1_2)

Node_story_3_2.add_child(Node_story_4_2_1)

Node_story_3_2.add_child(Node_story_4_2_2)

Node_story_3_3.add_child(Node_story_4_3_1)

Node_story_3_3.add_child(Node_story_4_3_2)

Node_story_3_4.add_child(Node_story_4_4_1)

Node_story_3_4.add_child(Node_story_4_4_2)

Node_story_3_5.add_child(Node_story_4_5_1)

Node_story_3_5.add_child(Node_story_4_5_2)

Node_story_3_6.add_child(Node_story_4_6_1)

Node_story_3_6.add_child(Node_story_4_6_2)

Node_story_3_7.add_child(Node_story_4_7_1)

Node_story_3_7.add_child(Node_story_4_7_2)

Node_story_3_8.add_child(Node_story_4_8_1)

Node_story_3_8.add_child(Node_story_4_8_2)

Node_story_3_9.add_child(Node_story_4_9_1)

Node_story_3_9.add_child(Node_story_4_9_2)

Node_story_3_10.add_child(Node_story_4_10_1)

Node_story_3_10.add_child(Node_story_4_10_2)

Node_story_3_11.add_child(Node_story_4_11_1)

Node_story_3_11.add_child(Node_story_4_11_2)


Node_story_4_1_1.add_child(Node_story_5_1_1)

Node_story_4_1_1.add_child(Node_story_5_1_2)

Node_story_4_2_1.add_child(Node_story_5_2_1)

Node_story_4_2_1.add_child(Node_story_5_2_2)

Node_story_4_3_1.add_child(Node_story_5_3_1)

Node_story_4_3_1.add_child(Node_story_5_3_2)

Node_story_4_4_1.add_child(Node_story_5_4_1)

Node_story_4_4_1.add_child(Node_story_5_4_2)

Node_story_4_5_1.add_child(Node_story_5_5_1)

Node_story_4_5_1.add_child(Node_story_5_5_2)

Node_story_4_6_1.add_child(Node_story_5_6_1)

Node_story_4_6_1.add_child(Node_story_5_6_2)

Node_story_4_7_1.add_child(Node_story_5_7_1)

Node_story_4_7_1.add_child(Node_story_5_7_2)

Node_story_4_8_1.add_child(Node_story_5_8_1)

Node_story_4_8_1.add_child(Node_story_5_8_2)

Node_story_4_9_1.add_child(Node_story_5_9_1)

Node_story_4_9_1.add_child(Node_story_5_9_2)

Node_story_4_10_1.add_child(Node_story_5_10_1)

Node_story_4_10_1.add_child(Node_story_5_10_2)

Node_story_4_11_1.add_child(Node_story_5_11_1)

Node_story_4_11_1.add_child(Node_story_5_11_2)


Node_story_5_1_1.add_child(Node_story_6_1_1)

Node_story_5_1_1.add_child(Node_story_6_1_2)

Node_story_5_2_1.add_child(Node_story_6_2_1)

Node_story_5_2_1.add_child(Node_story_6_2_2)

Node_story_5_3_1.add_child(Node_story_6_3_1)

Node_story_5_3_1.add_child(Node_story_6_3_2)

Node_story_5_4_1.add_child(Node_story_6_4_1)

Node_story_5_4_1.add_child(Node_story_6_4_2)

Node_story_5_5_1.add_child(Node_story_6_5_1)

Node_story_5_5_1.add_child(Node_story_6_5_2)

Node_story_5_6_1.add_child(Node_story_6_6_1)

Node_story_5_6_1.add_child(Node_story_6_6_2)

Node_story_5_7_1.add_child(Node_story_6_7_1)

Node_story_5_7_1.add_child(Node_story_6_7_2)

Node_story_5_8_1.add_child(Node_story_6_8_1)

Node_story_5_8_1.add_child(Node_story_6_8_2)

Node_story_5_9_1.add_child(Node_story_6_9_1)

Node_story_5_9_1.add_child(Node_story_6_9_2)

Node_story_5_10_1.add_child(Node_story_6_10_1)

Node_story_5_10_1.add_child(Node_story_6_10_2)

Node_story_5_11_1.add_child(Node_story_6_11_1)

Node_story_5_11_1.add_child(Node_story_6_11_2)


Node_story_6_1_1.add_child(Node_story_7_1_1)

Node_story_6_1_1.add_child(Node_story_7_1_2)

Node_story_6_2_1.add_child(Node_story_7_2_1)

Node_story_6_2_1.add_child(Node_story_7_2_2)

Node_story_6_3_1.add_child(Node_story_7_3_1)

Node_story_6_3_1.add_child(Node_story_7_3_2)

Node_story_6_4_1.add_child(Node_story_7_4_1)

Node_story_6_4_1.add_child(Node_story_7_4_2)

Node_story_6_5_1.add_child(Node_story_7_5_1)

Node_story_6_5_1.add_child(Node_story_7_5_2)

Node_story_6_6_1.add_child(Node_story_7_6_1)

Node_story_6_6_1.add_child(Node_story_7_6_2)

Node_story_6_7_1.add_child(Node_story_7_7_1)

Node_story_6_7_1.add_child(Node_story_7_7_2)

Node_story_6_8_1.add_child(Node_story_7_8_1)

Node_story_6_8_1.add_child(Node_story_7_8_2)

Node_story_6_9_1.add_child(Node_story_7_9_1)

Node_story_6_9_1.add_child(Node_story_7_9_2)

Node_story_6_10_1.add_child(Node_story_7_10_1)

Node_story_6_10_1.add_child(Node_story_7_10_2)

Node_story_6_11_1.add_child(Node_story_7_11_1)

Node_story_6_11_1.add_child(Node_story_7_11_2)


Node_story_7_1_1.add_child(Node_story_8_1_1)

Node_story_7_1_1.add_child(Node_story_8_1_2)

Node_story_7_2_1.add_child(Node_story_8_2_1)

Node_story_7_2_1.add_child(Node_story_8_2_2)

Node_story_7_3_1.add_child(Node_story_8_3_1)

Node_story_7_3_1.add_child(Node_story_8_3_2)

Node_story_7_4_1.add_child(Node_story_8_4_1)

Node_story_7_4_1.add_child(Node_story_8_4_2)

Node_story_7_5_1.add_child(Node_story_8_5_1)

Node_story_7_5_1.add_child(Node_story_8_5_2)

Node_story_7_6_1.add_child(Node_story_8_6_1)

Node_story_7_6_1.add_child(Node_story_8_6_2)

Node_story_7_7_1.add_child(Node_story_8_7_1)

Node_story_7_7_1.add_child(Node_story_8_7_2)

Node_story_7_8_1.add_child(Node_story_8_8_1)

Node_story_7_8_1.add_child(Node_story_8_8_2)

Node_story_7_9_1.add_child(Node_story_8_9_1)

Node_story_7_9_1.add_child(Node_story_8_9_2)

Node_story_7_10_1.add_child(Node_story_8_10_1)

Node_story_7_10_1.add_child(Node_story_8_10_2)

Node_story_7_11_1.add_child(Node_story_8_11_1)

Node_story_7_11_1.add_child(Node_story_8_11_2)


@bot.command()
async def mj(ctx, arg):
    def check(m):
        return int(m.author.id) == int(ctx.message.author.id) and int(m.channel.id) == int(ctx.message.channel.id)
    reponse = Node_story_1.testChild(arg)
    level = Node_story_2
    if reponse != Node_story_1:
        await ctx.send(f"{reponse.question_bot()}")
        while reponse.end == 0:
            msg = await bot.wait_for("message", check=check)
            reponse = reponse.testChild(msg.content)
            if level == reponse:
                await ctx.send(f"je ne comprend pas, veuillez rééssayer")
            else:
                await ctx.send(f"{reponse.question_bot()}")
                level = reponse
    else:
        await ctx.send(f"je ne comprend pas, veuillez réessayer")


@bot.command()
async def change_name(ctx, *, arg):
    await ctx.author.edit(nick=arg)
    await ctx.send(f'Nickname was changed for {ctx.author.mention} ', tts=True)


@bot.command()
async def create_r(ctx, r):
    colour = discord.Colour(0xffffff)
    # permissions=discord.Permissions(permissions=<>)
    guild = ctx.guild

    for role in guild.roles:
        if role.name == r:
            return

    await guild.create_role(name=r)


@bot.command()
async def add_r(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.guild.roles, name="test")
    await user.add_roles(role)


@bot.command()
async def create_t(ctx, *, nom_de_salon):

    for channel in bot.get_all_channels():
        if nom_de_salon == channel.name:
            return

    guild = ctx.guild
    role = nom_de_salon
    autorize_role = await guild.create_role(name=role)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        autorize_role: discord.PermissionOverwrite(read_messages=True)
    }
    await guild.create_text_channel(nom_de_salon, overwrites=overwrites)
    await ctx.author.add_roles(autorize_role)


@bot.command()
async def create_v(ctx, *, nom_de_salon):
    if ctx.channel.name != nom_de_salon:
        guild = ctx.guild
        role = nom_de_salon
        autorize_role = await guild.create_role(name=role)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            autorize_role: discord.PermissionOverwrite(read_messages=True)
        }
        await guild.create_voice_channel(nom_de_salon, overwrites=overwrites)
        await ctx.author.add_roles(autorize_role)


@bot.command(name='del')
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for each_message in messages:
        await each_message.delete()


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)

@bot.event
async def on_member_join(member):
    general_channel : discord.TextChannel = bot.get_channel(978215825439875106)
    general_channel.send(f"Un nouveau membre est arrivé : {member.display_name} pour plus d'information sur le bot merci de bien vouloir faire /help ")

@bot.command()
async def ping(ctx, role: discord.Role, *, message):

    await ctx.send(f"""
    {role.mention}
    cette personne {ctx.author.mention} a dit : {message}
    """)


@bot.command()
async def admin(ctx, *, message):
    admin = get(ctx.guild.roles, name='admin')
    await ctx.send(f"""
    {admin.mention}
    cette personne {ctx.author.mention} a dit : {message}
    """)


# faire le bot

bot.run("OTc4MjI5MzgxNjQ0MzE2NzEy.GrSDPk.7vgtGIoQlb2voSUzwN4UNh1KxbCJvK0V1Kpozk")
