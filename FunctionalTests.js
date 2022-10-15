import RSL from "./RSL.js";

let source_url="http://127.0.0.1"
let source_port=":30713/"
let local_url=source_url+source_port
let func_url_list={if_exist:local_url+"is_exist"}

let main=new RSL(source_url,source_port,func_url_list)
await main.check_connecting()
