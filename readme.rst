
Mike-rosoft Power File Renamer (c) 2003-2018
================================================

A tool to rename large numbers of files, such as MP3s or images.
Recently ported to Python 3.6+ from ancient untouched 2.0-era source complete
with silly name.

*Background:*

This tool does string modification operations in the order that they occur on
the command-line,
for each filename selected.
This is done so that results are consistent with expectations.
If modifications interact in unfortunate ways,
they may be reordered to suit.
This was a design goal.

Consequently, when performing many operations on a *huge* number of files, it
might be less than instantaneous,
due to the inefficiencies of looping through the argument list for each file.
In such case you can run fewer operations per run, or change a subset of files
at a time.
As many filesystems are unhappy with huge numbers of files in a single folder,
it hasn't been found to be a problem in practice so far.


Examples
-----------------------

Quick start—to replace underscores with spaces on some mp3s::

    ⏵ prn --replace _ ' ' *.mp3

Don't worry—this will preview results and won't do anything until confirmed,
as seen below.
Feel free to experiment, help is available of course::

    ⏵ prn -h  # or --help

Note:  --longform options in the following examples have one-letter
abbreviated aliases that are typically the first letter of the long form, e.g.:
 ``--replace``  becomes  ``-r``.


File Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several ways to select files for renaming.

- As seen above,
  one may select several files from a folder holding additional files,
  by simply placing them on the command-line,
  with or without shell wildcard expansion:  ``foo.bar *.mp3``

- In a folder with large numbers of files,
  command-line limits may be bypassed with ``--match 'GLOB'`` as shown below::

    ⏵ prn --match '*.mp3'  # OP1 OP2…

- As one may want to exclude some of the files gathered, filter is available::

    ⏵ prn --filter 'Rick Astley*'  # OP1 OP2…

  Match and filter may be passed multiple times to add to the selection.

*"You may dispense with the pleasantries Commander…"*

- Additionally, if there are no extraneous files in the current folder,
  selection criteria may be omitted.
  A listing of all files in the current folder will be used instead.

  ::

        ⏵ prn --replace _ ' '  # all files in current folder selected


Recursive Mode
++++++++++++++++

This will find files in and below the current folder.

When in recursive mode, note that currently folders aren't renamed.  Too
many issues came up,
so to rename folders you'll have to rename from each parent folder.

::

    # all mp3s at or below this folder:
    ⏵ prn -R --match '*.mp3' --replace _ ' '


Note that the glob method oddly requires a ``'**/'`` before the folder you want
to walk.
Power renamer handles that for you when a relative path is passed to match.
When an absolute path is passed, you must handle it yourself.


Regular Expression Substitutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When what you want to replace varies a bit between filenames use a regex::

    ⏵ prn --re-sub '\s+' ' '  # collapse whitespace to a single space

Now you've got two problems, *wink.*


Padding Frame Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This option is inflexible but did the one thing I needed::

    ⏵ prn --zfill 4 *.tif

    foo.3.tif                           │ foo.0003.tif
    foo.4.tif                           │ foo.0004.tif

Perhaps a more general pad function might be useful.


Swapping Text Trick
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The zfill operation above,
for example may be problematic if there are digits before the desired group::

    ⏵ prn -z 4 *.tif

    foo1.3.tif                          │ foo0001.3.tif  # Oops
    foo1.4.tif                          │ foo0001.4.tif


Doh, one way to get around this (that can help in several other situations) is
to hide the problem section by replacing it,
then later returning it to its original form::

    ⏵ prn -r foo1 _ -z 4 -r _ foo1 *.tif  # replace, pad, return

    foo1.3.tif                          │ foo1.0003.tif
    foo1.4.tif                          │ foo1.0004.tif

This works since operation arguments are processed in order from left to right.
The '@' is another good character for temporary use.


Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Numerous helpful string operations are also available:

- ``-c --capitalize``
- ``-l --lower --lower-ext``
- ``-u --upper``
- ``-s --strip``
- ``--insert # STR  --append STR  --prepend STR``

See ``-h`` for further details.


Refine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At this point,
you'll likely update the command-line a few times,
until things are just to your liking,
in terms of file selection and output filenames.

Hitting the up arrow in the shell often brings your last command-line back for
editing,
then hitting enter to see the results is a simple
matter.


Commit Changes
-----------------------

Once happy with the changes,
finalize them with ``-e`` or ``--execute`` like so::

    ⏵ prn --OP1 --OP2…  -e


*Whoomp!  There it is.*

prn won't rename files to destinations that already exist,
and will notify you early when they do.
