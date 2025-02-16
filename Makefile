all:
	docker build -t my-fastapi-app .
	docker run -d --env-file ./.env --name my_fast_docker -p 8000:8000 -v ~/logs:/app/logs my-fastapi-app

logs:
	cat ~/logs/app.log
	docker logs my_fast_docker

clean:
	-@docker stop my_fast_docker    
	-@docker rm my_fast_docker    


fclean: clean
	@docker system prune -af

re: clean all

.Phony: all logs clean fclean