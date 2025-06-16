from .basic_operations import AddOperation, SubtractOperation, MultiplyOperation, DivideOperation, PowerOperation

class OperationFactory:
    @staticmethod
    def create_operation(operator: str):
        operations = {
            '+': AddOperation(),
            '-': SubtractOperation(),
            '*': MultiplyOperation(),
            '/': DivideOperation(),
            '^': PowerOperation()
        }
        return operations.get(operator)
