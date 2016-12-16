CREATE DATABASE db_wanghong;
use db_wanghong;

CREATE TABLE Huajiao_live(
	liveId int NOT NULL,
	userId int NOT NULL,
	watches int NOT NULL default 0 comment '观看人数',
	praises int NOT NULL DEFAULT 0  COMMENT '赞数',
	reposts int NOT NULL default 0,
	replies int NOT NULL default 0,
	publishTime int NOT NULL default 0 comment '发布日期',
	title varchar(100) NOT NULL default '' comment '直播名称',
	image varchar(255) NOT NULL default '' comment '直播封面',
	location varchar(255) NOT NULL default '' comment '地点',
	scrapedTime timestamp NOT NULL comment '爬虫更新时间',
	primary key(liveId)

);

CREATE TABLE Huajiao_user(
	userId INT UNSIGNED NOT NULL,
    userName VARCHAR(255) NOT NULL DEFAULT '' COMMENT '昵称',
    level INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '等级',
    follow INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '关注数',
    followed INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '粉丝数',
    supported INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '赞数',
    experience INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '经验值',
    avatar VARCHAR(255) NOT NULL DEFAULT '' COMMENT '头像地址',
    scrapedTime timestamp NOT NULL COMMENT '爬虫时间',
    PRIMARY KEY(userId)
);