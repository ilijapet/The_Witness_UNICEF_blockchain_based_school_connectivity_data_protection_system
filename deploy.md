
Step 1
  
  cartesi build


+] Building 4.6s (22/22) FINISHED                                                                                                                                                                                                                    docker:default
 => [internal] load build definition from Dockerfile                                                                                                                                                                                                            0.0s
 => => transferring dockerfile: 1.45kB                                                                                                                                                                                                                          0.0s
 => resolve image config for docker-image://docker.io/docker/dockerfile:1                                                                                                                                                                                       1.5s
 => CACHED docker-image://docker.io/docker/dockerfile:1@sha256:fe40cf4e92cd0c467be2cfc30657a680ae2398318afd50b0c80585784c604f28                                                                                                                                 0.0s
 => [internal] load metadata for docker.io/cartesi/python:3.10-slim-jammy                                                                                                                                                                                       1.3s
 => [internal] load .dockerignore                                                                                                                                                                                                                               0.0s
 => => transferring context: 2B                                                                                                                                                                                                                                 0.0s
 => [ 2/14] ADD https://github.com/cartesi/machine-emulator-tools/releases/download/v0.14.1/machine-emulator-tools-v0.14.1.deb /                                                                                                                                1.1s
 => [internal] load build context                                                                                                                                                                                                                               0.0s
 => => transferring context: 50.09kB                                                                                                                                                                                                                            0.0s
 => [ 1/14] FROM docker.io/cartesi/python:3.10-slim-jammy@sha256:a60d99fcd98d563e633bd06d28e2be94c7da45f335691edd9cbf3a0830694638                                                                                                                               0.0s
 => CACHED [ 2/14] ADD https://github.com/cartesi/machine-emulator-tools/releases/download/v0.14.1/machine-emulator-tools-v0.14.1.deb /                                                                                                                         0.0s
 => CACHED [ 3/14] RUN dpkg -i /machine-emulator-tools-v0.14.1.deb   && rm /machine-emulator-tools-v0.14.1.deb                                                                                                                                                  0.0s
 => CACHED [ 4/14] RUN <<EOF (set -e...)                                                                                                                                                                                                                        0.0s
 => CACHED [ 5/14] RUN apt-get update  && apt-get install -y build-essential  && pip install --upgrade setuptools wheel                                                                                                                                         0.0s
 => CACHED [ 6/14] WORKDIR /opt/cartesi/dapp                                                                                                                                                                                                                    0.0s
 => CACHED [ 7/14] COPY ./requirements.txt .                                                                                                                                                                                                                    0.0s
 => CACHED [ 8/14] RUN <<EOF (set -e...)                                                                                                                                                                                                                        0.0s
 => CACHED [ 9/14] RUN apt-get install -y nano                                                                                                                                                                                                                  0.0s
 => CACHED [10/14] COPY ./utils ./utils                                                                                                                                                                                                                         0.0s
 => CACHED [11/14] COPY ./dapp.py .                                                                                                                                                                                                                             0.0s
 => CACHED [12/14] COPY ./.env .                                                                                                                                                                                                                                0.0s
 => CACHED [13/14] RUN chmod 777 ./dapp.py                                                                                                                                                                                                                      0.0s
 => CACHED [14/14] RUN chmod -R 777 ./utils                                                                                                                                                                                                                     0.0s
 => exporting to image                                                                                                                                                                                                                                          0.1s
 => => exporting layers                                                                                                                                                                                                                                         0.0s
 => => writing image sha256:fc69805119fb21dffcb8746c5e2e2eb8d7ef99ebd2e4af82608e6f3fc3fc3d99                                                                                                                                                                    0.0s

 1 warning found (use --debug to expand):
 - FromPlatformFlagConstDisallowed: FROM --platform flag should not use constant value "linux/riscv64" (line 2)
copying from tar archive /tmp/input

         .
        / \
      /    \
\---/---\  /----\
 \       X       \
  \----/  \---/---\
       \    / CARTESI
        \ /   MACHINE
         '

[INFO  rollup_http_server] starting http dispatcher service...
[INFO  rollup_http_server::http_service] starting http dispatcher http service!
[INFO  actix_server::builder] starting 1 workers
[INFO  actix_server::server] Actix runtime found; starting in Actix runtime
[INFO  rollup_http_server::dapp_process] starting dapp: python3 dapp.py


Step 2
cartesi deploy --hosting self-hosted --webapp https://sunodo.io/deploy 

? Cartesi machine templateHash 0x0e2c50f3459e8a7ba1b4890593dc4275762bcf5ab0b15f58c1eaa6ec11aa986d
? Cartesi machine templateHash 0x0e2c50f3459e8a7ba1b4890593dc4275762bcf5ab0b15f58c1eaa6ec11aa986d
Building application node Docker image...
[+] Building 4.5s (7/7) FINISHED                                                                                                                                                                                                                      docker:default
 => [internal] load build definition from DockerfileDeploy.txt                                                                                                                                                                                                  0.0s
 => => transferring dockerfile: 227B                                                                                                                                                                                                                            0.0s
 => [internal] load metadata for docker.io/cartesi/rollups-node:1.4.0                                                                                                                                                                                           2.6s
 => [internal] load .dockerignore                                                                                                                                                                                                                               0.0s
 => => transferring context: 2B                                                                                                                                                                                                                                 0.0s
 => [internal] load build context                                                                                                                                                                                                                               1.6s
 => => transferring context: 639.98MB                                                                                                                                                                                                                           1.6s
 => [1/2] FROM docker.io/cartesi/rollups-node:1.4.0@sha256:0e2e1c068dc6cd2b1183cd625f6ae7110643924dc164ff1e884c910eb3d7a805                                                                                                                                     0.1s
 => => resolve docker.io/cartesi/rollups-node:1.4.0@sha256:0e2e1c068dc6cd2b1183cd625f6ae7110643924dc164ff1e884c910eb3d7a805                                                                                                                                     0.1s
 => CACHED [2/2] COPY --chown=cartesi:cartesi . /usr/share/rollups-node/snapshot                                                                                                                                                                                0.0s
 => exporting to image                                                                                                                                                                                                                                          0.1s
 => => exporting layers                                                                                                                                                                                                                                         0.0s
 => => writing image sha256:832e5d99843add6b1161535b6922c04b874cd7c0c55b2bee6a5427583ea354ed                                                                                                                                                                    0.0s
