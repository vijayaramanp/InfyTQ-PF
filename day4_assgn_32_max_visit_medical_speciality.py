#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    max_visit=0
    P=patient_medical_speciality_list.count('P')
    E=patient_medical_speciality_list.count('E')
    O=patient_medical_speciality_list.count('O')
    
    if P>E and P>O:
        speciality= medical_speciality['P']
    elif E>O:
        speciality= medical_speciality['E']
    else:
        speciality= medical_speciality['O']
    
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'O',302, 'O' ,305, 'O' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
