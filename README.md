# python-ATM-

It looks like you've provided the full description and key features of the Python program and are asking for the same content back. Here is the requested content, which provides a complete overview of the Python University Registration System project.

***

### **Description**

This project is a **Python object-oriented program** that simulates a basic **University/College registration system**. It uses **Abstract Base Classes (ABC)** to enforce a common structure for different types of people (students, professors, and admins) and manages these individuals within a `universtiy` class. The entire system is driven by a simple, text-based **menu interface**.

***

### **Key Features**

#### **1. Abstract Base Class (`college`)**
* **Enforced Structure:** The `college` class inherits from `ABC` and defines an **abstract method** called `role()`. This forces all derived classes (`student`, `Admin`, `Prof`) to implement their own version of the `role()` method, ensuring they all have a defined role.
* **Encapsulation:** Basic details (`name`, `age`, `id`) are encapsulated using **private attributes** (e.g., `self.__name`).
* **Concrete Methods:** It provides **concrete methods** (`basic()` and `get_detail()`) to display common information, promoting code reuse.

#### **2. Derived Classes (`student`, `Admin`, `Prof`)**
* **Polymorphism:** Each class implements the required abstract method `role()` to return its specific designation ('Student', 'Admin', or 'Proff').
* **Unique Attributes:** Each class has unique attributes (e.g., `__course` for `student`, `__email` for `Admin`, `__dept` for `Prof`).
* **Helper Methods:** Each class has an informational method (e.g., `student_info()`, `prof_info()`) to display specific details.

#### **3. Management Class (`universtiy`)**
* **Data Management:** It uses a private list `self.__people` to store instances of the `student`, `Admin`, and `Prof` classes, enforcing **data encapsulation**.
* **Adding People:** The `display_addperson()` method adds new instances (polymorphically accepting any object derived from `college`) to the internal list.
* **Display:** The `display_people()` method iterates through the list and calls the **polymorphic** `person.get_detail()` method on each object to print their information.
* **Class Method:** It includes a **class method** `collegenames()` to access and display the class-level attribute `collegename`.

#### **4. Interactive Menu**
* The main part of the script runs an infinite `while True` loop to present a **command-line interface (CLI)**.
* Users can choose to register a new Student, Professor, or Admin (options 1, 2, 3), display all registered people (option 4), or exit the application (option 5).
* The appropriate class is instantiated based on the user's choice and added to the `universtiy` instance.
