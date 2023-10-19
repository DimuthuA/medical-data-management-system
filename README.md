# Medical Data Management System
A program with a CLI written in Python to record medical information related to patients.

There are four user roles defined, each with a different level of access privilege.
The names and the level of access are as follows:

• “doctor” – level of access 4

• “nurse” – level of access 3

• “lab_technician” – level of access 2

• “patient” – level of access 1

The first three user roles have both read and write access while the patient can only read data 
through the program. To access read and write functionalities, the user must first login using the 
correct credentials. A new user must sign up first before logging into the program.

The program writes into and reads from a data file the following data records: personal details, sickness details, drug prescriptions, and lab test prescriptions.
At the time of writing, the users must specify the level of sensitivity of the piece of information 
being recorded.

All users can read previously recorded data with a sensitivity level equal to or below their level 
of access. The patients can only view records about themselves. Only the records with the 
specified ‘type’ will be shown when reading records.
