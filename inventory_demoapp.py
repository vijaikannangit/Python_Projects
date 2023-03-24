"""
INVENTORY DEMO APPLICATION.
This Module is developed as a Demo Application for Inventory Storage.
This Module Contains Data Entry and Report.
Imports Packages such as Datetime, Json and OS for Date Operations, File Handling.
"""

from datetime import date, datetime, timedelta
import json
import os

#Prints the Heading for the Inventory Demo App.
print ("*************************************************")
print ("*\t   STORE INVENTORY APPLICATION\t        *")
print ("*\t        DATA ENTRY/REPORTS    \t        *")
print ("*************************************************")


CONT_ASK=True
inventory={}
FILE_NAME="Store_Inventory_Data.json"
USR_INP_UNIT_PRICE=""
DICT_REC_CNT=0
PARS_DAT_FILE=''
VALID_DATA_REP=True
tdays_dt=date.today()
inv_data=[]

def validate_optionfor_de_rep(dataentry_report_exit):
    """
    Validating User Options for Data Entry , Report and  Exit. Should Not Accept NULL Value.
    dataentry_report_exit: Boolean
                    True if option entered is other than 0, 1 or 2.
                    False if user enters proper data i.e 0 or 1 or 2.
    Exception:
        Exception raised if user enetred is alphabet. Other Exceptions also handled.
    Returns:
    --------
    Number
        Option Choosen by the User been returned . Either 0, 1 or 2.
    """

    dataentry_report_exit=True
    while dataentry_report_exit:
        while True:
            try:
                print ("\n\nEnter '0' for Inventory Data Entry")
                print ("Enter '1' for Inventory Report")
                print ("Enter '2' to Exit ")
                usr_inp_datarep = int(input("\nEnter Either Zero or 1  or 2    : "))
            except: #pylint: disable=bare-except
                print ('\nChoose 0(Zero) for Data Entry and 1 for Report. Please Re-Enter')
                dataentry_report_exit = True
                continue
            else:
                break

        if usr_inp_datarep < 0 or usr_inp_datarep > 2:
            print ('\nChoose 0(Zero) for Data Entry, 1 for Report and 2 to Exit. Please Re-Enter')
            dataentry_report_exit=True
        else:
            dataentry_report_exit=False
    return (usr_inp_datarep,dataentry_report_exit)

def fileexist_to_python(f_name):
    """
    If Data File Exists with Data load the data to Python.
    Keyword arguments:
    -----------------
    f_name : string format.
        File Name stored in this module as Variable.
    Returns:
    --------
    Data File
        Json Data File been Parsed and returned as Python File
    """
    pars_data_file=''
    read_data_file=''
    if os.path.exists(f_name):
        with open(f_name, 'rt') as read_data_file:
            file_sz=os.path.getsize(f_name)
            if file_sz != 0:
                pars_data_file=json.load(read_data_file)
    return pars_data_file

#Validate :- Choice for Data Entry or Report
usr_inp_dta_rep, VALID_DATA_REP=validate_optionfor_de_rep(VALID_DATA_REP)

"""
If data file exists with data downloaded to python.
File been converted to List and stored in PARS_DAT_FILE.
DICT_REC_CNT :- Variable created for finding number of records in the existing data file
"""

PARS_DAT_FILE=fileexist_to_python(FILE_NAME)
inv_data=list(PARS_DAT_FILE)
DICT_REC_CNT=len(inv_data)

def null_check_str(usr_inp_str,fld_name):
    """
    Validating User Input . Should Not Accept NULL Value.
    Keyword arguments:
    -----------------
    usr_inp_str : string format.
        Input from the user.
    fld_name    : String format.
        User Prompted for Category  / Product / Date Received.
    Returns:
    --------
    null_value : Boolean
        Returns True and Displays Error Message if user input value NULL/EMPTY.
        Returns False if user input value is NOT NULL/EMPTY.
    """

    if usr_inp_str=='':
        print (f'{fld_name} Cannot be NULL. Please Re-Enter')
        null_value=True
    else:
        null_value=False

    return null_value

