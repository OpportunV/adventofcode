class IntcodeComputer:
    def __init__(self, ind, intcode: list = None):
        if intcode is None:
            with open('d7_input.txt') as fin:
                intcode = [int(i) for i in fin.readline().split(',')]
                # intcode = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
                # intcode = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

        self.intcode = intcode
        self.pointer = 0
        self.ind = ind
        self.cor = 0
        self.cor = self.run()
        self.cor.send(None)
        
    @property
    def value(self):
        return self.intcode[self.pointer]
    
    @property
    def opcode(self):
        return self.value % 100
    
    def get_param_mode(self, order):
        return self.value // 10 ** (order + 1) % 10
    
    def get_param(self, order):
        if self.get_param_mode(order) == 0:
            return self.intcode[self.intcode[self.pointer + order]]
        elif self.get_param_mode(order) == 1:
            return self.intcode[self.pointer + order]
    
    def set_param(self, order, value):
        if self.get_param_mode(order) == 0:
            self.intcode[self.intcode[self.pointer + order]] = value
        elif self.get_param_mode(order) == 1:
            self.intcode[self.pointer + order] = value
    
    def run(self):
        while self.opcode != 99:
            if self.opcode == 1:
                self.set_param(3, self.get_param(1) + self.get_param(2))
                self.pointer += 4
            
            elif self.opcode == 2:
                self.set_param(3, self.get_param(1) * self.get_param(2))
                self.pointer += 4
            
            elif self.opcode == 3:
                tmp = yield
                self.set_param(1, tmp)
                self.pointer += 2
            
            elif self.opcode == 4:
                yield self.get_param(1)
                self.pointer += 2
            
            elif self.opcode == 5:
                if self.get_param(1):
                    self.pointer = self.get_param(2)
                else:
                    self.pointer += 3
            
            elif self.opcode == 6:
                if self.get_param(1) == 0:
                    self.pointer = self.get_param(2)
                else:
                    self.pointer += 3
            
            elif self.opcode == 7:
                self.set_param(3, int(self.get_param(1) < self.get_param(2)))
                self.pointer += 4
            
            elif self.opcode == 8:
                self.set_param(3, int(self.get_param(1) == self.get_param(2)))
                self.pointer += 4
