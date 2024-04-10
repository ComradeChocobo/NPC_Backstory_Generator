import random
import tkinter as tk
from tkinter import font as tkFont
import os
current_dir = os.getcwd()
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir + "/inputs")
print(f"The working directory has been set to: {script_dir}")
home = ""
name = ""
name_other = "her"
pronoun = ""

def load_data_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            # Reading each line and storing it into a list
            data = [line.strip() for line in file]
        return data
    except FileNotFoundError:
        print(f"File '{file_name}' not found in the current directory.")
        return []
    
def randomize():

    global home, name, name_other, adjective, place, noun, verb, jobs, weakness, future_aspiration, love_interest, significant_event, early_life_event, personality, like, dislike, pronoun
    global name_info, adjective_info, place_info, noun_info, verb_info, jobs_info, weakness_info, future_aspiration_info, love_interest_info, significant_event_info, early_life_event_info, personality_info, like_info, dislike_info
    global one, two, three, four, five, six, seven, eight, nine, ten

    name_other = random.choice(name_info)
    adjective = random.choice(adjective_info).lower()
    place = random.choice(place_info)
    noun= random.choice(noun_info).lower()
    verb = random.choice(verb_info).lower()
    jobs = random.choice(jobs_info).lower()
    weakness = random.choice(weakness_info).lower()
    future_aspiration = random.choice(future_aspiration_info).lower()
    love_interest = random.choice(love_interest_info).lower()
    significant_event  = random.choice(significant_event_info).lower()
    early_life_event = random.choice(early_life_event_info).lower()
    personality = random.choice(personality_info).lower()
    like = random.choice(like_info).lower()
    dislike = random.choice(dislike_info).lower()

    one = [
    f"{name} the {adjective} came forth a hero to the people of {home}.",
    f"Deep within {home}, {name}, a {adjective} {noun}, loved to {verb}.",
    f"In the heart of {home}, there was a {noun} known as {name} the {adjective}.",
    f"Legend speaks of {name}, the {adjective} {noun} from {home}.",
    f"From the shadows of {home}, emerged {name}, a {adjective} {noun}.",
    f"{name}, known as the {adjective} {noun}, hailed from the distant {home}.",
    f"Bearing the title of {adjective} {noun}, {name} ventured from {home}.",
    f"{home} was home to {name}, the {noun} with a {adjective} spirit.",
    f"Once a mere {noun} in {home}, {name} grew to be a {adjective} legend.",
    f"{name}, the {noun} of {home}, was celebrated for their {adjective} nature.",
        f"A tale of yore speaks of {name}, the {adjective} {noun} from the depths of {home}.",
    f"Known far and wide, {name} the {adjective} traveled across {home} in search of {noun}.",
    f"Under the skies of {home}, {name}, famed as a {adjective} {noun}, embarked on a quest to {verb}.",
    f"Whispers in {home} tell the story of {name}, a {noun} with a heart of {adjective} courage.",
    f"{name}, whose {adjective} prowess as a {noun} was unrivaled, hailed from the mystic {home}.",
    f"In {home}, legends spoke of {name}, a {adjective} soul who mastered the art of {noun}.",
    f"Emerging from the heart of {home}, {name}, known for {pronoun} {adjective} ways, sought the legendary {noun}.",
    f"Once a simple {noun} in {home}, {name} became a symbol of {adjective} strength.",
    f"From the bustling streets of {home}, {name} the {adjective} {noun} set out to {verb} the unknown.",
    f"In the annals of {home}, the name {name} stands out as a {adjective} {noun} of great renown.",
    f"Destiny called to {name}, a {noun} of {adjective} resolve, from the far reaches of {home}.",
    f"Among the tales told in {home}, none is as compelling as that of {name}, the {adjective} {noun}.",
    f"In {home}, a land of mystery, roamed {name}, a {noun} known for {pronoun} {adjective} demeanor.",
    f"Carrying the legacy of {home}, {name}, a {adjective} {noun}, rose to challenge the might of {noun}.",
    f"The chronicles of {home} herald {name} as a {adjective} {noun} who dared to {verb}.",
    f"From a lineage of {noun}s in {home}, {name} stood out as particularly {adjective}.",
    f"Beyond the hills of {home}, {name} the {adjective} {noun} sought to rewrite history.",
    f"Few in {home} could match the {adjective} prowess of {name}, a born {noun}.",
    f"Through the lands of {home}, {name} journeyed, a {noun} of {adjective} distinction, on a mission to {verb}.",
    f"The {adjective} {noun} of {home}, {name}, was a legend in their own time, known to {verb} with grace."
    ]

    two = [
    f"{name} comes from a family of {jobs} in {place}, where they always felt out of place.",
    f"In {place}, a land renowned for {jobs}, {name} grew up dreaming of a different life.",
    f"{name}, born into a long line of {jobs} in {place}, sought to break free from family traditions.",
    f"Despite hailing from a respected family of {jobs} in {place}, {name} yearned for adventure.",
    f"The {jobs} of {place} were well-known, but {name} never shared their family's passion for the trade.",
    f"Growing up in {place}, {name} was expected to follow in the {jobs} footsteps of {pronoun} family.",
    f"{name}'s family were prominent {jobs} in {place}, yet they always felt drawn to a different calling.",
    f"From a young age in {place}, {name}, child of {jobs}, dreamed of a life beyond {pronoun} destined path.",
    f"Among the {jobs} of {place}, {name} was the exception, always looking to the horizon.",
    f"{name}, a native of {place}, was born to a family of {jobs}, but {pronoun} heart lay elsewhere.",
    f"Destiny seemed to have chosen {jobs} for {name} in {place}, but {pronoun} aspirations were different.",
    f"In the world of {jobs} in {place}, {name} stood apart, a dreamer in a pragmatic family.",
    f"{name}, despite being born to the famed {jobs} of {place}, held a secret desire to change {pronoun} fate.",
    f"Raised by {jobs} in the heart of {place}, {name} always felt a call to a different life.",
    f"Life among the {jobs} in {place} never suited {name}, who sought something more.",
    f"As a descendant of the renowned {jobs} in {place}, {name} was expected to follow suit, but {pronoun} dreams lay elsewhere.",
    f"{name}'s lineage of {jobs} in {place} couldn't quell the restless spirit within themselves.",
    f"Amongst the {jobs} of {place}, {name} was an outlier, yearning for an escape from the mundane.",
    f"The {jobs} of {place} were a proud clan, but {name} never embraced the family trade.",
    f"{name}, offspring of the celebrated {jobs} of {place}, always felt a different calling tugging at {pronoun} soul.",
    f"Born to {jobs} in the bustling {place}, {name} was the first to rebel against the family norm.",
    f"Tradition dictated {name}, like {pronoun} ancestors in {place}, become a {jobs}, but {pronoun} ambitions lay far beyond.",
    f"{name}, from a lineage of {jobs} in {place}, harbored a secret passion that differed from {pronoun} heritage.",
    f"In {place}, where {jobs} were revered, {name} grew up feeling like an outcast in {pronoun} own family.",
    f"The {name} family were well-known {jobs} in {place}, but {name} always sought a different path.",
    f"Growing up among {jobs} in {place}, {name} often felt a dissonance."
    ]

    three = [
    f"{name}, known for {pronoun} {adjective} temperament, often surprised those in {place} with {pronoun} actions.",
    f"In {place}, {name} was famed for {pronoun} {adjective} nature, making friends and foes alike.",
    f"Despite {pronoun} {adjective} demeanor, {name} from {place} harbored unexpected depths.",
    f"{name}'s {adjective} personality was a legend in {place}, often leading to unforeseen adventures.",
    f"Underneath {pronoun} {adjective} exterior, {name} of {place} hid a world of thoughts and dreams.",
    f"Everyone in {place} knew {name} for {pronoun} {adjective} ways, but there was more to them than met the eye.",
    f"Though {adjective} at heart, {name} from {place} often displayed a surprisingly different side.",
    f"In the realm of {place}, {name}'s {adjective} character was as well-known as the local landmarks.",
    f"{name}, with {pronoun} unmistakably {adjective} personality, left a mark on everyone in {place}.",
    f"While {adjective} on the surface, {name} of {place} possessed a complexity that intrigued many.",
    f"The {adjective} nature of {name} was a tale often told in the corners of {place}.",
    f"{name}'s presence in {place} was always felt, thanks to {pronoun} {adjective} persona.",
    f"Despite living in {place}, {name} never let the surroundings dampen {pronoun} {adjective} spirit.",
    f"From a young age in {place}, {name} exhibited an {adjective} character, which defined many of {pronoun} choices.",
    f"{name}, a resident of {place}, was often the topic of discussion for {pronoun} {adjective} qualities.",
    f"Many in {place} thought they knew {name}, but {pronoun} {adjective} personality always had another layer.",
    f"{name} of {place} was a paradox, {adjective} yet deeper than most realized.",
    f"The {adjective} charm of {name} was something the folks of {place} often spoke about.",
    f"Known in {place} for {pronoun} {adjective} traits, {name} was a subject of much curiosity.",
    f"{name}, hailing from {place}, managed to be both {adjective} and enigmatic.",
    f"Everyone in {place} had an opinion about {name}'s {adjective} personality.",
    f"The {adjective} {name} from {place} was as complex as the history of the land itself.",
    f"Life in {place} was never dull with {name}'s {adjective} presence.",
    f"{name}, the {adjective} soul of {place}, was a riddle wrapped in a mystery.",
    f"Within the bounds of {place}, {name} was renowned for {pronoun} {adjective} nature, often leading to remarkable tales.",
    f"The {adjective} disposition of {name} made life in {place} all the more interesting.",
    f"In {place}, {name}'s {adjective} behavior was as well-known as the town square.",
    f"{name}, the heart and soul of {place}, was admired for {pronoun} {adjective} qualities.",
    f"Few could match the {adjective} character of {name} in {place}, a trait that often led to unexpected journeys.",
    f"Amidst the hustle of {place}, {name} stood out with a(n) {adjective} personality that captivated many.",

    ]
    four = [
    f"Despite {name}'s strengths, they always struggled with {weakness} in {place}.",
    f"In {place}, {name}'s battle with {weakness} was well-known, shaping much of {pronoun} life.",
    f"{name}, hailing from {place}, often found {pronoun} {weakness} to be {pronoun} greatest hurdle.",
    f"While {name} excelled in many areas, {pronoun} {weakness} remained a constant challenge in {place}.",
    f"For {name} of {place}, {pronoun} {weakness} was a shadow that loomed large over {pronoun} accomplishments.",
    f"Even in {place}, no one could deny {name}'s {weakness}, a struggle that defined {pronoun} journey.",
    f"{name}'s life in {place} was marked by an ongoing battle against {pronoun} {weakness}.",
    f"Though {name} was known for {pronoun} skills, {pronoun} {weakness} was an ever-present challenge in {place}.",
    f"Living with {weakness} in {place}, {name} learned to navigate a world not made for them.",
    f"Every step of the way in {place}, {name}'s journey was hindered by {pronoun} {weakness}.",
    f"{name}'s experience with {weakness} in {place} taught them resilience in the face of adversity.",
    f"In {place}, {name}'s struggle with {weakness} was a testament to {pronoun} perseverance.",
    f"Despite growing up in {place}, {name} could never fully overcome {pronoun} {weakness}.",
    f"{name}'s {weakness} was a well-known aspect of {pronoun} life story in {place}.",
    f"Among the tales of {place}, {name}'s battle with {weakness} was both inspiring and heart-wrenching.",
    f"{name}, a figure of renown in {place}, faced {pronoun} {weakness} with courage, but not always with success.",
    f"The people of {place} often spoke of {name}'s {weakness} with a mix of sympathy and admiration.",
    f"For {name}, {pronoun} {weakness} was as much a part of themselvese as the streets of {place}.",
    f"In {place}, {name}'s {weakness} was an obstacle that shaped much of {pronoun} path.",
    f"While {name} was a respected figure in {place}, {pronoun} {weakness} was a burden they carried daily.",
    f"Despite the vibrant life in {place}, {name}'s {weakness} cast a long shadow over their experiences.",
    f"{name}'s story in {place} was one of triumph and tragedy, intertwined with {pronoun} struggle with {weakness}.",
    f"In the heart of {place}, {name} faced {pronoun} {weakness} with a mixture of defiance and resignation.",
    f"The legacy of {name} in {place} was colored by the constant presence of {pronoun} {weakness}.",
    f"For {name}, a resident of {place}, living with {weakness} was a daily reality that tested {pronoun} limits.",
    f"Though {name} made a name for themself in {place}, {pronoun} {weakness} was always a part of {pronoun} story.",
    f"In {place}, {name}'s life was a journey of navigating and coping with {pronoun} {weakness}.",
    f"{name}'s tale in {place} is one of endurance in the face of {pronoun} {weakness}.",
    f"While {name} achieved much in {place}, {pronoun} {weakness} remained a defining aspect of {pronoun} life.",
    f"Every day in {place}, {name} confronted {pronoun} {weakness}, a battle that shaped {pronoun} existence.",

    ]

    five = [
    f"Dreaming of {future_aspiration}, {name} from {place} often reminisced about {early_life_event}.",
    f"In {place}, {name}'s heart longed for {love_interest} {name_other}, while {pronoun} mind was set on {future_aspiration}.",
    f"Ever since they {early_life_event}, {name} of {place} had aspired to {future_aspiration}, despite distractions like {love_interest}.",
    f"Haunted by {significant_event} in {place}, {name} sought solace in {love_interest} {name_other}'s arms, dreaming of {future_aspiration}.",
    f"For {name}, who had experienced {early_life_event} in {place}, {future_aspiration} was a guiding light, overshadowing fleeting romances.",
    f"Among the tales of {place}, {name}'s pursuit of {future_aspiration} and love for {name_other} were legendary.",
    f"{name}, after {early_life_event} in {place}, vowed to achieve {future_aspiration}, even if it meant leaving {love_interest} {name_other} behind.",
    f"Life in {place} for {name} was a tapestry of {early_life_event}, aspirations like {future_aspiration}, and romances with people like {love_interest} {name_other}.",
    f"Following {significant_event}, {name} of {place} found hope in {future_aspiration} and comfort in {love_interest} {name_other}'s presence.",
    f"In {place}, {name} balanced {pronoun} ambition for {future_aspiration} with a tumultuous affair with {love_interest} {name_other}.",
    f"Since {early_life_event}, {name} from {place} had pursued {future_aspiration} relentlessly, finding occasional respite with {love_interest} {name_other}.",
    f"{name}, shaped by {significant_event} in {place}, dreamed of {future_aspiration} while navigating complex relationships with people like {love_interest} {name_other}.",
    f"For {name}, hailing from {place}, {future_aspiration} was a distant dream, often eclipsed by the allure of {love_interest} {name_other}.",
    f"{place} whispered tales of {name}'s {early_life_event} and {pronoun} quest for {future_aspiration}, entangled with escapades involving {love_interest} {name_other}.",
    f"Despite the shadows of {significant_event}, {name} from {place} clung to the dream of {future_aspiration}, occasionally distracted by {love_interest} {name_other}.",
    f"{name}, known in {place} for surviving {early_life_event}, chased {future_aspiration} with a fervor, often sidetracked by liaisons with {love_interest} {name_other}.",
    f"In {place}, {name}'s path was a blend of {significant_event}, the pursuit of {future_aspiration}, and complicated dynamics with {love_interest} {name_other}.",
    f"After {early_life_event}, {name} of {place} set sights on {future_aspiration}, though {pronoun} heart was frequently stolen by {love_interest} {name_other}.",
    f"Amidst the echoes of {significant_event} in {place}, {name} dreamt of {future_aspiration}, while juggling romances with individuals like {love_interest} {name_other}.",
    f"For {name}, {early_life_event} in {place} was a pivotal chapter, leading to dreams of {future_aspiration} and entanglements with {love_interest} {name_other}.",
    f"Life for {name} in {place}, marked by {significant_event}, was a quest for {future_aspiration}, interspersed with romantic encounters with {love_interest} {name_other}.",
    f"{name}, after enduring {early_life_event} in {place}, pursued {future_aspiration} passionately, often finding refuge in the company of {love_interest} {name_other}.",
    f"Despite {significant_event}'s impact, {name} from {place} never lost sight of {future_aspiration}, even amidst passionate moments with {love_interest} {name_other}.",
    f"In {place}, {name}'s journey from having  {early_life_event} towards {future_aspiration} was frequently colored by the presence of {love_interest} {name_other}.",
    f"After {significant_event}, {name}'s life in {place} became a pursuit of {future_aspiration}, with {love_interest} playing a key role in {pronoun} story.",
    f"From the aftermath of them having {early_life_event}, {name} in {place} sought {future_aspiration}, while navigating a complicated relationship with {love_interest} {name_other}.",
    f"The path to {future_aspiration} for {name} of {place} was never straightforward, especially with {love_interest} in the picture.",
    f"Following the fact they {early_life_event}, {name}'s ambition to achieve {future_aspiration} in {place} was often in conflict with {pronoun} feelings for {love_interest} {name_other}.",
    f"Even amidst the trials of they {significant_event} in {place}, {name}'s focus on {future_aspiration} remained strong, though occasionally shaken by {love_interest} {name_other}.",
    f"Growing up in {place} after they {early_life_event}, {name}'s pursuit of {future_aspiration} often intertwined with {pronoun} romantic escapades, especially with {love_interest} {name_other}.",
    ]

    six = [
    f"Always {personality}, {name}  had a penchant for {like}, but they couldn't stand {dislike}.",
    f"With her {personality} nature, {name}  adored {like} yet always avoided {dislike}.",
    f"Being exceptionally {personality}, {name} was passionate about {like}, but they detested {dislike}.",
    f"{personality} at heart, {name}  found joy in {like}, but {dislike} was never her cup of tea.",
    f"{name} , known for their {personality} demeanor, relished every moment of {like} but turned away from {dislike}.",
    f"As a {personality} individual, {name}  loved {like} but had an aversion to {dislike}.",
    f"The {personality} {name}  always had a soft spot for {like}, in stark contrast to their dislike for {dislike}.",
    f"{name} , who was {personality}, found solace in {like} but could not bear {dislike}.",
    f"{personality} and spirited, {name}  spent hours with {like}, but {dislike} always irked him.",
    f"{name}, with her {personality} nature, was drawn to {like} but repulsed by {dislike}.",
    f"{name}, a {personality} soul, cherished their time with {like}, but steered clear of {dislike}.",
    f"{name}'s {personality} personality meant their was naturally inclined towards {like} but recoiled at {dislike}.",
    f"Known for being {personality}, {name} had an affinity for {like}, but an undeniable distaste for {dislike}.",
    f"{name}, ever so {personality}, found {like} to be her refuge, unlike {dislike}, which they found unbearable.",
    f"{name}'s {personality} traits led her to embrace {like} and reject {dislike}.",
    f"{name}, a {personality} character, always sought out {like}, but {dislike} was their nemesis.",
    f"With a {personality} spirit, {name} was naturally drawn to {like}, but {dislike} was her pet peeve.",
    f"{name}, who was {personality} in nature, had a deep passion for {like}, but a strong disdain for {dislike}.",
    f"{name}, known for her {personality} attitude, always leaned towards {like} and away from {dislike}.",
    f"Being {personality}, {name} could spend hours engaged in {like}, but they had no tolerance for {dislike}.",
    f"{name}, a {personality} figure, had a lifelong love for {like}, but {dislike} was her bane.",
    f"{name}, characterized by their {personality} nature, was always involved in {like}, but they never got along with {dislike}.",
    f"A {personality} person, {name} had a profound love for {like}, but a deep-seated aversion to {dislike}.",
    f"{name}, always {personality}, was fascinated by {like}, yet {pronoun} found {dislike} utterly off-putting.",
    f"With her {personality} personality, {name} was irresistibly drawn to {like}, but they had a strong aversion to {dislike}.",
    f"{name}'s {personality} demeanor led him to seek out {like}, but they always kept a distance from {dislike}.",
    f"A {personality} individual, {name} found her joy in {like}, but {dislike} was something they could never get used to.",
    f"As someone who was {personality}, Michael had an undying love for {like}, but they couldn't stand the sight of {dislike}.",
    f"{name}, with her {personality} nature, thrived in the presence of {like}, but withered at {dislike}.",
    f"Being uniquely {personality}, {name} treasured every moment they spent with {like}, but had no patience for {dislike}.",

    ]

    seven = [
        f"Their best friend, {name_other}, always knew how to lift their spirits.",
        f"Their sibling {name_other} had been their rival in games but their partner in mischief.",
        f"{name_other}, their mentor, had a profound influence on their life choices.",
        f"In childhood, {name_other} was their constant companion and fellow explorer.",
        f"During difficult times, their cousin {name_other} was a pillar of strength.",
        f"Their partner {name_other} stood beside them, steadfast in every storm.",
        f"Alongside their comrade {name_other}, they faced many life challenges.",
        f"Their grandmother {name_other} would recount tales of her youth, filled with wisdom and wit.",
        f"Their teacher, {name_other}, provided guidance and knowledge beyond the classroom.",
        f"The neighbor {name_other} had been like a guardian, always watching over them.",
        f"Their childhood friend {name_other} shared with them the purest joys of youth.",
        f"{name_other}, their colleague, was a source of endless encouragement.",
        f"Their elder brother {name_other} was both a mentor and a protector in their early years.",
        f"Their confidante {name_other} shared in both their sorrows and their joys.",
        f"Working with {name_other} brought new perspectives and growth.",
        f"Growing up, their twin {name_other} was their mirror and their opposite.",
        f"Aunt {name_other} inspired them to chase their dreams, no matter the odds.",
        f"Childhood adventures were always more exciting with {name_other} by their side.",
        f"Coffee sessions with {name_other} were the highlights of their week.",
        f"Study sessions with {name_other} turned even tedious subjects into fun challenges.",
        f"Adventures with {name_other} were never short of excitement and discovery.",
        f"Living with {name_other} taught them the art of sharing and understanding.",
        f"Training under {name_other} was an experience that shaped their very core.",
        f"Loyal and steadfast, their friend {name_other} never failed them.",
        f"Their elder sister {name_other} was the epitome of grace and resilience.",
        f"Science experiments with {name_other} led to many surprising discoveries.",
        f"Long walks with {name_other} were moments of peace and reflection.",
        f"Traveling the world, they discovered its wonders with {name_other}.",
        f"Navigating the complexities of city life, {name_other} was their invaluable guide.",
        f"In debates, {name_other} always challenged them to think deeper and argue smarter.",
    ]
    eight = [
    f"{name}, seeking to overcome {pronoun} {weakness}, ventured into {place} to confront {noun}, guided by {pronoun} love for {love_interest} {name_other}.",
    f"In {place}, the {noun} that once {verb} {name} became the catalyst for {pronoun} journey towards conquering {pronoun} {weakness} and winning the heart of {love_interest} {name_other}.",
    f"Haunted by {pronoun} {weakness}, {name} from {place} found solace in the company of {love_interest} {name_other}, as they together faced the perils of {noun}.",
    f"With a heart burdened by {weakness}, {name} of {place} sought redemption in the eyes of {love_interest} {name_other}, embarking on a quest to vanquish the infamous {noun}.",
    f"Driven by {pronoun} past {early_life_event}, {name} confronted {pronoun} {weakness} in the depths of {place}, all for the affection of {love_interest} {name_other}.",
    f"Amidst the chaos of {place}, {name} battled {pronoun} inner {weakness} while navigating the complexities of {pronoun} relationship with {love_interest} {name_other}.",
    f"In a daring escapade in {place}, {name}, plagued by {pronoun} {weakness}, sought to prove {pronoun} worth to {love_interest} {name_other} by facing the fearsome {noun}.",
    f"{name}, tormented by {weakness} yet driven by love for {love_interest} {name_other}, embarked on a perilous journey to {place} to confront the legendary {noun}.",
    f"Destiny led {name} from {place} to seek {pronoun} fortune and conquer {pronoun} {weakness}, all while holding a torch for {love_interest} {name_other}, who inspired {pronoun} bravery against the dreaded {noun}.",
    f"In {place}, {name}'s struggle with {weakness} intertwined with {pronoun} deep affection for {love_interest} {name_other}, setting them on a path to face the enigmatic {noun}.",
    f"Compelled by {pronoun} {weakness} and the pull of {pronoun} heart towards {love_interest} {name_other}, {name} ventured into the unknown of {place} to challenge the ancient {noun}.",
    f"As {name} battled with {pronoun} {weakness} in the wilds of {place}, the thought of {love_interest} {name_other} gave them strength to confront the treacherous {noun}.",
    f"In a twist of fate, {name} from {place}, burdened by {weakness}, found {pronoun} destiny intertwined with {love_interest} {name_other} as they faced the perilous {noun}.",
    f"Driven by a desire to overcome {pronoun} {weakness} and win the heart of {love_interest} {name_other}, {name} embarked on a daunting quest in {place} to conquer the fearsome {noun}.",
    f"In the heart of {place}, {name}, haunted by {pronoun} {weakness}, forged an unlikely alliance with {love_interest} {name_other} to defeat the formidable {noun}.",
    f"Seeking to redeem themselves from {pronoun} {weakness}, {name} of {place} joined forces with {love_interest} {name_other} to brave the dangers of the {noun}.",
    f"The tale of {name} from {place}, battling {pronoun} {weakness} while yearning for the affections of {love_interest} {name_other}, led them tothe lair of the formidable {noun}.",
    f"Amidst the mysteries of {place}, {name}'s quest to overcome {pronoun} {weakness} became entangled with {pronoun} blossoming feelings for {love_interest} {name_other}, culminating in a showdown with the enigmatic {noun}.",
    f"Under the spell of {place}, {name}, grappling with {pronoun} {weakness}, embarked on a fateful journey to earn the admiration of {love_interest} {name_other} and confront the legendary {noun}.",
    f"With {pronoun} heart torn between {pronoun} {weakness} and the allure of {love_interest} {name_other}, {name} faced the ultimate challenge in {place}: to vanquish the dreaded {noun}.",
    f"Confronted with {pronoun} {weakness} in the heart of {place}, {name} sought not only redemption but also the love of {love_interest} {name_other}, leading to a perilous encounter with the mysterious {noun}.",
    f"In pursuit of {pronoun} true calling and the affection of {love_interest} {name_other}, {name}, overshadowed by {pronoun} {weakness}, ventured deep into {place} to challenge the power of the {noun}.",
    f"The journey of {name}, marked by {pronoun} struggle with {weakness} and devotion to {love_interest} {name_other}, led them through the treacherous terrains of {place} to seek the holy {like}",
    ]
    nine = [
    f"In a dramatic turn of events, {name} was falsely accused of stealing the {noun} in {place}, altering their life forever.",
    f"A fateful encounter with a {adjective} sorcerer in {place} bestowed upon {name} an unexpected magical ability, changing their destiny.",
    f"Surviving a harrowing attack by bandits in {place}, {name} discovered a hidden strength within them, reshaping their future.",
    f"During a rare celestial event in {place}, {name} witnessed a vision of {noun}, setting them on a path they never expected.",
    f"A chance meeting with {name_other}, a mysterious traveler in {place}, revealed to {name} a secret about their heritage, turning their world upside down.",
    f"Captured and then miraculously escaping from a demonic cult in {place}, {name}'s perspective on life was forever altered.",
    f"After being saved from a near-death experience by a {noun} in {place}, {name} pledged to change their ways, embarking on a new journey.",
    f"Uncovering an ancient {noun} in the ruins of {place} led {name} to a revelation about their true purpose in life.",
    f"A devastating natural disaster in {place} left {name} as the sole survivor of their clan, thrusting them into an unexpected role.",
    f"An accidental brush with a cursed {noun} in {place} granted {name} a glimpse into the future, compelling them to take a different path.",
    f"While exploring the depths of {place}, {name} fell into a hidden realm, emerging with memories of a past life and a new destiny.",
    f"Betrayed by {name_other} in {place}, {name} was forced to flee, leading to a journey of self-discovery and transformation.",
    f"During a festival in {place}, a {noun} chose {name} as its champion, setting them on a course filled with danger and glory.",
    f"A sudden uprising in {place} saw {name} taking an unexpected leadership role, drastically changing their life's trajectory.",
    f"An encounter with a legendary creature in {place} left {name} with a rare and powerful artifact, altering the course of their future.",
    f"After being wrongly imprisoned in {place}, {name}'s escape led them to uncover a conspiracy that would change their fate.",
    f"Rescuing {name_other} from a perilous situation in {place} led {name} to uncover a talent for heroism they never knew they had.",
    f"A mysterious illness in {place} robbed {name} of an important ability, forcing them to adapt and find new strengths.",
    f"Stumbling upon an ancient prophecy in {place}, {name} realized that their destiny was intertwined with the fate of the realm.",
    f"In a bizarre twist of fate, {name} swapped bodies with a {noun} in {place}, leading to a series of adventures and a new perspective on life.",
    f"Upon discovering they were the heir to a forgotten throne in {place}, {name}'s life was thrust into a world of politics and intrigue.",
    f"A devastating loss in a battle against bandits in {place} left {name} seeking vengeance, reshaping their identity and purpose.",
    f"Finding themselves the sole witness to a supernatural event in {place}, {name} was entrusted with a powerful secret that would define their future.",
    f"An unexpected inheritance from a distant relative in {place} revealed to {name} a hidden world of magic and danger they were destined to be a part of.",
    f"After a mystical encounter with a {noun} during a storm in {place}, {name} gained insights that set them on a quest for truth and enlightenment."
    ]
    ten = [
    f"Now residing in {place}, {name} has become a renowned {jobs}, respected and feared for their past and present deeds.",
    f"In the bustling heart of {place}, {name} leads a double life as a {jobs} by day and a secret defender of the downtrodden by night.",
    f"Currently, {name} serves as a trusted {jobs} in {place}, hiding their complex past from those around them.",
    f"After their life-altering experiences, {name} now wanders the lands of {place} as a nomadic {jobs}, seeking new adventures.",
    f"In {place}, {name} has established themselves as a {jobs}, using the skills learned from their tumultuous past.",
    f"Having settled in {place}, {name} now lives a life of quiet contemplation as a {jobs}, a stark contrast to their once turbulent existence.",
    f"{name}, once a wanderer, now holds a position of power as a {jobs} in {place}, their past adventures having shaped their leadership.",
    f"Reformed and refocused, {name} now dedicates their life to being a {jobs} in {place}, helping others avoid the pitfalls of their own past.",
    f"Currently, {name} is a well-known {jobs} in {place}, their reputation built on the foundations of their extraordinary life experiences.",
    f"In {place}, {name} has turned their back on adventuring, choosing instead to live a peaceful life as a {jobs}, though their past still haunts them.",
    f"{name} now thrives in {place} as a {jobs}, their life's journey having prepared them uniquely for the challenges of their role.",
    f"Today, {name} finds themselves as a {jobs} in {place}, constantly drawing upon their varied experiences to guide their decisions.",
    f"Having embraced their destiny, {name} now stands as a respected {jobs} in {place}, their past adventures having become legends told in hushed tones.",
    f"Living in {place}, {name} has taken up the mantle of a {jobs}, using their hard-earned wisdom to make a difference in the world.",
    f"Now, {name} is a beloved {jobs} in {place}, their past trials having endowed them with a unique perspective and set of skills.",
    f"In the wake of their tumultuous past, {name} has emerged as a {jobs} in {place}, renowned for their resilience and expertise.",
    f"Currently, {name} holds the esteemed position of {jobs} in {place}, their journey from hardship to heroism inspiring many.",
    f"After many trials, {name} has settled in {place} as a {jobs}, finding solace and purpose in a role that reflects their growth and experiences.",
    f"Today, {name} is a key figure in {place} as a {jobs}, their past adventures having paved the way for their current standing.",
    f"With a life full of twists and turns, {name} now finds stability and satisfaction as a {jobs} in {place}, their experiences shaping their daily life."
    ]
    return 

