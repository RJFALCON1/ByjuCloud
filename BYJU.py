token = "sl.BPm3KQDnFPe9n5lTHIfzdJ6La4-DsO3I5Kuajy4ZJ7X6Kvyab1-gPIDQ3VHdZT1CBSGrmJgxKK2ZxsuDUQpMBKes4fwyCdqbLQsO3ecrV30OoBiQ5GIjCJBiggL53sRoL1ZZGdNS72k"
import dropbox
dbx = dropbox.Dropbox(token)
fileName = "/Users/arjunrajdev/Downloads/img.png"
f = open(fileName,"rb")
dbx.files_upload(f.read(),'/CloudBYJU/img.png')