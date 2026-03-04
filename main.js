const express = require("express")
const app = express()

const PORT=3000

app.get("/sora", (req, res)=>{
    res.json({data: "sora hello"})
})

app.get("/daniel", (req, res)=>{
    res.json({data: "daniel hello"})
})

app.get("/test", (req, res)=>{
    res.json({data: "test test test"})
})
app.listen(PORT, () => { console.log("started") })

// localhost:3000/sora
// data: hello from / mcb