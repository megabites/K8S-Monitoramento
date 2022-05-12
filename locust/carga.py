from locust import HttpUser, task, between

class SimpleLocustTest(HttpUser):
   wait_time = between(1, 3)
   
   @task
   def get_pedido(self):
       self.client.get("/api/pedido")

  
   @task(1)
   def post_pedido(self):
     pedido = { "idusuario" : 1,
                "itensPedido":[ {"idProduto":"264621f3-1544-43fd-af43-3f61b32e9cc7",
                "quantitade":1 }]
               }
     post_pedido=self.client.post("/api/pedido",json=pedido)
