SSN_white_list = [1324, 5678, 9101, 44557]

while True:

    user_ssn_number = input('Enter your SSN number in format (0000): ')


    # check the length
    if len(user_ssn_number) not in (4, 5):
        print('Invalid SSN, please check the format (0000)!!!')
        continue

    if not user_ssn_number.isdigit():
        print('Please enter digits only!!!')
        continue

    if int(user_ssn_number) not in SSN_white_list:
        print('Your permissions are prohibited, please contact your manager!')
        continue
