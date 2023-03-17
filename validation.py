
def validate_Name(data, conditon:int):
    illegal_Characters: list = ['<', '>', ':','"', '/', '.','\\', '|', '?', '*', ]
    first_Character : list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_',' ']
    
    if data[0] != first_Character:
            failed = print(f'You can not have {first_Character} at the start of name')
            return failed, conditon
    elif data == 'test':
        failed = print(f'Name can not be "test"')
        return failed, conditon
    else:
        for x in data:
            if x != illegal_Characters:
                conditon = 1
            else:
                conditon = 0
                return conditon
                
    return conditon