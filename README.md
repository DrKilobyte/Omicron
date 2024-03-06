# Omicron
Omicron is an esoteric (Turing-complete?) interpreted programming language written in Python.<br>
Compiled to a standalone executable with Nuitka.

## Use
Download <code>omicron.exe</code>. To run a program, open a command line and navigate into the directory containing the interpreter, and run <code>omicron.exe &lt;file&gt;</code>, where <code>&lt;file&gt;</code> is path to your <code>.omi</code> program.

## Instructions
Pointer starts at memory cell 0. Negative addresses are valid.<br>
Memory cells store either a number (integer or floating point), or <code>nil</code>.<br>
<code>nil</code> can be used in a program to test for an empty cell, erase a cell, etc.

<table>
	<tr>
		<th>Name</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>(any number)</td>
		<td>Set current memory cell</td>
	</tr>
	<tr>
		<td>!f</td>
		<td>Import program from file f and insert it into current program (pre-execution)
	</tr>
	<tr>
		<td>:n</td>
		<td>Mark position in program as n</td>
	</tr>
	<tr>
		<td>@n</td>
		<td>Get value at memory cell n (can be nested, e.g. @@@n)</td>
	</tr>
	<tr>
		<th colspan="2">Pointer</th>
	</tr>
	<tr>
		<td>&gt;</td>
		<td>Increment memory pointer</td>
	</tr>
	<tr>
		<td>&lt;</td>
		<td>Decrement memory pointer</td>
	</tr>
	<tr>
		<td>&gt;&gt; n</td>
		<td>Move memory pointer forward n</td>
	</tr>
	<tr>
		<td>&lt;&lt; n</td>
		<td>Move memory pointer back n</td>
	</tr>
	<tr>
		<td>~ n</td>
		<td>Move memory pointer to n</td>
	</tr>
	<tr>
		<th colspan="2">Arithmetic</th>
	</tr>
	<tr>
		<td>++</td>
		<td>Increment current memory cell</td>
	</tr>
	<tr>
		<td>--</td>
		<td>Decrement current memory cell</td>
	</tr>
	<tr>
		<td>+ n</td>
		<td>Add n to current memory cell</td>
	</tr>
	<tr>
		<td>- n</td>
		<td>Subtract n from current memory cell</td>
	</tr>
	<tr>
		<td>* n</td>
		<td>Multiply current memory cell by n</td>
	</tr>
	<tr>
		<td>/ n</td>
		<td>Divide current memory cell by n</td>
	</tr>
	<tr>
		<td>// n</td>
		<td>Floor-divide current memory cell by n</td>
	</tr>
	<tr>
		<td>^ n</td>
		<td>Raise current memory cell to the nth power</td>
	</tr>
	<tr>
		<td>% n</td>
		<td>Divide current memory cell by n and set to the remainder</td>
	</tr>
	<tr>
		<td>\ n</td>
		<td>Set current memory cell to its nth root</td>
	</tr>
	<tr>
		<td>log n</td>
		<td>Set current memory cell to its base-n logarithm</td>
	</tr>
	<tr>
		<td>round</td>
		<td>Round current memory cell</td>
	</tr>
	<tr>
		<td>ceil</td>
		<td>Round up current memory cell</td>
	</tr>
	<tr>
		<td>floor</td>
		<td>Round down current memory cell</td>
	</tr>
	<tr>
		<td>sin</td>
		<td>Set current memory cell to its sine</td>
	</tr>
	<tr>
		<td>cos</td>
		<td>Set current memory cell to its cosine</td>
	</tr>
	<tr>
		<td>tan</td>
		<td>et current memory cell to its tangent</td>
	</tr>
	<tr>
		<td>abs</td>
		<td>Set current memory cell to its absolute value</td>
	</tr>
	<tr>
		<td>fact n</td>
		<td>Set current memory cell to n factorial</td>
	</tr>
	<tr>
		<td>rand n1 n2</td>
		<td>Set current memory cell to random number between n1 and n2 (inclusive)</td>
	</tr>
	<tr>
		<td>pi</td>
		<td>Set current memory cell to pi</td>
	</tr>
	<tr>
		<td>e</td>
		<td>Set current memory cell to e</td>
	</tr>
	<tr>
		<th colspan="2">Comparison</th>
	<tr>
		<td>eq n</td>
		<td>Set current memory cell to 1 if it is equal to n, else 0
	</tr>
	<tr>
		<td>gt n</td>
		<td>Set current memory cell to 1 if it is greater than n, else 0
	</tr>
	<tr>
		<td>gte n</td>
		<td>Set current memory cell to 1 if it is greater then or equal to n, else 0
	</tr>
	<tr>
		<td>lt n</td>
		<td>Set current memory cell to 1 if it is less than n, else 0
	</tr>
	<tr>
		<td>lte n</td>
		<td>Set current memory cell to 1 if it is lesser then or equal to n, else 0
	</tr>
	<tr>
		<td>not</td>
		<td>Set current memory cell to 1 if it is 0, else 0</td>
	</tr>
	<tr>
		<td>and n</td>
		<td>Set current memory cell to 1 if (current memory cell && n), else 0</td>
	</tr>
	<tr>
		<td>or n</td>
		<td>Set current memory cell to 1 if (current memory cell || n), else 0</td>
  	</tr>
	<tr>
		<td>xor n</td>
		<td>Set current memory cell to 1 if (current memory cell ^ n), else 0</td>
  	</tr>
	</td>
	<tr>
		<th colspan="2">Flow</th>
	</tr>
	<tr>
		<td>goto n</td>
		<td>Goto marker n</td>
	</tr>
	<tr>
		<td>qoto q n1 n2</td>
		<td>Goto marker n1 if current memory cell is equal to q, otherwise goto marker n2</td>
	</tr>
	<tr>
		<td>wait</td>
		<td>Pause program until <code>Enter</code> is pressed.</td>
	</tr>
	<tr>
		<td>stop</td>
		<td>End program</td>
	</tr>
	<tr>
		<th colspan="2">I/O</th>
	</tr>
	<tr>
		<td>input</td>
		<td>Accept an integer value (0 if none given) and sets current memory cell</td>
	</tr>
	<tr>
		<td>inputc</td>
		<td>Accept a single character (first if more than one given) and sets current memory cell to ASCII value</td>
	</tr>
	<tr>
		<td>read f n</td>
		<td>Read nth byte (zero-based) from file f and set current memory cell</td>
	</tr>
	<tr>
		<td>size f</td>
		<td>Set current memory cell to size of file f (bytes)</td>
	</tr>
	<tr>
		<td>print</td>
		<td>Print current memory cell</td>
	</tr>
	<tr>
		<td>printc</td>
		<td>Print ASCII character of current memory cell</td>
	</tr>
	<tr>
		<td>write f</td>
		<td>Write ASCII char of current memory cell to file f (truncates file)</td>
	</tr>
	<tr>
		<td>awrite f</td>
		<td>Append ASCII char of current memory cell to file f</td>
	</tr>
	<tr>
		<td>writeb f</td>
		<td>Write current memory cell to file f (binary) (truncates file)</td>
	</tr>
	<tr>
		<td>awriteb f</td>
		<td>Append current memory cell to file f (binary)</td>
	</tr>
	<tr>
		<td>mem</td>
		<td>Prints the memory tape</td>
	</tr>
