# # import requests

    
    
# # url = "https://reqres.in/api/users"

# # payload = "{\r\n    \"name\": \"John\",\r\n    \"job\": \"leader\"\r\n}"
# # headers = {
# #   'Content-Type': 'text/plain'
# # }

# # response = requests.request("POST", url, headers=headers, data=payload)

# # print(response.text)


# # import mysql.connector

# # # Establish a connection to the MySQL server
# # mydb = mysql.connector.connect(
# #   host="localhost",
# #   user="yourusername",
# #   password="yourpassword",
# #   database="yourdatabase"
# # )

# # # Create a cursor object to interact with the database
# # mycursor = mydb.cursor()

# # # Define the data to be inserted
# # data = ("John", "Doe", "johndoe@example.com")

# # # Define the query to insert the data
# # sql = "INSERT INTO customers (first_name, last_name, email) VALUES (%s, %s, %s)"

# # # Execute the query and commit the changes to the database
# # mycursor.execute(sql, data)
# # mydb.commit()

# # # Print a message to confirm that the data was successfully inserted
# # print(mycursor.rowcount, "record inserted.")



# import mysql.connector


# id = "79ba3ca5-4270-4b20-9e5b-2597107cb825"

# mydb = mysql.connector.connect(
#   host="nadsidevd4csql.mysql.database.azure.com",
#   user="mysqladmin@nadsidevd4csql",
#   password="_tP9HS!F}FM:G40Q+!f$c11[BG0B2Ar)",
#   database="d4c_fhir_datastore"
# )

# mycursor = mydb.cursor()

# mycursor.execute('SELECT * FROM d4c_fhir_datastore.acknowledge')

# # data = ("John", "Doe", "johndoe@example.com")
# # sql = "INSERT INTO customers (first_name, last_name, email) VALUES (%s, %s, %s)"
# # mycursor.execute(sql, data)
# # mydb.commit()
# # print(mycursor.rowcount, "record inserted.")

# rows = mycursor.fetchall()

# for row in rows:
#   # print(row[0], row[1], row[4])
  
#   if id == row[1]:
#     print(row[0], row[1], row[4])



# import json

# with open("C:/Users/Johnbabu/Documents/00LaerningsDemo/value.json") as data:
#     json_data=json.load(data)
    
# # print(json_data)
# for mrnvalue in json_data["blob_name"]:
#     # print(mrnvalue["mrn"])
#     try:
#         # print(mrnvalue["mrn"])
#         if mrnvalue["mrn"] == "7475889500":
#             print(mrnvalue["mrn"])
#             print("mrnsame")
#     except:
#         pass

# name1 = "sachin"
# name2 = "kohli"

# result = name1 + name2[::-1]
# print(result)

# ***********************************************************************

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# # Set up the WebDriver (ChromeDriver in this example)
# # driver = webdriver.Chrome('.//C://Users/Johnbabu//AppData//Local//Programs//Python//Python310//Scripts//chromedriver')  # Replace 'path_to_chromedriver' with the actual path to the ChromeDriver executable
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # Open the Flipkart website
# driver.get("https://www.flipkart.com/")

# # Find and interact with elements on the UI
# search_box = driver.find_element(By.CSS_SELECTOR, 'input[name="q"]')
# search_box.send_keys("laptop")
# search_box.send_keys(Keys.RETURN)

# # Wait for the search results to load
# driver.implicitly_wait(10)

# # Get the search results
# product_titles = driver.find_elements(By.CSS_SELECTOR, 'a[class="IRpwTa"]')

# # Print the titles of the search results
# for title in product_titles:
#     print(title.text)

# # Close the browser
# driver.quit()


# import 



# from bs4 import BeautifulSoup

# with open("C:/Users/Johnbabu/Pictures/requirements.html", "r") as F:
#     doc = BeautifulSoup(F, "html.parser")
# tag = doc.title
# tag.string = "hello"
# # print(doc.Title)    
# print(doc)

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# # Replace these with your Flipkart login credentials
# username = "your_username"
# password = "your_password"

# # Initialize the WebDriver
# driver = webdriver.Chrome()  # You need to have ChromeDriver installed and its path added to PATH

# # Open Flipkart login page
# driver.get("https://www.flipkart.com/account/login")

# # Find the username and password fields and input your credentials
# username_field = driver.find_element_by_xpath("//input[@class='_2IX_2- VJZDxU']")
# username_field.send_keys(username)

# password_field = driver.find_element_by_xpath("//input[@class='_2IX_2- _3mctLh VJZDxU']")
# password_field.send_keys(password)

# # Submit the login form
# login_button = driver.find_element_by_xpath("//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
# login_button.click()

# # Add some delay to allow the page to load (you can use WebDriverWait for better synchronization)
# time.sleep(5)

# # Close the browser
# driver.quit()


# n = 22
# if n % 2 != 0:
#     print("Weird")
# elif n % 2 == 0 and 2 <= n <= 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not Weird")
# else:
#     print("fail")
    
# year =2100

def is_leap(year):
    leap = False
    if year%4==0:
        leap=True
    else:
        leap=False
    
    # Write your logic here
    
    return leap
print(is_leap(2100))


# is_leap(2100)