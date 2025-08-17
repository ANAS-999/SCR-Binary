class Binary:
    def getBinary(self, decimal: int) -> str:
        list = []
        output = ''

        if decimal == 0:
            return '0'

        while decimal != 1:
            r = decimal % 2
            decimal = decimal // 2

            list.append(r)

        list.append(1)
        list.reverse()

        for i in list:
            output += str(i)

        return output

    def getDecimal(self, binary: str) -> int:
        if not self.isBinary(binary):
            return None

        decimal = 0

        for i in range(len(binary)):
            item = int(binary[i])
            power = len(binary) - i - 1

            decimal += 2 ** power * item

        return decimal

    def isBinary(self, binary: str) -> bool:
        for i in binary:
            if i != '0' and i != '1':
                return False

        return True

    def sumBinaryByDecimal(self, binary1: str, binary2: str) -> str:
        if not self.isBinary(binary1) or not self.isBinary(binary2):
            return None

        decimal1 = self.getDecimal(binary1)
        decimal2 = self.getDecimal(binary2)

        return self.getBinary(decimal1 + decimal2)

    def sumBinary(self, binary1: str, binary2: str) -> str:
        if not self.isBinary(binary1) or not self.isBinary(binary2):
            return None

        length = max(len(binary1), len(binary2))

        result = ''
        binary1 = self.setUpBinary(binary1, length)[::-1]
        binary2 = self.setUpBinary(binary2, length)[::-1]

        i = 0
        output = 0
        carry_out = '0'

        for i in range(length):
            output, carry_out = self.adder(binary1[i], binary2[i], carry_out)
            result += output

        if carry_out == '1':
            result += carry_out

        return result[::-1]

    def adder(self, x: str, y: str, carry_in: str) -> list[str, str]:
        carry_out = '0'
        output = str(int(x) + int(y) + int(carry_in))

        if output == '2':
            output = '0'
            carry_out = '1'

        elif output == '3':
            output = '1'
            carry_out = '1'

        return [output, carry_out]

    def setUpBinary(self, binary: str, length: int) -> str:

        if len(binary) == length:
            return binary

        for _ in range(length - len(binary)):
            binary = '0' + binary

        return binary
