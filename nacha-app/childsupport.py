'''
User GUI for Electronic Child Support Payments

Using the Child Support Application Banking Convention

Version 9.0
(Revised September 24, 2024)

NACHA -- The Electronic Payments Association

Table of Contents

Purpose and Scope: 1

Background: 2

Process: 4

NACHA RECORD FORMATS: 9

Third Party Sender and SDUs: 11

Interstate Payments Between SDUs: 13

Child Support Application Banking Convention: 15

820 Payment Order/Remittance Advice TRasaction Set (API): 20

Definitions and Terms - (API 820 Transaction Set): 22

Child Support Mapping: 25

Glossary: 38



'''
option_1 "Purpose"
print(option_1)


'''

1: Purpose and Scope
- The State Disbursement Units and their financial formats, definitions and implentation
    recommend to remit child support payments and payment information electronically through
    the Automated Clearing House (ACH) Network according to current standards.

    Electronic Funds Transfer and Electronic Data Interchange are realized.

- The Child Support Application Banking Convention provides an electronic method for sending
    child support obligations to the SDU via ACH credit payments through the ACH Network.

    The convention forms together with remittance detail about payments use the NACHA CCD+ format.
    Remittance detail for single payment is conveyed in 80-character (Payment Related Information)
    field of DED for (Deduction) Addenda Record 
        of
            the CCD+

    All SDUs are required to accept withholding payments sent in NACHA CCD+ format
    - 9/30/97. 
    - excluding South Carolina

    States allow remittance details and payments using NACHA CTX format containing
    an Accredited Standards Committee (ASC) X12 820 Payment Order/Remittance Advice Transaction
    Set.

    (ASC X12 inter-industry standard) for (EDI)

    If using CTX/820 employers can send multiple payment remittance transactions at once.
    - maximum allowance: 9999 (payment records)
    - max transaction: 820 (transactions)

    within ACH format
'''

def ACHFormat():
    pass


'''

2: Background

    In 1975 US Congress established the Child Support Enforcement Program with the passage of
    Title IV-D of the Social Security Act
        - collecting support payments
        - disbursing funds collected

    As part of the Personal Responsibility and Work Opportunity Act of 1996
    require states that centralized payment processing sites or SDUs to:
        - disburse electronic payments within 2 days
        - provide electronic receipts with all payments

    Child Support Enforcement Program and Family Support Act of 1988
    ================================================================
    exceptions:
        - require immediate handling of payments
        - required to have automated state-wide enforcement management systems
        - required electronic [CA, FL, GU, IA, IL, IN, MA, OH, OR, ND, NE, NV, PA, TX, VA, WV]
    
    Payments must be:
        - scanned
        - identified
        - deposited
        - credited
        - disbursed


    Personal Responsibility and Work Opportunity Act of 1996
    ========================================================
    Personal payments must be:
        - set up via centralized payment processing site
        - disburse payments within 2 days of receipt
        - opened
        - scanned
        - identified
        - deposited
        - credited
        - disbursed

'''

is_scanned = False

'''

4: Process

    account: <balance on file bounded by File Header Record and File Control Record>

    employer: <notified to withhold wages of particular employee by income according to order>
    
    state: <notifies employer to withhold wages and serves as legal basis for employer to do so>

    employee: <provides necessary SDUs bank information for sending payments electronically>

    SDU: <determine which payment formats enforcement support systems are required to use>
        - update records
        - credits account
        - disburses via electronic payment

    Bank/Financial Institution: <orginiates the ACH entries to transfer to the SDU>


    workflow: <order to transfer funds and data in payment instructions>
       state - order to transfer funds and data
       employer/person - transmit payment instructions and remittance information to financial institution
       bank - originates the entries to transfer the payment and remittance data via ACH network
       sdu - posts funds to SDU account and provides remittance information(EDI) of payments in agreed format
       account - credited to serve facilitation and balancing of the file to Entry Detail Records
       addenda record - used to supply additional payment relation information in the EDR


    
    workflow a:
        - employee uses employee_bank via ACH network
        - ACH network send to SDU bank
        - SDU distribute remittance and information to account

    workflow b:
        - employer send remittance to employee_bank
        - employee_bank send via ACH network to SDU bank
        - SDU distrubte remittance and information to account


    workflow sdu:
        - SDU_bank send remittance information to SDU
        - SDU send payment instructions to SDU_bank
        - SDU_bank send via ACH network to account
        - custodial_bank send via electronic system to account

    workflow by_state:
        - SDU_1 send payment instructions and information to SDU_bank_1
        - SDU_bank_1 send via ACH network to SDU_bank_2
        - SDU_bank_2 send info to SDU_2
        - SDU_2 send instructions to SDU_bank_2
        - SDU_bank_2 send via ACH network to account
       
'''
def workflow_sdu(payment:float, instr: str, acct: str, branch: str) -> RECORD:
    pass

def workflow_b(employerId: str, employee_bank_id: str, remittance: float) -> str:
    pass

def workflow_by_state(state_id_1: str, state_id_2: str, sdu_bank_1_id: str, sdu_bank_2_id: str, acct: str) -> str:
    pass

def get_record_for_account(account: str, recd: dict, target: str) -> str:
    # search record for target and return the string representation
    pass

def get_record_size():
    pass


SDU_bank_2_name = "Child Support | Florida"
account_id = "12344"

def instituion_post(funds: int) -> str:
    # provides the remittance information EDI
    # in the format agreed with entity
    pass



'''
9: NACHA Record Formats
'''
