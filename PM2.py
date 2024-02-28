class Job:
    def __init__(self, name, Constitution, Strength, Intelligence, Refinement, Charisma, Morality, Faith, Sin, Sensitivity, Stress, gold, min_age):
        self.name = name
        self.Constitution = Constitution
        self.Strength = Strength
        self.Intelligence = Intelligence
        self.Refinement = Refinement
        self.Charisma = Charisma
        self.Morality = Morality
        self.Faith = Faith
        self.Sin = Sin
        self.Sensitivity = Sensitivity
        self.Stress = Stress
        self.gold = gold
        self.min_age = min_age

        self.stats = [self.Constitution, self.Strength, self.Intelligence, 
                      self.Refinement, self.Charisma, self.Morality, 
                      self.Faith, self.Sin, self.Sensitivity, 
                      self.Stress, self.gold]
    def __str__(self):
        r_string = f"\nJob Name: {self.name}\n"
        if self.Constitution != 0:
            r_string += f"Constitution: {self.Constitution}\n"
        if self.Strength != 0:
            r_string += f"Strength: {self.Strength}\n"
        if self.Intelligence != 0:
            r_string += f"Intelligence: {self.Intelligence}\n"
        if self.Refinement != 0:
            r_string += f"Refinement: {self.Refinement}\n"
        if self.Charisma != 0:
            r_string += f"Charisma: {self.Charisma}\n"
        if self.Morality != 0:
            r_string += f"Morality: {self.Morality}\n"
        if self.Faith != 0:
            r_string += f"Faith: {self.Faith}\n"
        if self.Sin != 0:
            r_string += f"Sin: {self.Sin}\n"
        if self.Sensitivity != 0:
            r_string += f"Sensitivity: {self.Sensitivity}\n"
        if self.Stress != 0:
            r_string += f"Stress: {self.Stress}\n"
        if self.gold != 0:
            r_string += f"Gold: {self.gold}\n"
        r_string += f"Minimum Age: {self.min_age}\n"
        return r_string


    def return_work_week(self, days):
        return [val * days for val in self.stats]

    def check_age(self, age_given):
        return age_given >= self.min_age
    
    def return_week_str(self, days):
        r_string = f"\nJob Name: {self.name}\nDays Worked: {days}\n"
        if self.Constitution != 0:
            r_string += f"Constitution: {self.Constitution*days}\n"
        if self.Strength != 0:
            r_string += f"Strength: {self.Strength*days}\n"
        if self.Intelligence != 0:
            r_string += f"Intelligence: {self.Intelligence*days}\n"
        if self.Refinement != 0:
            r_string += f"Refinement: {self.Refinement*days}\n"
        if self.Charisma != 0:
            r_string += f"Charisma: {self.Charisma*days}\n"
        if self.Morality != 0:
            r_string += f"Morality: {self.Morality*days}\n"
        if self.Faith != 0:
            r_string += f"Faith: {self.Faith*days}\n"
        if self.Sin != 0:
            r_string += f"Sin: {self.Sin*days}\n"
        if self.Sensitivity != 0:
            r_string += f"Sensitivity: {self.Sensitivity*days}\n"
        if self.Stress != 0:
            r_string += f"Stress: {self.Stress*days}\n"
        if self.gold != 0:
            r_string += f"Gold: {self.gold*days}\n"
        return r_string



jobs_data = [
    ("Housework", 0, 0, 0, 0, 0, 0, 0, 0, -2, 1, 0, 10),
    ("Babysitting", 0, 0, 0, 0, -1, 0, 0, 0, 1, 3, 4, 10),
    ("Church", 0, 0, 0, 0, 0, 1, 2, -2, 0, 1, 1, 10),
    ("Farm", 1, 1, 0, -1, 0, 0, 0, 0, 0, 3, 10, 10),
    ("Inn", 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 10),
    ("Restaurant", 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 10),
    ("Lumberjack", 0, 2, 0, -2, 0, 0, 0, 0, 0, 4, 12, 11),
    ("Salon", 0, -1, 0, 0, 0, 0, 0, 0, 1, 3, 20, 11),
    ("Masonry", 2, 0, 0, -1, 0, 0, 0, 0, 0, 3, 28, 12),
    ("Hunter", 1, 0, 0, -1, 0, 0, 0, 0, 0.5, 3, 8, 12),
    ("Graveyard", 0, 0, 0, 0, -1, 0, 0, 0, 1, 5, 8, 13),
    ("Bar", 0, 0, -2, 0, 0, 0, 0, 0, 0, 5, 12, 14),
    ("Tutor", 0, 0, 0, 0, -1, 1, 0, 0, 0, 7, 20, 14),
    ("Sleazy Bar", 0, 0, 0, 0, 2, -3, -3, 2, 0, 12, 45, 15),
    ("Cabaret", 0, 0, -1, -2, 3, 0, 0, 1, 0, 8, 35, 16)


]


