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