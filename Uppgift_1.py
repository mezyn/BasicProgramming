print("Välkomna till denna pensionssimulator")
print("Vad heter du i förnamn?")
förnamn = input()
print("Hur gammal är du?")
ålder = int(input())
år_till_pension =  65 - ålder
print("Hej " + förnamn + ". Du går i pension om " + str(år_till_pension) + " år.")
print("Tryck på valfri tangent för att förtsätta . . .")
input()