# Stimiamo i costi dell'assicurazione medica per due persone, Giovanna e Gabriel, sulla base di cinque variabili:
# age: età dell'individuo in anni
# sex: 0 per la femmina, 1 per il maschio
# bmi: indice di massa corporea dell'individuo
# num_of_children: numero di figli che l'individuo ha
# smoker: 0 per non fumatore, 1 per fumatore


def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost is " + str(estimated_cost) + " dollars.")
  return estimated_cost

Giovanna_insurance_cost = calculate_insurance_cost(age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)
Gabriel_insurance_cost = calculate_insurance_cost(age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)


# Aggiungiamo il nome nel messaggio. Procediamo inserendo una nuovo parametro nella nostra funzione di calcolo.
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
  return estimated_cost


Giovanna_insurance_cost = calculate_insurance_cost(name = "Giovanna", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)
Gabriel_insurance_cost = calculate_insurance_cost(name = "Gabriel", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)


# Message for smoker 
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")
 
# Message for bmi value
def analyze_bmi(bmi_value):
  if bmi_value > 30:
    print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI")
  elif bmi_value >= 25 and bmi_value <= 30:
    print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI.")
  elif bmi_value >= 18.5 and bmi_value < 25:
    print("Your BMI is in a healthy range.")
  else:
    print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.")  
    
    
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost

Giovanna_insurance_cost = calculate_insurance_cost(name = "Giovanna", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)
Gabriel_insurance_cost = calculate_insurance_cost(name = "Gabriel", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)
