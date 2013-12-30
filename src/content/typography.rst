====================
Typography
====================

:date: 2013-12-30 21:32
:tags: typography, demo


Heading 1
===============

Heading 2
-----------------

Heading 3
~~~~~~~~~~~~~~~~~~~~~~

Heading 4
######################

Heading 5
++++++++++++++++++++++

Heading 6
::::::::::::::::::::::

Paragraph
-----------------

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

List
-----------------

1. List Item

   - Sub-item
   - Sub-item

2. List Item
3. List Item

Table
-----------------

+------------+------------+-----------+ 
| Header 1   | Header 2   | Header 3  | 
+============+============+===========+ 
| body row 1 | column 2   | column 3  | 
+------------+------------+-----------+ 
| body row 2 | Cells may span columns.| 
+------------+------------+-----------+ 
| body row 3 | Cells may  | - Cells   | 
+------------+ span rows. | - contain | 
| body row 4 |            | - blocks. | 
+------------+------------+-----------+

Math
-----------------

Inline math: :math:`E=mc^2`. Math block:

.. math:: \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)

Code
-----------------

.. code:: java
	
	public static boolean prime(int n) {
	  return !new String(new char[n]).matches(".?|(..+?)\\1+");
	}