? Application node Docker image sha256:832e5d99843add6b1161535b6922c04b874cd7c0c55b2bee6a5427583ea354ed


Step 3

fly app create cartesi-iot

Step 4

fly postgres create --initial-cluster-size 1 --name cartesi-iot-database --vm-size shared-cpu-1x --volume-size 1


automatically selected personal organization: Ilija
Some regions require a Launch plan or higher (bom, fra).
See https://fly.io/plans to set up a plan.

? Select region: Amsterdam, Netherlands (ams)
Creating postgres cluster in organization personal
Creating app...
Setting secrets on app cartesi-iot-database...
Provisioning 1 of 1 machines with image flyio/postgres-flex:16.3@sha256:6543202a303281a2be884fb49d82f3de9f3fd30389790c4150f4c861a046b01a
Waiting for machine to start...
Machine 185e640a449de8 is created
==> Monitoring health checks
  Waiting for 185e640a449de8 to become healthy (started, 3/3)
^[
Postgres cluster cartesi-iot-database created
  Username:    postgres
  Password:    GXMeC42vokXBzvN
  Hostname:    cartesi-iot-database.internal
  Flycast:     fdaa:9:a7fd:0:1::5
  Proxy port:  5432
  Postgres port:  5433
  Connection string: postgres://postgres:GXMeC42vokXBzvN@cartesi-iot-database.flycast:5432

Save your credentials in a secure place -- you won't be able to see them again!

Connect to postgres
Any app within the Ilija organization can connect to this Postgres using the above connection string

Now that you've set up Postgres, here's what you need to understand: https://fly.io/docs/postgres/getting-started/what-you-should-know/
(.venv)  device_data_integrity_system/cartesi_backend git:(live) ✗ ➜ 


Step 5

fly postgres attach cartesi-iot-database -a cartesi-iot

Checking for existing attachments
Registering attachment
Creating database
Creating user

Postgres cluster cartesi-iot-database is now attached to cartesi-iot
The following secret was added to cartesi-iot:
  DATABASE_URL=postgres://cartesi_iot:eLxZ3CHyOmvWdt9@cartesi-iot-database.flycast:5432/cartesi_iot?sslmode=disable





Step 6 => Setting secrets

fly secrets set -a cartesi-iot CARTESI_BLOCKCHAIN_HTTP_ENDPOINT=https://eth-sepolia.g.alchemy.com/v2/xxxxxxxxxxxxxxxxxxx
fly secrets set -a cartesi-iot CARTESI_BLOCKCHAIN_WS_ENDPOINT=wss://eth-sepolia.g.alchemy.com/v2/xxxxxxxxxxxxxxxxxxxxxxx
fly secrets set -a cartesi-iot CARTESI_AUTH_MNEMONIC='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
fly secrets set -a cartesi-iot CARTESI_POSTGRES_ENDPOINT=postgres://postgres:TroutHSBhvKiBRl@cartesi-iot-database.flycast:5432

Step 7

flyctl auth docker

Step 8

docker image tag fc69805119fb registry.fly.io/cartesi-iot  

Step 9

docker image push registry.fly.io/cartesi-iot

Using default tag: latest
The push refers to repository [registry.fly.io/cartesi-iot]
61ab8700700d: Pushed 
6021a0b0b4eb: Pushed 
122086df6772: Pushed 
a2aab8c3cf89: Pushed 
230bce532096: Pushed 
5c6fa7bb993c: Pushed 
53025a9e6e70: Pushed 
71bdf7e83bf3: Pushed 
b178afc35ae3: Pushed 
85152d37c991: Pushed 
d424ce7619ec: Pushed 
c0d2d3d5d071: Pushed 
b4fc001d3758: Pushed 
7ee2b85396cb: Pushed 
d79db3a9d81a: Pushed 
0a4c7757e4d0: Pushed 
1ef825697072: Pushed 
8cbddf025c7e: Pushed 
latest: digest: sha256:5d3dc7d4e61e9e7a827269b84d35564fa093a43a6cc0e78ba38fc4b9c646d871 size: 4094

Step 10

fly deploy -a cartesi-iot

==> Verifying app config
Validating /home/ilija/code/device_data_integrity_system/cartesi_backend/fly.toml
✓ Configuration is valid
--> Verified app config
==> Building image
Searching for image 'registry.fly.io/cartesi-iot' remotely...
==> Building image
Searching for image 'registry.fly.io/cartesi-iot' remotely...
Error: failed to fetch an image or build from source: image must be amd64 architecture for linux os, found riscv64 linux


