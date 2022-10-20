<b>What is Array?</b>

Arrays are the most commonly used data structure in Computer Programming. An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together.It falls under the category of linear data structures.And most of the algorithms and problem-solving approaches use arrays in their implementation. Arrays have a fixed size where the size of the array is defined when the array is initialized.

Two essential terminologies that are used in the array-<br>
<b>Element —</b> Each item stored in an array is called an element.<br>
<b>Index —</b> Each memory location of an element in an array is identified by a numerical index.

<br>
<b>How to create the Array?</b>

Arrays are represented in various ways in different languages. Generally, we need three things to declare an array.
<br>
<b>Data Type: </b>Data type of element you want to store in an array.
<b>Name:</b> Name of the array.
Size: Length of the array i.e. how many elements you want to store.<br>
In C language, the array is declared as<br>
<b>Syntax:</b> data_type name_of_array[size_of_array];<br>
<b>Example:</b> string cars[4];
<br>
<b>How many types of array?</b>

In the C programming language, arrays are classified into two types. They are as follows...<br>
<b>Single Dimensional Array / One Dimensional Array<br>
Multi Dimensional Array</b><br>

<b>1. Single Dimensional Array</b>

In the C programming language, single dimensional arrays are used to store a list of values of the same datatype. In other words, single dimensional arrays are used to store a row of values. In a single dimensional array, data is stored in linear form. Single dimensional arrays are also called one-dimensional arrays, Linear Arrays or simply 1-D Arrays.
<br>
<b>Declaration of Single Dimensional Array</b><br>
<b>Syntax:</b> datatype arrayName [ size ] ;<br>
<b>Example:</b> int rollNumbers [60] ;<br>
<b>Initialization of Single Dimensional Array</b><br>
<b>Syntax:</b> datatype arrayName [ size ] = {value1, value2, ...} ;<br>
<b>Example:</b> int marks [6] = { 89, 90, 76, 78, 98, 86 } ;<br>
<b>Accessing Elements of Single Dimensional Array</b><br>
<b>Syntax:</b> arrayName [ indexValue]<br>
<b>Example:</b> marks [2] = 99 ;<br>

<b>2. Multi Dimensional Array</b><br>
An array of arrays is called a multi dimensional array. In simple words, an array created with more than one dimension (size) is called a multi dimensional array. Multi dimensional array can be of two dimensional array or three dimensional array or four dimensional array or more...
 Most popular and commonly used multi dimensional array is two dimensional array. The 2-D arrays are used to store data in the form of tables. We also use 2-D arrays to create mathematical matrices.
<br>
<b>Declaration of Two Dimensional Array</b><br>
<b>Syntax:</b>datatype arrayName [ rowSize ] [ columnSize ] ;<br>
<b>Example:</b> int matrix_A [2][3] ;<br>
<b>Initialization of Two Dimensional Array</b><br>
<b>Syntax:</b> datatype arrayName [rows][colmns] = {{r1c1value, r1c2value, ...},{r2c1, r2c2,...}...} ;<br>
<b>Example:</b> int matrix_A [2][3] = { {1, 2, 3},{4, 5, 6} } ;<br>
<b>Accessing Individual Elements of Two Dimensional Array</b><br>
<b>Syntax:</b> arrayName [ rowIndex ] [ columnIndex ]<br>
<b>Example:</b> matrix_A [0][1] = 10 ;<br>

<b>How to insert elements into an array?</b><br>
To insert an element item at any position pos, we will shift the array elements from this position to one position forward and will do this for all the elements next to it.
<br>// A is an array<br>
// n is the number of elements in the array<br>
// maxSize is the size of the array<br>
// item is the element to insert<br>
// pos is position at which element will be inserted<br>
void insert(int A[], int n, int maxSize, int item, int pos)
{
    n += 1 // increasing the number of elements
    
    for(i = n; i >= pos; i--)
    {
        A[i] = A[i-1] // shift elements forward
    }
    
    A[pos-1] = item // insert item at pos
}

<b>How to delete elements into an array?</b><br>
To delete an element at any position pos, we will shift the array elements from this position to one position forward and will do this for all elements next to it.
<br>
void delete(int A[], int n, int pos)<br>
{<br>
    for( i = pos-1 to n-2 )<br>
    {<br>
        A[i] = A[i+1] // shift element backwards<br>
    }<br>
    n -= 1 // decreasing size by 1<br>
}<br>
<br>
<b>Add Problem links</b><br>
https://www.geeksforgeeks.org/top-50-array-coding-problems-for-interviews/

