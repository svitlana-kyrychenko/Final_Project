# Final_Project

# Date Scema

![Untitled Diagram drawio (2)](https://user-images.githubusercontent.com/102665740/173417609-521603f5-7ba6-45ad-9bb0-46775e87bed5.png)

Each table was constructed to be effective for some query.
Under each table have been written down it`s queries.
PK - Partition Key
CK - Clustering Key

# Order or run

> cd streaming
> 
> run_kafka.sh
> 
> run_messages.sh
> 
> cd ..
> 
> cd reast_api
> 
> run_cassandra.sh
> 
> read_batch_kafka.sh
> 
> cd ..
> 
> run_rest_api.sh



# Screenshots of rest api

1) Open in browser  http://localhost:8080/all_domains

![image](https://user-images.githubusercontent.com/102665740/173418914-4e70f429-cfbe-45e2-a148-36af1bf5416c.png)

2) Open in browser  http://localhost:8080/user_pages&user_id=<user_id>

![image](https://user-images.githubusercontent.com/102665740/173419331-96e45fa7-292e-49ff-9569-a5d5ef95b33d.png)

3) Open in browser  http://localhost:8080/domain_articles&domain=<domain>

![image](https://user-images.githubusercontent.com/102665740/173419525-00d05cc1-f046-4930-b393-6167097fc68d.png)
  
4) Open in browser  http://localhost:8080/page&page_id=<page_id>
  
![image](https://user-images.githubusercontent.com/102665740/173419777-62923c28-26a6-4b53-9454-14f81432908e.png)

