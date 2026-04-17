# Window Manager Simulation – Submission

This program simulates a simple Window Manager. Each window has an ID and can be OPEN, MINIMIZED, or CLOSED. OPEN windows are kept in strict z-order (top to bottom). All operations run in O(1) time using a Dictionary and a Doubly Linked List.

## Key Points:
1. Data Structures: Dictionary + Doubly Linked List 
2. O(1) time for all operations 
3. Correct state handling for OPEN, MINIMIZED, CLOSED 
4. Maintains z-order from top to bottom

## Sample Input:
```python
if __name__ == "__main__":
	wm = WindowManager()
  
	wm.open(1)
	wm.open(2)
	wm.open(3)
	print(wm.top())


	wm.minimize(3)
	print(wm.top())


	wm.focus(1)
	print(wm.list())


	wm.restore(3)
	print(wm.list())


	wm.close(1)
	print(wm.list())
```

## Sample Output:
```text
3
2
[1, 2]
[3, 1, 2]
[3, 2]
```
