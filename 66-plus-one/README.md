
# Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.


## Constrain

- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading 0's.

## Example 1

```javascript
Input: digits = [9,9,9]
Output: [1,0,0,0]
Explanation: The array represents the integer 999.
Incrementing by one gives 999 + 1 = 1000.
Thus, the result should be `[1, 0, 0, 0]`..
```





### Solution: `digits = [9, 9, 9]`

| Step | Current Digits | `i` (Current Index) | Action                                       | Explanation                                                                 |
|------|----------------|---------------------|----------------------------------------------|-----------------------------------------------------------------------------|
| 1    | `[9, 9, 9]`     | 2                   | `digits[2]` is set to `0`                    | Last digit is `9`, so set it to `0` and move to the previous digit.        |
| 2    | `[9, 9, 0]`     | 1                   | `digits[1]` is set to `0`                    | Second-to-last digit is `9`, so set it to `0` and move to the previous digit. |
| 3    | `[9, 0, 0]`     | 0                   | `digits[0]` is set to `0`                    | First digit is `9`, so set it to `0`. All digits are now `0`.               |
| 4    | `[0, 0, 0]`     | -                   | Insert `1` at the start                      | Since all digits were `9`, insert `1` at the beginning to get `[1, 0, 0, 0]`. |

### Final Result
The function returns `[1, 0, 0, 0]`, which represents `999 + 1 = 1000`.

## Example 1

```javascript
Input: digits = [1,2,9]
Output: [1,0,0,0]
Explanation: The array represents the integer 999.
Incrementing by one gives 129 + 1 = 130.
Thus, the result should be `[1, 3, 0]`..
```


### Solution: `digits = [1, 2, 9]`

The array represents the integer 129. Incrementing by one gives 129 + 1 = 130. Thus, the result should be `[1, 3, 0]`.

| Step | Current Digits | `i` (Current Index) | Action                        | Explanation                                                                |
|------|-----------------|---------------------|--------------------------------|----------------------------------------------------------------------------|
| 1    | `[1, 2, 9]`    | 2                   | `digits[2]` is set to `0`     | Last digit is `9`, so set it to `0` and move to the previous digit.        |
| 2    | `[1, 3, 0]`    | 1                   | Increment `digits[1]` to `3` and stop | Second-to-last digit is `2` (not `9`), so increment it to `3` and stop. No carry required. |

### Final Result
The function returns `[1, 3, 0]`, which represents `129 + 1 = 130`.

