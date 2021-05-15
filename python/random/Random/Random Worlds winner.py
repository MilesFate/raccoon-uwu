import random

group_a= ['G2 Esports','Suning','Machi Esports','Team Liquid']
group_b= ['DAMWON Gaming','Rogue','JD Gaming','PSG Talon']
group_c= ['Gen G','TSM','Fnatic','LGD Gaming']
group_d= ['FlyQuest','DRX','Top Esports','Unicorns of Love']
playins_group_1 = ['Team Liquid','Legacy Esports','Papara SuperMassive','MAD Lions','INTZ']
playins_group_2 = ['PSG','Unicorns of Love','Rainbow7','LGD Gaming','V3 Esports']
Worlds_team_pool =['G2 Esports','Suning','Machi Esports','DAMWON Gaming','Rogue','JD Gaming','Gen G','TSM','Fnatic','FlyQuest','DRX','Top Esports','Team Liquid', 'Legacy Esports','Papara SuperMassive','MAD Lions','INTZ','PSG','Unicorns of Love','Rainbow7','LGD Gaming','V3 Esports']

g1_winner = random.choice(group_a)
g2_winner = random.choice(group_b)
g3_winner = random.choice(group_c)
g4_winner = random.choice(group_d)
pLIG1 = random.choice(playins_group_1)
pLIG2 = random.choice(playins_group_2)
pLIG3 = random.choice(playins_group_1)
pLIG4 = random.choice(playins_group_2)
Worlds_Winner = random.choice(Worlds_team_pool)

Groups_outcome_1 = ("{} will win 1st in group A.").format(g1_winner)
Groups_outcome_2 = ("{} will win 1st in group B.").format(g2_winner)
Groups_outcome_3 = ("{} will win 1st in group C.").format(g3_winner)
Groups_outcome_4 = ("{} will win 1st in group D.").format(g4_winner)
Play_ins_outcome_1 = ("{} will win 1st in their play in group.").format(pLIG1)
Play_ins_outcome_2 = ("{} will win 1st in their play in group.").format(pLIG2)
Play_ins_outcome_3 = ("{} will win 1st in their play in group.").format(pLIG3)
Play_ins_outcome_4 = ("{} will win 1st in their play in group.").format(pLIG4)
Winner = ("The Winner of Worlds will be {}, can't wait for the skins!").format(Worlds_Winner)

print(Groups_outcome_1)
print(Groups_outcome_2)
print(Groups_outcome_3)
print(Groups_outcome_4)
print(Play_ins_outcome_1)
print(Play_ins_outcome_3)
print(Play_ins_outcome_2)
print(Play_ins_outcome_4)
print(Winner)