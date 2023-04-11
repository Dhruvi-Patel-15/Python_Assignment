# Python_Assignment

### Question1
>**Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.The program should take input from console or args and should handle unexpected inputs.**<br><br>
>**Constraints:**
> - For loop is not allowed
> - input should be in words:
> - e.g.: onetwo = 12, sixone = 61
> - words will be within zero to nine
> - Cannot use inbuilt methods like max, min, or any math function <br><br>
>**Example 1:**
>- Input 1: onezero
>- Input 2: twozero
>- Output: onezero <br><br>
>**Example 2:**
> - Input 1: twosix
> - Input 2: twofour
> - Output: two

>**Approach to solve:  **<br>
> - For changing the words to numbers a function "words_to_number" is made which checks for a specific word and replaces it with the specific number.  
> - On changing the words to numbers, that string is converted to integer and passed to GCD function.  
> - The GCD of those two numbers are calculated.  
> - On getting the answer it is once again converted to words by using a function "number_to_word". 

>**Output of this Practical will be:**<br>
>https://simformsolutionspvtltd-my.sharepoint.com/:i:/r/personal/dhruvi_p_simformsolutions_com/Documents/Python_Assignment/P1.png?csf=1&web=1&e=eHIglc

### Question2
>**Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.**<br><br>
>**Constraints:**
> - 1 <= n <= 8 <br><br>
>**Example 1:**
> - Input: n = 3
> - Output: ["((()))","(()())","(())()","()(())","()()()"]<br><br>
>**Example 2:**
> - Input: n = 1
> - Output: ["()"] 

>**Approach to solve:  **<br>
> - A function is created for generating parenthesis.
> - In that another function is created "backtrack".
> - By using if conditional statement the left ,right parenthesis are incremented.
> - The constraints are given and raise the valueerror for this.

>**Output of this Practical will be:**<br>
>https://simformsolutionspvtltd-my.sharepoint.com/:i:/r/personal/dhruvi_p_simformsolutions_com/Documents/Python_Assignment/P2.png?csf=1&web=1&e=CCrTr0

### Question3
>**Given an array of strings strs, group the anagrams together. You can return the answer in any order.An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.**<br><br>
>**Constraints:**
> - 1 <= strs.length <= 104
> - 0 <= strs[i].length <= 100
> - strs[i] consists of lowercase English letters.<br><br>
>**Example 1:**
> - Input: strs = ["eat","tea","tan","ate","nat","bat"]
> - Output: [["bat"],["nat","tan"],["ate","eat","tea"]]<br><br>
>**Example 2:**
> - Input: strs = [""]
> - Output: [[""]]<br><br>
>**Example 3:**
> - Input: strs = ["a"]
> - Output: [["a"]]

>**Approach to solve:  **<br>
> - The function is created "group_anagrams" amd in that empty dictionary is created.
> - After that the inputs are appended to a list.  
> - The words collected in list is sorted and stored as a key.  
> - The values of this dictionary is converted to list.  
> - The final list is printed as output.

>**Output of this Practical will be:**<br>
>https://simformsolutionspvtltd-my.sharepoint.com/:i:/r/personal/dhruvi_p_simformsolutions_com/Documents/Python_Assignment/P3.png?csf=1&web=1&e=FFBwhH
