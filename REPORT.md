Development Comments
------

- Updated Django to 2.0.5.
- Use pipenv. Apologies, easiest way to keep my dependencies separate. The requirements.txt will be kept in sync with the Pipfile.lock.
- Importing is slow. Maybe sqlite is a bit slower than I expected it to be...?
- Seems transactions were not the issue with slowness when importing, guess half a million items are just a tad much ¯\\_(ツ)_/¯.
- I could add a lot more error handling to the import, mainly to see if the necessary files exist, but the files are never going to change, so I left that out.
- Showing a graph of all the consumption aggregated per half hour on the summary page might be a bit much, but the plotting library allows zooming, so I guess it's ok for this example.
- I kind of want to do a pre-calculation for values per-day in the import command, as well as add fields to split out the date components (e.g. day, month, etc.) since this would allow more interesting graphs (like comparing days, do people use more or less electricity on the weekend) without going straight to plain SQL, so can keep it DB agnostic.
- Import should really not be a single big class, could make that a separate class to do the import, and a separate one to parse the files to an array structure, so we could import from a variety of data sources and only rewrite the one that reads the files.
- I could add more plots on both pages, but it would just be a bunch of different queries, so I assume this is good enough.
- Realize 1.11 version of Django is a requirement and downgrade again.
- The aggregator service I created so I could add some tests is a bit contrived, but it works.
- The system should really have a test for the importer as well, but it would be more of the same, so I'll leave that out. It would be setting up a few fixture files, running those through the import, and making sure the correct items get added to the database.
- Added the day of week field because I'm curious how they compare.
- Great fun can be had by comparing days and wondering what people are doing at 11 in the morning on Wednesday that requires more energy on average than at any other point during the rest of the week.

Total time: 5 hrs