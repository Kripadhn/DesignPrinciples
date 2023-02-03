 Dependency Inversion Principle (DIP) - The principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions.
Problem:

In this example, the `Frontend` class depends on the `Backend` class. This violates the DIP because the high-level `Frontend` class is dependent on the low-level `Backend` class.

Solution:
In this solution, we've created an abstraction `Database` and both the `Backend` and `Frontend` classes depend on it. This adheres to the DIP, as the high-level and low-level modules are now dependent on the same abstraction.