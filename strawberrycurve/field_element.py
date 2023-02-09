class FieldElement:
    # constructs new finite field element
    def __init__(self,num,prime):
        # ensure the number is within xrange 0 and prime-1 (inclusive)
        if num >= prime or num < 0:
            error = f'Number {num} is not in the field range of 0 to {prime -1}'
            raise ValueError(error)
        self.num = num
        self.prime = prime
    
    # asserts equality of field elements
    def __eq__(self,other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime     
    
    # asserts inequality field elements
    def __ne__(self,other):
        if other is None:
            return False
        return not(self == other)
       
    # reproduces field element 
    def __repr__(self):
        return f'FieldElement_{self.prime}_{self.num}'
    
    # adds field elements
    def __add__(self,other):
        if self.prime != other.prime:
            error = f'FieldElement addition error - field prime: {self.prime}, received prime: {other.prime}'
            raise TypeError(error)
        numadd = (self.num + other.num) % self.prime
        return self.__class__(numadd,self.prime)
    
    # subtracts field elements
    def __sub__(self,other):
        if self.prime != other.prime:
            error = f'FieldElement subtraction error - field prime: {self.prime}, received prime: {other.prime}'
            raise TypeError(error)
        numsub = (self.num - other.num) % self.prime
        return self.__class__(numsub,self.prime)
    
    # multiplies field elements
    def __mul__(self,other):
        if self.prime != other.prime:
            error = f'FieldElement multiplication error - field prime: {self.prime}, received prime: {other.prime}'
            raise TypeError(error)
        nummul = (self.num * other.num) % self.prime
        return self.__class__(nummul,self.prime)

    # divides field elements
    def __truediv__(self,other):
        if self.prime != other.prime:
            error = f'FieldElement division error - field prime: {self.prime}, received prime: {other.prime}'
            raise TypeError(error)
        numdiv = self.num * pow(other.num,self.prime-2,self.prime) % self.prime
        return self.__class__(numdiv,self.prime)
    
    # exponentiates field elements (exponent is not required to be within finite field)
    def __pow__(self,expn):
        # make exponent within 0 to p-2 range (inclusive)
        nexp = expn % (self.prime - 1)  
        numpow = pow(self.num, nexp, self.prime)
        return self.__class__(numpow,self.prime)