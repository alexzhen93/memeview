drop view if exists view_allcomments;

create view view_allcomments as 
	select id as comment_id, id as author_id, comment,username,email,timestamp
	from auth_user natural join posts_comment;