def neg_val_chk(usr_inp_num, fld_name):
    """
    User Input Validation. Should be Greater than Zero. Negative Value Not Allowed.
    Keyword arguments:
    -----------------
    usr_inp_num : number format.
        Input from the user.
    fld_name    : String format.
        User Prompted for Unit Price / Quantity.
    Returns:
    --------
    negative_value_check : Boolean
        Returns True and Displays Error Message if user input value is less than or equal to Zero.
        Returns False if user input value is greater than zero.
    """

    if usr_inp_num<=0:
        print (f"{fld_name} should be greater than Zero. Please Re-Enter")
        negative_value_check=True
    else:
        negative_value_check=False

    return negative_value_check

def disp_up_qty_errmsg(fld_name):
    """
    User Input Validation. Exception Handled when alphabets entered in numerical field.
    Keyword arguments:
    -----------------
    fld_name : String format.
        Input from the user. To display the prompt name in the error message.
    Returns:
    --------
    Boolean
        Returns True and Displays Error Message if user input value is alphabet.
    """

    print (f"{fld_name} should be greater than Zero. Please Re-Enter")
    return True

def duplication_chk(dic_reccnt):
    """
    If already the record exists in list, user should get error messsage.
    Duplication Entry not allowed.
    Keyword arguments:
    -----------------
    dic_reccnt : Number(length of List).
        Number of Records in the List.
    Returns:
    --------
    cos_dup_exists : String
        Returns 'Y' if Duplicate exists else 'N'.
    """

    lst_category_name=''
    lst_product_name=''
    lst_unit_price=''
    lst_quantity=''
    lst_date_added=''
    cos_dup_exists = 'N'
    if dic_reccnt>0 :
        for inv_lst in inv_data :
            for i in inv_lst.items():
                if i[0] == 'category_name':
                    lst_category_name = i[1]
                elif i[0] == 'product_name':
                    lst_product_name = i[1]
                elif i[0] == 'unit_price':
                    lst_unit_price = i[1]
                elif i[0] == 'quantity' :
                    lst_quantity = i[1]
                elif i[0] == 'date_added':
                    lst_date_added = i[1]

                if (lst_category_name == usr_inp_category_name and
                    lst_product_name == usr_inp_product_name and
                    lst_unit_price == USR_INP_UNIT_PRICE and
                    lst_quantity == usr_inp_quantity and
                    lst_date_added == usr_inp_date_added):

                    cos_dup_exists = 'Y'
                    print ('\nItem Already Exists. Duplicate Entry. Entries must be UNIQUE.')

    return cos_dup_exists

def insert_records_to_dict():
    """
    If the entered data is not found in the list, then the same is appended to list.
    Record count also increased by one.

    COSMETIC_DUP_EXISTS : String. If no duplicate then added to List.

    Result:
    -------
    If no Duplicate exists user data will be appened to the list.
    Record count is increased by one when data is added to list by DICT_REC_CNT variable.
    """

    inventory["category_name"] = usr_inp_category_name
    inventory["product_name"]  = usr_inp_product_name
    inventory["unit_price"]    = USR_INP_UNIT_PRICE
    inventory["quantity"]      = usr_inp_quantity
    inventory["date_added"]    = usr_inp_date_added

    inv_data.append(inventory.copy())

