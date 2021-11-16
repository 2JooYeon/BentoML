"""
This type stub file was generated by pyright.
"""

import typing
from typing import Optional, Text, Union

from .base import FS
from .walk import Walker

"""Function for *mirroring* a filesystem.

Mirroring will create a copy of a source filesystem on a destination
filesystem. If there are no files on the destination, then mirroring
is simply a straight copy. If there are any files or directories on the
destination they may be deleted or modified to match the source.

In order to avoid redundant copying of files, `mirror` can compare
timestamps, and only copy files with a newer modified date. This
timestamp comparison is only done if the file sizes are different.

This scheme will work if you have mirrored a directory previously, and
you would like to copy any changes. Otherwise you should set the
``copy_if_newer`` parameter to `False` to guarantee an exact copy, at
the expense of potentially copying extra files.

"""
if typing.TYPE_CHECKING: ...

def mirror(
    src_fs: Union[FS, Text],
    dst_fs: Union[FS, Text],
    walker: Optional[Walker] = ...,
    copy_if_newer: bool = ...,
    workers: int = ...,
) -> None:
    """Mirror files / directories from one filesystem to another.

    Mirroring a filesystem will create an exact copy of ``src_fs`` on
    ``dst_fs``, by removing any files / directories on the destination
    that aren't on the source, and copying files that aren't.

    Arguments:
        src_fs (FS or str): Source filesystem (URL or instance).
        dst_fs (FS or str): Destination filesystem (URL or instance).
        walker (~fs.walk.Walker, optional): An optional walker instance.
        copy_if_newer (bool): Only copy newer files (the default).
        workers (int): Number of worker threads used
            (0 for single threaded). Set to a relatively low number
            for network filesystems, 4 would be a good start.

    """
    ...