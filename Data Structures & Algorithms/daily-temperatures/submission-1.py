class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Input: temperatures = [30,38,30,36,35,40,28]
        Output:               [1,4,1,2,1,0,0]
        stack                 [30,38,30,36,35,40,28]
                                                            0
                                x                           1
                                   x                        2
                                   x  x                     3
                                   x     x  x               4
                                   x     x                  5     
                                               0  0         6
        
        Pseude:
        Initiate = empty array len(temperatures) [0]
        Call a stack   #pair: [temp:index]

        Interate index, temperature in enumerate(temperature)
            while stack and t > stack the top object on the stack initial val[0]
                #pair (30:0)
                stackT, stackInd = stack.pop()
                #i is the day, so 
                res[stackInd] = i - stackInd
            
            #if not
            stack.append the smaller values
        return res                                   
        """
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t,i))
        return res