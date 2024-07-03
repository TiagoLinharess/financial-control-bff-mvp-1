### Title

# Crie a rede Docker personalizada
docker network create financial-control-network 

# Construa a imagem Docker
docker build -t my-financial-control-bff . 

# Execute o contêiner Flask na rede personalizada
docker run -d --name financial-control-bff --network financial-control-network -p 5000:5000 my-financial-control-bff

# Execute a outra API na mesma rede personalizada
docker run -d --name financial-control-login-mvp-1 --network financial-control-network -p 3000:3000 financial-control-login-mvp-1