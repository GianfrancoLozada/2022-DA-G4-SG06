const express = require('express');
const jwt = require('jsonwebtoken');
const appRouter = express.Router();

const con = require("../config/connection");

const bodyParser = require("body-parser");
appRouter.use(bodyParser.urlencoded({extended:true}));
appRouter.use(bodyParser.json());

let sql_all = 'CALL P_get()';
let sql_insert = 'CALL P_post(?,?,?)';
let sql_modify = 'CALL P_put(?,?,?,?)';
let sql_delete = 'CALL P_delete(?)';

function verifyToken(req,res,next){
	const bearerHeader = req.headers['authorization'];
	if(typeof bearerHeader !== 'undefined'){
		const bearerToken = bearerHeader.split(" ")[1];
		req.token = bearerToken;
        next();
	}else{
		res.sendStatus(403);
	}
};

appRouter.link("/score",(req,res) => {
    const user = {
        id: 1,
        nombre: 'Rodrigo'
    }
    jwt.sign({user},'secretkey',{expiresIn:'45s'},(err, token) => {
        res.json({
            token
        })
    });
})


appRouter.get('/score', verifyToken, (req,res) => {
    con.query(sql_all,(error,results) => {
        if(error) {
            throw error;
        }
        var respuesta = results;
        jwt.verify(req.token, 'secretkey', (error, authData) => {
            if(error) res.sendStatus(403);
            res.send(respuesta);
        });
    })
});

appRouter.post('/score', (req,res) => {
    const book = {
        Us : req.body.Usuario,
        MJ : req.body.ModoJuego,
        Pu : req.body.Puntaje
    }
    con.query(sql_insert,[book.Us,book.MJ,book.Pu],(error,results)=>{
        if(error) throw error;
        res.send(results);
    })
});

appRouter.put('/score', verifyToken, (req,res) => {
    const score ={
        ID : req.body.ID,
        Us : req.body.Usuario,
        MJ : req.body.ModoJuego,
        Pu : req.body.Puntaje
    }
    con.query(sql_modify,[score.ID,score.Us,score.MJ,score.Pu],(error,results)=>{
        if(error) throw error;
        var respuesta = results;
        jwt.verify(req.token, 'secretkey', (error, authData) => {
            if(error) res.sendStatus(403);
            res.send(respuesta);
        });
    })
});

appRouter.delete('/score', (req,res) => {
    const score ={
        ID : req.body.ID
    }
    con.query(sql_delete,[score.ID],(error,results)=>{
        if(error) throw error;
        res.send(results);
    })
});

module.exports=appRouter;