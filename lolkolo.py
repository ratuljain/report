__author__ = 'rjain1'
import json

medicines = """{

  "prescription_id" : 0,
  "Date" : "30/12/2015",
  "Patient_Name": "Random Patient",
  "Doctor_Name": "Random Doctor",

  "Diagnosis" : "",

  "Medicines" : {
    "Name1" : {
    "Morning" : {"Take" : true ,"With_Food" : true, "time" : "", "Quantity" : 1},
    "Afternoon" : {"Take" : false ,"With_Food" : true, "time" : "", "Quantity" : 1},
    "Evening" : {"Take" : false ,"With_Food" : true, "time" : "","Quantity" : 1},
    "Night" : {"Take" : true ,"With_Food" : true, "time" : "", "Quantity" : 1},
    "Total_Quantity" : 10
    },

    "Name2" : {
    "Morning" : {"Take" : true ,"With_Food" : true, "time" : "", "Quantity" : 1},
    "Afternoon" : {"Take" : false ,"With_Food" : true, "time" : "", "Quantity" : 1},
    "Evening" : {"Take" : false ,"With_Food" : true, "time" : "", "Quantity" : 1},
    "Night" : {"Take" : true ,"With_Food" : true, "time" : "", "Quantity" : 1},
    "Total_Quantity" : 10
    },

    "Name3" : {
    "Morning" : {"Take" : true ,"With_Food" : true, "time" : "", "Quantity" : 1},
    "Afternoon" : {"Take" : false ,"With_Food" : true, "time" : "", "Quantity" : 1},
    "Evening" : {"Take" : false ,"With_Food" : true, "time" : "", "Quantity" : 1},
    "Night" : {"Take" : true ,"With_Food" : true, "time" : "", "Quantity" : 1},
    "Total_Quantity" : 10
    }
  },

  "Signature" : ""
}"""

data = json.loads(medicines)
medicinesdic = data["Medicines"]

list_of_medicine = []
list_of_medicine = medicinesdic.items()
s = list_of_medicine[0]
print s


def retreiveTake(s):
    n = s[0]
    s = s[1]
    for i in s:
        if i == "Total_Quantity":
            continue
        if s[i]['Take'] == True:
            print n, s[i]


for s in list_of_medicine:
    retreiveTake(s)

# def retreiveTake(tup):
#     name = tup[0]
#     phase = tup[1]
#     print name
#     # for i in phase:
#     #     print i,phase[i]
# retreiveTake(list_of_medicine[0])
#
