class EmployerEntity:
    def __init__(self, employer_id, employee_id):
        self.employer_id = employer_id
        self.employee_id = employee_id

    def send_remittance_information(self, employer_id, emplyee_id, ccd_format):
        '''Send payment instructions and Remittance Information to Employers Bank'''

        # payment related information field
        pass

    def get_order_from_sdu(self):
        '''employer is notified to withhold/non-withhold wages of particular employee'''
        pass

    def withhold_wages_for_employee(self, employee_id, withhold_amnt):
        '''withhold wages of particular employee by an income'''
        pass


    def get_payment_format_from_sdu(self, sdu_id, pay_format):
        '''contact the sdu that issued the order to determine payment formats'''
        pass

    def get_state_of_operation_id(self, state):
        ''' [CA, FL, GU, IA, IL, IN, MA, OH, OR, ND, NE, NV, PA, TX, VA, WV]'''
        pass


