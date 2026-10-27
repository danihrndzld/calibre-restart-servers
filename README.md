# Restart Servers plugin for calibre

[![MobileRead][mobileread-image]][mobileread-url]
[![History][changelog-image]][changelog-url]
[![License][license-image]][license-url]
[![calibre Version][calibre-image]][calibre-url]
[![Version][version-image]][release-url]
[![Status][status-image]][status-url]
[![Languages][languages-image]][languages-url]

## Overview

Restart Servers adds one toolbar button to calibre that restarts the Content server and the wireless device connection, and it never asks you a question while it does it. I wrote it because my Kindle, which runs KOReader, often fails to connect to calibre over Wi-Fi until I stop and start both servers.

Doing the restart by hand from the Connect/share menu takes five clicks and two dialogs. When you stop the wireless device connection, calibre asks if you want to keep it starting automatically, and when you start it again, calibre opens the "Smart device control" window so you can confirm settings you didn't change. The plugin calls the same calibre functions the menu calls, so it skips both dialogs and keeps your saved password, port and autostart setting as they are.

## What the button does

1. First, it stops the wireless device connection, if it's running.
2. Second, it stops the Content server and waits up to 60 seconds for it to shut down.
3. Third, it starts the Content server, and then it starts the wireless device connection with your saved settings.
4. Last, it shows "Servers restarted" and the port number in the calibre status bar for 8 seconds.

If either server fails to start, the plugin shows an error dialog with the message calibre returned. The Connect/share menu shows the new state after the restart, so you can check the IP address and port there.

## Languages

The plugin is available in English and Spanish, and calibre picks the language from Preferences > Look & feel > User interface language. English is the source language, so any language without a translation shows the English text.

To add a language, copy `translations/messages.pot` to `translations/<code>.po`, e.g., `fr.po`, fill in each `msgstr`, and run `./build.sh`. The build script compiles every `.po` file into a `.mo` file and puts it in the zip. When you add or change a string in the code, regenerate the template with `xgettext -L Python --from-code=UTF-8 --no-location -k_ -o translations/messages.pot __init__.py ui.py` and update each `.po` file with `msgmerge -U translations/es.po translations/messages.pot`.

## Requirements

- calibre 7.0 or newer. The plugin was written and checked against calibre 9.17 on macOS.
- The wireless device connection must be set up once from Connect/share > Start wireless device connection, so calibre has a saved password and port to reuse.

## Installation

1. Download `restart-servers-0.1.0.zip` from the [Releases][release-url] page.
2. In calibre, open Preferences > Plugins, click "Load plugin from file", and pick the zip.
3. Restart calibre.
4. Open Preferences > Toolbars & menus, choose "The main toolbar", and move "Restart servers" from the left list to the right list.

You can also install the zip from a terminal with `calibre-customize -a restart-servers-0.1.0.zip`.

## Building from source

Run `./build.sh` to create `dist/restart-servers-<version>.zip`. The script needs `msgfmt` from GNU gettext, which you can install on macOS with `brew install gettext`. The script reads the version from `__init__.py`, so you don't pass it by hand.

While you work on the code, `calibre-customize -b .` installs the plugin straight from the folder, and `calibre-debug -g` starts calibre with its log printed in the terminal.

## Releasing a new version

1. First, change `version` in `__init__.py`.
2. Second, add a section for the new version at the top of `CHANGELOG.md`.
3. Third, commit, then tag and push, e.g., `git tag v0.2.0 && git push origin main v0.2.0`.

The GitHub Actions workflow in `.github/workflows/release.yml` fails if the tag doesn't match the version in `__init__.py`. When the versions match, it builds the zip and creates a GitHub release with the changelog section as the release notes.

If GitHub Actions can't run, e.g., because the account hit its Actions spending limit, you can publish the release from your machine with `./build.sh` and `gh release create v0.2.0 dist/restart-servers-0.2.0.zip --notes-file <notes>`.

## License

The plugin is released under the [GNU General Public License v3][license-url], the same license calibre uses.

[mobileread-image]: https://img.shields.io/badge/MobileRead-Plugin%20Thread-blue
[mobileread-url]: https://www.mobileread.com/forums/forumdisplay.php?f=237

[changelog-image]: https://img.shields.io/badge/History-CHANGELOG-blue.svg
[changelog-url]: CHANGELOG.md

[license-image]: https://img.shields.io/badge/License-GPL%20v3-yellow.svg
[license-url]: LICENSE

[calibre-image]: https://img.shields.io/badge/calibre-7.0%2B-green
[calibre-url]: https://calibre-ebook.com/

[version-image]: https://img.shields.io/badge/Version-0.1.0-informational
[release-url]: https://github.com/danihrndzld/calibre-restart-servers/releases

[status-image]: https://img.shields.io/badge/Status-Beta-orange
[status-url]: CHANGELOG.md

[languages-image]: https://img.shields.io/badge/Languages-English%20%7C%20Espa%C3%B1ol-blueviolet
[languages-url]: translations/
