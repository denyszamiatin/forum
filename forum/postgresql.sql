create database forum ENCODING 'UTF8' LC_COLLATE = 'uk_UA.UTF-8' LC_CTYPE = 'uk_UA.UTF-8';
create user forum_user password '1';
grant all privileges on database forum to forum_user;