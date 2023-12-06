
"""
Python Script for COMP3008 A2, P2, (a), (b)
Computes descriptive statistics, plots distribution graphs
Dec 5, 23
"""
import matplotlib.pyplot as plt 
import numpy as np
from scipy import stats
import csv 
  
participantGroupPM = [] 
participantGroupPW = [] 
csvLines = 0
  
with open('comp3008_assn2_data.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
      
    for row in plots: 
        if(csvLines != 0):
            if(row[1] == 'pm'):
                participantGroupPM.append(row)
            else:
                participantGroupPW.append(row)
        else:
            print(row)
        csvLines += 1
            

# funcs
def retStrArrOfArrWNewline(thisArray):
    return ('\n'.join(str(x) for x in thisArray))

# to make arr for each dep var
def makeArrOutOfThisIndex(rowArray, index):
    indexArr = []
    for row in rowArray:
        indexArr.append(float(row[index]))

    return indexArr


pmSuccesses = makeArrOutOfThisIndex(participantGroupPM, 2)
pmFailures = makeArrOutOfThisIndex(participantGroupPM, 3)
pmResets = makeArrOutOfThisIndex(participantGroupPM, 4)
pmSloginTime = makeArrOutOfThisIndex(participantGroupPM, 5)
pmMaxMemTime = makeArrOutOfThisIndex(participantGroupPM, 6)
pmTotalLastingSuccess = makeArrOutOfThisIndex(participantGroupPM, 7)
pmAvgLeadingFailures = makeArrOutOfThisIndex(participantGroupPM, 8) 

pwSuccesses = makeArrOutOfThisIndex(participantGroupPW, 2)
pwFailures = makeArrOutOfThisIndex(participantGroupPW, 3)
pwResets = makeArrOutOfThisIndex(participantGroupPW, 4)
pwSloginTime = makeArrOutOfThisIndex(participantGroupPW, 5)
pwMaxMemTime = makeArrOutOfThisIndex(participantGroupPW, 6)
pwTotalLastingSuccess = makeArrOutOfThisIndex(participantGroupPW, 7)
pwAvgLeadingFailures = makeArrOutOfThisIndex(participantGroupPW, 8) 

#pm success mean, median, mode, SD
#(type(pmSuccesses[0]))
#pmSuccessMean = np.mean(pmSuccesses)

print("BASIC DESC STATS: " + '\n')

#successes
print("PM vs PW group Successes -----------" + '\n')
print("PM Successes Mean: " + str(np.mean(pmSuccesses)))
print("PM Successes Median: " + str(np.median(pmSuccesses)))
print("PM Successes Mode: " + str(stats.mode(pmSuccesses)))
print("PM Successes SD: " + str(np.std(pmSuccesses, ddof=1)))
print('\n')
print("PW Successes Mean: " + str(np.mean(pwSuccesses)))
print("PW Successes Median: " + str(np.median(pwSuccesses)))
print("PW Successes Mode: " + str(stats.mode(pwSuccesses)))
print("PW Successes SD: " + str(np.std(pwSuccesses, ddof=1)))
print("------------------------------------" + '\n')


#failures 
print("PM vs PW group Failures -----------" + '\n')
print("PM Failures Mean: " + str(np.mean(pmFailures)))
print("PM Failures Median: " + str(np.median(pmFailures)))
print("PM Failures Mode: " + str(stats.mode(pmFailures)))
print("PM Failures SD: " + str(np.std(pmFailures, ddof=1)))
print('\n')
print("PW Failures Mean: " + str(np.mean(pwFailures)))
print("PW Failures Median: " + str(np.median(pwFailures)))
print("PW Failures Mode: " + str(stats.mode(pwFailures)))
print("PW Failures SD: " + str(np.std(pwFailures, ddof=1)))
print("------------------------------------" + '\n')

#resets
print("PM vs PW group Resets -----------" + '\n')
print("PM Resets Mean: " + str(np.mean(pmResets)))
print("PM Resets Median: " + str(np.median(pmResets)))
print("PM Resets Mode: " + str(stats.mode(pmResets)))
print("PM Resets SD: " + str(np.std(pmResets, ddof=1)))
print('\n')
print("PW Resets Mean: " + str(np.mean(pwResets)))
print("PW Resets Median: " + str(np.median(pwResets)))
print("PW Resets Mode: " + str(stats.mode(pwResets)))
print("PW Resets SD: " + str(np.std(pwResets, ddof=1)))
print("------------------------------------" + '\n')

#successful log in time avg
print("PM vs PW group successful log in time avg -----------" + '\n')
print("PM Slogintime Mean: " + str(np.mean(pmSloginTime)))
print("PM Slogintime Median: " + str(np.median(pmSloginTime)))
print("PM Slogintime Mode: " + str(stats.mode(pmSloginTime)))
print("PM Slogintime SD: " + str(np.std(pmSloginTime, ddof=1)))
print('\n')
print("PW Slogintime Mean: " + str(np.mean(pwSloginTime)))
print("PW Slogintime Median: " + str(np.median(pwSloginTime)))
print("PW Slogintime Mode: " + str(stats.mode(pwSloginTime)))
print("PW Slogintime SD: " + str(np.std(pwSloginTime, ddof=1)))
print("------------------------------------" + '\n')

#max memory time
print("PM vs PW group max time btw pwd creation and successful recall -----------" + '\n')
print("PM Maxmemtime Mean: " + str(np.mean(pmMaxMemTime)))
print("PM Maxmemtime Median: " + str(np.median(pmMaxMemTime)))
print("PM Maxmemtime Mode: " + str(stats.mode(pmMaxMemTime)))
print("PM Maxmemtime SD: " + str(np.std(pmMaxMemTime, ddof=1)))
print('\n')
print("PW Maxmemtime Mean: " + str(np.mean(pwMaxMemTime)))
print("PW Maxmemtime Median: " + str(np.median(pwMaxMemTime)))
print("PW Maxmemtime Mode: " + str(stats.mode(pwMaxMemTime)))
print("PW Maxmemtime SD: " + str(np.std(pwMaxMemTime, ddof=1)))
print("------------------------------------" + '\n')

#lasting success binary
print("PM vs PW group use of the same pwd throughout whole study -----------" + '\n')
print("PM totalLastingSucccess Mean: " + str(np.mean(pmTotalLastingSuccess)))
print("PM totalLastingSucccess Median: " + str(np.median(pmTotalLastingSuccess)))
print("PM totalLastingSucccess Mode: " + str(stats.mode(pmTotalLastingSuccess)))
print("PM totalLastingSucccess SD: " + str(np.std(pmTotalLastingSuccess, ddof=1)))
print('\n')
print("PW totalLastingSucccess Mean: " + str(np.mean(pwTotalLastingSuccess)))
print("PW totalLastingSucccess Median: " + str(np.median(pwTotalLastingSuccess)))
print("PW totalLastingSucccess Mode: " + str(stats.mode(pwTotalLastingSuccess)))
print("PW totalLastingSucccess SD: " + str(np.std(pwTotalLastingSuccess, ddof=1)))
print("------------------------------------" + '\n')

#avg number of unsuccessful log in attempts before successful log in attempts
print("PM vs PW group avg number of unsuccessful log in attempts before successful log in attempts -----------" + '\n')
print("PM avgLeadingFailure Mean: " + str(np.mean(pmAvgLeadingFailures)))
print("PM avgLeadingFailure Median: " + str(np.median(pmAvgLeadingFailures)))
print("PM avgLeadingFailure Mode: " + str(stats.mode(pmAvgLeadingFailures)))
print("PM avgLeadingFailure SD: " + str(np.std(pmAvgLeadingFailures, ddof=1)))
print('\n')
print("PW avgLeadingFailure Mean: " + str(np.mean(pwAvgLeadingFailures)))
print("PW avgLeadingFailure Median: " + str(np.median(pwAvgLeadingFailures)))
print("PW avgLeadingFailure Mode: " + str(stats.mode(pwAvgLeadingFailures)))
print("PW avgLeadingFailure SD: " + str(np.std(pwAvgLeadingFailures, ddof=1)))
print("------------------------------------" + '\n')

#scatter plots and histograms
f1 = plt.figure(1,figsize=(10, 7))
f1TicksArr = [0.33, 1, 1.6666666667]
f1TicksLabelsArr = ['0 Successful Logins', '1 Successful Login', '2 Successful Logins']
plt.xticks(f1TicksArr, f1TicksLabelsArr)
plt.hist(pmSuccesses, bins=3)
plt.ylabel('Number of Participants')
plt.xlabel('Bins corresponding to Number of Successful Logins')
plt.title('Password Memorized Group: Dist.of Number of Successful Logins over the Study Duration')

f2 = plt.figure(2, figsize=(10, 7))
f2TicksArr = [1.33, 2 , 2.666]
f2TicksLabelsArr = ['1 Successful Login', '2 Successful Logins', '3 Successful Logins']
plt.xticks(f2TicksArr, f2TicksLabelsArr)
plt.hist(pwSuccesses, bins=3)
plt.ylabel('Number of Participants')
plt.xlabel('Bins corresponding to Number of Successful Logins')
plt.title('Password Written Group: Dist.of Number of Successful Logins over the Study Duration')


f3 = plt.figure(3,figsize=(10, 7))
f3TicksArr = [(0.75/2), 1+(0.75/2), 2+(0.75/2), 3+(0.75/2)]
f3TicksLabelsArr = ['0 Failed Logins', '1 Failed Login', '2 Failed Logins', '3 Failed Logins']
plt.xticks(f3TicksArr, f3TicksLabelsArr)
plt.hist(pmFailures, bins=4)
plt.ylabel('Number of Participants')
plt.xlabel('Bins corresponding to Number of Failed Logins')
plt.title('Password Memorized Group: Dist.of Number of Failed Logins over the Study Duration')

f4 = plt.figure(4,figsize=(10, 7))
f4TicksArr = [0.456, 1.369, 3.232, 11.476]
f4TicksLabelsArr = ['0 '+ '\n' +'Failed' + '\n' + 'Logins', '1 '+ '\n' +'Failed'+ '\n' +'Login', '3 Failed Logins', '12 Failed Logins']
plt.xticks(f4TicksArr, f4TicksLabelsArr)
plt.hist(pwFailures, bins=13)
plt.ylabel('Number of Participants')
plt.xlabel('Bins corresponding to Number of Failed Logins')
plt.title('Password Written Group: Dist.of Number of Failed Logins over the Study Duration')


f5 = plt.figure(5,figsize=(10, 7))
f5TicksArr = [0.33, 1, 1.6666666667]
f5TicksLabelsArr = ['0 Password Resets', '1 Password Reset', '2 Password Resets']
plt.xticks(f5TicksArr, f5TicksLabelsArr)
plt.hist(pmResets, bins=3)
plt.ylabel('Number of Participants')
plt.xlabel('Bins corresponding to Number of Password Resets')
plt.title('Password Memorized Group: Dist.of Number of Password Resets over the Study Duration')

f6 = plt.figure(6,figsize=(10, 7))
f6TicksArr = [0.2417, 0.7505]
f6TicksLabelsArr = ['0 Password Resets', '1 Password Reset']
plt.xticks(f6TicksArr, f6TicksLabelsArr)
plt.hist(pwResets, bins=2)
plt.ylabel('Number of Participants')
plt.xlabel('Bins corresponding to Number of Password Resets')
plt.title('Password Written Group: Dist.of Number of Password Resets over the Study Duration')


f7 = plt.figure(7,figsize=(10, 7))
plt.hist(pmSloginTime, bins = 8)
plt.ylabel('Number of Participants')
plt.xlabel('Average Time to Login Sucessfully - (seconds)')
plt.title('Password Memorized Group: Dist.of Average Time to Login Sucessfully')

f8 = plt.figure(8,figsize=(10, 7))
plt.hist(pwSloginTime)
plt.ylabel('Number of Participants')
plt.xlabel('Average Time to Login Sucessfully - (seconds)')
plt.title('Password Written Group: Dist.of Average Time to Login Sucessfully')

f9 = plt.figure(9,figsize=(10, 7))
plt.hist(pmMaxMemTime)
plt.ylabel('Number of Participants')
plt.xlabel('Longest Duration between Successful Password Creation and Entry - (seconds)')
plt.title('Password Memorized Group: Dist.of Longest Duration between Successful Password Creation and Entry')


f10 = plt.figure(10,figsize=(10, 7))
plt.hist(pwMaxMemTime)
plt.ylabel('Number of Participants')
plt.xlabel('Longest Duration between Successful Password Creation and Entry - (seconds)')
plt.title('Password Written Group: Dist.of Longest Duration between Successful Password Creation and Entry')

f11 = plt.figure(11,figsize=(10, 7))
f11TicksArr = [0.2417, 0.7505]
f11TicksLabelsArr = ['Not Successful', 'Successful']
plt.xticks(f11TicksArr, f11TicksLabelsArr)
plt.hist(pmTotalLastingSuccess, bins=2)
plt.ylabel('Number of Participants')
plt.xlabel('Was Able to Use Same Password for Entirety of Study?')
plt.title('Password Memorized Group: Dist.of Whether Participant was Able to Use Same Password for Duration of Study')

f12 = plt.figure(12,figsize=(10, 7))
f12TicksArr = [0.2417, 0.7505]
f12TicksLabelsArr = ['Not Successful', 'Successful']
plt.xticks(f12TicksArr, f12TicksLabelsArr)
plt.hist(pwTotalLastingSuccess, bins=2)
plt.ylabel('Number of Participants')
plt.xlabel('Was Able to Use Same Password for Entirety of Study?')
plt.title('Password Written Group: Dist.of Whether Participant was Able to Use Same Password for Duration of Study')


f13 = plt.figure(13,figsize=(10, 7))
f13TicksArr = [0.25, 0.75, 1.25, 1.75]
f13TicksLabelsArr = ['0.5 Failed Attempts', '1 Failed Attempts', '1.5 Failed Attempts', '2 Failed Attempts']
plt.xticks(f13TicksArr, f13TicksLabelsArr)
plt.hist(pmAvgLeadingFailures, bins = 4)
plt.ylabel('Number of Participants')
plt.xlabel('Average Number of Failed Password Attempts before Successful Login')
plt.title('Password Memorized Group: Dist.of Average Number of Failed Attempts before Successfully Logging In')

f14 = plt.figure(14,figsize=(10, 7))
plt.hist(pwAvgLeadingFailures)
plt.ylabel('Number of Participants')
plt.xlabel('Average Number of Failed Password Attempts before Successful Login')
plt.title('Password Written Group: Dist.of Average Number of Failed Attempts before Successfully Logging In')


plt.show()