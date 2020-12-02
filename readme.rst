
Mike-rosoft™ Power File Renamer (c) 2003-2020
===============================================

A tool to rename large numbers of files, such as MP3s or images.
Recently ported to Python 3.6+ from ancient untouched 2.0-era source complete
with its original silly name.


Background
-----------------------

In short,
this tool does string operations on filenames in the order that
they occur on the command-line.
Why?
So that results are consistent with expectations.

Therefore,
if the given modifications interact in unfortunate ways,
they may be reordered to suit.
This was a design goal.

The final rename happens at once however.
No need to worry about files renamed half-way.

Consequently, when performing many operations on an
*absolutley huge* number of files,
it might be less than instantaneous,
due to the inefficiencies of looping through the argument list for each file.
In such case you can run fewer operations per run,
or change a subset of files at a time.
As many filesystems are unhappy with huge numbers of files in a single folder,
this limitation hasn't been found to be a problem in practice so far.

Note that the term PRN (from *pro re nata* in Latin),
is used in the medical industry as an abbreviation for *as needed*.
Therefore use ``prn`` as needed and directed under the supervision of a
physician:

    *All information, content, and material of this website is for informational
    purposes only and are not intended to serve as a substitute for the
    consultation, diagnosis, and/or medical treatment of a qualified physician
    or healthcare provider.*

    *"Do not taunt P.R.N.—Accept no substitutes!"*


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
Feel free to experiment,
help is available of course:

.. code-block:: shell

    ⏵ prn -h  # or --help

Note:  --longform options in the following examples have one-letter
abbreviated aliases that are typically the first letter of the long form, e.g.:
 ``--replace``  becomes  ``-r``.

Also, all options of ``prn`` can be passed multiple times,
allowing more to be done in a single invocation and enabling relatively complex
scenarios.


File Selection
~~~~~~~~~~~~~~~~

There are several ways to select files for renaming.

- As seen above,
  one may select several files from a folder holding additional files,
  by simply placing them on the command-line,
  with or without shell wildcard expansion:

  .. code-block:: shell

        ⏵ prn … foo.bar *.mp3

- In a folder with huge numbers of files,
  command-line limits may be bypassed with ``--match 'GLOB'`` as shown below:

  .. code-block:: shell

        ⏵ prn --match '*.mp3'  # OP1 OP2…

- As one may want to exclude some of the files gathered,
  filter is available::

    ⏵ prn --filter 'Rick Astley*'  # Never gonna…

  Match and filter may be passed multiple times to add to or subtract from the
  selected file set.

*"You may dispense with the pleasantries Commander…"*

- Additionally, if there are no extraneous files in the current folder,
  selection criteria may be omitted.
  All files in the current folder will be selected instead:

  .. code-block:: shell

        ⏵ prn --replace _ ' '


Recursive Mode
++++++++++++++++

This will find files in and below the current folder.

When in recursive mode, note that folders aren't renamed.  Too
many issues came up,
so to rename folders you'll have to rename them from each parent folder.

.. code-block:: shell

    # all jpegs at or below this folder:
    ⏵ prn -R --match '*.jpeg' --replace .jpeg .jpg


.. TODO: Huh?  Need to explain

Note that the glob method oddly requires a ``'**/'`` before the folder you want
to walk.
Power renamer handles that for you when a relative path is passed to match.
When an absolute path is passed, you must handle it yourself.


Common String Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~

Numerous helpful string operations are also available:

- ``-c --capitalize`` → *A "smart cap" of words*
- ``-l --lower --lower-ext``
- ``-u --upper``
- ``-s --strip``
- ``--insert STR  --append STR  --prepend STR``


Simple Replace
~~~~~~~~~~~~~~~~

We've already seen how ``--replace old new`` or its short form ``-r old new``
works above.
It'll likely be the most used,
workhorse operation.


Regular Expression Substitutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When what you want to replace varies a bit between filenames,
use a regex instead:

.. code-block:: shell

    # collapse consecutive whitespace to a single space
    ⏵ prn --re-sub '\s+' ' '

``-x …`` works as well.
I find `regex101.com <https://regex101.com/>`_
very helpful when writing them.

Now you've got two problems, *wink.*


Adding an Index Number
~~~~~~~~~~~~~~~~~~~~~~~

Several of the operations,
such as replacement, insert, append, and prepend support an index number,
assigned in the order of the file selection list.
This helps when destination filenames will not be unique.
Below we do a regex replace,
substituting a GUID (of hex digits) with a zero padded index number:

.. code-block:: shell

    ⏵ prn --prepend img_ -x '[A-F\d-]+' '%02i' -r .jpeg .jpg

    DEADBEEF-CAFE-123456.jpeg           │ img_00.jpg                                                      ✓
    DEADBEEF-CAFE-654321.jpeg           │ img_01.jpg                                                      ✓

Without the formatted index number, these filenames would collide.
A prefix is also added as well as a minor extension tweak.


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


See ``-h`` for further details.


Refine It!
~~~~~~~~~~~~~~

At this point,
you'll likely update the command-line a few times,
until things are just to your liking,
in terms of file selection and output filenames.

Newbie?
Hitting the up arrow in the shell often brings your last command-line back for
editing.
Press Enter to see the results.


Now, Commit Changes
---------------------

Happy with the results?
Finalize them with ``-e`` or ``--execute`` like so:

.. code-block:: shell

    ⏵ prn …  -e


*Whoomp!  There it is.*


Safety
--------

``prn`` is written with safety in mind.

It won't make changes until you are happy with the results and pass the execute
flag.
It won't even try to rename files to destinations that already exist
(or clobber them either),
and will notify you beforehand when they do.

Despite its version number it has been used for (pushing two) decades now.
However, as mentioned it was ported recently to Python3.
There is a test suite but it is not currently large.
Therefore:

*☛  Make a backup before trusting prn with large or important file collections. ☚*
