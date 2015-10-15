# on_corp.py

This condition expects there to be a URL with a plist that returns the following if the Mac is on the corporate network:

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>response</key>
    <string>active</string>
</dict>
</plist>
```

If the client recieves the above plist, the ``on_corp`` conditon will be set to ``True``. If the client receieves a HTTP error or cannot access the URL at all, ``on_corp`` will be set to ``False``.