

# Despliegue de la infraestructura

Para realizar el despliegue de la infraestructura de este proyecto, se debe ejecutar el siguiente comando:

1) Clone este repositorio
```bash
git clone 
```
2) Cree su propio repositorio en github
3) Cambie el origen del repositorio clonado
```bash
git remote set-url origin
```
3) Agregue variables de entorno para github actions del usuario IAM de AWS con permisos necesarios para crear pilas de cloudFormation, backend de S3, roles de IAM, Lambda, API Gateway, CloudWatch. 

```bash
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
```

4) Realice el push a su repositorio en github en la rama main
```bash
git push -u origin main
```
Esto desplegará la infraestructura en AWS y creará el backend de S3 para el proyecto.
Ademas, creará un pipeline de github actions que se encargará de desplegar la aplicación en AWS Lambda y API Gateway.
Este pipeline se ejecutará cada vez que se realice un push a la rama main, dicho pipeline se encuentra en el archivo 
```bash
.github/workflows/main.yml
```
En el detalle del pipeline podra ver la url de la API Gateway creada, la cual se puede utilizar para realizar las pruebas de la aplicación.


# Deploy del frontend en docker localmente

Para realizar el deploy del frontend, se debe ejecutar el siguiente comando:

1) Ingrese a la terminal de su equipo y dirijase a la carpeta frontApp
```bash
cd frontApp
```
2) Relice el build de la imagen de docker
```bash
 docker build -t tecnical-test .
```
3) Ejecute el contenedor de docker
```bash
docker run -d -v $(pwd)/src:/var/www/html  --name tecnical-test -e TZ=UTC -p 8080:80 tecnical-test
```

# Deploy del frontend en docker en AWS ECS

Para realizar el deploy del frontend en AWS ECS, se debe ejecutar el siguiente comando:

1) Cree un repositorio de ECR en AWS tecnicaltest
2) Cree un repositorio de ECS en AWS tecnicaltest
3) Creete task definition en AWS tecnicaltest
4) Creete service en AWS tecnicaltest