def generate():

    global name, home
    
    name = random.choice(name_info)
    home = random.choice(place_info)
    # Clear the textbox
    text_box.delete("1.0", tk.END)

    # Generate the new backstory
    new_backstory = ""
    randomize()
    new_backstory += random.choice(one) + "\n"
    randomize()
    new_backstory += random.choice(two) + "\n"
    randomize()
    new_backstory += random.choice(three) + "\n"
    randomize()
    new_backstory += random.choice(four) + "\n"
    randomize()
    new_backstory += random.choice(five) + "\n"
    randomize()
    new_backstory += random.choice(six) + "\n"
    randomize()
    new_backstory += random.choice(seven)
    randomize()
    new_backstory += random.choice(eight) + "\n"
    randomize()
    new_backstory += random.choice(nine) + "\n"
    randomize()
    new_backstory += random.choice(ten) + "\n"
    randomize()
    # Insert new backstory into the textbox
    text_box.insert(tk.END, new_backstory)







name = "NULL"
name_other = "NULL"
adjective = "NULL"
place = "NULL"
noun= "NULL"
verb = "NULL"
jobs = "NULL"
weakness ="NULL"
future_aspiration = "NULL"
love_interest = "NULL"
significant_event  = "NULL"
early_life_event = "NULL"
personality = "NULL"
like = "NULL"
dislike = "NULL"

