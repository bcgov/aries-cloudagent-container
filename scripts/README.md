# Rocket.Chat Incoming WebHook Scripting:

Refer to the official [Incoming WebHook Scripting](https://rocket.chat/docs/administrator-guides/integrations/) documentation for information on how to setup an incoming WebHook in Rocket.Chat.  Use one of the following scripts (or create your own) and paste it into the **Script** field associated with the WebHook integration.

## Docker Hub

The [Docker Hub WebHook Integration Script](./rocket.chat.integration.js) can be used to post notifications to a channel when new images are pushed to your Docker Hub repository.

The payload of the Docker WebHook is not well documented, a recent (2019.08.12) sample can be found here; [Docker Hub WebHook Payload Example](./DockerHubWebhookPayloadExample.json).

On the WebHook tab of your Docker Hub repository, add a new WebHook and use the generated **WebHook URL** from the Rocket.Chat integration.

## Debugging 

The [Debug WebHook Integration Script](./rocket.chat.capturepayload.js) can be used to capture sample payloads from a WebHook.  This integration script will simple print out the WebHook payload into a Rocket.Chat message.