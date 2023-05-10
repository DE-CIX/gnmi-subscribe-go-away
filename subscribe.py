import asyncio

import grpclib.client
from grpclib.config import Configuration
import gnmi.proto
from gnmi.proto import PathElem, Encoding, SubscriptionListMode, SubscriptionMode


async def subscribe():
    channel_config = Configuration(
        _keepalive_time=120.0,
        _keepalive_timeout=30.0,
        _keepalive_permit_without_calls=True,
        _http2_max_pings_without_data=0,
        _http2_min_sent_ping_interval_without_data=120.0,
    )

    channel = grpclib.client.Channel(
        host="10.34.8.167",
        port=57400,
        ssl=None,
        config=channel_config,
    )

    stub = gnmi.proto.gNMIStub(
        channel=channel,
        metadata={
            "username": "admin",
            "password": "admin",
        },
    )

    gnmi_subscription = gnmi.proto.Subscription(
        # concrete path does not meter. This is just an arbitrary path to avoid unnecessary traffic from the device
        path=gnmi.proto.Path(elem=[PathElem(name='configure', key={}), PathElem(name='system', key={}),
                                   PathElem(name='bluetooth', key={})]),
        mode=SubscriptionMode.ON_CHANGE,
    )

    subscription_list = gnmi.proto.SubscriptionList(
        subscription=[gnmi_subscription],
        mode=SubscriptionListMode.STREAM,
        encoding=Encoding.JSON
    )
    notifications = stub.subscribe(
        iter([gnmi.proto.SubscribeRequest(subscribe=subscription_list)])
    )

    async for notification in notifications:
        # simply print the message to verify that the subscription is working
        print(notification)

loop = asyncio.get_event_loop()
loop.run_until_complete(subscribe())
