#Status: Complete

#this gets all the information needed to fillout the blacks
adjective_1 = input('First Adjective: ')
adjective_2 = input('Second Adjective: ')
type_of_bird = input('Type of Bird: ')
room_in_house = input('Room in House: ')
verb_1 = input('First Verb: ')
verb_2 = input('Second Verb: ')
relatives_name = input('Relatives Name: ')
noun_1 = input('First Noun: ')
liquid = input('Type of Liquid: ')
verb_ending_in_ing = input('First Verb Ending in ing: ')
part_of_the_body_plural = input('Part of the Body (Plural): ')
plural_noun = input('Noun (Plural): ')
verb_ending_in_ing_2 = input('Second Verb Ending in ing: ')
noun_2 = input('Second Noun: ')

#this is the story where the above is placed
story = """
It was a {}, cold November day.
I woke up to the {} smell of {} roasting in the {} downstairs.
I {} down the stairs to see if I could help {} the dinner.
My mom said, "see if {} needs a fresh {}."
So I carried a tray of glasses full of {} into the {} room.
When I got there, I couldn't believe my {}!
There were {} {} on the {}!
"""

#this shows the story with the blanks filled in
print(story.format(adjective_1, adjective_2, type_of_bird, room_in_house, verb_1 ,verb_2 ,relatives_name ,noun_1 ,liquid,
                   verb_ending_in_ing ,part_of_the_body_plural ,plural_noun ,verb_ending_in_ing_2 ,noun_2))
