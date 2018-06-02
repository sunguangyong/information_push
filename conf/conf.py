CONF = {
	
		"url":{
				"auth": "https://device.api.ct10649.com:8743/iocm/app/sec/v1.1.0/login",
				"commandys": "https://device.api.ct10649.com:8743/iocm/app/cmd/v1.4.0/deviceCommands",
				"devicepost": "https://device.api.ct10649.com:8743/iocm/app/reg/v1.1.0/deviceCredentials",
				"deviceget": "https://device.api.ct10649.com:8743/iocm/app/reg/v1.1.0/deviceCredentials/",
				"deviceput": "https://device.api.ct10649.com:8743/iocm/app/dm/v1.4.0/devices/",
				"devicedelete": "https://device.api.ct10649.com:8743/iocm/app/dm/v1.4.0/devices/",
				"subscribeInfo": "https://device.api.ct10649.com:8743/iocm/app/sub/v1.2.0/subscribe"

		},

		"cert": ("/etc/nginx/cert/client.crt", "/etc/nginx/cert/client.key")
}
