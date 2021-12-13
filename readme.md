## Project overview
Random c++ code 

bitwise trick

```c++
    bool b_selected = false; 
    bool b_exclusiveSelected;
    bool b_included = true;

    b_exclusiveSelected = (b_exclusiveSelected|b_selected)^true;
    //return inverse of b_exclusiveSelected or 1 depending on value of b_selected
    b_selected |= b_included;
    //return true or b_selected: basically it says if included then selected otherwise unselected since b_selected initialized as false;
    
```
in short a|b gives a or true. a^b gives a or a_inverse. (a|b)^true gives 1 or a_inverse. (a|b)^false gives 0 or a.....

bit shift operator <<
```c++
    //set nth-bit on
    unsighed int n;
    data |= (1UL << n); //UL : unsigned long int
    //clear nth-bit 
    data &= ~(1UL << n);
    //toggle bit
    data ^= (1UL << n);    

```

Setting variable with current path location a.k.a. work space

```batch
    SET WS=%cd%
    SET "CurrentWorkSpace=%cd%"
```
This is also called the "sadow" variable cd

Now the following is to show how to navigate to the outside of the work space, suppose we have the following folder structure:\
Products\MyProuct\Module\Input\config.ini \
Products\MyProuct\Module\Output\ \
ToolKit\MyTool\tool.exe
Our workspace is of course in MyProduct, how do we run tool.exe?
```batch
    cd ..\..\tool.exe --inputFilePath Module\Input  --output Module\Output
```
Let the tool be able to config from and output result to our file systems. 