#Tf the option choosen is for Inventory Data Entry
if usr_inp_dta_rep==0:

    #Inputs from End User
    while CONT_ASK:

        # Validate Category Name
        VALID_CATEGORY_NAME=True
        while VALID_CATEGORY_NAME:
            usr_inp_category_name=input("\nEnter Category                  : ")
            VALID_CATEGORY_NAME=null_check_str(usr_inp_category_name,"Category")

        # Validate Product Name
        VALID_PRODUCT_NAME=True
        while VALID_PRODUCT_NAME:
            usr_inp_product_name=input("Product Name                    : ")
            VALID_PRODUCT_NAME=null_check_str(usr_inp_product_name,"Product")

        # Validate Unit Price
        VALID_UNIT_PRICE=True
        while VALID_UNIT_PRICE:
            while True:
                try:
                    USR_INP_UNIT_PRICE=float(input("Enter Unit Price of the Product : "))
                except: #pylint: disable=bare-except
                    VALID_UNIT_PRICE=disp_up_qty_errmsg('Unit Price')
                    continue
                else:
                    break

            VALID_UNIT_PRICE=neg_val_chk(USR_INP_UNIT_PRICE, "Unit Price")

        # Validate Quantity
        VALID_QUANTITY=True
        while VALID_QUANTITY:
            while True:
                try:
                    usr_inp_quantity = int(input("Enter Quantity Received         : "))
                except: #pylint: disable=bare-except
                    VALID_QUANTITY=disp_up_qty_errmsg('Quantity')
                    continue
                else:
                    break

            VALID_QUANTITY=neg_val_chk(usr_inp_quantity, "Quantity")

        # Validate Date Received
        VALID_DATE_ADDED=True
        while VALID_DATE_ADDED:
            usr_inp_date_added=input("Date Received (DD/MM/YYYY)      : ")
            VALID_DATE_ADDED=null_check_str(usr_inp_date_added,"Date Received")

        # Duplication Check in nested dictionary
        COSMETIC_DUP_EXISTS='N'
        COSMETIC_DUP_EXISTS=duplication_chk(DICT_REC_CNT)

        # User Input inserted to dictionary as Nested Dictionary
        if COSMETIC_DUP_EXISTS == 'N':
            insert_records_to_dict()
            DICT_REC_CNT+=1

        # Validate Yes / No for Continuity
        VALID_YES_NO=True
        while VALID_YES_NO:
            inp_cont_ask=input ("\nDo You Want To Continue (Y/N)  : ")

            if inp_cont_ask.upper()=='Y':
                CONT_ASK = True
                VALID_YES_NO = False
            elif inp_cont_ask.upper()=='N':
                CONT_ASK = False
                VALID_YES_NO = False
            #elif inp_cont_ask.isdigit() == True :
            elif inp_cont_ask.isdigit():
                print ('Invalid Entry. Enter Either Y(es) or N(o)')
                VALID_YES_NO = True
            elif inp_cont_ask != 'Y' or inp_cont_ask != 'N':
                print ('Enter Either Y(es) or N(o)')
                VALID_YES_NO = True


    #Write from Nested dictionary to JSON file
    with open(FILE_NAME, 'w') as access_data:
        json.dump(inv_data, access_data, indent = 4)
        # Close File
        access_data.close()
        print ("\n")

