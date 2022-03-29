class MirianDB {
  constructor(url){
    if (url !== void 0){
      this.url = String(url)
      const existBar = (this.url.slice(this.url.length-1,this.url.length) == "/" ? true :false)
      if (existBar == true){
        this.url = String(this.url).slice(0,this.url.length-1)
      }
    }
  }

  read(calback){
    if (calback !== void 0)
      fetch(this.url+"/read-database",{method:"GET"}).then(
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
      }).catch(() => {
        throw Error("ERROR IN TRY FETCH")
      })
  }

  write(object,calback){
    if (object !== void 0 && calback !== void 0)
      fetch(this.url+`/write-database/?value=${JSON.stringify(object)}`,{method:"GET"}).then(
        (data) => {
          return data.json()
        }
      ).then((value) => {
        if (value.writed === true){
          calback(value)
        } else {
          throw Error("Not Possible Write Values")
        }
      }).catch(() => {
        throw Error("ERROR IN TRY FETCH")
      })
  }
}