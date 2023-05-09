# Omicron
Omicron is an interpreted Turing-complete esoteric programming language written in Python.
## Instructions
Memory cells are zero-based.

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
		<td>:n</td>
		<td>Mark position in program as n</td>
	</tr>
	<tr>
		<td>@n</td>
		<td>Get value at memory cell n</td>
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
		<td>&amp;n</td>
		<td>Move memory pointer to n</td>
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
		<td>goto n</td>
		<td>Goto marker n</td>
	</tr>
	<tr>
		<td>qoto n1 n2</td>
		<td>Goto marker n1 if current memory cell is not zero, otherwise goto marker n2</td>
	</tr>
	<tr>
		<td>wait</td>
		<td>Pause program until <code>Enter</code> is pressed.</td>
	</tr>
	<tr>
		<td>input</td>
		<td>Accept an integer value (0 if none given) and sets current memory cell</td>
	</tr>
	<tr>
		<td>ascii</td>
		<td>Accept a single character (first if more than one given) and sets current memory cell to ASCII value</td>
	</tr>
	<tr>
		<td>print</td>
		<td>Print current memory cell</td>
	</tr>
	<tr>
		<td>char</td>
		<td>Print ASCII character of current memory cell</td>
	</tr>
	<tr>
		<td>stop</td>
		<td>End program</td>
	</tr>
</table>

## Examples
### Hello, World!
<pre>
72 char
101 char
108 char char
111 char
44 char
32 char
87 char
111 char
114 char
108 char
100 char
33 char
stop
</pre>
### Cat
<pre>
ascii char stop
</pre>
### Truth machine
<pre>
input qoto 1 2 :1 print goto 2 :2 stop
</pre>
### Pythagorean theorem
<pre>
input ^ 2 > input ^ 2 + @0 \ 2 print stop
</pre>
### Fibonacci sequence (with user input)
<pre>
input - 2 > 1 print > 1 print > :1 @1 + @2 print << 2 @2 > @3 > &0 -- qoto 2 3 :2 &3 goto 1 :3 wait stop
</pre>
