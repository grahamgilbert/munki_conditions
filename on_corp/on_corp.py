#!/usr/bin/python

import urllib2
import os
import plistlib
import errno
from Foundation import CFPreferencesCopyAppValue


# Address that should be available when the device is on coprporate network
target = 'https://yourcorportateresource.com/somewhere.plist'

def check_connectivity():
    req = urllib2.Request(target)
    try:
        resp = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        return False
    except urllib2.URLError as e:
        return False
    else:
        # 200
        body = resp.read()

        try:
            result = plistlib.readPlistFromString(body)
        except:
            return False

        if result['response'] == 'active':
            return True
        else:
            return False
        

def main():

    # Read the location of the ManagedInstallDir from ManagedInstall.plist
    BUNDLE_ID = 'ManagedInstalls'
    pref_name = 'ManagedInstallDir'
    managedinstalldir = CFPreferencesCopyAppValue(pref_name, BUNDLE_ID)
    # Make sure we're outputting our information to "ConditionalItems.plist"
    conditionalitemspath = os.path.join(managedinstalldir, 'ConditionalItems.plist')

    results_dict = {}

    results_dict['on_corp'] = check_connectivity()

    if os.path.exists(conditionalitemspath):
        # "ConditionalItems.plist" exists, so read it FIRST (existing_dict)
        existing_dict = plistlib.readPlist(conditionalitemspath)
        # Create output_dict which joins new data generated in this script with existing data
        output_dict = dict(existing_dict.items() + results_dict.items())
    else:
        # "ConditionalItems.plist" does not exist,
        # output only consists of data generated in this script
        output_dict = results_dict

    # Write out data to "ConditionalItems.plist"
    plistlib.writePlist(output_dict, conditionalitemspath)

if __name__ == '__main__':
    main()