print(" ===Trapped inside a video game=== \n")
print("")
name = (
    input("I'll require from you eight words, please give me a name: ").strip().title()
)
adjective = input("Give me an adjective. ").strip().lower()
verb = input("Give me a verb. ").strip().lower()
place = input("Give me an a place. ").strip().title()
food = input("Give me a food. ").strip().lower()
animal = input("Give me an animal. ").strip().lower()
number = int(input("Give me a number. ").strip())
item = input("Give me an object. ").strip().lower()
shouted = "shouted".upper()

story = f"""The digital sky of Aethelgard fractured into a brilliant neon glare, 
sealing thousands of players inside a reality where logging out was no longer an option.
{name} sat tightly gripped by panic in the starting plaza of {place},
his knuckles white as his fingers raced across the keyboard of a high-tier relic {item}
to parse the game's locked source code. A pixelated companion {animal} suddenly nudged his elbow,
causing his hand to slip and accidentally execute a rogue data loop that multiplied his experience
variable instantly. "SYSTEM INTRUSION!" {name} {shouted}, staring in utter disbelief as a flashing
holographic notification materialized above his head to announce he had reached Level {number}.
His guildmate Hana rushed over, scanning his stats in shock. "Incredible,
your level doubled from {number}!" she gasped, pulling up a tactical interface.
"Let's see... {number} times two means your combat power is now {number * 2}!" {name} 
nodded eagerly, replying, "Yes, that math gives us the exact damage output we need!" 
Hana handed him a steaming clay pot of savory {food}, urging, 
"Perfect, now {verb} this before the server detects the glitch and wipes your character!"
Gulping down the food as the {adjective} twilight deepened, {name} watched his boosted 
stat bars permanently lock an a {place}, ready to face the floor boss."""

print(f"Name:{name}")
print(f"Adjective:{adjective}")
print(f"Verb:{verb}")
print(f"Place:{place}")
print(f"Food:{food}")
print(f"Animal:{animal}")
print(f"Number:{number * 2}.")
print(f"Item:{item}")
print(story)
print("")
print(f"Your story has {len(story.split())} words.")
