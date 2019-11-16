def create(path,archiveList,xFilesFactor=None,aggregationMethod=None,sparse=False,useFallocate=False):
  # Set default params
  if xFilesFactor is None:
    xFilesFactor = 0.5
  if aggregationMethod is None:
    aggregationMethod = 'average'

  #Validate archive configurations...
  validateArchiveList(archiveList)

  #Looks good, now we create the file and write the header
  if os.path.exists(path):
    raise InvalidConfiguration("File %s already exists!" % path)
  fh = None
  try:
    fh = open(path,'wb')
    if LOCK:
      fcntl.flock( fh.fileno(), fcntl.LOCK_EX )

    aggregationType = struct.pack( longFormat, aggregationMethodToType.get(aggregationMethod, 1) )
    oldest = max([secondsPerPoint * points for secondsPerPoint,points in archiveList])
    maxRetention = struct.pack( longFormat, oldest )
    xFilesFactor = struct.pack( floatFormat, float(xFilesFactor) )
    archiveCount = struct.pack(longFormat, len(archiveList))
    packedMetadata = aggregationType + maxRetention + xFilesFactor + archiveCount
    fh.write(packedMetadata)
    headerSize = metadataSize + (archiveInfoSize * len(archiveList))
    archiveOffsetPointer = headerSize

    for secondsPerPoint,points in archiveList:
      archiveInfo = struct.pack(archiveInfoFormat, archiveOffsetPointer, secondsPerPoint, points)
      fh.write(archiveInfo)
      archiveOffsetPointer += (points * pointSize)

    #If configured to use fallocate and capable of fallocate use that, else
    #attempt sparse if configure or zero pre-allocate if sparse isn't configured.
    if CAN_FALLOCATE and useFallocate:
      remaining = archiveOffsetPointer - headerSize
      fallocate(fh, headerSize, remaining)
    elif sparse:
      fh.seek(archiveOffsetPointer - 1)
      fh.write('\x00')
    else:
      remaining = archiveOffsetPointer - headerSize
      chunksize = 16384
      zeroes = '\x00' * chunksize
      while remaining > chunksize:
        fh.write(zeroes)
        remaining -= chunksize
      fh.write(zeroes[:remaining])

    if AUTOFLUSH:
      fh.flush()
      os.fsync(fh.fileno())
  finally:
    if fh:
      fh.close()