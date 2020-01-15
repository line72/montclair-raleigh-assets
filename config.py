# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'raleigh',
    package_name = 'montclair-raleigh',
    name = 'Go Raleigh',
    description = 'Real Time Tracking of the Buses for Raleigh, NC',
    url = 'https://raleigh.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.4.3',
        revision = 1,
        title = 'Go Raleigh',
        first_run_text = "Welcome to Raleigh, NC's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.5',
        revision = 1,
        app_id = 'com.gotransitapp.raleigh',
        app_store_id = '1493869208',
        app_store_url = 'https://apps.apple.com/us/app/go-raleigh/id1493869208'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.2',
        revision = 1,
        app_id = 'com.gotransitapp.raleigh',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.raleigh'
    )
)
