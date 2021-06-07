-- docker run --name some-mysql -p 3306:3306 -v /Users/li/Coding/docker_dir/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7.34

create database alchemy_lab CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

use alchemy_lab;

create table t_user
(
    id          int primary key auto_increment comment '无关逻辑的主键',
    username    varchar(32) not null default '' comment '用户名',
    enable      int         not null default 1 comment '1的时候可用，为0的时候账号不可用',
    create_time timestamp   not null default CURRENT_TIMESTAMP comment '创建时间'
) ENGINE = InnoDB
  CHARSET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = Compact comment ='用户表';

insert into t_user(username, enable)
values ('tom', 1),
       ('ben', 0),
       ('kitty', 1);

select * from t_user;