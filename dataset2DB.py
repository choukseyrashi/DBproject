# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:47:44 2020

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:46:09 2020

@author: HP
"""

import csv


def datagenerate( headers):
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
    with open("Fine_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers, lineterminator='\n')
        writer.writeheader()
        writer.writerow({
                "Violation": s1,
                "Fine" : 500,
                "Frequency" : 1
                })
        writer.writerow({
                "Violation": s1,
                "Fine" : 1500,
                "Frequency" : 2
                })
        writer.writerow({
                "Violation": s2,
                "Fine" : 500,
                "Frequency" : None
                })
        writer.writerow({
                "Violation": s3,
                "Fine" : 2000,
                "Frequency" : None
                })
        writer.writerow({
                "Violation": s4,
                "Fine" : 5000,
                "Frequency" : None
                })
        writer.writerow({
                "Violation": s5,
                "Fine" : 10000,
                "Frequency" : None
                })
        writer.writerow({
                "Violation": s6,
                "Fine" : 2000,
                "Frequency" : None
                })
        writer.writerow({
                "Violation": s7,
                "Fine" : 5000,
                "Frequency" : 1
                })
        writer.writerow({
                "Violation": s7,
                "Fine" : 10000,
                "Frequency" : 2
                })
        writer.writerow({
                "Violation": s8,
                "Fine" : 10000,
                "Frequency" : 1
                })
        writer.writerow({
                "Violation": s8,
                "Fine" : 15000,
                "Frequency" : 2
                })
        writer.writerow({
                "Violation": s9,
                "Fine" : 5000,
                "Frequency" : None
                })
        writer.writerow({
                "Violation": s10,
                "Fine" : 1000,
                "Frequency" : 1
                })
        writer.writerow({
                "Violation": s10,
                "Fine" : 2000,
                "Frequency" : 2
                })
        writer.writerow({
                "Violation": s11,
                "Fine" : 5000,
                "Frequency" : 1
                })
        writer.writerow({
                "Violation": s11,
                "Fine" : 10000,
                "Frequency" : 2
                })
        writer.writerow({
                "Violation": s12,
                "Fine" : 2000,
                "Frequency" : 1
                })
        writer.writerow({
                "Violation": s12,
                "Fine" : 4000,
                "Frequency" : 2
                })
        writer.writerow({
                "Violation": s13,
                "Fine" : 10000,
                "Frequency" : None
                })
        writer.writerow({
                "Violation": s14,
                "Fine" : 1000,
                "Frequency" : None
                })
        writer.writerow({
                "Violation": s15,
                "Fine" : 1000,
                "Frequency" : None
                })
        writer.writerow({
                "Violation": s16,
                "Fine" : 2000,
                "Frequency" : None
                })
        writer.writerow({
                "Violation": s17,
                "Fine" : 1000,
                "Frequency" : None
                })
        writer.writerow({
                "Violation": s18,
                "Fine" : 10000,
                "Frequency" : None
                })
        
    
if __name__ == '__main__':
    #records = 200
    headers = ["Violation", "Fine","Frequency"]
    datagenerate( headers)
    print("CSV generation complete!")