name_data = "name.txt"
adjective_data = "adjective.txt"
place_data = "place.txt"
noun_data = "noun.txt"
verb_data = "verb.txt"
jobs_data = "jobs.txt"
weakness_data = "weakness.txt"
future_aspiration_data = "future_aspiration.txt"
love_interest_data = "love_interest.txt"
significant_event_data = "significant_event.txt"
early_life_event_data = "early_life_event.txt"
personality_data = "personality.txt"
like_data = "like.txt"
dislike_data = "dislike.txt"

name_info = load_data_from_file(name_data)
name_other_info = load_data_from_file(name_data)
adjective_info = load_data_from_file(adjective_data)
place_info = load_data_from_file(place_data)
noun_info = load_data_from_file(noun_data)
verb_info = load_data_from_file(verb_data)
jobs_info = load_data_from_file(jobs_data)
weakness_info = load_data_from_file(weakness_data)
future_aspiration_info = load_data_from_file(future_aspiration_data)
love_interest_info = load_data_from_file(love_interest_data)
significant_event_info = load_data_from_file(significant_event_data)
early_life_event_info = load_data_from_file(early_life_event_data)
personality_info = load_data_from_file(personality_data)
like_info = load_data_from_file(like_data)
dislike_info = load_data_from_file(dislike_data)

randomize()

pronoun = "their"

root = tk.Tk()
root.title("Backstory Generator")
root.minsize(500, 300)  # Set a minimum size for the window

# Styling
modernFont = tkFont.Font(family="Times New Roman", size=12)

main_background_color = "#123456"  # Dark blue background
trim_color = "#789abc"  # Trim color
button_color = "#f0f0f0"  # Button color

root.configure(bg=main_background_color)

# Text Box
text_box = tk.Text(root, height=10, width=250, font=modernFont, padx=10, pady=10, wrap=tk.WORD, borderwidth=2, relief="groove", bg=trim_color, fg="black")
text_box.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Generate Button
generate_button = tk.Button(root, text="Generate new backstory", command=generate, font=modernFont, bg=button_color, fg="black", bd=2, padx=10, pady=5, relief="raised")
generate_button.pack(pady=10)

root.mainloop()