class MirianDB {
  constructor(url){
    if (url !== void 0){
      this.url = url
    }
  }

  read(calback){
    if (calback !== void 0)
      fetch(this.url+"/read-database").then(
        (data) => {
          return data.json()
        }
      ).then((value) => {
        // console.log(value)
        if (value.error == false){
          calback(JSON.parse(value.values))
        } else {
          throw Error("Not Possible Get Values")
        }
      })
  }

  write(object,calback){
    if (object !== void 0 && calback !== void 0)
      fetch(this.url+`/write-database?value=${JSON.stringify(object)}`).then(
        (data) => {
          return data.json()
        }
      ).then((value) => {
        if (value.writed === true){
          calback(value)
        } else {
          throw Error("Not Possible Write Values")
        }
      })
  }
}