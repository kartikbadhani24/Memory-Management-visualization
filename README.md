# Memory-Management-visualization
Sure! Here's the plain *text version* of the GitHub README file (no markdown syntax):

---

*Memory Allocation Simulator (Tkinter GUI)*

A visual simulator built with Python and Tkinter that helps understand how memory allocation works in operating systems. This project simulates classic allocation strategies like First Fit, Best Fit, Worst Fit, Buddy System, and Paging — all in an interactive and user-friendly GUI.

---

*Features:*

* Create custom memory blocks and process sizes.
* Simulate multiple memory allocation strategies:

  * First Fit
  * Best Fit
  * Worst Fit
  * Buddy System
  * Paging
* Visual representation of memory usage using ASCII bars.
* Shows statistics: Total memory, Used memory, Fragmentation, and Efficiency.
* Reset or Deallocate processes.
* Search a process to see where it is allocated.

---

*How to Run:*

1. Make sure Python 3.6 or above is installed.
2. Save the code as memory_simulator.py.
3. Run using the command:

   bash
   python memory_simulator.py
   

No external modules are required. It uses only built-in libraries like tkinter and math.

---

How It Works:

* Enter the number of memory blocks and processes.
* Enter sizes for each block and process.
* Choose an allocation strategy.
* View memory allocation, fragmentation, and efficiency in the GUI.
* Paging simulation splits each process into 100KB pages.
* You can also:

  * Reset allocations
  * Deallocate any process by ID
  * Search where a process is placed

---

*Allocation Strategies Explained:*

* First Fit: Allocates the first memory block that fits.
* Best Fit: Allocates the smallest suitable block.
* Worst Fit: Allocates the largest block available.
* Buddy System: Splits memory blocks into halves until a fit is found.
* Paging: Splits memory into fixed 100KB pages.

---

*Future Improvements:*

* Add memory compaction simulation.
* Add support for internal/external fragmentation display.
* Simulate page table mappings.
* Add dark/light mode option.

---

*Author:*
Kartikey
Uttarakhand, India

---

*License:*
This project is open-source and available under the MIT License.

---


