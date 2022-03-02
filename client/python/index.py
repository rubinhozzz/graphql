from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# transport = AIOHTTPTransport(url="https://countries.trevorblades.com/")
token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjA5NzI5QTkyRDU0RDlERjIyRDQzMENBMjNDNkI4QjJFIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2NDU3ODY0NzIsImV4cCI6MTY0NTg3Mjg3MiwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5uZXhhci5jb20iLCJjbGllbnRfaWQiOiI0MmFmNzVkZi03OGZkLTRlOWQtYTQ2Ny1jMDA2YzgxNThlYjIiLCJzdWIiOiJCQzMwMkUzMS1CODc4LTQ1N0ItODg1RC1EMEQxNDk5ODQxNDMiLCJhdXRoX3RpbWUiOjE2NDU3ODQwNDUsImlkcCI6ImxvY2FsIiwianRpIjoiNUVGOEQ1NEUyRDZDQUMyRTY1RjE4QzNFRTQ5MThGNDkiLCJzaWQiOiJFMzlCQkQ4RjlDRDJGQTc1QzY0ODM0Qzg1Mjg3RkIzMyIsImlhdCI6MTY0NTc4NjQ3Miwic2NvcGUiOlsib3BlbmlkIiwidXNlci5hY2Nlc3MiLCJwcm9maWxlIiwiZW1haWwiLCJ1c2VyLmRldGFpbHMiLCJzdXBwbHkuZG9tYWluIiwiZGVzaWduLmRvbWFpbiJdLCJhbXIiOlsicHdkIl19.XZgKMXg_rrjWRbU52pnn2v3svNK-KyWaVEqvI7DJ5pjSfX3PNa7tmjSTwddhCHj4-cpwAkiz1GWa9hpJXBhycygJMYafSIBSNPinksaJqXN_ZHcknbokgSzidJRDgzgcOXF0Esk4CbYAUz6F0E7o-va5yNhu9eCIhLFfWRwU9uRRWY84yHdT5nckIND5J8tN_RTletrTchjCubsjaIu5ngAt5uP2YRDfsSmFmNSOztbFi3qElRMMyOe_MkWNNJas1gPteYYLiaf1SayTI4vVTc7UXYunCob8-5aEqySf-gwrV2Jk6QB7iYkuZTAue-DyFMg-uoo-3RmqOAESoq4r2A'
transport = AIOHTTPTransport(url="https://api.nexar.com/graphql/", headers={'token': token})

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
"""
query WorkspacesById($id: ID!) {
  desWorkspaceById(id: $id) {
        id
        url
        name
      projects {
        id
        url
        name
        design 
        {
         releases
         {
            nodes
            {
                id
                variants
                {
                    pcbAssembly
                    {
                        pickAndPlace
                        {
                            pickAndPlaceFiles
                            {
                                fileName
                                relativePath
                                downloadUrl
                            }
                            packageName
                            downloadUrl

                        }
                    }
                }
            }
         }
         workInProgress
         {
             variants
             {
                name
                bom
                {
                    bomItems
                    {
                        component
                        {
                            id
                            name
                            comment
                            description
                            manufacturerParts
                            {
                                octopartId
                                companyName
                                partNumber
                                priority
                            }
                            details
                            {
                                parameters
                                {
                                    name
                                    value
                                    type
                                }
                            }
                        }
                        quantity
                        bomItemInstances
                        {
                            designator
                        }
                    }
                }
             }
         }
        }
      }
  }
}
"""
)

# Execute the query on the transport
id = "RGVzV29ya3NwYWNlCmRiNDkyOWY4Ny03NzI5LTRmMjAtYTU5Mi1kNmY4NjZjNWFmMjQ="
result = client.execute(query, variable_values={'id': id})
print(result)