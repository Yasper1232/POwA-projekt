Projekt tworzony z mysla o zachowaniu zasad SOLID ... i innych :
----------------------------------
S - Single Responsibility Principle
Zasada pojedynczej odpowiedzialnosci
Klasa/ funkcja ma miec jedna odpowiedzialnosc i tylko jeden powod do zmiany
----------------------------------
----------------------------------
O – Open/Closed Principle
Klasa powinna byc otwarta na rozszerzenia ale zamknieta na modyfikacje
 - zamiast zmienaic istniejaca klase , dodaj nowa implementacje przez dziedziczenie!
 ----------------------------------
L-Baska Liskov
Obiekty klasy bazowej powinny być
zastępowalne przez obiekty klas pochodnych bez zmiany logiki programu.
Przyklad bledu : bird ma metode Fly() , a pengiun : Bird ja dziedziczy,
pomimo tego ze jest nie-lotem
 ----------------------------------
 I - Interface Segregation Principle
 Lepeiej miec wiele malych interfejsow niz jeden ogolny do wszystkiego:
 np IPrintalbe, Iscanalbe , IFaxable , zamiast IMultiFunction
  ----------------------------------
  D - Dependency Inversion Principle
  Wysokopoziomowe moduły nie powinny zależeć
   od niskopoziomowych, obie powinny zależeć od abstrakcji.
Przykład:
Klasa OrderService używa IPaymentProcessor,
 a nie konkretnej klasy PayPalPayment.

Wydzielilem logikę ui do osobnego pliku wiec jest to zgodne z S
tak samo jak z plikami w models