from Homework4 import main 
import pytest

def test_values():
	assert main("Boston") == "Boston"
	assert main("school") == "school"
	assert main("family") == "family"
	assert main("coffee") == "coffee"
