-- To create VIEW log_slug
CREATE VIEW log_arts as SELECT replace(path,'/article/','') as slug, count(*) as views
FROM log
WHERE path<>'/' AND status ='200 OK' GROUP BY path;


-- To create VIEW authors_name
CREATE VIEW author_name as SELECT authors.name as name, articles.slug as slug
FROM authors INNER JOIN articles
ON articles.author=authors.id
ORDER BY authors.id;

-- To create VIEW log_total
CREATE VIEW anals_total as SELECT Date(time), count(Date(time)) 
FROM log
GROUP BY Date(time);

-- To create VIEW log_fail
CREATE VIEW error_fail as SELECT Date(time), count(Date(time))
FROM log
WHERE status='404 NOT FOUND' GROUP BY Date(time) ORDER BY Date(time);