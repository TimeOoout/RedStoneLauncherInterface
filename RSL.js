import axios from "axios";

class RSL{
    constructor(src_url,src_port,src_list){
        //this.init()
        this.init(src_url,src_port,src_list)
        return 0
    }
    Src_url
    Src_port
    Src_list

    init(src_url,src_port,src_list) {
        this.Src_url=src_url
        this.Src_port=src_port
        this.Src_list=src_list
        return 0
    }

    async check_connecting() {
        const a = await this.post(this.Src_list.if_exist)
        log(a["INFO"] === 0)
        return a["INFO"] === 0
    }

    async post(url="",data=""){

        if (url!==""){
            var results;
            await axios.post(url,data).then(function (response) {
                results=response.data
                log(results)
            })
                .catch(function (error) {
                    log(error)

                })

            return results
        }else {
            throw "Parameter error:No link entered!"
        }
    }

}


function log(...obj){
    console.log(obj)
}

export default RSL;
