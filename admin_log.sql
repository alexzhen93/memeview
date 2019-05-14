DROP TRIGGER IF EXISTS user_creation;
DROP TRIGGER IF EXISTS user_post;
DROP TRIGGER IF EXISTS user_post_delete;

DELIMITER //
CREATE  TRIGGER user_creation AFTER INSERT ON auth_user 
	FOR EACH ROW BEGIN
		INSERT INTO posts_adminlog VALUES(id, CONCAT('New user ', NEW.username, ' was created'), CURRENT_TIMESTAMP);
	END//
DELIMITER ;

DELIMITER //
CREATE  TRIGGER user_post AFTER INSERT ON posts_posts 
	FOR EACH ROW BEGIN
		INSERT INTO posts_adminlog VALUES(id, CONCAT('Author ', NEW.author_id, ' posted with caption ', NEW.caption), CURRENT_TIMESTAMP);
	END//
DELIMITER ;

DELIMITER //
CREATE  TRIGGER user_post_delete AFTER DELETE ON posts_posts 
	FOR EACH ROW BEGIN
		INSERT INTO posts_adminlog VALUES(id, CONCAT('Author ', OLD.author_id, ' deleted with caption: ', OLD.caption), CURRENT_TIMESTAMP);
	END//
DELIMITER ;