# Generating Report according to User Input
elif usr_inp_dta_rep == 1 :
    usr_inp_rep_cat_name = input("\nEnter Category                 : ")
    usr_inp_rep_prd_name = input("Entry Product Name             : ")
    usr_inp_rep_num_days = input("Stock Aging (Number of days)   : ")

    print ('Category         Product Name        Unit Price      Quantity     Date Received')
    print ('-------------------------------------------------------------------------------')
    DATA_FOUND = 'N'
    for key, value in inventory.items():
        for key1, value1 in value.items():
            pass

        #Display all data if Entry is null
        if usr_inp_rep_cat_name == '' and usr_inp_rep_prd_name == '' and usr_inp_rep_num_days =='':
            print (f'{value["category_name"]:<15}  {value["product_name"]:<15}  {value["unit_price"]:>13}  {value["quantity"]:>12} \t   {value["date_added"]:<25} ') #pylint: disable=line-too-long
            DATA_FOUND = 'Y'

        #Display data for the entered Category Name
        if (value["category_name"]==usr_inp_rep_cat_name and
            usr_inp_rep_prd_name == '' and
            usr_inp_rep_num_days ==''):
            print (f'{value["category_name"]:<15}  {value["product_name"]:<15}  {value["unit_price"]:>13}  {value["quantity"]:>12} \t   {value["date_added"]:<25} ') #pylint: disable=line-too-long
            DATA_FOUND = 'Y'

        #Display data for the entered Product Name
        if (usr_inp_rep_cat_name == '' and
            value["product_name"] == usr_inp_rep_prd_name and
            usr_inp_rep_num_days ==''):
            print (f'{value["category_name"]:<15}  {value["product_name"]:<15}  {value["unit_price"]:>13}  {value["quantity"]:>12} \t   {value["date_added"]:<25} ') #pylint: disable=line-too-long
            DATA_FOUND = 'Y'

        #Display data for the entered Number days old data
        if (usr_inp_rep_cat_name == '' and
            usr_inp_rep_prd_name == '' and
            usr_inp_rep_num_days !=''):
            #print (f'{old_date} , {tdays_dt}')
            old_date = tdays_dt - timedelta(days=int(usr_inp_rep_num_days))
            #print (old_date)
            #print (datetime.date((datetime.strptime(value["date_added"],'%d/%m/%Y'))))
            if (datetime.date((datetime.strptime(value["date_added"],'%d/%m/%Y'))) >= old_date and
                usr_inp_rep_cat_name == '' and
                usr_inp_rep_prd_name == ''):
                print (f'{value["category_name"]:<15}  {value["product_name"]:<15}  {value["unit_price"]:>13}  {value["quantity"]:>12} \t   {value["date_added"]:<25} ') #pylint: disable=line-too-long
                DATA_FOUND = 'Y'

        #Display data for the entered Category and Product Name
        if (value["category_name"] == usr_inp_rep_cat_name and
            value["product_name"] == usr_inp_rep_prd_name and
            usr_inp_rep_num_days ==''):
            print (f'{value["category_name"]:<15}  {value["product_name"]:<15}  {value["unit_price"]:>13}  {value["quantity"]:>12} \t   {value["date_added"]:<25} ') #pylint: disable=line-too-long
            DATA_FOUND = 'Y'

        #Display data for the entered Product Name and Number of days
        if (usr_inp_rep_cat_name == '' and
            value["product_name"] == usr_inp_rep_prd_name and
            usr_inp_rep_num_days != ''):
            old_date = tdays_dt - timedelta(days=int(usr_inp_rep_num_days))
            if (value["product_name"] == usr_inp_rep_prd_name and
                datetime.date((datetime.strptime(value["date_added"],'%d/%m/%Y'))) >= old_date):
                print (f'{value["category_name"]:<15}  {value["product_name"]:<15}  {value["unit_price"]:>13}  {value["quantity"]:>12} \t   {value["date_added"]:<25} ') #pylint: disable=line-too-long
                DATA_FOUND = 'Y'

        #Display data for the entered Category,Product Name and Stock Aging
        if (value["category_name"] == usr_inp_rep_cat_name and
            value["product_name"] == usr_inp_rep_prd_name and
            usr_inp_rep_num_days != ''):
            old_date = tdays_dt - timedelta(days=int(usr_inp_rep_num_days))
            if (value["category_name"] == usr_inp_rep_cat_name and
                value["product_name"] == usr_inp_rep_prd_name and
                datetime.date((datetime.strptime(value["date_added"],'%d/%m/%Y'))) >= old_date):
                print (f'{value["category_name"]:<15}  {value["product_name"]:<15}  {value["unit_price"]:>13}  {value["quantity"]:>12} \t   {value["date_added"]:<25} ') #pylint: disable=line-too-long
                DATA_FOUND = 'Y'

    #If no record exists according to the user input
    if DATA_FOUND == 'N':
        print ('\t\t\t ****** No Data Found ******')

#Exit from Stores Invntory Appl
else :
    VALID_DATA_REP = True
    print ("\n")
