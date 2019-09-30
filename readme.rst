
Mike-rosoft Power File Renamer (c) 2003-2019
==============================================

A tool to rename large numbers of files, such as MP3s or images.
Recently ported to Python 3.6+ from ancient untouched 2.0-era source complete
with silly name.

Background
-----------------------

This tool does string updates on filenames in the order that
they occur on the command-line.
This is done so that results are consistent with expectations.
If modifications interact in unfortunate ways,
they may be reordered to suit.
This was a design goal.
(The final rename happens once however.)

Consequently, when performing many operations on a
*absolutley huge* number of files,
it might be less than instantaneous,
due to the inefficiencies of looping through the argument list for each file.
In such case you can run fewer operations per run, or change a subset of files
at a time.
As many filesystems are unhappy with huge numbers of files in a single folder,
this limitation hasn't been found to be a problem in practice so far.


Note that the term PRN (from *pro re nata* in Latin),
is used in the medical industry as an abbreviation for *as needed*.
Therefore use ``prn`` as needed and directed under the supervision of a
physician.

    *All information, content, and material of this website is for informational
    purposes only and are not intended to serve as a substitute for the
    consultation, diagnosis, and/or medical treatment of a qualified physician
    or healthcare provider.*

    *"Do not taunt P.R.N.  Accept no substitutes!"*


Installen-Sie, Bitte
-----------------------

.. code-block:: shell

    ⏵ pip3 install [--user] prn


Examples
-----------------------

A quick start with something simple—\
to replace underscores with spaces on some mp3s,
try this,
is shown below:

.. code-block:: shell

    ⏵ prn --replace _ ' ' *.mp3

Don't worry—this will simply show a preview of the results and won't do
anything until confirmed,
as we'll see later.
Feel free to experiment, help is available of course:

.. code-block:: shell

    ⏵ prn -h  # or --help

Note:  --longform options in the following examples have one-letter
abbreviated aliases that are typically the first letter of the long form, e.g.:
 ``--replace``  becomes  ``-r``.

Also, all options of ``prn`` can be passed multiple times,
allowing more to be done in a single invocation and enabling relatively complex
scenarios.


File Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several ways to select files for renaming.

- As seen above,
  one may select several files from a folder holding additional files,
  by simply placing them on the command-line,
  with or without shell wildcard expansion:

  .. code-block:: shell

        ⏵ prn … foo.bar *.mp3

- In a folder with large numbers of files,
  command-line limits may be bypassed with ``--match 'GLOB'`` as shown below:

  .. code-block:: shell

        ⏵ prn --match '*.mp3'  # OP1 OP2…

- As one may want to exclude some of the files gathered, filter is available::

    ⏵ prn --filter 'Rick Astley*'  # Never gonna…

  Match and filter may be passed multiple times to add to or subtract from the
  selected file set.

*"You may dispense with the pleasantries Commander…"*

- Additionally, if there are no extraneous files in the current folder,
  selection criteria may be omitted.
  A selection of all files in the current folder will be used instead:

  .. code-block:: shell

        ⏵ prn --replace _ ' '


Recursive Mode
++++++++++++++++

This will find files in and below the current folder.

When in recursive mode, note that currently folders aren't renamed.  Too
many issues came up,
so to rename folders you'll have to rename from each parent folder.

.. code-block:: shell

    # all mp3s at or below this folder:
    ⏵ prn -R --match '*.mp3' --replace _ ' '


Note that the glob method oddly requires a ``'**/'`` before the folder you want
to walk.
Power renamer handles that for you when a relative path is passed to match.
When an absolute path is passed, you must handle it yourself.


Regular Expression Substitutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When what you want to replace varies a bit between filenames,
use a regex:

.. code-block:: shell

    # collapse consecutive whitespace to a single space
    ⏵ prn --re-sub '\s+' ' '

Now you've got two problems, *wink.*


Padding Frame Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This option is relatively inflexible but did the one thing I needed:

.. code-block:: shell

    ⏵ prn --zfill 4 *.tif

    foo.3.tif                           │ foo.0003.tif
    foo.4.tif                           │ foo.0004.tif

Perhaps a more general pad function might be useful.


Swapping Text Trick
~~~~~~~~~~~~~~~~~~~~~~

The zfill operation above,
for example,
may be problematic if there are digits before the desired group:

.. code-block:: shell

    ⏵ prn -z 4 *.tif

    foo1.3.tif                          │ foo0001.3.tif  # Oops
    foo1.4.tif                          │ foo0001.4.tif


Doh, one way to get around this (that can help in several other situations) is
to hide the problem section by replacing it,
then later returning it to its original form:

.. code-block:: shell

    # replace, pad, then return
    ⏵ prn -r foo1 @  -z 4  -r @ foo1  *.tif

    foo1.3.tif                          │ foo1.0003.tif
    foo1.4.tif                          │ foo1.0004.tif

This works since operation arguments are processed in order from left to right.
Use a character for substitution that is not being used in the filenames,
of course.
Here we used the "``@``" symbol.


Operations
~~~~~~~~~~~~~~

Numerous helpful string operations are also available:

- ``-c --capitalize``
- ``-l --lower --lower-ext``
- ``-u --upper``
- ``-s --strip``
- ``--insert STR  --append STR  --prepend STR``

See ``-h`` for further details.


Refine It!
~~~~~~~~~~~~~~

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
finalize them with ``-e`` or ``--execute`` like so:

.. code-block:: shell

    ⏵ prn --OP1 --OP2…  -e


*Whoomp!  There it is.*


Safety
--------

``prn`` is written with safety in mind.

It won't make changes until you are happy with the results and pass the execute
flag.
It won't rename files to destinations that already exist,
and will notify you right away when they do.
Despite its version number it has been used for (pushing two) decades now.

However, as mentioned it was ported recently to Python3.
There is a test suite but it is not currently large.
Therefore:

*☛  Make a backup before trusting with large or important file collections. ☚*
