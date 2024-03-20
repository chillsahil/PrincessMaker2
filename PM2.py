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
    
    def return_job_week_str(self, days):
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

class Class:
    def __init__(self, name, Constitution, Strength, Intelligence, Refinement, Charisma, Morality, Faith, Sin, Sensitivity, Stress, gold):
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

        self.stats = [self.Constitution, self.Strength, self.Intelligence, 
                      self.Refinement, self.Charisma, self.Morality, 
                      self.Faith, self.Sin, self.Sensitivity, 
                      self.Stress, self.gold]
        
    def __str__(self):
        r_string = f"\nClass Name: {self.name}\n"
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


    def return_class_week(self, days):
        return [val * days for val in self.stats]
    
    def afford(self, days, wallet):
        cp = abs(self.gold) 
        if wallet//cp < days:
            return wallet//cp
        else:
            return days
        
    def return_class_week_str(self, days):
        r_string = f"\nClass Name: {self.name}\nDays Studied: {days}\n"
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


#region Jobs and Classes
Housework = Job("Housework", 0, 0, 0, 0, 0, 0, 0, 0, -2, 1, 0, 10)
Babysitting = Job( "Babysitting", 0, 0, 0, 0, -1, 0, 0, 0, 1, 3, 4, 10)
Church = Job("Church", 0, 0, 0, 0, 0, 1, 2, -2, 0, 1, 1, 10)
Farm = Job("Farm", 1, 1, 0, -1, 0, 0, 0, 0, 0, 3, 10, 10)
Inn = Job("Inn", 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 10)
Restaurant = Job("Restaurant", 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 10)
Lumberjack = Job("Lumberjack", 0, 2, 0, -2, 0, 0, 0, 0, 0, 4, 12, 11)
Salon = Job("Salon", 0, -1, 0, 0, 0, 0, 0, 0, 1, 3, 20, 11)
Masonry = Job("Masonry", 2, 0, 0, -1, 0, 0, 0, 0, 0, 3, 28, 12)
Hunter = Job("Hunter", 1, 0, 0, -1, 0, 0, 0, 0, 0.5, 3, 8, 12)
Graveyard = Job("Graveyard", 0, 0, 0, 0, -1, 0, 0, 0, 1, 5, 8, 13)
Bar = Job("Bar", 0, 0, -2, 0, 0, 0, 0, 0, 0, 5, 12, 14)
Tutor = Job("Tutor", 0, 0, 0, 0, -1, 1, 0, 0, 0, 7, 20, 14)
Sleazy_Bar = Job("Sleazy Bar", 0, 0, 0, 0, 2, -3, -3, 2, 0, 12, 45, 15)
Cabaret = Job("Cabaret", 0, 0, -1, -2, 3, 0, 0, 1, 0, 8, 35, 16)


Painting = Class("Painting", 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 1, -40)
Dance = Class("Dance", 1, 0, 0, 0, 0.5, 0, 0, 0, 0, 1, -50)
Fighting = Class("Fighting", 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -30)
Fencing = Class("Fencing", 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -40)
Magic = Class("Magic", 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -60)
Poetry = Class("Poetry", 0, 0, 1, 1, 0, 0, 0, 0, 1.5, 1, -40)
Protocol = Class("Protocol", 0, 0, 0, 1.5, 0, 0, 0, 0, 0, 1, -40)
Science = Class("Science", 0, 0, 3, 0, 0, 0, 2, 0, 0, 1, -30)
Strategy = Class("Strategy", 0, 0, 2, 0, 0, 0, 0, 0, -0.5, 1, -50)
Theology = Class("Theology", 0, 0, 1, 0, 0, 0, 1.5, 0, 0, 1, -40)
#endregion

Jobs = [
    Housework, 
    Babysitting, 
    Church, 
    Farm, 
    Inn, 
    Restaurant, 
    Lumberjack, 
    Salon, 
    Masonry, 
    Hunter, 
    Graveyard, 
    Bar, 
    Tutor, 
    Sleazy_Bar, 
    Cabaret
    ]

Classes = [
    Painting,
    Dance,
    Fighting,
    Fencing,
    Magic,
    Poetry,
    Protocol,
    Science,
    Strategy,
    Theology
    ]




