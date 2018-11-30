# ping

tioxyorg/ping application manifests

## [Configuration](#configuration)
-----

| **Helm Value**                | **Description**                                                                                                 	    | **Type**  	|
|-----------------------------  |---------------------------------------------------------------------------------------------------------------------- |-----------	|
| **`serviceType`**             | Kubernetes Service Type                                                                                         	    | str       	|
| **`servicePort`**             | Kubernetes Service Port                                                                                       	    | int       	|
| **`image`**    	            | Image to be deployed                                                                                              	| str       	|
| **`deployPort`** 	            | Container port inside Kubernetes Deploymennt                                                                          | int       	|
| **`replicas`**                | Kubernetes Deployment replicas                                                                                    	| int       	|
| **`minCPU`**                	| Minimum CPU required                                                                                          	    | str       	|
| **`maxCPU`**                	| Maximum CPU required                                                                                           	    | str       	|
| **`minRAM`**                	| Minimum RAM required                                                                                          	    | str       	|
| **`maxRAM`**                	| Maximum CPU required                                                                                          	    | str       	|
| **`hitAppearances`**          | Environment variable HIT_APPEARANCES                                                               	                | int       	|
| **`missAppearances`**         | Environment variable MISS_APPEARANCES                                                                         	    | int       	|
| **`ingressEnabled`**          | Usage of ingress to expose service                                                               	                    | bool      	|
| **`ingressHost`**             | Requires **ingressEnabled:true** - Ingress Hostname                                                              	    | str       	|


## Example](#example)
-----

```yaml
# Service
serviceType: ClusterIP
servicePort: 80

# Deployment
image: tioxyorg/ping:latest
deployPort: 5000
replicas: 2
minRAM: 64Mi
minCPU: 100m
maxRAM: 256Mi
maxCPU: 500m

# Environment Variables
hitAppearances: 75
missAppearances: 25

# Ingress
ingressEnabled: true
ingressHost: ping.tioxy.com
```
