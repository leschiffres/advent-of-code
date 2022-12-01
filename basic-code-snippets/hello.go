package main

import (
    "fmt"
    "os"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {
    fmt.Println("Hello, World!")

    dat, err := os.ReadFile("file2.txt")
    check(err)
    fmt.Print(string(dat))
}