from gem.gem_services import gem_collection

test = gem_collection('0x5cc5b05a8a13e3fbdb0bb9fccd98d38e50f90c38')
print(test['data'][0]['name'], test['data'][0]['address'], test['data'][0]['slug'])
