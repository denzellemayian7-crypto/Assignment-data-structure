2.	Research where the data structures types are applied and give reasons why.

1.	LINEAR DATA STRUCTURES
1.1	Array
Applications:
                           •  Storing student marks in a system
                            •  Image pixel storage

                    Reasons:
•	Allows fast access using index (O(1))
•	Stores data in contiguous memory

    

1.2 Stack (LIFO – Last In First Out)
Applications:
•	Undo/Redo operations in text editors
•	Function call management (Call Stack)

     Reasons:
•	Works on Last In First Out principle
•	Easy to reverse data


                    1.3 Queue (FIFO – First In First Out)
Applications:
•	Printer job scheduling
•	CPU task scheduling

Reasons:
•	Processes tasks in order of arrival
•	Prevents starvation of earlier tasks

1.4 Linked List
Applications:
•	Music playlist management
•	Dynamic memory allocation


                    Reasons:
•	Dynamic size (no fixed memory)
•	Easy insertion and delete



2.	NON-LINEAR DATA STRUCTURES
2.1 Tree
Applications:
•	File system directories (folders & subfolders)
•	Database indexing (B-trees, BST)

Reasons:
•	Represents hierarchical relationships
•	Fast searching and sorting



                      2.2 Graph
                       Applications:
•	Social media networks (Facebook friends, Instagram followers)
•	Road maps and GPS navigation

Reasons:
•	Models relationships between entities
•	Handles complex connections



   
               3. Give examples of applications that are using the data structure type and algorithm .
                      Give reasons why
                            
                       1. Google Maps (Navigation System)
Data Structure Type:
•	Graph
Algorithm:
•	Dijkstra’s Algorithm (Shortest Path Algorithm)
Reason:
•	Roads and intersections are represented as nodes and edges in a graph.
•	Dijkstra’s algorithm finds the shortest and fastest route between two locations.
•	This reduces travel time and fuel consumption for users.
   

 
2.	Web Browser (Chrome / Firefox)

Data Structure Type:
•	Stack

Algorithm:
•	Backtracking Algorithm (Undo/Redo Navigation)
Reason:
•	Stack follows the Last In First Out (LIFO) principle.
•	It allows users to go back to the previously visited webpage.
•	Efficient for handling browser history and navigation.



3. Banking System (ATM / Online Banking)
Data Structure Type:

•	Tree (B-Tree / Binary Search Tree)
Algorithm:
•	Searching Algorithm (Binary Search)
Reason:
•	Customer account records are stored in trees for fast access.
•	Searching algorithms quickly locate customer information.
•	This ensures fast, accurate, and secure transactions.

       Conclusion
        These applications use appropriate data structures and algorithms because they:

•	Organize data efficiently
•	Improve speed and performance
•	Solve real-world problems effectively
•	Provide reliable and accurate results


 
             4.Research how data structures and algorithms work within systems
1. Introduction

Data structures and algorithms are the foundation of all computer systems. Data structures provide a way to organize and store data efficiently, while algorithms define the steps used to process that data. Together, they ensure that systems operate correctly, quickly, and with minimal resource usage.

2. Role of Data Structures in Systems

Data structures determine how data is stored and accessed inside a system. Different systems use different structures based on their needs:

Operating Systems: use queues for process scheduling, stacks for function calls, and linked lists for memory management.

Database Systems: use trees (such as B-trees) and hash tables for fast searching and indexing of records.

File Systems: use tree structures to represent directories and files.

Network Systems: use queues to manage data packets and graphs to model network connections.

These structures allow systems to handle large amounts of data efficiently and in an organized manner.

3. Role of Algorithms in Systems

Algorithms are procedures that manipulate and process data stored in data structures. They control operations such as searching, sorting, inserting, deleting, and updating data.

Examples include:

Searching algorithms (binary search, hash lookup) to find data quickly.

Sorting algorithms (merge sort, quick sort) to organize data.

Scheduling algorithms (round robin, priority scheduling) to manage CPU processes.

Routing algorithms (Dijkstra’s algorithm) to determine the shortest path in networks.

Algorithms ensure systems make correct decisions and perform tasks efficiently.

4. Interaction Between Data Structures and Algorithms

Data structures and algorithms work together as a unit:

Data structures store and organize information.

Algorithms operate on that information to solve problems.

For example:

A graph stores a road network, while Dijkstra’s algorithm finds the shortest route.

A queue stores processes waiting for execution, while a scheduling algorithm selects which process runs next.

A tree stores database records, while a search algorithm retrieves specific data.

Choosing the correct data structure improves the performance of the algorithm and the entire system.

5. Use in Major System Components
a) Operating Systems

Data Structures: Stack, Queue, Linked List

Algorithms: CPU scheduling, memory allocation

Function: Manage processes, memory, and hardware resources.

b) Database Systems

Data Structures: B-trees, Hash tables

Algorithms: Searching and indexing

Function: Enable fast data storage and retrieval.

c) Network Systems

Data Structures: Graphs, Queues

Algorithms: Routing and packet scheduling

Function: Ensure efficient data transmission.

d) Application Software

Data Structures: Arrays, Lists, Trees

Algorithms: Sorting, searching, recommendation algorithms

Function: Provide responsive and accurate user services.

6. Impact on System Performance

Data structures and algorithms influence:

Speed (time complexity): how fast a system responds.

Memory usage (space complexity): how efficiently memory is used.

Scalability: ability to handle more data and users.

Reliability: accuracy and consistency of operations.

Efficient choices reduce processing time and prevent system overload.

7. Conclusion

Data structures and algorithms are essential to the functioning of computer systems. Data structures organize data, while algorithms process and manipulate it. Together, they allow systems such as operating

