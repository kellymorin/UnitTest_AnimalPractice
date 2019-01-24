# Testing the Animals

## Setup

Copy the contents of [animals.py](./assets/animal.py) into the file you just created.

## Overview

As a team, we'll be building unit test coverage for all the functionality of the code in the `animal` module. We'll discuss how writing tests often affect the implementation code, and how to think about covering edge cases in your test suite.

## Instructions

In the test class' `setUpClass()` method, create an instance of `Animal` and `Dog` (Be sure to pass in a name argument). Write test cases to verify the I/O of the following methods of `Animal` and `Dog`.

1. Animal object has the correct `name` property.
1. Set a species and verify that the object property of `species` has the correct value.
1. Invoking the `walk()` method sets the correct speed on the both objects.
1. The animal object is an instance of `Animal`.
1. The dog object is an instance of `Dog`.
