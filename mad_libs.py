


print(" ===Trapped inside a video game=== \n")
print("")
name = input("I'll require from you eight words, please give me a name: ").strip().title()
adjective = input("Give me an adjective. ").lower()
verb = input("Give me a verb. ").lower()
place = input("Give me an a place. ").strip().title()
food = input("Give me a food. ").lower()
animal = input("Give me an animal. ").lower()
number = int(input("Give me a number. "))
object = input("Give me an object. ").lower()
story = f"""Trapped in the digital world of {place}, {name} stared intently at his {object} as the sky shifted into a deep, synthetic {adjective}. 
      The system architecture is locked down tight, he sighed, trying to ignore his companion’s digital companion—a hyperactive {animal} that kept nudging his arm. 
      His guildmate smiled and passed him a steaming clay pot, saying, Don't blame the animal, {verb} some of this {food} before the stat buffs wear off. 
      {name} took a bite, causing a sudden holographic text to flash across his vision: Level {number} Reached. Looking up in amazement, he whispered, 
      This premium meal just gave me the exact experience boost we need to face tomorrow's boss."""

print(f"Name:{name}")
print(f"Adjective:{adjective}")
print(f"Verb:{verb}")
print(f"Place:{place}")
print(f"Food:{food}")
print(f"Animal:{animal}")
print(f"Number:{number * 2}.")
print(f"Object:{object}")
print(story)
print(f"Your story has {len(story.split())} words.")
