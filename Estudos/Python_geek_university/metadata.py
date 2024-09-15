from importlib import metadata



metadata_pip = metadata.metadata('pip')
print(list(metadata_pip))

print(metadata.requires('django'))

