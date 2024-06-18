select firstName, lastName, city, state 
from Person left join Address
On Person.personID = Address.personID