Housework=Job(jobs_data[0][0], jobs_data[0][1], jobs_data[0][2], jobs_data[0][3], jobs_data[0][4], jobs_data[0][5], jobs_data[0][6], jobs_data[0][7], jobs_data[0][8], jobs_data[0][9], jobs_data[0][10], jobs_data[0][11], jobs_data[0][12])
Babysitting=Job(jobs_data[1][0], jobs_data[1][1], jobs_data[1][2], jobs_data[1][3], jobs_data[1][4], jobs_data[1][5], jobs_data[1][6], jobs_data[1][7], jobs_data[1][8], jobs_data[1][9], jobs_data[1][10], jobs_data[1][11], jobs_data[1][12])
Church=Job(jobs_data[2][0], jobs_data[2][1], jobs_data[2][2], jobs_data[2][3], jobs_data[2][4], jobs_data[2][5], jobs_data[2][6], jobs_data[2][7], jobs_data[2][8], jobs_data[2][9], jobs_data[2][10], jobs_data[2][11], jobs_data[2][12])
Farm=Job(jobs_data[3][0], jobs_data[3][1], jobs_data[3][2], jobs_data[3][3], jobs_data[3][4], jobs_data[3][5], jobs_data[3][6], jobs_data[3][7], jobs_data[3][8], jobs_data[3][9], jobs_data[3][10], jobs_data[3][11], jobs_data[3][12])
Inn=Job(jobs_data[4][0], jobs_data[4][1], jobs_data[4][2], jobs_data[4][3], jobs_data[4][4], jobs_data[4][5], jobs_data[4][6], jobs_data[4][7], jobs_data[4][8], jobs_data[4][9], jobs_data[4][10], jobs_data[4][11], jobs_data[4][12])
Restaurant=Job(jobs_data[5][0], jobs_data[5][1], jobs_data[5][2], jobs_data[5][3], jobs_data[5][4], jobs_data[5][5], jobs_data[5][6], jobs_data[5][7], jobs_data[5][8], jobs_data[5][9], jobs_data[5][10], jobs_data[5][11], jobs_data[5][12])
Lumberjack=Job(jobs_data[6][0], jobs_data[6][1], jobs_data[6][2], jobs_data[6][3], jobs_data[6][4], jobs_data[6][5], jobs_data[6][6], jobs_data[6][7], jobs_data[6][8], jobs_data[6][9], jobs_data[6][10], jobs_data[6][11], jobs_data[6][12])
Salon=Job(jobs_data[7][0], jobs_data[7][1], jobs_data[7][2], jobs_data[7][3], jobs_data[7][4], jobs_data[7][5], jobs_data[7][6], jobs_data[7][7], jobs_data[7][8], jobs_data[7][9], jobs_data[7][10], jobs_data[7][11], jobs_data[7][12])
Masonry=Job(jobs_data[8][0], jobs_data[8][1], jobs_data[8][2], jobs_data[8][3], jobs_data[8][4], jobs_data[8][5], jobs_data[8][6], jobs_data[8][7], jobs_data[8][8], jobs_data[8][9], jobs_data[8][10], jobs_data[8][11], jobs_data[8][12])
Hunter=Job(jobs_data[9][0], jobs_data[9][1], jobs_data[9][2], jobs_data[9][3], jobs_data[9][4], jobs_data[9][5], jobs_data[9][6], jobs_data[9][7], jobs_data[9][8], jobs_data[9][9], jobs_data[9][10], jobs_data[9][11], jobs_data[9][12])
Graveyard=Job(jobs_data[10][0], jobs_data[10][1], jobs_data[10][2], jobs_data[10][3], jobs_data[10][4], jobs_data[10][5], jobs_data[10][6], jobs_data[10][7], jobs_data[10][8], jobs_data[10][9], jobs_data[10][10], jobs_data[10][11], jobs_data[10][12])
Bar=Job(jobs_data[11][0], jobs_data[11][1], jobs_data[11][2], jobs_data[11][3], jobs_data[11][4], jobs_data[11][5], jobs_data[11][6], jobs_data[11][7], jobs_data[11][8], jobs_data[11][9], jobs_data[11][10], jobs_data[11][11], jobs_data[11][12])
Tutor=Job(jobs_data[12][0], jobs_data[12][1], jobs_data[12][2], jobs_data[12][3], jobs_data[12][4], jobs_data[12][5], jobs_data[12][6], jobs_data[12][7], jobs_data[12][8], jobs_data[12][9], jobs_data[12][10], jobs_data[12][11], jobs_data[12][12])
Sleazy_Bar=Job(jobs_data[13][0], jobs_data[13][1], jobs_data[13][2], jobs_data[13][3], jobs_data[13][4], jobs_data[13][5], jobs_data[13][6], jobs_data[13][7], jobs_data[13][8], jobs_data[13][9], jobs_data[13][10], jobs_data[13][11], jobs_data[13][12])
Cabaret=Job(jobs_data[14][0], jobs_data[14][1], jobs_data[14][2], jobs_data[14][3], jobs_data[14][4], jobs_data[14][5], jobs_data[14][6], jobs_data[14][7], jobs_data[14][8], jobs_data[14][9], jobs_data[14][10], jobs_data[14][11], jobs_data[14][12])

