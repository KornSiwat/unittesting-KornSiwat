[![Build Status](https://travis-ci.com/KornSiwat/unittesting-KornSiwat.svg?branch=master)](https://travis-ci.com/KornSiwat/unittesting-KornSiwat)
[![codecov](https://codecov.io/gh/KornSiwat/unittesting-KornSiwat/branch/master/graph/badge.svg)](https://codecov.io/gh/KornSiwat/unittesting-KornSiwat)

## Unit Testing Assignment

by Siwat Ponpued 6110546640.

## Test Cases for unique

Write a table describing your test cases.

| Test case                                      | Expected Result              |
| ---------------------------------------------- | ---------------------------- |
| empty list                                     | empty list                   |
| one item without duplication                   | list with 1 item             |
| one item with duplications                     | list with 1 item             |
| n items without duplication                    | list with n items            |
| n items same data type with duplications       | n items list with same order |
| n items different data types with duplications | n items list with same order |
| wrong input type (not a list)                  | raises TypeError             |

## Test Cases for Fraction

| Test case              | Expected Result                                          |
| ---------------------- | -------------------------------------------------------- |
| init with int type     | instance of Fraction class                               |
| init with not int type | raises TypeError                                         |
| call \_\_str\_\_       | string of simplified fraction                            |
| call \_\_repr\_\_      | string of fraction initialization                        |
| equality               | true if their values are equal and false if not          |
| addition               | sum of fractions is mathematically correct               |
| subtraction            | result of subtraction is mathematically correct          |
| multiplication         | product of fractions is mathematically correct           |
| division               | result of fractions division is mathematically correct   |
| greater than operation | true if a fraction is greater and false if not           |
| less than operation    | true if a fraction is lesser and false if not            |
| negation               | result is equal to the initial fraction multiplied by -1 |
