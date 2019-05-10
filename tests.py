import os
import pathlib
import unittest

from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome('C:\\Users\\mykeltuz\\Downloads\\Programs\\chromedriver') # change this path to run this test on your device.

class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("tasks.html"))
        self.assertEqual(driver.title, "Tasks")
    
    def test_form_input(self):
        driver.get(file_uri("tasks.html"))
        task = driver.find_element_by_id("task")
        task.send_keys("Testing 1")
        task.submit()
        tasks = driver.find_element_by_id("tasks")
        items = tasks.find_element_by_tag_name("li")
        
        self.assertEqual(items.text, "Testing 1")
    
    def test_empty_input(self):
        driver.get(file_uri("tasks.html"))
        task = driver.find_element_by_id("task")
        task.send_keys('')
        submit = driver.find_element_by_id("submit")
        self.assertTrue(submit.get_property('disabled'), False)



if __name__ == "__main__":
    unittest.main()