Jobs = [Housework, Babysitting, Church, Farm, Inn, Restaurant, Lumberjack, Salon, Masonry, Hunter, Graveyard, Bar, Tutor, Sleazy_Bar, Cabaret]



class Game:
    def __init__(self, name):
        self.name = name
        self.Constitution = 0
        self.Strength = 0
        self.Intelligence = 0
        self.Refinement = 0
        self.Charisma = 0
        self.Morality = 0
        self.Faith = 0
        self.Sin = 0
        self.Sensitivity = 0
        self.Stress = 0
        self.gold = 0
        self.age = 10

    def work(self, job, days):
        if self.age < job.min_age:
            print(f"Too young to work {job.name}")
            return
        stats_gained = job.return_work_week(days)
        self.Constitution += stats_gained[0]
        self.Strength += stats_gained[1]
        self.Intelligence += stats_gained[2]
        self.Refinement += stats_gained[3]
        self.Charisma += stats_gained[4]
        self.Morality += stats_gained[5]
        self.Faith += stats_gained[6]
        self.Sin += stats_gained[7]
        self.Sensitivity += stats_gained[8]
        self.Stress += stats_gained[9]
        self.gold += stats_gained[10]

    def __str__(self):
        r_string = f"\nGame: {self.name}\n"
        if self.Constitution != 0:
            r_string += f"Constitution: {self.Constitution}\n"
        if self.Strength != 0:
            r_string += f"Strength: {self.Strength}\n"
        if self.Intelligence != 0:
            r_string += f"Intelligence: {self.Intelligence}\n"
        if self.Refinement != 0:
            r_string += f"Refinement: {self.Refinement}\n"
        if self.Charisma != 0:
            r_string += f"Charisma: {self.Charisma}\n"
        if self.Morality != 0:
            r_string += f"Morality: {self.Morality}\n"
        if self.Faith != 0:
            r_string += f"Faith: {self.Faith}\n"
        if self.Sin != 0:
            r_string += f"Sin: {self.Sin}\n"
        if self.Sensitivity != 0:
            r_string += f"Sensitivity: {self.Sensitivity}\n"
        if self.Stress != 0:
            r_string += f"Stress: {self.Stress}\n"
        if self.gold != 0:
            r_string += f"Gold: {self.gold}\n"
        return r_string
    
    def grow_up(self):
        self.age += 1
    
    def get_money(self, amount):
        self.gold += amount
    

NG = Game('NG')
NG.work(Housework, 7)
NG.work(Cabaret, 7)

print(NG)