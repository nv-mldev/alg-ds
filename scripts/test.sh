#!/bin/bash

x=10
function first {
local x=20
    second
}
function second {
    echo "Inside Second : $x"
}

first 
second 