### 📘 2025-05-23 Daily Coding Log - GCD of Strings
Today, I struggled with this problem.
Because I didn’t figure out all the conditions at first.
So I tried solving it in different ways.

First, I wrote code that compares two strings — checking if they have the same letters or not. But that was a big mistake.
I didn’t understand the point of the problem.

Later, I realized that the important thing was finding the greatest common divisor (GCD) of the two strings.
So I made a GCD function and used it.

At the end, I also tried solving it without using GCD — just with a loop.
But it was slower than the GCD version.

Through this, I learned that sometimes using math functions makes the code simpler and faster.



<h2><a href="https://leetcode.com/problems/greatest-common-divisor-of-strings">1071. Greatest Common Divisor of Strings</a></h2><h3>Easy</h3><hr><p>For two strings <code>s</code> and <code>t</code>, we say &quot;<code>t</code> divides <code>s</code>&quot; if and only if <code>s = t + t + t + ... + t + t</code> (i.e., <code>t</code> is concatenated with itself one or more times).</p>

<p>Given two strings <code>str1</code> and <code>str2</code>, return <em>the largest string </em><code>x</code><em> such that </em><code>x</code><em> divides both </em><code>str1</code><em> and </em><code>str2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> str1 = &quot;ABCABC&quot;, str2 = &quot;ABC&quot;
<strong>Output:</strong> &quot;ABC&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> str1 = &quot;ABABAB&quot;, str2 = &quot;ABAB&quot;
<strong>Output:</strong> &quot;AB&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> str1 = &quot;LEET&quot;, str2 = &quot;CODE&quot;
<strong>Output:</strong> &quot;&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= str1.length, str2.length &lt;= 1000</code></li>
	<li><code>str1</code> and <code>str2</code> consist of English uppercase letters.</li>
</ul>
