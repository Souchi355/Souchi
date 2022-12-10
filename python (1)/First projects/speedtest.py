import speedtest

test = speedtest.Speedtest()
down = test.download()
upload = test.upload()
print(f"download speed: {down}")
print("upload speed: {upload}")
