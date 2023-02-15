# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._role_assignment_schedules_operations import build_get_request, build_list_for_scope_request

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class RoleAssignmentSchedulesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.authorization.v2020_10_01.aio.AuthorizationManagementClient`'s
        :attr:`role_assignment_schedules` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self, scope: str, role_assignment_schedule_name: str, **kwargs: Any
    ) -> _models.RoleAssignmentSchedule:
        """Get the specified role assignment schedule for a resource scope.

        :param scope: The scope of the role assignment schedule. Required.
        :type scope: str
        :param role_assignment_schedule_name: The name (guid) of the role assignment schedule to get.
         Required.
        :type role_assignment_schedule_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleAssignmentSchedule or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2020_10_01.models.RoleAssignmentSchedule
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-10-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-10-01"))
        cls: ClsType[_models.RoleAssignmentSchedule] = kwargs.pop("cls", None)

        request = build_get_request(
            scope=scope,
            role_assignment_schedule_name=role_assignment_schedule_name,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("RoleAssignmentSchedule", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/{scope}/providers/Microsoft.Authorization/roleAssignmentSchedules/{roleAssignmentScheduleName}"
    }

    @distributed_trace
    def list_for_scope(
        self, scope: str, filter: Optional[str] = None, **kwargs: Any
    ) -> AsyncIterable["_models.RoleAssignmentSchedule"]:
        """Gets role assignment schedules for a resource scope.

        :param scope: The scope of the role assignments schedules. Required.
        :type scope: str
        :param filter: The filter to apply on the operation. Use $filter=atScope() to return all role
         assignment schedules at or above the scope. Use $filter=principalId eq {id} to return all role
         assignment schedules at, above or below the scope for the specified principal. Use
         $filter=assignedTo('{userId}') to return all role assignment schedules for the current user.
         Use $filter=asTarget() to return all role assignment schedules created for the current user.
         Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either RoleAssignmentSchedule or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.authorization.v2020_10_01.models.RoleAssignmentSchedule]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-10-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-10-01"))
        cls: ClsType[_models.RoleAssignmentScheduleListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_for_scope_request(
                    scope=scope,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list_for_scope.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("RoleAssignmentScheduleListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_for_scope.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleAssignmentSchedules"}
