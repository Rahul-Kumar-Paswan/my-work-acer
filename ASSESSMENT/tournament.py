import random

class Tournament:

    team1_total_score=0
    team2_total_score=0

    def __init__(self,team1,team2,team1_dic,team2_dic,n) -> None:
        self.team1=team1
        self.team2=team2
        self.team1_dic=team1_dic
        self.team2_dic=team2_dic
        self.n=n
        # print(team1)
        # print(team2)
        # print(team1_dic)
        # print(team2_dic)

    def bat(self,team,team_score,batters,bowlers,n):
        total_score = 0
        self.team = team
        self.batters = batters
        self.bowlers = bowlers
        self.team_score = team_score
        self.n=n
        # print("bating")
        z=n
        members=0
        bow_ind=0
        strike = 0
        # print(self.team)
        wickets={}
        while n>0 and members <11 and bow_ind<6:
            print()
            if members >=10 :
                break
            if z!=n :
                self.bowlers.append(temp_rem)
            temp_rem=self.bowlers[bow_ind]
            print("over :",n,"   ",self.team[members]," and  ",self.team[members+1]," is batting")
            print("over :",n,"   ",self.bowlers[bow_ind]," is bowling")
            # str=self.bowlers[bow_ind]
            # wickets[str]=0
            if self.bowlers[bow_ind] not in wickets :
                wickets.update({self.bowlers[bow_ind]:0})
            for ball in range(0,6):
                r=random.randrange(0,7)
                if r == 5:
                    print("OH NO ! ",self.team[members]," is out on ",ball+1," ball")
                    wickets[self.bowlers[bow_ind]] = wickets[self.bowlers[bow_ind]]+1
                    # print(wickets[self.bowlers[bow_ind]])
                    members+=1
                    print(self.team[members]," is batting")
                elif r==0 or r==2 or r== 4 or r==6 :
                    print(self.team[members],"is on the Strike on ",ball+1,"  ball :"," and run is :",r)
                    total_score+=r
                    self.team_score[self.team[members]]=self.team_score[self.team[members]]+r
                else:
                    print(self.team[members],"is on the Strike on ",ball+1," ball :"," and run is :",r)
                    total_score+=r
                    self.team_score[self.team[members]]=self.team_score[self.team[members]]+r
                    if strike == 0 :
                        strike=1
                        members+=1
                    else:
                        strike=0
                        members-=1
            bow_ind+=1
            n-=1
            self.bowlers.remove(temp_rem)
            bow_ind=0

        
        print("______________________________")
        print(f" PLAYER_NAME \t SCORE_OF_EACH_PLAYER ")
        print("______________________________")
        for x, y in self.team_score.items():
            print(f"| {x} \t\t {y} ")

        print("________________________________")
        print("      TOTAL SCORE : ",total_score)
        print("________________________________")


        print("______________________________")
        print(f" PLAYER_NAME \t WICKETS_OF_EACH_PLAYER ")
        print("______________________________")
        for x, y in wickets.items():
            print(f"| {x} \t\t {y} ")

        print("________________________________")

        
        return total_score
   


    def toss(self):
        cap1=self.team1[0]
        cap2=self.team2[0]
        print(cap1)
        print(cap2)
        toss_call=input("enter head or tail :")
        r=random.randrange(0, 2)
        print(r)
        bowlers_team1=[]
        batters_team1=[]
        for i in range(len(self.team1)):
            if i>5:
                bowlers_team1.append(self.team1[i])
            else:
                batters_team1.append(self.team1[i])
        
        bowlers_team2=[]
        batters_team2=[]
        for i in range(len(self.team2)):
            if i>5:
                bowlers_team2.append(self.team2[i])
            else:
                batters_team2.append(self.team2[i])
            
        # print(bowlers_team1)
        # print(bowlers_team2)

        if r==0:
            print(cap1+" won the toss ")
            print("choose wherther you want to bat/bowl first ")
            print("enter 0 to bowl or 1 to bat :",end='')
            option=int(input())
            print(option)
            if option==0:
                print(cap1+" chooses bowling ")
                a1=self.bat(self.team2,self.team2_dic,batters_team2,bowlers_team1)
                a2=self.bat(self.team1,self.team1_dic,batters_team1,bowlers_team2)
                if a1>a2:
                    print("Team1 is Winner")
                    return
                else:
                    print("Team2 is Winner")
                    return

            else:
                print(cap1+" chooses batting ")
                a1=self.bat(self.team1,self.team1_dic,batters_team1,bowlers_team2,n)
                a2=self.bat(self.team2,self.team2_dic,batters_team2,bowlers_team1,n)
                if a1>a2:
                    print(" ---- Team1 is Winner ---- ")
                    return
                else:
                    print(" ---- Team2 is Winner ---- ")
                    return
            
        else:
            print(cap2+" won the toss ")
            print("choose wherther you want to bat/bowl first ")
            print("enter 0 to bowl or 1 to bat :",end='')
            option=int(input())
            print(option)
            if option==0:
                print(cap1+" chooses bowling ")
                a2=self.bat(self.team2,self.team2_dic,batters_team2,bowlers_team1,n)
                a1=self.bat(self.team1,self.team1_dic,batters_team1,bowlers_team2,n)
                if a1>a2:
                    print(" ---- Team1 is Winner ----")
                    return
                else:
                    print(" ---- Team2 is Winner ----")
                    return

            else:
                print(cap2+" chooses batting ")
                a2=self.bat(self.team2,self.team2_dic,batters_team2,bowlers_team1,n)
                a1=self.bat(self.team1,self.team1_dic,batters_team1,bowlers_team2,n)
                if a1>a2:
                    print(" ---- Team1 is Winner ----")
                    return
                else:
                    print(" ---- Team2 is Winner ----")
                    return


team1=['rahul','raj','rakesh','sriram','saicharan','obul','manoj','sumer','sumanth','sai','jayanth']
team2=['aashish','junaid','pavan','madhukar','prasad','harsha','abhinav','abhishek','vinay','hemanth','rushi']

team1_dic={'rahul':0,'raj':0,'rakesh':0,'sriram':0,'saicharan':0,'obul':0,'manoj':0,'sumer':0,'sumanth':0,'sai':0,'jayanth':0}
team2_dic={'aashish':0,'junaid':0,'pavan':0,'madhukar':0,'prasad':0,'harsha':0,'abhinav':0,'abhishek':0,'vinay':0,'hemanth':0,'rushi':0}

n=int(input("Enter number of overs lessthan 5 :"))
cricket = Tournament(team1,team2,team1_dic,team2_dic,n)
print("---------- TOSS -----------")
cricket.toss()