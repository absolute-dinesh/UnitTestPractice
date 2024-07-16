class EncodingTech:

    def __init__(self,value) -> None:
        self.value = value

    # AAAABBBCCDAA to 4A3B2C1D2A
    # encodes sequences of repeated values (runs) by storing the value and the length of the run

    def run_length_encoding(self):
        self.final = ""
        i = 0
        lngth = len(self.value)

        while i < lngth:
            count = 1
            while i+1 < lngth and self.value[i] == self.value[i+1]:
                count += 1
                i += 1

            self.final = self.final + str(count) + (self.value[i])
            i = i + 1
        
        return self.final
    
if __name__ == '__main__':
    encoder = EncodingTech("AAAABBBCCDAA")
    print(encoder.run_length_encoding())

            
            


