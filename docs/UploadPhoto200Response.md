# UploadPhoto200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**UploadPhoto200ResponseData**](UploadPhoto200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.upload_photo200_response import UploadPhoto200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UploadPhoto200Response from a JSON string
upload_photo200_response_instance = UploadPhoto200Response.from_json(json)
# print the JSON string representation of the object
print(UploadPhoto200Response.to_json())

# convert the object into a dict
upload_photo200_response_dict = upload_photo200_response_instance.to_dict()
# create an instance of UploadPhoto200Response from a dict
upload_photo200_response_from_dict = UploadPhoto200Response.from_dict(upload_photo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


