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
This is also called the "shadow" variable cd

Now the following is to show how to navigate to the outside of the work space, suppose we have the following folder structure:\
Products\MyProuct\Module\Input\config.ini \
Products\MyProuct\Module\Output\ \
ToolKit\MyTool\tool.exe
Our workspace is of course in MyProduct, how do we run tool.exe?
```batch
    cd ..\..\tool.exe --inputFilePath Module\Input  --output Module\Output
```
Let the tool be able to config from and output result to our file systems. 

### bit flag
boolean variables consume 1 byte of memory but all we need is just 1 bit. Observe the following example:
```c++
	
unsigned char options;

enum Options {
  OpAutoRedraw    = 0x01,
  OpAntiAlias     = 0x02,
  OpPixelShader   = 0x04,
  OpVertexShader  = 0x08,
  OpFullscreen    = 0x10,
  OpDaylight      = 0x20,
  Opfocus         = 0x40;
  OpOthers        = 0x80;
};

// 0x01 ==   1 == "00000001"
// 0x02 ==   2 == "00000010"
// 0x04 ==   4 == "00000100"
// 0x08 ==   8 == "00001000"
// 0x10 ==  16 == "00010000"
// 0x20 ==  32 == "00100000"
// 0x40 ==  64 == "01000000"
// 0x80 == 128 == "10000000"

//Manipulate relationship
options = OpAutoRedraw | OpVertexShader | OpFullscreen;
// options == 0x01 | 0x08 | 0x10 == "00011001" 

if (options & OpAutoRedraw) {} // true
if (options & OpAntiAlias) {} // false 
```
Additional reading [read me](https://blog.podkalicki.com/bit-level-operations-bit-flags-and-bit-masks/)
