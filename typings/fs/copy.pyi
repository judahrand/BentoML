"""
This type stub file was generated by pyright.
"""

import typing
from typing import Callable, Optional, Text, Union

from .base import FS
from .walk import Walker

"""Functions for copying resources *between* filesystem.
"""
if typing.TYPE_CHECKING:
    _OnCopy = Callable[[FS, Text, FS, Text], object]

def copy_fs(
    src_fs: Union[FS, Text],
    dst_fs: Union[FS, Text],
    walker: Optional[Walker] = ...,
    on_copy: Optional[_OnCopy] = ...,
    workers: int = ...,
) -> None:
    """Copy the contents of one filesystem to another.

    Arguments:
        src_fs (FS or str): Source filesystem (URL or instance).
        dst_fs (FS or str): Destination filesystem (URL or instance).
        walker (~fs.walk.Walker, optional): A walker object that will be
            used to scan for files in ``src_fs``. Set this if you only want
            to consider a sub-set of the resources in ``src_fs``.
        on_copy (callable): A function callback called after a single file copy
            is executed. Expected signature is ``(src_fs, src_path, dst_fs,
            dst_path)``.
        workers (int): Use `worker` threads to copy data, or ``0`` (default) for
            a single-threaded copy.

    """
    ...

def copy_fs_if_newer(
    src_fs: Union[FS, Text],
    dst_fs: Union[FS, Text],
    walker: Optional[Walker] = ...,
    on_copy: Optional[_OnCopy] = ...,
    workers: int = ...,
) -> None:
    """Copy the contents of one filesystem to another, checking times.

    If both source and destination files exist, the copy is executed
    only if the source file is newer than the destination file. In case
    modification times of source or destination files are not available,
    copy file is always executed.

    Arguments:
        src_fs (FS or str): Source filesystem (URL or instance).
        dst_fs (FS or str): Destination filesystem (URL or instance).
        walker (~fs.walk.Walker, optional): A walker object that will be
            used to scan for files in ``src_fs``. Set this if you only want
            to consider a sub-set of the resources in ``src_fs``.
        on_copy (callable):A function callback called after a single file copy
            is executed. Expected signature is ``(src_fs, src_path, dst_fs,
            dst_path)``.
        workers (int): Use ``worker`` threads to copy data, or ``0`` (default) for
            a single-threaded copy.

    """
    ...

def copy_file(
    src_fs: Union[FS, Text], src_path: Text, dst_fs: Union[FS, Text], dst_path: Text
) -> None:
    """Copy a file from one filesystem to another.

    If the destination exists, and is a file, it will be first truncated.

    Arguments:
        src_fs (FS or str): Source filesystem (instance or URL).
        src_path (str): Path to a file on the source filesystem.
        dst_fs (FS or str): Destination filesystem (instance or URL).
        dst_path (str): Path to a file on the destination filesystem.

    """
    ...

def copy_file_internal(src_fs: FS, src_path: Text, dst_fs: FS, dst_path: Text) -> None:
    """Copy a file at low level, without calling `manage_fs` or locking.

    If the destination exists, and is a file, it will be first truncated.

    This method exists to optimize copying in loops. In general you
    should prefer `copy_file`.

    Arguments:
        src_fs (FS): Source filesystem.
        src_path (str): Path to a file on the source filesystem.
        dst_fs (FS): Destination filesystem.
        dst_path (str): Path to a file on the destination filesystem.

    """
    ...

def copy_file_if_newer(
    src_fs: Union[FS, Text], src_path: Text, dst_fs: Union[FS, Text], dst_path: Text
) -> bool:
    """Copy a file from one filesystem to another, checking times.

    If the destination exists, and is a file, it will be first truncated.
    If both source and destination files exist, the copy is executed only
    if the source file is newer than the destination file. In case
    modification times of source or destination files are not available,
    copy is always executed.

    Arguments:
        src_fs (FS or str): Source filesystem (instance or URL).
        src_path (str): Path to a file on the source filesystem.
        dst_fs (FS or str): Destination filesystem (instance or URL).
        dst_path (str): Path to a file on the destination filesystem.

    Returns:
        bool: `True` if the file copy was executed, `False` otherwise.

    """
    ...

def copy_structure(
    src_fs: Union[FS, Text], dst_fs: Union[FS, Text], walker: Optional[Walker] = ...
) -> None:
    """Copy directories (but not files) from ``src_fs`` to ``dst_fs``.

    Arguments:
        src_fs (FS or str): Source filesystem (instance or URL).
        dst_fs (FS or str): Destination filesystem (instance or URL).
        walker (~fs.walk.Walker, optional): A walker object that will be
            used to scan for files in ``src_fs``. Set this if you only
            want to consider a sub-set of the resources in ``src_fs``.

    """
    ...

def copy_dir(
    src_fs: Union[FS, Text],
    src_path: Text,
    dst_fs: Union[FS, Text],
    dst_path: Text,
    walker: Optional[Walker] = ...,
    on_copy: Optional[_OnCopy] = ...,
    workers: int = ...,
) -> None:
    """Copy a directory from one filesystem to another.

    Arguments:
        src_fs (FS or str): Source filesystem (instance or URL).
        src_path (str): Path to a directory on the source filesystem.
        dst_fs (FS or str): Destination filesystem (instance or URL).
        dst_path (str): Path to a directory on the destination filesystem.
        walker (~fs.walk.Walker, optional): A walker object that will be
            used to scan for files in ``src_fs``. Set this if you only
            want to consider a sub-set of the resources in ``src_fs``.
        on_copy (callable, optional):  A function callback called after
            a single file copy is executed. Expected signature is
            ``(src_fs, src_path, dst_fs, dst_path)``.
        workers (int): Use ``worker`` threads to copy data, or ``0`` (default) for
            a single-threaded copy.

    """
    ...

def copy_dir_if_newer(
    src_fs: Union[FS, Text],
    src_path: Text,
    dst_fs: Union[FS, Text],
    dst_path: Text,
    walker: Optional[Walker] = ...,
    on_copy: Optional[_OnCopy] = ...,
    workers: int = ...,
) -> None:
    """Copy a directory from one filesystem to another, checking times.

    If both source and destination files exist, the copy is executed only
    if the source file is newer than the destination file. In case
    modification times of source or destination files are not available,
    copy is always executed.

    Arguments:
        src_fs (FS or str): Source filesystem (instance or URL).
        src_path (str): Path to a directory on the source filesystem.
        dst_fs (FS or str): Destination filesystem (instance or URL).
        dst_path (str): Path to a directory on the destination filesystem.
        walker (~fs.walk.Walker, optional): A walker object that will be
            used to scan for files in ``src_fs``. Set this if you only
            want to consider a sub-set of the resources in ``src_fs``.
        on_copy (callable, optional):  A function callback called after
            a single file copy is executed. Expected signature is
            ``(src_fs, src_path, dst_fs, dst_path)``.
        workers (int): Use ``worker`` threads to copy data, or ``0`` (default) for
            a single-threaded copy.

    """
    ...