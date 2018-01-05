package main

import (
    "os"
    "net/http"
    "io"
//    "gopkg.in/cheggaaa/pb.v2"
//    "time"
    "fmt"
    "reflect"

)


func downloadFile(filepath string, url string) (err error) {

  // Create the file
  out, err := os.Create(filepath)
  if err != nil  {
    return err
  }
  defer out.Close()
  
  // count := 1000
  // bar := pb.StartNew(count)
  // Get the data
  // for i := 0; i < count; i++ {
  resp, err := http.Get(url) 
  fmt.Println(resp)
  
  if err != nil {
    return err
  }
  // bar.Increment()
  // time.Sleep(time.Millisecond * 2)
  // }
  // bar.Finish()
  defer resp.Body.Close()
//  fmt.Println(reflect.TypeOf(resp.Body))

  // Writer the body to file
  _, err = io.Copy(out, resp.Body)
  if err != nil  {
    return err
 }

  return nil
}


func main() {

downloadFile("/home/jeffrin/dollect/src/go/lfy.pdf","https://archive.org/download/Linux-For-You-Issue-78/Linux-For-You-78-2009-07.pdf")
}

