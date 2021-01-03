# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 17:46:06 2020

@author: HP
"""
from tkinter import *
from pymongo import MongoClient
#import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime

client = MongoClient('localhost', 27017)
root = Tk()
root.title('Traffic Rule Management System')
root.geometry("800x800")

def violDetail():
    
    show=""
    vehno = vnumber.get()
    with client:
        db = client.TrafficRuleViolation
        for v in db.Violation.find({"VehicleNo":vehno}).sort("Date"):
            show=show+str(v['VehicleNo']+", "+v['Owner_Name']+", "+v['Violation']+
                    ", "+v['Date'].strftime("%m/%d/%Y")+", "+v['Time']+", "+v['Location']+", "+str(v['Penalty'])+" \n")
        global showLabel    
        showLabel = Label(root, text=show)
        showLabel.grid(row=9,column=0,columnspan=2,pady=10,padx=10)
        
        client.close()
    vnumber.delete(0,END)
    
def locViol():
    location = locat.get()
    violate=""
    with client:
        db=client.TrafficRuleViolation
        
        agg_result = db.Violation.aggregate(
                                            [
                                             {
                                              "$match":{"Location":location}
                                              },
                                              {
                                              "$group": {
                                                       "_id": "$Violation",
                                                       "count":{"$sum": 1},
                                                       }
                                            },
                                            {
                                            "$sort":{"count":-1}
                                             }])
        for i in agg_result:
            violate=i['_id']
            break
        client.close()
        global vLabel
        vLabel = Label(root, text=violate)
        vLabel.grid(row=12,column=0,columnspan=2,pady=10,padx=10)
        locat.delete(0,END)
            
def locGraph():
    with client:
        db = client.TrafficRuleViolation
        agg = db.Violation.aggregate(
                                     [
                                          {
                                          "$group": {
                                                   "_id": "$Location",
                                                   "count":{"$sum": 1},
                                                   }
                                        }])
        loct=[]
        cnt=[]
        for l in agg:
            loct.append(l['_id'])
            cnt.append(l['count'])
        fig = plt.figure(figsize = (10, 5)) 
  
        # creating the bar plot 
        plt.bar(loct, cnt, color ='maroon',  
                width = 0.4) 
          
        plt.xlabel("Location") 
        plt.ylabel("No. of violations") 
        plt.title("Areawise Violations") 
        plt.show()
        client.close()
        

def insert():
    vno = vnum.get()
    violation = rule.get()
    name =  oname.get()
    location = loc.get()
    print(type(vno))
    print(type(violation))
    print(type(name))
    print(type(location))
    
    
    with client:
        db = client.TrafficRuleViolation
        freq = db.Fine.find({'Violation_type': violation}).count()
        print(" {} rows for this violation".format(freq))
        
        if(freq == 1):
            fine_row = db.Fine.find_one({'Violation_type': violation})
            fine = fine_row['Fine']
            print(" {} is the fine".format(fine))
        
        elif(freq == 2):
            num = db.Violation.find({'VehicleNo':vno, 'Violation':violation}).count()
            print(" {} is num".format(num))
            if(num == 0):
                fine_row = db.Fine.find_one({'Violation_type':violation , 'Frequency':1})
            else:
                fine_row = db.Fine.find_one({'Violation_type':violation , 'Frequency':2})
            fine = fine_row['Fine']
            print(" {} is the fine".format(fine))
            
        doc={'VehicleNo':vno, 
             'Owner_Name':name,
             'Violation':violation,
             'Date':datetime.now(),
             'Time':datetime.now().strftime("%H:%M:%S"),
             'Location':location,
             'Penalty':fine}
             
        violcol = db.Violation
        in_id = violcol.insert_one(doc).inserted_id
        print(in_id)
        ins = db.Violation.find_one({'_id':in_id})
        inserted=str(ins['VehicleNo']+", "+ins['Owner_Name']+", "+ins['Violation']+
                    ", "+ins['Date'].strftime("%m/%d/%Y")+", "+ins['Time']+", "+ins['Location']+", "+str(ins['Penalty']))
        print(inserted)
        myLabel = Label(root,text="Inserted record:")
        myLabel.grid(row=5,column=0,columnspan=2,pady=10,padx=10)
        insertLabel = Label(root, text=inserted)
        insertLabel.grid(row=6,column=0,columnspan=2,pady=10,padx=10)
        
        client.close()
    
    vnum.delete(0,END)
    oname.delete(0,END)
    rule.delete(0,END)
    loc.delete(0,END)
    
vnum = Entry(root,width=30)
vnum.grid(row=0,column=1,padx=20)
oname = Entry(root,width=30)
oname.grid(row=1,column=1)
rule = Entry(root,width=30)
rule.grid(row=2,column=1)
loc = Entry(root,width=30)
loc.grid(row=3,column=1)

vnum_label = Label(root,text="Vehicle Number")
vnum_label.grid(row=0,column=0)
oname_label = Label(root,text="Owner Name")
oname_label.grid(row=1,column=0)
rule_label = Label(root,text="Rule Violated")
rule_label.grid(row=2,column=0)
loc_label = Label(root,text="Location")
loc_label.grid(row=3,column=0)

insertButton = Button(root,text="Add Record to the database", command=insert)
insertButton.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

vnolabel = Label(root,text="Vehicle Number")
vnolabel.grid(row=7,column=0)
vnumber = Entry(root,width=30)
vnumber.grid(row=7,column=1,padx=20)
vButton = Button(root,text="Get the details of violations by this vehicle no.", command=violDetail)
vButton.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=100)


loclabel = Label(root,text="Location")
loclabel.grid(row=10,column=0)
locat = Entry(root,width=30)
locat.grid(row=10,column=1,padx=20)
locButton = Button(root,text="Get the most violated rule in this location", command=locViol)
locButton.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

graphButton = Button(root,text="Click Here to get the graph for areawise violations",command=locGraph)
graphButton.grid(row=13,column=0,columnspan=2,pady=10,padx=10,ipadx=100)



root.mainloop()

# KA23UN1043 , Audrey Frost , General Offence
#KA46RN1537, Brian Bryan , Overspeeding