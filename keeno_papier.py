voetbalclub = input("Wat is de naam van de voetbalclub?")

# turn string input to integer
oppervlakte = int(
  float(input("Wat is de oppervlakte van het grasveld in vierkante meter?")))

oppervlakeInSquareFoot = float(oppervlakte) * 10.76

kosten = oppervlakeInSquareFoot * 0.30

# formating price with two decimals
text = "De kosten zijn {:.2f} euro."

# new line
print("\n")
print("Wat is de naam van de voetbalclub?", voetbalclub)
print("\n")
print("Wat is de oppervlakte van het grasveld in vierkante meter?",
      oppervlakte)
print("\n")
print("De oppervlakte van", voetbalclub, "is", oppervlakte,
      "vierkante meter, dit is", oppervlakeInSquareFoot, "square foot.")
print("\n")
print(text.format(kosten))