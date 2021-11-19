# healer
## Design decisions:

Uses sql alchemy and postgress for loading data and used pandas for reading in between for the ease of use.
Initially decided to implement a command line tool with click but given the csv files were more "malformed" than I thought my time was not enough for the full implementation.
Addrc file does not have column names therefore a design decision made to write column names instead of copying as this could occur in other files as well.

And also the csv file rows does not have ids therefore added pseudo ids in the model classes.

the code gives the top ten list when its run the read_quantity data without the practice names.

For db setup used sql and bash


healer tool for pharmacy


# Installation

#### DB Setup

"""Run db.sh to setup db if you have MAC,
Otherwise 
start postgress for your OS
add user and password of your choice 
and update the upload_data.py """







# Usage


## Upload data
In order to upload data, you need to pass the file path as in the example below:

##### upload_data('PDPIC.csv')
##### upload_data('ADDRC.csv')
##### upload_data('CHEMC.csv')

## Read data
In order to read the data you need pass list of the chemical names to the read data as in the example below:

The exact same query for quantity information did not work for names.  
##### read_quantity_data(['melatonin'])
##### read_data(['melatonin'])      



known issue:
The exact same query for quantity information did not work for names.  
I did not have time to fix it further