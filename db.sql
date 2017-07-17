CREATE TABLE users(uid BIGINT UNIQUE PRIMARY KEY, username varchar(32));
CREATE TABLE groups(gid BIGINT UNIQUE PRIMARY KEY , maxmsg TINYINT NOT NULL DEFAULT 5 , maxlease REAL(1,1) DEFAULT 3.5 , pardon REAL(1,1) DEFAULT 0.2);
CREATE TABLE whitelist(gid BIGINT REFERENCES groups(gid), uid BIGINT REFERENCES users(uid));
CREATE TABLE admins (gid BITINT REFERENCES groups(id), uid BIGIN REFERENCES users(uid));
CREATE TABLE banlist(gid,BIGINT REFERENCES groups(gid),uid BIGINT REFERENCES users(uid));
CREATE TABLE botlist(gid,BIGINT REFERENCES groups(gid),botId BIGINT);