</table>

## Examples
### Hello, World!
<pre>
72 printc
101 printc
108 printc printc
111 printc
44 printc
32 printc
87 printc
111 printc
114 printc
108 printc
100 printc
33 printc
</pre>
### Cat
<pre>
inputc printc
</pre>
### Truth machine
<pre>
input qoto 0 2 1 :1 print goto 1 :2
</pre>
### Pythagorean theorem
<pre>
input ^ 2 > input ^ 2 + @0 \ 2 print
</pre>
### Fibonacci sequence (with user input)
<pre>
input - 2 > 1 print > 1 print > :1 @1 + @2 print << 2 @2 > @3 ~ 0 -- qoto 0 3 2 :2 ~ 3 goto 1 :3 wait
</pre>
Alternative; only final output
<pre>
input - 2 > 1 > 1 > :1 @1 + @2 << 2 @2 > @3 ~ 0 -- qoto 0 3 2 :2 ~ 3 goto 1 :3 ~ 3 print wait
</pre>
### Binary counter ###
<pre>
:1 qoto nil 11 2
:11 < goto 4
:2 qoto 0 22 3
:22 > goto 1
:3 qoto 1 22 4
:4 qoto nil 44 5
:44 1 mem goto 1
:5 qoto 0 55 6 
:55 1 mem goto 1
:6 0 < goto 4
</pre>
