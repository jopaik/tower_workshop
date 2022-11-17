class FilterModule(object):
    def filters(self):
        return {
            'my_filter1': self.my_filter1,
            'my_filter2': self.my_filter2,
            'my_filter3': self.my_filter3
        }

    def my_filter1(self, a_variable):
        a_new_variable = a_variable + ' JP NEW FILTER1'
        return a_new_variable
    
    def my_filter2(self, b_variable):
        b_new_variable = b_variable + ' JP NEW FILTER2'
        return b_new_variable
    
    def my_filter3(self, c_variable):
        c_new_variable = c_variable + ' JP NEW FILTER3'
        return c_new_variable