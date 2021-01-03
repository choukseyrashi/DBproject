# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:46:09 2020

@author: HP
"""

import csv
from faker import Faker
#import datetime
#import pytz
import  random

def datagenerate(records, headers):
    s1="General Offence"
    s2="Road Rules Violation"
    s3="Disobeying orders of Authorities"
    s4="Driving Without License"
    s5="Driving With Disqualified License"
    s6="Overspeeding"
    s7="Rash Driving"
    s8="Driving Under Influence of Alcohol or Intoxicating Substance"
    s9="Driving Oversized Vehicles without permission"
    s10="Driving When Mentally/Physically Unfit"
    s11="Accident Related Offences"
    s12="Driving Uninsured Vehicle (without valid Insurance)"
    s13="Vehicle Without Permit"
    s14="Overloading of Passengers"
    s15="Not Wearing Seatbelt"
    s16="Overloading of Two-Wheelers"
    s17="Not Wearing Helmet"
    s18="Not Providing Way for Emergency Vehicles"
    fake = Faker('en_US')
    #fake1 = Faker('en_GB')   # To generate phone numbers
    with open("Violation_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers, lineterminator='\n')
        writer.writeheader()
        for i in range(records):
            state = ["KA","MH","MP","GJ"]
            part2 =  random.randrange(11, 50, 1)
            seq = ["DB","BH","UN","RN"]
            rto = random.randrange(1001, 5000, 1) 
            vehNo = random.choice(state) + str(part2) + random.choice(seq) + str(rto)
            vtypes = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18]
            v=random.choice(vtypes)
            if(v==s1):
                fine=500
            elif(v==s2):
                fine=500
            elif(v==s3):
                fine=2000
            elif(v==s4):
                fine=5000
            elif(v==s5):
                fine=10000
            elif(v==s6):
                fine=2000
            elif(v==s7):
                fine=5000
            elif(v==s8):
                fine=10000
            elif(v==s9):
                fine=5000
            elif(v==s10):
                fine=1000
            elif(v==s11):
                fine=5000
            elif(v==s12):
                fine=2000
            elif(v==s13):
                fine=10000
            elif(v==s14):
                fine=4000
            elif(v==s15):
                fine=1000
            elif(v==s16):
                fine=2000
            elif(v==s17):
                fine=1000
            elif(v==s18):
                fine=10000
            
            loc = ["Sadar","Ramdaspeth","Gittikhadan Chowk" , "Bardi" , "Ganeshpeth" ,"Dharampeth" , "Dhantoli" ,"Itwari", "Chhaoni"]
            writer.writerow({
                    "Vehicle_Num_id" : vehNo,
                    "Owner_Name": fake.name(),
                    "Violation": v,
                    "Date" : fake.date_between(start_date='-1y', end_date='now'),
                    "Time": fake.time(),
                    "Location" : random.choice(loc),
                    "Penalty" : fine,
                    })
    
if __name__ == '__main__':
    records = 2000
    headers = ["Vehicle_Num_id", "Owner_Name", "Violation", "Date","Time", "Location",
               "Penalty"]
    datagenerate(records, headers)
    print("CSV generation complete!")