class Game:
    def __init__(self, name):
        self.name = name
        self.Constitution = 45
        self.Strength = 45
        self.Intelligence = 13
        self.Refinement = 10
        self.Charisma = 7
        self.Morality = 14
        self.Faith = 21
        self.Sin = 0
        self.Sensitivity = 6
        self.Stress = 0
        self.gold = 500
        self.age = 10
        self.month = 12

        self.season = "SU" #dec-feb is winter, june-august is summer, september-nov is fall, march-may is spring

    def curr_season(self):
        if self.month == 12 or self.month == 1 or self.month == 2:
            self.season = "WI"
        elif self.month == 6 or self.month == 7 or self.month == 8:
            self.season = "SU"
        elif self.month == 9 or self.month == 10 or self.month == 11:
            self.season = "FA"
        else:
            self.season = "SP"
        
        return self.season

    def pass_month(self):
        if self.month == 12:
            self.month = 1
        else:
            self.month +=1
        self.Morality += 3
        self.Stress +=2
        self.curr_season()
        self.fix_stats()

        if self.Sin > self.Morality or self.Sin > self.Faith:
            print('WARNING: Daughter Risk of Delinquent')
        elif self.Stress > self.Constitution:
            print('WARNING: Daughter Risk of Sickness')
        elif self.Sensitivity == max(self.Constitution, self.Strength, self.Intelligence, self.Refinement, self.Charisma, self.Morality, self.Faith, self.Sin, self.Sensitivity, self.Stress):
            print('WARNING: Daughter Risk of Running away')




    def pocket_money(self):
        if self.age == 10:
            self.gold -= 20
            self.Stress =- 20
        else:
            money = (18 - self.age)*10 + 20
            self.gold -= money
            self.Stress -= 20
        self.fix_stats()

    def free_time(self, days, paid = False):
        if paid:
            self.Stress -= 10*days
            self.gold -= 10*days
        else: 
            self.Stress -= 5*days
        self.fix_stats()


    def work(self, job, days, output = False):
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

        if output == True:
            r_string = f"You worked {days} days.\nStats Gained:\n\n"

            if stats_gained[0] != 0:
                r_string += f"Constitution: {stats_gained[0]}\n"
            if stats_gained[1] != 0:
                r_string += f"Strength: {stats_gained[1]}\n"
            if stats_gained[2] != 0:
                r_string += f"Intelligence: {stats_gained[2]}\n"
            if stats_gained[3] != 0:
                r_string += f"Refinement: {stats_gained[3]}\n"
            if stats_gained[4] != 0:
                r_string += f"Charisma: {stats_gained[4]}\n"
            if stats_gained[5] != 0:
                r_string += f"Morality: {stats_gained[5]}\n"
            if stats_gained[6] != 0:
                r_string += f"Faith: {stats_gained[6]}\n"
            if stats_gained[7] != 0:
                r_string += f"Sin: {stats_gained[7]}\n"
            if stats_gained[8] != 0:
                r_string += f"Sensitivity: {stats_gained[8]}\n"
            if stats_gained[9] != 0:
                r_string += f"Stress: {stats_gained[9]}\n"
            if stats_gained[10] != 0:
                r_string += f"Gold: {stats_gained[10]}\n"
            r_string += '#############################'

            print(r_string)

        self.fix_stats()

    def take_class(self,class_taken, days, output = False):
        actual_days = class_taken.afford(days, self.gold)
        if actual_days != days:
            print(f"Out of money. {actual_days} out of {days} taken.")

        stats_gained = class_taken.return_class_week(actual_days)

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
        self.fix_stats()


    def __str__(self):
        self.fix_stats()
        r_string = f"\nGame: {self.name}\n"
        r_string += f'Current Month: {self.month}\n'
        r_string += f"Current Season: {self.season}\n\n"

        r_string += f"Constitution: {int(self.Constitution)}\n"
        r_string += f"Strength: {int(self.Strength)}\n"
        r_string += f"Intelligence: {int(self.Intelligence)}\n"
        r_string += f"Refinement: {int(self.Refinement)}\n"
        r_string += f"Charisma: {int(self.Charisma)}\n"
        r_string += f"Morality: {int(self.Morality)}\n"
        r_string += f"Faith: {int(self.Faith)}\n"
        r_string += f"Sin: {int(self.Sin)}\n"
        r_string += f"Sensitivity: {int(self.Sensitivity)}\n"
        r_string += f"Stress: {int(self.Stress)}\n"
        r_string += f"Gold: {int(self.gold)}\n"
        r_string += '#############################'
        
        return r_string

    
    def grow_up(self):
        self.age += 1
        self.fix_stats()

        
    def vacation(self, type, days):
        price = self.age * 10
        if self.gold < price:
            print("Not enough money for a vacation")
            return
        self.gold -= price
        v_string = f'Olive had a fun {type} vacation\n'
        if type == "sea":
            if self.season == "SU":
                self.Stress -= days*6
                v_string += f'Stress Reduced: -{days*6}\n'
            if self.season == "WI":
                self.Stress -= days*2
                v_string += f'Stress Reduced: -{days*2}\n'
            else:
                self.Stress -= days*3
                v_string += f'Stress Reduced: -{days*3}\n'


        if type == "mountain":
            if self.season == "FA":
                self.Stress -= days*6
                self.Sensitivity += 2*days
                v_string += f'Stress Reduced: -{days*6}\n'
                v_string += f'Sensitivity Gained: -{days*2}\n'
            else:
                self.Stress -= days*3
                self.Sensitivity += 1*days
                v_string += f'Stress Reduced: -{days*3}\n'
                v_string += f'Sensitivity Gained: -{days*1}\n'

        v_string += '#############################'

        self.fix_stats()

        print(v_string)


    def add_money(self, amount):
        self.gold += amount
        self.fix_stats()

    def fix_stats(self):
        self.curr_season()

        for attr, value in vars(self).items():
            if isinstance(value, int) and value < 0:
                setattr(self, attr, 0)



########################
                
def automate_game(inputfile):
    with open(inputfile, 'r') as file:
        for line in file:
            if "Name:" in line:
                title = "".join(line.split("Name:"))
                ng = Game(title)
                print('Starting Stats: \n')
                print(ng)
                break

        command_functions = {
            'work': lambda ng, command: ng.work(globals()[command[1]], int(command[2])),
            'class': lambda ng, command: ng.take_class(globals()[command[1]], int(command[2])),
            'display': lambda ng, command: print(ng),
            'passmonth': lambda ng, command: ng.pass_month(),
            'grow': lambda ng, command: ng.grow_up(),
            'vacation': lambda ng, command: ng.vacation(command[1], int(command[2])),
            'freetime': lambda ng, command: ng.free_time(int(command[1]), len(command) == 3), #checks if there is a paid indicator or not
            'pocket': lambda ng, command: ng.pocket_money(),
            'addmoney': lambda ng, command: ng.add_money(int(command[1])),
        }

        for line in file:
            command = line.split()
            if '#' in line:
                pass
            elif command[0] in command_functions:
                command_functions[command[0]](ng, command)
                

automate_game("commandfile.txt")

