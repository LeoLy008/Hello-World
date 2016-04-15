# GFM
GFM is stand for: GitHub Flavored Markdown. It differ from standard Markdown(SM), add some additonal functionality.

[GitHub GFM introduce](https://help.github.com/articles/github-flavored-markdown/)
[GitHub all markup](https://github.com/github/markup)

## 段内的换行 2016-01-20
直接回车不会被视为是新行，需要使用至少两个连续的空格+回车表示段内的新行  
**直接回车**
，不同的行生成单个`<a>`标签的html  
**两个连续的空格+回车**
表示段内的新行，生成独立的`<br>`标签的html  

**GFM 改进了这个问题，每个回车都会被转换为一个`<br>`标签**


## quote contents
"> " started contents is the quote contents like this
> Attitude is everything.

## strikethrough
use "~~text~~" express strikethrough text

## code block
standard Markdown converts text with for spaces at the beginning of each line into a code block; GFM can use **```** to indicate a code block start, do not need to indent it by four spaces, but need a preceded blank line.

### syntax highlight
add syntax hightlighting by add optional language identifier after **```** as **```golang**

- bellow is a golang code snip

```golang
package main
import "fmt"

func main() {
  fmt.Printf("Hello, golang!\n")
}
```

## Tables
create table like this:

First Header | Second Header | Third Header
---:|:-----------:|----
 FH1 | SH1 | TH1
 FH2 | SH2 | TH2

use ```:``` at the header row to define text aligned:
- default left-aligned
- ```|:----|``` left-aligned
- ```|----:|``` right-aligned
- ```|:---:|``` center-aligned
