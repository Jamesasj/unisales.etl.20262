
delete from f_venda where 1=1;

f_venda 1000000 1Mb 

insert into f_venda (column1, column2, column3) 100000+2000 ;


Como eu atualizo as minhas tabelas?

Estrategias Incrementais
Incrmento controlado pelo ID
var x = (max(id)-100)

delete from f_venda where id > x; ///200

insert into f_venda (column1, column2, column3)
    select * from venda where id > x; /// 204

CRUD

Incremento Controlado Por data com update;

dt_ref = (select max(dt_criacao) from f_venda);

insert into f_venda (column1, column2, column3)     
    select * from venda where dt_criacao > dt_ref;

var res = select * from venda where dt_atualizacao > dt_ref;

update f_venda
    set column1 = res.column1,
        column2 = res.column2,
        column3 = res.column3
    from res
    where f_venda.id = res.id;

Incremento Controlado Por data com rotação;

dt_ref = (select max(dt_criacao) from f_venda);

/// creates
insert into f_venda (column1, column2, column3)
    select * from venda where dt_criacao > dt_ref;

/// updates
var res = select * from venda where dt_atualizacao > dt_ref;
delete from f_venda where id in (select id from res);
insert into f_venda (column1, column2, column3)
    select * from res;

/// deletes
var res2 = select * from venda where dt_atualizacao > dt_ref and Active=false;
delete from f_venda where id in (select id from res2);