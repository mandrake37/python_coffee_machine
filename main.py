MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100
}

applicable_coin_values = {
    'penny': 0.01,
    'nickle': 0.05,
    'dime': 0.1,
    'quarter': 0.25
}

available_options = ['espresso', 'cappuccino', 'latte', 'report', 'off']

def validate_user_input(option):
    return True if option in available_options else False


def check_resources(drink):
    drink_ingredients = MENU[drink]['ingredients']
    result = {
        'is_enough': True,
        'message': ''
    }

    for ingredient in drink_ingredients:
        # Don't need to list each missing ingredient, only first
        if drink_ingredients[ingredient] > resources[ingredient]:
            result['is_enough'] = False
            result['message'] = f'Sorry there is not enough {ingredient}'
            break

    return result

def subtract_resources(drink):
    for item in MENU[drink]['ingredients']:
        resources[item] -= MENU[drink]['ingredients'][item]


def coffee_machine(money):
    customer_money = 0
    customer_choice = input('What would you like? (espresso/latte/cappuccino): ')
    is_option_valid = validate_user_input(customer_choice)

    if is_option_valid:
        match customer_choice:
            case 'espresso' | 'latte' | 'cappuccino':
                check_result = check_resources(customer_choice)

                if check_result['is_enough']:
                    print('Please insert coins.')

                    for option in applicable_coin_values:
                        coins_amount = int(input(f'How many {option}? '))
                        customer_money += applicable_coin_values[option] * coins_amount

                    if customer_money < MENU[customer_choice]['cost']:
                        print('Sorry that\'s not enough money. Money refunded.')
                    else:
                        customer_change = customer_money - MENU[customer_choice]['cost']
                        money += MENU[customer_choice]['cost']
                        subtract_resources(customer_choice)
                        print(f'Here is ${round(customer_change, 2)} in change')
                        print(f'Here is your {customer_choice} ☕️. Enjoy!')
                else:
                    print(check_result['message'])

            case 'report':
                print(f'Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g  \nMoney: ${money}')
            case 'off':
                print('Turning off...')
                return
    else:
        print('Invalid input')

    # Recursively invoke the function
    coffee_machine(money)

coffee_machine(0)