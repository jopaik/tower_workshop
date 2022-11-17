class FilterModule(object):
    def filters(self):
        return {
            'my_filter1': self.my_filter1,
            'my_filter2': self.my_filter2,
            'my_filter3': self.my_filter3
        }

    def my_filter1(self, filter_input):
        filter_input = filter_input + ' JP NEW FILTER1'
        return filter_input
    
    def my_filter2(self, filter_input):
        filter_input = filter_input + ' JP NEW FILTER2'
        return filter_input
    
    def my_filter3(self, filter_input):
        filter_input = filter_input + ' JP NEW FILTER3'
        return filter_input