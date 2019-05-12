drop view if exists view_allcomments;

create view view_allcomments as 
	select posts_comment.id as comment_id_id,comment,username,email,timestamp,
	posts_posts.id as post_id_id, caption
	from auth_user join posts_comment on auth_user.id = posts_comment.user_id
	join posts_posts on posts_comment.parentPost_id=posts_posts.id;