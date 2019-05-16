CREATE PROCEDURE sort_users()
	SELECT username FROM auth_user ORDER BY username;