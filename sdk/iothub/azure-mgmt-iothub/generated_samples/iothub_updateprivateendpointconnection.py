# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.iothub import IotHubClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-iothub
# USAGE
    python iothub_updateprivateendpointconnection.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = IotHubClient(
        credential=DefaultAzureCredential(),
        subscription_id="91d12660-3dec-467a-be2a-213b5544ddc0",
    )

    response = client.private_endpoint_connections.begin_update(
        resource_group_name="myResourceGroup",
        resource_name="testHub",
        private_endpoint_connection_name="myPrivateEndpointConnection",
        private_endpoint_connection={
            "properties": {
                "privateLinkServiceConnectionState": {
                    "description": "Approved by johndoe@contoso.com",
                    "status": "Approved",
                }
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/iothub/resource-manager/Microsoft.Devices/stable/2021-07-02/examples/iothub_updateprivateendpointconnection.json
if __name__ == "__main__":
    main()
