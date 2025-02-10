from behave import given, when, then
from src.calculator import Calculator

@given("I have two numbers {num1:d} and {num2:d}")
def step_given_two_numbers(context, num1, num2):
    context.num1 = num1
    context.num2 = num2
    context.calculator = Calculator()

@when("I add the numbers")
def step_when_add_numbers(context):
    context.result = context.calculator.add(context.num1, context.num2)

@when("I subtract the numbers")
def step_when_subtract_numbers(context):
    context.result = context.calculator.subtract(context.num1, context.num2)

@then("the result should be {expected:d}")
def step_then_result_should_be(context, expected):
    assert context.result == expected, f"Expected {expected}, but got {context.result}"
