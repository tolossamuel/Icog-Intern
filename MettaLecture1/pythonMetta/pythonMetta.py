from hyperon import * # type: ignore
metta = MeTTa()
result = metta.run(
    '''
    !(+ 1 2)
    '''
)
print(result)
