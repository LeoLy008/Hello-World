#!/bin/bash
aaa=1
bbb=${aaa}
: ${aaa?"aaa not set!!!"}
: ${bbb:?"bbb is declare but is null!"}

ccc=
echo "ccc=${ccc} + ${ccc+"abc"}"
echo "ccc=${ccc} :+ ${ccc:+"def"}"

: ${abc=123} # if abc is not define, set abc=123, else do nothing
echo "abc=${abc}"
abd=1
: ${abd:=123} # if abc is not define or abc is null, set abc=123, else do nothing
echo "abd=${abd}"
