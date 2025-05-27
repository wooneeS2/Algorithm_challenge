### 2025-05-26

Today, I solved this problem.
I figured out the main logic, 

but I didn’t consider some edge cases — like when the flowerbed’s length is 1, or when the first or last place is empty.

That’s why I struggled with this quiz!!!



In the end, I used the ?? logical operator.
Also, I missed the i++ part after planting a flower.

If I don’t do i++, it checks the next spot even though it’s no longer valid.



I feel so tired...



<h2><a href="https://leetcode.com/problems/can-place-flowers">605. Can Place Flowers</a></h2><h3>Easy</h3><hr><p>You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in <strong>adjacent</strong> plots.</p>

<p>Given an integer array <code>flowerbed</code> containing <code>0</code>&#39;s and <code>1</code>&#39;s, where <code>0</code> means empty and <code>1</code> means not empty, and an integer <code>n</code>, return <code>true</code>&nbsp;<em>if</em> <code>n</code> <em>new flowers can be planted in the</em> <code>flowerbed</code> <em>without violating the no-adjacent-flowers rule and</em> <code>false</code> <em>otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> flowerbed = [1,0,0,0,1], n = 1
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> flowerbed = [1,0,0,0,1], n = 2
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= flowerbed.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>flowerbed[i]</code> is <code>0</code> or <code>1</code>.</li>
	<li>There are no two adjacent flowers in <code>flowerbed</code>.</li>
	<li><code>0 &lt;= n &lt;= flowerbed.length</code></li>
</ul>
