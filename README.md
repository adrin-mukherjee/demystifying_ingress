# demystifying_ingress
Supporting code for [Demystifying Kubernetes Ingress blog](https://medium.com/@adrin-mukherjee/demystifying-kubernetes-ingress-b725f9f52ebc)

Contains:
1. FastAPI based service named user_service along with Dockerfile for containerization
2. FastAPI based service named item_service along with Dockerfile for containerization
3. Essential Kubernetes manifest files which could be run using the command: "microk8s.kubectl apply -f {file-name} -n ingress-res" in the following order:
   -   user_service_deployment.yaml
   -   user_service.yaml
   -   item_service_deployment.yaml
   -   item_service.yaml
   -   ingress-definition.yaml
