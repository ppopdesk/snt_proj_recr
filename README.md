# snt_proj_recr

The loaning system in its core aims to search and add costumers (lenders or borrowers) to the database using oop. This database contains various information about the costumers and the scheme they are applying for. It also has a provision to add different loan schemes and modify the same.

Code Explantion : 

The PersonalInformation() class contains the broad spectrum of information that a lender and borrower has. It also has various methods to display information of the costumer.

The Schemes() class contains broad information about various schemes provided by the loaning service and LenderSchemes() and BorrowerSchemes() are its subclasses that has the method (pseudomethod actually :)) to calculate interest rate and emi respectively

Borrower() and Lender() are child classes of PersonalInformation(). Borrower() has a init method which check (pseudochecks) whether loan is approved or not and some other methods. Both these classes also have a class method to search for borrower/lender based on FULL NAME.

I have also initialized 3 loan schemes and 3 fd schemes in the code.

What follows is basically asking for user inputs 

How to run?

If you want to search for a costumer enter 'Search' in the first question
If you want to add  a costumer enter 'Add' in the first question
If you want to exit user input loop press 1
Subsequently answer all questions and answer in proper format i.e. :
    full name format : "XXX.. YYY.." (name and surname seperated by space)
    Enter one of the available scheme types (displayed in the start) when asked for scheme types 

** We can access interest rate, total amount to be paid, emi and other features through some other changes in the UI. It is available as class method but not implemented in UI. **

Note : We have to add data so as to search as of now there are no data available in borrowers or costumers


Part 2 of the test answer : 

The loaning system created is a centralized system as the bank authorities are responsible in handling customers funds and carrying out transactions from their part. Intermediaries have access to costumer data and have the authority to manipulate them. 

Disadvantage of this type of a system is that the banking authorities work under the hood. They can misuse the authority they posses to their advantage as long as the costumer side of things runs smoothly. Also we must place our trust on a single entity which may or may not be very practical. The data is stored in a single system in a single server and is thus a single point of failure